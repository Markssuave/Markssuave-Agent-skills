---
name: ops-telemetry
description: >-
  Sets up structured JSON logging, correlation IDs, and Sentry error monitoring.
---

# /ops-telemetry

Instruments application observability, structured logging, distributed tracing, and real-time error tracking.

## Core Principles

1. **Structured JSON Logging**:
   - Never use unstructured `console.log` in production backend code.
   - Use high-performance structured loggers (Pino for Node.js, Structlog for Python, Zap for Go).
   - Log entries must be single-line JSON objects with standard fields: `timestamp`, `level`, `msg`, `requestId`, `userId`.

2. **Correlation / Request IDs**:
   - Extract `X-Request-ID` from incoming requests or generate a UUIDv4 on entry.
   - Propagate the request ID across all downstream HTTP requests, database queries, and background jobs.

3. **Error Monitoring (Sentry)**:
   - Capture unhandled exceptions with full stack traces, breadcrumbs, and sanitized request context.
   - Scrub sensitive fields (passwords, credit cards, bearer tokens, API keys) before transmitting to Sentry.

4. **Health Check Probes**:
   - Provide `/health/liveness`: Returns `200 OK` if the process is responsive.
   - Provide `/health/readiness`: Returns `200 OK` only if all critical dependencies (database, Redis) are connected and ready to accept traffic.
