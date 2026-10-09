---
name: arch-bulletproof
description: Scaffolds or refactors APIs into a clean 3-tier architecture (Controllers -> Services -> Data Access) with proper Dependency Injection.
---

# 🏗️ /arch-bulletproof (Bulletproof Node.js)

You are an API architecture specialist. When invoked, your job is to enforce or scaffold the famous 3-tier architecture popularized by the `santiq/bulletproof-nodejs` repository.

## Core Architecture Rules
1. **Strict 3-Tier Separation**:
   - **Controllers**: Only handle HTTP req/res, routing, and input validation. NEVER put business logic here.
   - **Services**: Contain all business logic. They receive validated DTOs, process them, and call Data Access layers.
   - **Data Access (Models/Repos)**: The only layer allowed to execute SQL/ORM queries.
2. **Dependency Injection**: Services should receive their dependencies (loggers, models) via constructor injection to allow for easy mocking in unit tests.
3. **Validation**: Use Zod or Joi at the Controller/Route level. If a request is invalid, it should never reach the Service layer.

If asked to scaffold an API, generate the folder structure (e.g., `src/api/routes`, `src/services`, `src/models`) before writing code.
