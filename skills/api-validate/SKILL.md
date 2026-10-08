---
name: api-validate
description: >-
  Implements strict input validation, sanitization, and Zod/Pydantic schemas.
---

# /api-validate

Guarantees data integrity and type safety at all system boundaries (HTTP request payloads, query params, headers, and environment variables).

## Core Principles

1. **Schema-Driven Boundaries**:
   - Parse, don't validate: Transform raw external input into validated domain types immediately at the controller or route layer.
   - Strip unknown/unwhitelisted fields to prevent parameter injection attacks.

2. **TypeScript / Zod Standards**:
   ```typescript
   import { z } from 'zod';

   export const CreateUserSchema = z.object({
     email: z.string().email().toLowerCase().trim(),
     name: z.string().min(2).max(100).trim(),
     role: z.enum(['admin', 'member', 'viewer']).default('member'),
   });

   export type CreateUserInput = z.infer<typeof CreateUserSchema>;
   ```

3. **Python / Pydantic Standards**:
   ```python
   from pydantic import BaseModel, EmailStr, Field

   class CreateUserRequest(BaseModel):
       email: EmailStr
       name: str = Field(..., min_length=2, max_length=100)
       role: str = Field(default="member", pattern="^(admin|member|viewer)$")

       class Config:
           str_strip_whitespace = True
   ```

4. **Error Formatting**:
   Convert library-specific validation errors into standardized field-level errors:
   ```json
   {
     "success": false,
     "error": {
       "code": "VALIDATION_FAILED",
       "message": "Input validation failed on 1 field.",
       "details": [
         { "field": "email", "issue": "Must be a valid email address." }
       ]
     }
   }
   ```
