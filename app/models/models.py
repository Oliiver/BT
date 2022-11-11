"""
app.models.py
-------------
Defines the propper JSON to be sent and received from the API
"""
import typing
from pydantic import BaseModel, ValidationError, validator


class ConvertRequest(BaseModel):
    """Request for convert entpoint"""
    num_list: list[int | float]


class ConvertResponse(BaseModel):
    """Response for convert request"""
    str_list: list[str]


class MidRequest(BaseModel):
    """Request for mid request endpoint"""
    string: str


class MidResponse(BaseModel):
    """Response for mid request"""
    letter: str


class FormatNumberRequest(BaseModel):
    """Response for format_number request"""
    number: int

    @validator('number')
    def cannot_be_negative(cls, v):
        if v < 0:
            raise ValueError('Cannot be negativ')
        return v


class FormatNumberResponse(BaseModel):
    """Response for format_number request"""
    formatted_number: str


class OnlyIntsRequest(BaseModel):
    """Response for only_ints request"""
    value1: float | int
    value2: float | int


class OnlyIntsResponse(BaseModel):
    """Response for only_ints request"""
    truth_value: bool


class ZapRequest(BaseModel):
    """Response for Zap request"""
    list1: list[typing.Any]
    list2: list[typing.Any]


class ZapResponse(BaseModel):
    """Response for Zap request"""
    combined_list: list[tuple]
