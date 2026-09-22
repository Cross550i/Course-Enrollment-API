from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime


class CourseCreate(BaseModel):
    title: str
    max_student: int = Field(gt=0, lt=31)
    date: datetime


class CourseResponse(BaseModel):
    id: int
    title: str
    max_student: int = Field(gt=0, lt=31)
    date: datetime

    model_config = ConfigDict(from_attributes=True)


class StudentCreate(BaseModel):
    name: str
    email: EmailStr = Field(description="User email")


class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr = Field(description="User email")
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
