---
name: db-query-opt
description: >-
  Analyzes query execution plans, indexes, and eliminates N+1 query bottlenecks.
---

# /db-query-opt

Diagnoses slow database queries, designs composite and partial indexes, and resolves N+1 ORM data-fetching bottlenecks.

## Core Principles

1. **Index Strategy**:
   - Every foreign key used in joins or lookups must be indexed (`CREATE INDEX idx_members_user_id ON members(user_id)`).
   - Use composite indexes following the equality-first rule: `(status, created_at)` for queries filtering `WHERE status = 'active' ORDER BY created_at DESC`.
   - Use partial indexes for skewed boolean columns or soft-deletes: `CREATE INDEX idx_active_users ON users(email) WHERE is_active = true`.

2. **Eliminating N+1 Queries**:
   - Detect loops where an ORM executes 1 query for the parent records, then N additional queries for child relationships.
   - Use eager loading / joins (`include` in Prisma, `joinedload` in SQLAlchemy, or dataloaders in GraphQL).

3. **Query Inspection (`EXPLAIN ANALYZE`)**:
   - Look for `Seq Scan` on large tables—this indicates a missing index.
   - Look for high `Rows Removed by Filter`—indicates an index covers part of the query but lacks filter predicates.
   - Watch for sorting in memory (`Sort Method: external merge Disk`) and increase `work_mem` or add an index that satisfies the ordering.

4. **Connection Pooling**:
   - Use connection poolers (PgBouncer, Prisma Accelerate, HikariCP) in serverless environments to prevent exhausting PostgreSQL `max_connections`.
