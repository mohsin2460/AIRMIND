import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from routers.auth import router as auth_router
from routers.topics import router as topics_router
from routers.questions import router as questions_router
from routers.tests import router as tests_router
from routers.plans import router as plans_router

load_dotenv()

app = FastAPI()

origins = [o.strip() for o in os.getenv("CORS_ORIGINS", "").split(",") if o.strip()] or ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"ok": True}

app.include_router(auth_router)
app.include_router(topics_router)
app.include_router(questions_router)
app.include_router(tests_router)
app.include_router(plans_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", "4000")), reload=True)
