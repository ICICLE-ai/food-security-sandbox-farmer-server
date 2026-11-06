# Food Security Sandbox farmer server

Dataset storage, privacy tooling (differential privacy, location privacy, k-anonymity), local model training for collaborative learning, and membership-inference risk analysis.

## Configuration

Read from environment variables (or a local `.env` file, which is never copied into the image).

| Variable | Value |
|---|---|
| `MONGODB_URI` | MongoDB connection string |
| `TAPIS_BASE_URL` | `https://icicleai.tapis.io` |
| `HOST`, `PORT`, `DEBUG` | Optional; default `0.0.0.0`, `8000`, `false`. Never enable `DEBUG` on a pod. |

`GET /health` returns `{"status": "ok", "build_sha": ...}` for the deployment check.

## Run locally

```bash
uv sync
uv run python app.py
```

Dependencies are locked with uv: after changing `pyproject.toml`, run `uv lock` and commit `uv.lock`.

## Deployment

Deployed to the existing `fsssandbox` Tapis pod (image `ghcr.io/icicle-ai/food-security-sandbox-sandbox`) by `.github/workflows/deploy.yaml`, using the shared
[ICICLE CI/CD templates](https://github.com/ICICLE-ai/cicd-templates/wiki/Quick-start) (`v2.2.1`).
Bump `service-version` in `icicle-service.yaml` and push to `main` to release.
CI checks the rollout through `GET /health`.
