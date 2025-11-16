from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
import os
from app.api import ping, summaries
from app.db import init_db
def create_application() -> FastAPI:
  application = FastAPI()
  
  register_tortoise(
    application,
    db_url=os.environ.get("DATABASE_URL"),
    modules={"models": ["app.models.tortoise"]},
    generate_schemas=True,
    add_exception_handlers=True
  )
  
  application.include_router(ping.router)
  application.include_router(summaries.router, prefix="/summaries", tags=["summaries"])  
  return application

kek = create_application()
  
init_db(kek)