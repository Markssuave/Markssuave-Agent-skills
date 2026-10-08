---
name: api-design
description: >-
  Designs clean, standardized REST/GraphQL endpoints with consistent envelopes.
---

# /api-design

Designs production-ready, standardized API architectures, endpoint contracts, and resource schemas.

## Core Principles

1. **Resource-Oriented Naming**:
   - Use plural nouns for resource collections (`/api/v1/users`, `/api/v1/workspaces/:id/projects`).
   - Use standard HTTP methods: `GET` (read-only/idempotent), `POST` (create), `PUT` (full replace), `PATCH` (partial update), `DELETE` (remove).
   - Reserve verbs only for explicit actions that do not map to CRUD: `POST /api/v1/invoices/:id/refund`.

2. **Standardized Response Envelope**:
   All responses must follow a consistent JSON structure:
   ```json
   {
     "success": true,
     "data": {},
     "meta": {
       "page": 1,
       "limit": 20,
       "total": 142
     }
   }
   ```
   For errors:
   ```json
   {
     "success": false,
     "error": {
       "code": "RESOURCE_NOT_FOUND",
       "message": "User with ID '123' does not exist.",
       "details": []
     }
   }
   ```

3. **Status Code Standards**:
   - `200 OK`: Successful read or update.
   - `201 Created`: Resource successfully created (include `Location` header when applicable).
   - `204 No Content`: Successful deletion or action returning no body.
   - `400 Bad Request`: Validation failure or malformed payload.
   - `401 Unauthorized`: Missing or invalid authentication token.
   - `403 Forbidden`: Authenticated user lacks permission to access resource.
   - `404 Not Found`: Resource does not exist.
   - `409 Conflict`: Unique constraint violation or state machine conflict.
   - `429 Too Many Requests`: Rate limit exceeded (include `Retry-After` header).
   - `500 Internal Server Error`: Unhandled server exception (never leak stack traces in production).

4. **Pagination, Sorting & Filtering**:
   - Prefer cursor-based pagination for high-volume or real-time collections: `?cursor=eyJpZ...&limit=20`.
   - Provide offset-based pagination only for administrative tables: `?page=1&limit=20`.
   - Explicit sorting syntax: `?sort=-created_at,name` (prefix `-` for descending).
