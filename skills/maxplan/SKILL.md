---
name: maxplan
description: Use this workflow when the user types /maxplan or $maxplan. Plan the requested work and recommend only the skills relevant to it; do not execute the task.
---

# Maxplan

Act as the user's project manager and AI workflow planner.

When the user invokes `/maxplan` or `$maxplan`:

1. Restate the goal clearly.
2. Recommend an efficient agent strategy and a suitable Codex model, with a short reason.
3. Select only the relevant installed skills. Always include `/maxplan` and `/caveman` in the workflow.
4. Give the plan in this format:

```text
Goal: [Restate the user's goal clearly]
Recommended Agent & Model: [agent strategy + model] - [Why this fits]

Proposed Skill Workflow:

/maxplan - Coordinates the plan and relevant tools.
/caveman - Keeps interaction concise.
/[relevant-skill] - [Plain-language reason this skill is needed].
```

Do not start implementation when `/maxplan` is invoked. Keep the plan specific to the request; do not list unrelated skills or invent skills that are not installed.
