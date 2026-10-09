import json
import os
import sys
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 3456
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "latest_annotation.json")
annotations_queue = []

def save_annotation(data):
    annotations_queue.append(data)
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        sys.stderr.write(f"Failed to write annotation file: {e}\n")

class AnnotationHTTPHandler(BaseHTTPRequestHandler):
    def _send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(204)
        self._send_cors_headers()
        self.end_headers()

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self._send_cors_headers()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok", "pending": len(annotations_queue)}).encode("utf-8"))
            return

        if self.path == "/annotator.js":
            script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "annotator.js")
            if os.path.exists(script_path):
                self.send_response(200)
                self._send_cors_headers()
                self.send_header("Content-Type", "application/javascript")
                self.end_headers()
                with open(script_path, "rb") as f:
                    self.wfile.write(f.read())
                return

        if self.path in ("/", "/demo", "/demo.html"):
            demo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo.html")
            if os.path.exists(demo_path):
                self.send_response(200)
                self._send_cors_headers()
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                with open(demo_path, "rb") as f:
                    self.wfile.write(f.read())
                return

        if self.path == "/latest":
            self.send_response(200)
            self._send_cors_headers()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            latest = annotations_queue[-1] if annotations_queue else None
            self.wfile.write(json.dumps({"latest": latest}).encode("utf-8"))
            return

        self.send_response(404)
        self._send_cors_headers()
        self.end_headers()

    def do_POST(self):
        if self.path == "/annotate":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            try:
                data = json.loads(body.decode("utf-8"))
                save_annotation(data)
                
                # Log to stderr (so stdio MCP stdout stays clean)
                sys.stderr.write(f"\n[Codex Annotator] 🎯 Received annotation for: {data.get('selector', 'unknown')}\n")
                sys.stderr.write(f"[Codex Annotator] 💬 Instruction: {data.get('instruction', '')}\n\n")
                sys.stderr.flush()

                self.send_response(200)
                self._send_cors_headers()
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "message": "Annotation received"}).encode("utf-8"))
            except Exception as e:
                self.send_response(400)
                self._send_cors_headers()
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
            return

        self.send_response(404)
        self._send_cors_headers()
        self.end_headers()
    def log_message(self, format, *args):
        # Silence default HTTP server access logs to keep stdout/stderr clean
        pass

def start_http_server():
    server = HTTPServer(("127.0.0.1", PORT), AnnotationHTTPHandler)
    sys.stderr.write(f"[Codex Annotator] HTTP Bridge listening on http://127.0.0.1:{PORT}\n")
    sys.stderr.flush()
    server.serve_forever()

def run_mcp_server():
    # MCP Protocol over stdio (JSON-RPC 2.0)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception:
            continue

        req_id = req.get("id")
        method = req.get("method")

        if method == "initialize":
            res = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {}},
                    "serverInfo": {
                        "name": "codex-annotator",
                        "version": "1.0.0"
                    }
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "notifications/initialized":
            pass

        elif method == "tools/list":
            res = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "tools": [
                        {
                            "name": "get_latest_annotation",
                            "description": "Fetch the most recent UI element annotation dispatched from the browser.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "pop": {
                                        "type": "boolean",
                                        "description": "If true, marks this annotation as consumed."
                                    }
                                }
                            }
                        },
                        {
                            "name": "clear_annotations",
                            "description": "Clears all pending annotations.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {}
                            }
                        }
                    ]
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "tools/call":
            params = req.get("params", {})
            tool_name = params.get("name")
            arguments = params.get("arguments", {})

            if tool_name == "get_latest_annotation":
                if annotations_queue:
                    ann = annotations_queue.pop() if arguments.get("pop", True) else annotations_queue[-1]
                    text = (
                        f"### 🎯 Browser Annotation\n"
                        f"- **URL**: {ann.get('url', 'N/A')}\n"
                        f"- **Element**: `{ann.get('selector', 'N/A')}`\n"
                        f"- **Component**: `{ann.get('componentName', 'Unknown')}`\n"
                        f"- **Instruction**: **{ann.get('instruction', 'None')}**\n"
                        f"- **Text Content**: `{ann.get('text', '')}`\n"
                        f"- **HTML Snippet**:\n```html\n{ann.get('outerHTML', '')}\n```\n"
                    )
                else:
                    text = "No pending browser annotations."

                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [{"type": "text", "text": text}]
                    }
                }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()

            elif tool_name == "clear_annotations":
                annotations_queue.clear()
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [{"type": "text", "text": "All annotations cleared."}]
                    }
                }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()
            else:
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {"code": -32601, "message": f"Method {tool_name} not found"}
                }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()

if __name__ == "__main__":
    # Start the HTTP bridge in background thread
    t = threading.Thread(target=start_http_server, daemon=True)
    t.start()

    # If run with --http-only, just keep main thread alive for standalone console usage
    if "--http-only" in sys.argv:
        sys.stderr.write("[Codex Annotator] Running in standalone HTTP mode. Press Ctrl+C to exit.\n")
        try:
            while True:
                threading.Event().wait(1)
        except KeyboardInterrupt:
            sys.exit(0)
    else:
        # Default: MCP stdio server mode (used by Antigravity)
        run_mcp_server()
