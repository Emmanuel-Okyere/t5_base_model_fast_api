"""Entry point the fast api"""

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from .api.v1.translate import router


app = FastAPI(title="Translate APP")
app.include_router(router)


@app.get("/", include_in_schema=False)
async def root():
    """Default root for the application where users get redirected to /doc"""
    return RedirectResponse(url="/docs")
