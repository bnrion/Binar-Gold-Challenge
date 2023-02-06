from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from schemas.response import ValidationErrorSchema, SuccessSchema

app = FastAPI(
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ValidationErrorSchema},
        status.HTTP_200_OK: {"model": SuccessSchema},
    }
)

@app.get("/")
async def index():
    return JSONResponse(
        content= {
            "ok": True,
            "code": 200,
            "data": {"version": "0.1.2"},
            "message": "Success",
    }
)

from routes import analytics
from routes import cleansing

app.include_router(analytics.router, tags=["Analytics"])
app.include_router(cleansing.router, tags=["Cleansing"])
