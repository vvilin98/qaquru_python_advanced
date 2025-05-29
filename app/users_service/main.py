from fastapi import FastAPI
from app.users_service.models import UserData, UserResponse
from fastapi import HTTPException

from data import db

app = FastAPI()


@app.get("/")
def get_status():
    return "Hello world : Status code 200"


@app.get("/api/users/{user_id}", response_model=UserResponse)
def get_single_user(user_id: int):
    user = db.users_db.get(user_id)
    if user:
        return UserResponse(data=user, support=db.support_info)
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/api/users/", response_model=UserData)
def create_user(user: UserData):
    if user.id in db.users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    db.users_db[user.id] = user
    return user


@app.delete("/api/users/{user_id}")
def delete_user(user_id: int):
    db.users_db.get(user_id)
    if db.users_db.get(user_id):
        del db.users_db[user_id]
        raise HTTPException(status_code=200, detail="User deleted")
    raise HTTPException(status_code=404, detail="User not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8003)
