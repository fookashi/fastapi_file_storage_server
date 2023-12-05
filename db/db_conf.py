from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import text


engine = create_async_engine('sqlite+aiosqlite:///files.db')

    
async_session = async_sessionmaker(engine, expire_on_commit=True)


async def init_db():
    async with engine.begin() as conn:
        await conn.execute(text(f"CREATE TABLE IF NOT EXISTS files (id UUID PRIMARY KEY, name VARCHAR(255), status VARCHAR(64))"))
        