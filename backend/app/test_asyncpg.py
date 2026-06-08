import asyncio
import asyncpg


async def main():
    conn = await asyncpg.connect(
        user="postgres",
        password="root",
        database="prueba",
        host="127.0.0.1",
        port=5433,
        ssl=False
    )

    value = await conn.fetchval("SELECT 1")

    print("Conexión OK:", value)

    await conn.close()


asyncio.run(main())