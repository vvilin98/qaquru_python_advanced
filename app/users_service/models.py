from pydantic import BaseModel


# Структура данных
class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class SupportData(BaseModel):
    url: str
    text: str


class UserResponse(BaseModel):
    data: UserData
    support: SupportData
