# Smoke test: builds the database and checks that WEATHER has rows.
import sqlite3
from build_db import build

build()

conn = sqlite3.connect("project.db")
rows = conn.execute("SELECT COUNT(*) FROM WEATHER").fetchone()[0]
conn.close()

print("WEATHER rows:", rows)
assert rows > 0, "The database built, but WEATHER is empty"