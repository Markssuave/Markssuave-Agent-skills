---
name: arch-queue
description: >-
  Designs background worker jobs, queue retries, and scheduled workers.
---

# /arch-queue

Implements asynchronous background processing, message queues, and worker jobs.

## Core Principles

1. **When to Offload to a Queue**:
   - Any operation taking longer than 200ms (sending emails, image/video compression, generating PDFs, webhook delivery, AI completions).
   - Return `202 Accepted` immediately from HTTP endpoints with a task ID or polling URL.

2. **Idempotency & Safe Retries**:
   - Background jobs *will* be executed multiple times in distributed environments.
   - Every job must be idempotent: processing the same job ID twice must have the same outcome as processing it once.
   - Use exponential backoff with jitter on retries (`attempts: 5, backoff: { type: 'exponential', delay: 2000 }`).

3. **Dead-Letter Queue (DLQ)**:
   - Route permanently failing jobs to a dead-letter queue after maximum retries.
   - Alert engineering when DLQ depth exceeds threshold.

4. **BullMQ Worker Example**:
   ```typescript
   import { Worker, Queue } from 'bullmq';

   export const emailQueue = new Queue('emails', { connection: redisOptions });

   export const emailWorker = new Worker('emails', async (job) => {
     const { to, template, data } = job.data;
     await sendEmail(to, template, data);
   }, {
     connection: redisOptions,
     concurrency: 5,
   });
   ```
