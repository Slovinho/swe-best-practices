# Learning log

Interview prep for a senior full-stack role on a credit ratings technology team. The product in this repo is fictional. One section gets appended after each phase.

## Starting point

- SQL joins: cannot write an `INNER JOIN` or a `LEFT JOIN` from memory.
- Docker: has written a Dockerfile. Compose files have been agent-written.
- TypeScript: prefers it. Has not written it by hand.
- Migrations: Alembic is unfamiliar. It is the tool that versions database schema changes. That is Phase 1.
- React: knows the concepts. Has not written components, state, or effects by hand.

The gap to close is judgment you can explain out loud, on code you wrote yourself.

## Phase 0 — Setup

### Concepts

- A Dockerfile builds one image. Compose runs containers from images and sets ports, environment, and disks.
- A named volume (`ratings_pg_data`) keeps Postgres data when the container is replaced. `docker compose down` keeps the volume. `docker compose down -v` deletes it.
- `.env` holds local values and is gitignored. `.env.example` is the committed list of names. The password in the example is a laptop dummy.
- `GET /health` is the piece to write by hand. The generated handler was removed. The assignment is the comment in `backend/app/main.py`.

### Decisions and tradeoffs

- Postgres in Docker, not SQLite and not a Homebrew Postgres. Indexes, `EXPLAIN`, transactions, and later `pgvector` are Postgres behavior. SQLite would boot the app and hide those topics.
- Compose runs only the database. The API runs on the host so reload and the debugger stay ordinary Python. Putting the API in Compose belongs with the Dockerfile, in Phase 8.
- `frontend/` is not scaffolded yet. A Vite app is a pile of files with nothing to learn until Phase 6.
- `DATABASE_URL` uses `127.0.0.1`. On a Mac, `localhost` can resolve to IPv6 while the published port is IPv4.
- `load_dotenv` runs at import and reads the repo-root `.env` (`Path(__file__).parents[2]`). Convenient locally. Importing the module changes the process environment, which is a side effect. A settings object created on purpose replaces this in Phase 5.
- Dependencies live in `pyproject.toml`. A lockfile waits until CI needs bit-for-bit installs.

### What we hit on this machine

- `docker` was not installed. Postgres was not installed.
- `brew` on `PATH` is the Intel Homebrew at `/usr/local`, on an Apple Silicon Mac. `brew install colima` tried to compile Go and stopped because the Command Line Tools check failed. That is an environment mismatch, not a Compose problem.
- Installed arm64 binaries instead: `docker`, `docker-compose`, `colima`, `lima`, and `limactl` in `~/bin`, plus Lima's shared files in `~/share/lima`. Colima's first check looks for a `lima` binary, not only `limactl`.
- Verified before the rewrite: the Postgres container became healthy and `SELECT 1` inside it returned a row. The API was not left running.
- The generated `/health` handler and its test were removed so they can be written by hand. Status codes and the response body are intentionally not recorded here.

### Mistakes

The health check was generated, then treated as something to review. That does not stick. The rewrite is the actual Phase 0 exercise.

### Interview Q&A

Checkpoint waits until `/health` and its test are written by hand.
