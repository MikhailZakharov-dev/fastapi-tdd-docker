from fastapi import FastAPI, Depends
from app.config import get_settings, Settings
from tortoise.contrib.fastapi import register_tortoise
import os

kek = FastAPI()


register_tortoise(
  kek,
  db_url=os.environ.get("DATABASE_URL"),
  modules={"models": ["app.models.tortoise"]},
  generate_schemas=True,
  add_exception_handlers=True
)

@kek.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
      "ping": "pong!",
      "environment": settings.environment,
      "testing": settings.testing
    }