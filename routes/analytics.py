from typing import Optional
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import Query
from services.analytics import AnalyticServices

router = APIRouter()

@router.get( "/sentiment")
async def sentiment_analytics(
    text: str 
):
    result = await AnalyticServices().get_sentiment_analytics(text= text)
    return result