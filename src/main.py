# Packages
import uvicorn
from fastapi import FastAPI

# Modules
from config import PROJECT_NAME

app = FastAPI(title=PROJECT_NAME)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

