---
name: sec-audit
description: >-
  Audits endpoints and configurations against OWASP Top 10 security risks.
---

# /sec-audit

Conducts rigorous security audits across application code, configurations, headers, and dependencies.

## Audit Checklist

1. **Injection & Input Sanitization**:
   - Verify parameterized SQL queries (no raw string interpolation or concatenated SQL).
   - Check HTML template escaping to prevent Stored / Reflected Cross-Site Scripting (XSS).

2. **CORS & Security Headers**:
   - Ensure CORS is restricted to known production origins; avoid wildcard `*` with credentials.
   - Configure Helmet or equivalent to set:
     - `Content-Security-Policy` (CSP)
     - `Strict-Transport-Security` (HSTS)
     - `X-Content-Type-Options: nosniff`
     - `X-Frame-Options: DENY`

3. **Broken Object-Level Authorization (BOLA / IDOR)**:
   - Ensure every query checking an ID checks ownership:
     `SELECT * FROM projects WHERE id = :id AND workspace_id = :current_user_workspace_id`.
   - Never rely on client-provided IDs without verifying tenancy.

4. **Secrets & Dependency Scans**:
   - Check `.env` files are in `.gitignore`.
   - Audit dependencies using `npm audit`, `pip audit`, or `trivy`.
