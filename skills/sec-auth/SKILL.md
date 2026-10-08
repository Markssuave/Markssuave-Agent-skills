---
name: sec-auth
description: >-
  Implements secure auth flows like JWT rotation, session cookies, and OAuth.
---

# /sec-auth

Implements production authentication, token lifecycles, and identity management.

## Core Principles

1. **Session & Cookie Security**:
   - Store refresh tokens or session IDs in `httpOnly`, `Secure`, `SameSite=Lax` (or `Strict`) cookies.
   - Never store sensitive JWTs or session secrets in browser `localStorage` or `sessionStorage` (vulnerable to XSS).

2. **Access & Refresh Token Lifecycle**:
   - Short-lived Access Tokens: 10–15 minutes validity containing minimal user claims (`sub`, `role`).
   - Long-lived Refresh Tokens: 7–30 days validity, hashed in the database, with automatic token reuse detection and family revocation.

3. **Password Security**:
   - Use Argon2id or bcrypt (cost factor >= 12). Never use MD5, SHA-256, or unsalted hashes.
   - Implement timing-safe string comparison to protect against timing attacks.

4. **OAuth 2.0 / OIDC Flow**:
   - Always use Authorization Code Flow with PKCE (Proof Key for Code Exchange).
   - Validate and verify `state` parameter to prevent CSRF login attacks.
