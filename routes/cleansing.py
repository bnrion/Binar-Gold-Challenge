from typing import Optional
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import Query
from services.cleansing import CleansingServices
from fastapi import FastAPI, File, UploadFile
from io import StringIO
import pandas as pd

router = APIRouter()


@router.get("/cleansing-text")
async def cleansing_tweets_text(
        text: str
):
    result = await CleansingServices().cleansing(type="text", text=text)
    return result


@router.post("/cleansing-file")
async def cleansing_tweets_file(
        file: UploadFile = File(...)
):
    data = pd.read_csv(StringIO(str(file.file.read(), 'latin-1')), encoding='latin-1')
    result = await CleansingServices().cleansing(type="file", text=data)
    return result
