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


# Your turn: implement this route. Delete this comment when the behavior is yours.
#
# A process supervisor calls GET /health to decide whether to send traffic.
# Postgres has to accept a query before the answer is yes.
#
# Handle three situations, and choose a status code for each:
# - DATABASE_URL is not set
# - the database cannot be reached or will not run a query
# - a trivial query succeeds
#
# Bound how long a dead database can stall the call.
# A bug in this function should still surface as a server error.
# One new connection per call is enough.
#
# os, JSONResponse, Error, and connect are already imported.
@app.get("/health")
def health():
    raise NotImplementedError
