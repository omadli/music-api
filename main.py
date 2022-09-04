import uvicorn
from fastapi import FastAPI
from routes.muztv import muztv_router

app = FastAPI(debug=True, )

app.include_router(muztv_router, prefix="/muztv")


if __name__ == '__main__':
    uvicorn.run(app)