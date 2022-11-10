"""app.routers.v1.py"""
import json
from fastapi import APIRouter, status, HTTPException

from app.internal.convert import convert
from app.internal.format_number import format_number
from app.internal.mid import mid
from app.internal.only_ints import only_ints
from app.internal.zap import zap

from app.models.models import (ConvertRequest, ConvertResponse,
                               FormatNumberRequest, FormatNumberResponse,
                               MidRequest, MidResponse,
                               OnlyIntsRequest, OnlyIntsResponse,
                               ZapRequest, ZapResponse)

v1 = APIRouter()


@v1.post("/convert/", tags=["Convert"], status_code=status.HTTP_200_OK, response_model=ConvertResponse)
async def only_ints_request(payload: ConvertRequest) -> ConvertResponse:
    try:
        str_list = convert(payload.num_list)
        response = ConvertResponse(str_list=str_list)
        return response
    except:
        raise HTTPException(status_code=400, detail='no values provided')


@v1.post("/format/", tags=["Format"], status_code=status.HTTP_200_OK, response_model=FormatNumberResponse)
async def only_ints_request(payload: FormatNumberRequest) -> FormatNumberResponse:
    try:
        formatted_number = format_number(payload.number)
        response = FormatNumberResponse(formatted_number=formatted_number)
        return response
    except:
        raise HTTPException(status_code=400, detail='no values provided')


@v1.post("/mid/", tags=["Mid"], status_code=status.HTTP_200_OK, response_model=MidResponse)
async def convert_request(payload: MidRequest) -> MidResponse:
    try:
        mid_letter = mid(payload.string)
        response = MidResponse(letter=mid_letter)
        return response
    except:
        raise HTTPException(status_code=400, detail='no string')


@v1.post("/only_ints/", tags=["OnlyInts"], status_code=status.HTTP_200_OK, response_model=OnlyIntsResponse)
async def only_ints_request(payload: OnlyIntsRequest) -> OnlyIntsResponse:
    try:
        truth_value = only_ints(payload.value1, payload.value2)
        response = OnlyIntsResponse(truth_value=truth_value)
        return response
    except:
        raise HTTPException(status_code=400, detail='no values provided')


@v1.post("/zap/", tags=["Zap"], status_code=status.HTTP_200_OK, response_model=ZapResponse)
async def only_ints_request(payload: ZapRequest) -> ZapResponse:
    try:
        combined_list = zap(payload.list1, payload.list2)
        response = ZapResponse(combined_list=combined_list)
        return response
    except:
        raise HTTPException(status_code=400, detail='no values provided')
