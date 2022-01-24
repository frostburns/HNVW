from sqlite3 import connect

from . import DATABASE
TABLE = "guild_table"

# schema
with connect(DATABASE) as conn:
    conn.execute(
        f"""CREATE TABLE IF NOT EXISTS {TABLE} (
            guild_id TEXT PRIMARY KEY,
            auto_shuffle INTEGER NOT NULL DEFAULT 0,
            auto_loop INTEGER NOT NULL DEFAULT 0
        )"""
    )

class Guild:
    pass
