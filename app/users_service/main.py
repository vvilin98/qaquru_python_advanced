from fastapi import FastAPI
from app.users_service.models import UserData, UserResponse
from fastapi import HTTPException, Response

from data import db

app = FastAPI()


@app.get("/")
def get_status():
    return "Hello world : Status code 200"


@app.get("/api/users/{user_id}", response_model=UserResponse)
def get_single_user(user_id: int) -> UserResponse:
    user = db.users_db.get(user_id)
    if user:
        return UserResponse(data=user, support=db.support_info)
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/api/users/", response_model=UserData)
def create_user(user: UserData) -> UserData:
    if user.id in db.users_db:
        raise HTTPException(status_code=409, detail="User already exists")
    db.users_db[user.id] = user
    return user


@app.delete("/api/users/{user_id}")
def delete_user(user_id: int) -> Response:
    db.users_db.get(user_id)
    if db.users_db.get(user_id):
        del db.users_db[user_id]
        return Response(status_code=204)
    raise HTTPException(status_code=404, detail="User not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8003)
