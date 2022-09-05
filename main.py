import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routes.muztv import muztv_router

app = FastAPI(debug=True, )

app.include_router(muztv_router, prefix="/muztv")


@app.get("/", deprecated=True)
async def home_page() -> dict:
    return HTMLResponse(
        content="<p>Simple music API</p>"
            "Show more <a href='/docs'>docs</a> or <a href='/redoc'>redoc</a>"
        
    )


if __name__ == '__main__':
    uvicorn.run(app)