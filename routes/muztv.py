from fastapi import APIRouter, status, HTTPException, Body
from schemas.muztv_musics import TopMusics, SearchResult
from parsers.muztv import MuzTv
from typing import Optional
from models.muztv import Query


muztv_router = APIRouter(tags=["Muztv.net"])
m = MuzTv()


@muztv_router.on_event('startup')
async def on_startup():
    await m.start()
    
    
@muztv_router.on_event('shutdown')
async def on_shutdown():
    await m.close()
    
 
@muztv_router.get("", deprecated=True)
async def hello_world() -> dict:
    """test hello world"""
    return {"message": "hello world"}
    
 
    
@muztv_router.post(path='/search/', response_model=SearchResult)
async def search(q: Query = Body(...)) -> SearchResult:
    """
    ## Search any music
    Parametrs:
    - **query**:str [required] search query
    - **page**:int [optional, default=1] search page
    """
    res = await m.search(q.query, q.page)
    if res is not None:
        return SearchResult(**res)
    
    raise HTTPException(
        status_code=status. HTTP_404_NOT_FOUND,
        detail="Not found music on this query"
    )


@muztv_router.get(path="/top", response_model=TopMusics)
async def top() -> TopMusics:
    """Top 100 musics list"""
    res = await m.top()
    if res is not None:
        return TopMusics(musics=res)
    
    raise HTTPException(
        status_code=status. HTTP_404_NOT_FOUND,
        detail="Not found any music"
    )
