from fastapi import FastAPI, Depends
from .routers import auth, users
from . import schemas, oauth2, models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

prefix = "/api"
app.include_router(router=auth.router, prefix=prefix)
app.include_router(router=users.router, prefix=prefix)


# ログインテスト用
# 本来は要りません
@app.get("/api")
def root(current_user: schemas.User = Depends(oauth2.get_current_user)):
    return {"current_user": current_user}
