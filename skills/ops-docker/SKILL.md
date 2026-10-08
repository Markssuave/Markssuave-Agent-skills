---
name: ops-docker
description: >-
  Crafts minimal, multi-stage Dockerfiles and local compose environments.
---

# /ops-docker

Builds production-grade container images and local multi-service development stacks.

## Core Principles

1. **Multi-Stage Builds**:
   - Separate build-time dependencies (TypeScript compilers, dev dependencies) from the minimal production runtime image.
   - Use minimal base images (e.g., `node:20-alpine`, `python:3.12-slim`, `distroless`).

2. **Non-Root Execution**:
   - Always create and run under an unprivileged user:
     ```dockerfile
     USER node
     ```

3. **Layer Caching Optimization**:
   - Copy dependency manifests (`package.json`, `package-lock.json`, `requirements.txt`) and install dependencies *before* copying application source code to maximize Docker cache hits.

4. **Production Dockerfile Template (Node.js)**:
   ```dockerfile
   # Stage 1: Build
   FROM node:20-alpine AS builder
   WORKDIR /app
   COPY package*.json ./
   RUN npm ci
   COPY . .
   RUN npm run build && npm prune --production

   # Stage 2: Production Runner
   FROM node:20-alpine AS runner
   WORKDIR /app
   ENV NODE_ENV=production
   USER node
   COPY --chown=node:node --from=builder /app/package*.json ./
   COPY --chown=node:node --from=builder /app/node_modules ./node_modules
   COPY --chown=node:node --from=builder /app/dist ./dist
   EXPOSE 3000
   CMD ["node", "dist/main.js"]
   ```
