from fastapi.testclient import TestClient

from app.main import app


# Your turn: replace the body. Delete this comment when the test is yours.
#
# Cover the missing-DATABASE_URL case only.
# Call the route in-process. Do not start uvicorn, and do not require Postgres.
# Importing the app loads .env, so clear DATABASE_URL for this test. Otherwise
# it hits the database on your machine and fails in CI.
# Assert both the status code and the JSON body.
# `monkeypatch` is pytest's fixture for changing the environment during one test.
def test_health_when_database_url_is_missing(monkeypatch):
    raise NotImplementedError
