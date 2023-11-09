from fastapi import FastAPI
import asyncio
import uvicorn

from routers import storage_router, health_check_router
from db.db_conf import init_db



app = FastAPI()
app.include_router(health_check_router)
app.include_router(storage_router)


async def main() -> None:
    await init_db()
    
    
if __name__ == "__main__":
    asyncio.run(main())
    uvicorn.run("main:app", host="0.0.0.0", reload=True)