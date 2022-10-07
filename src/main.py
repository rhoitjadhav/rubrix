# Packages
import uvicorn
from fastapi import FastAPI

# Modules
from config import PROJECT_NAME
from apis.apis import router as api_router

app = FastAPI(title=PROJECT_NAME)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
