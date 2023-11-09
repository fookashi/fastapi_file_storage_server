from uuid import UUID

from sqlalchemy import text

from interfaces.db.repository import IRepository
from .db_conf import async_session

class SQLiteFileRepository(IRepository):
    
    
    def __init__(self) -> None:
        self.session = async_session()
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.aclose()
    
    async def create(self, name: str, id: UUID) -> str:
        async with self.session as cursor:
            query = text(f"INSERT INTO files VALUES ('{id}','{name}')")
            await cursor.execute(query)
            await cursor.commit()
            
    async def read(self, id: UUID) -> str:
        async with self.session as cursor:
            query = text(f"SELECT name FROM files WHERE id='{id}'")
            exc = await cursor.execute(query)
        return exc.fetchone()[0]
            
    async def update(self, id: UUID, new_name: str) -> str:
        async with self.session as cursor:
            query = text(f"UPDATE files SET name='{new_name}' WHERE id='{id}'")
            await cursor.execute(query)
            await cursor.commit()
    
    async def delete(self, id: UUID) -> str:
        async with self.session as cursor:
            query = text(f"DELETE FROM files WHERE id='{id}'")
            await cursor.execute(query)
            await cursor.commit()
