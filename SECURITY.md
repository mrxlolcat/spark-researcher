# Security

Spark Researcher runs local project commands and records research/memory artifacts. Treat commands, generated patches, and imported chip logic as privileged local execution.

## Launch Boundaries

- Researcher does not own Telegram ingress.
- Researcher does not own Spawner mission control.
- Researcher should be invoked by the operator, Builder, or explicit local CLI flows.
- Generated code changes should remain reviewable; do not auto-apply unreviewed patches in launch workflows.

## Secrets

Never commit:

- `.env`, `.env.*`
- API keys
- local project state containing user data
- generated artifacts that contain private prompts, private code, or credentials

Prefer environment variables or Spark CLI secret storage for provider keys.

## Safe Bootstrap

Inspect installer scripts before running them. Do not pipe remote install scripts directly into a shell.
