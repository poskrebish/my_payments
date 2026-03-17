import asyncpg
from typing import Optional

pg_pool: Optional[asyncpg.Pool] = None

async def init_db():
    global pg_pool
    pg_pool = await asyncpg.create_pool(
        user="postgres",
        password="postgres",
        database="payments",
        host="postgres",
        port=5432,
        min_size=5,
        max_size=20
    )
    await create_tables()

async def create_tables():
    async with pg_pool.acquire() as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS payments (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                amount DECIMAL(10,2) NOT NULL,
                status VARCHAR(50) NOT NULL,
                created_at TIMESTAMP DEFAULT NOW()
            )
        """)

async def close_db():
    if pg_pool:
        await pg_pool.close()