from fastapi import FastAPI

from invoice_router import router as invoice_router
from user_router import router as user_router

app = FastAPI(title="LLM Powered Database Agent")

app.include_router(user_router)
app.include_router(invoice_router)