# Ratings Workflow

Fictional internal tool for a credit ratings team. Analysts track issuers, record rating actions, and move those actions through review. The data, company names, and ratings in this repo are invented.

This repository is a study project. The reasoning lives in [LEARNING.md](LEARNING.md).

## Layout

- `backend/` — Python API (FastAPI). Runs on your machine so code reload stays fast.
- `frontend/` — React and TypeScript. Added in Phase 6, when there is a UI to build.
- `docker-compose.yml` — local Postgres 16 only.

## Run locally

Docker is required. Docker Desktop is the usual install. Colima is the CLI alternative: once `docker` and `colima` are on your PATH, run `colima start`, then the commands below.

```bash
cp .env.example .env
docker compose up -d

cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

pytest
uvicorn app.main:app --reload --port 8000
```

`GET http://127.0.0.1:8000/health` returns 200 when Postgres accepts a query, and 503 when it does not.

The password in `.env.example` is a local dummy. `.env` is gitignored so a real password never has to be committed. Do not reuse that dummy password anywhere but this laptop.

Stop the database with `docker compose down`. That keeps the data. `docker compose down -v` deletes it.
