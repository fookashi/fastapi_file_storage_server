from fastapi import FastAPI
import uvicorn

from routers.health_check import health_check_router


app = FastAPI()
app.include_router(health_check_router)


def main() -> None:
    uvicorn.run("main:app", host="0.0.0.0")
    
    
if __name__ == "__main__":
    main()