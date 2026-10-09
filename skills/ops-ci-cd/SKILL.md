---
name: ops-ci-cd
description: >-
  Builds automated GitHub Actions CI/CD test and deployment pipelines.
---

# /ops-ci-cd

Configures continuous integration and continuous delivery workflows using GitHub Actions.

## Core Principles

1. **Fast Failure & Parallelism**:
   - Split pipeline jobs into parallel stages: Lint & Typecheck, Unit Tests, Integration Tests, Build.
   - Use caching for package managers (`actions/setup-node` with `cache: 'npm'`, `actions/cache`).

2. **Standard Pull Request CI Workflow**:
   ```yaml
   name: CI Pipeline
   on:
     pull_request:
       branches: [main, master]

   jobs:
     verify:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - uses: actions/setup-node@v4
           with:
             node-version: 20
             cache: 'npm'
         - run: npm ci
         - run: npm run lint
         - run: npm run typecheck
         - run: npm test -- --coverage
   ```

3. **Security in CI**:
   - Grant minimal permissions (`permissions: contents: read`).
   - Pin external GitHub Actions to full commit SHAs or verified major versions.
   - Store deployment credentials exclusively in GitHub Secrets or use OpenID Connect (OIDC) cloud federation.
