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
- `GET /health` is for a process supervisor, not for an analyst. `200` means the API can serve. `503` means the process is alive and Postgres is not. `500` would mean the health check itself is broken.
- `SELECT 1` is the smallest query that proves Postgres accepted a connection and ran SQL. `connect_timeout=3` stops a dead host from hanging the probe.
- The handler catches `psycopg.Error` only. A bug in our own code still surfaces as `500`.
- `.env` holds local values and is gitignored. `.env.example` is the committed list of names. The password in the example is a laptop dummy.

### Decisions and tradeoffs

- Postgres in Docker, not SQLite and not a Homebrew Postgres. Indexes, `EXPLAIN`, transactions, and later `pgvector` are Postgres behavior. SQLite would boot the app and hide those topics.
- Compose runs only the database. The API runs on the host so reload and the debugger stay ordinary Python. Putting the API in Compose belongs with the Dockerfile, in Phase 8.
- `frontend/` is not scaffolded yet. A Vite app is a pile of files with nothing to learn until Phase 6.
- One new database connection per health check. A pool is the right tool once many requests share the database. A probe does not justify one.
- `DATABASE_URL` uses `127.0.0.1`. On a Mac, `localhost` can resolve to IPv6 while the published port is IPv4.
- `load_dotenv` runs at import and reads the repo-root `.env` (`Path(__file__).parents[2]`). Convenient locally. Importing the module changes the process environment, which is a side effect. A settings object created on purpose replaces this in Phase 5.
- Dependencies live in `pyproject.toml`. A lockfile waits until CI needs bit-for-bit installs.

### What we hit on this machine

- `docker` was not installed. Postgres was not installed.
- `brew` on `PATH` is the Intel Homebrew at `/usr/local`, on an Apple Silicon Mac. `brew install colima` tried to compile Go and stopped because the Command Line Tools check failed. That is an environment mismatch, not a Compose problem.
- Installed arm64 binaries instead: `docker`, `docker-compose`, `colima`, `lima`, and `limactl` in `~/bin`, plus Lima's shared files in `~/share/lima`. Colima's first check looks for a `lima` binary, not only `limactl`.
- Verified: Postgres healthcheck is `healthy`, `SELECT 1` inside the container returns a row, and `GET /health` returns `200` with the database up and `503` with `database: unreachable` when the port is closed. The unit test covers `503` when `DATABASE_URL` is missing. Pytest passed.
- The API was not left running. The check called the route in-process.

### Mistakes

No design mistake in the files. The code and Compose file were written for you. Phase 1 is the first design you draft.

### Interview Q&A

Checkpoint questions are asked in the Phase 0 review. Graded answers get appended after you reply.
