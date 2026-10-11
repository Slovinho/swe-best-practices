# Ratings Workflow

Fictional internal tool for a credit ratings team. Analysts track issuers, record rating actions, and move those actions through review. The data, company names, and ratings in this repo are invented.

This repository is a study project. The reasoning lives in [LEARNING.md](LEARNING.md).

## Layout

- `backend/` — Python API (FastAPI). Added in Phase 0.
- `frontend/` — React and TypeScript. Added in Phase 6, when there is a UI to build.
- `docker-compose.yml` — local Postgres only. The API runs on your machine so reload stays fast.

## Phase 0 status

The database and the API health check are added in the next commit of this phase. Until that file exists, there is nothing to run.
