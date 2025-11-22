from fastapi import APIRouter
import os
from datetime import datetime

router = APIRouter()


@router.get("/version")
async def get_version():
    """
    Returns deployment version information.
    Useful for checking if deployment was successful and what version is running.
    """
    return {
        "commit_sha": os.environ.get("GIT_COMMIT_SHA", "unknown"),
        "build_time": os.environ.get("BUILD_TIME", "unknown"),
        "deployed_at": datetime.utcnow().isoformat() + "Z",
        "environment": os.environ.get("ENVIRONMENT", "unknown"),
    }

