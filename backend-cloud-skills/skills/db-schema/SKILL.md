---
name: db-schema
description: >-
  Generates relational database schemas, migrations, and Prisma/Drizzle models.
---

# /db-schema

Designs relational database schemas, entity relationships, migration scripts, and ORM models.

## Core Principles

1. **Relational Normalization & Types**:
   - Primary keys: Prefer UUIDv7 (time-sortable UUID) or identity `BIGINT` over random UUIDv4 for improved B-Tree index locality.
   - Timestamps: Always include `created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()` and `updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()`.
   - Soft deletes: Use `deleted_at TIMESTAMPTZ NULL` only when data auditing or restoration is strictly required; prefer explicit state columns otherwise.

2. **Foreign Key Cascades & Constraints**:
   - Define foreign key constraints explicitly with intentional `ON DELETE` behavior (`CASCADE`, `RESTRICT`, or `SET NULL`).
   - Use `CHECK` constraints at the database level to enforce domain invariants (e.g., `CHECK (price >= 0)`).

3. **Prisma Example Pattern**:
   ```prisma
   model Workspace {
     id        String    @id @default(uuid())
     name      String
     createdAt DateTime  @default(now()) @map("created_at")
     updatedAt DateTime  @updatedAt @map("updated_at")
     members   Member[]

     @@map("workspaces")
   }

   model Member {
     id          String    @id @default(uuid())
     workspaceId String    @map("workspace_id")
     userId      String    @map("user_id")
     role        String    @default("member")
     workspace   Workspace @relation(fields: [workspaceId], references: [id], onDelete: Cascade)

     @@unique([workspaceId, userId])
     @@map("members")
   }
   ```

4. **Safe Migrations**:
   - Never perform destructive schema changes (dropping columns, changing types) in a single deployment.
   - Follow expand-and-contract: 1) add new column, 2) write to both, 3) backfill data, 4) read from new column, 5) remove old column.
