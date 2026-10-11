"""Ratings Workflow API. Phase 0 exposes a health check and nothing else."""

import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from psycopg import Error, connect

# This file lives at backend/app/main.py. parents[2] is the repository root,
# which is also where Docker Compose reads .env.
load_dotenv(Path(__file__).resolve().parents[2] / ".env")

app = FastAPI(title="Ratings Workflow")


@app.get("/health")
def health():
    database_url = os.environ.get("DATABASE_URL")
    if not database_url:
        return JSONResponse(
            status_code=503,
            content={"status": "degraded", "database": "missing_config"},
        )

    try:
        # A new connection per check. A pool earns its complexity once real
        # requests exist; a health probe does not need one.
        with connect(database_url, connect_timeout=3) as conn:
            conn.execute("SELECT 1")
    except Error:
        return JSONResponse(
            status_code=503,
            content={"status": "degraded", "database": "unreachable"},
        )

    return {"status": "ok", "database": "ok"}
