from typing import List
from pydantic import BaseModel, AnyUrl

class Music(BaseModel):
    name: str
    url: AnyUrl
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Doston Ergashev - O'shalar",
                "url" : "http://muztv.net/mp3/Uzbek/Doston%20Ergashev%20-%20O%27shalar.mp3"
            }
        }


class SearchResult(BaseModel):
    count: int
    musics: List[Music]
    
    class Config:
        schema_extra = {
            "example": {
                "count": 2,
                "musics" : [
                    {
                        "name": "Doston Ergashev - O'shalar",
                        "url" : "http://muztv.net/mp3/Uzbek/Doston%20Ergashev%20-%20O%27shalar.mp3"
                    },
                    {
                        'name': 'Dildora Niyozova - Onajonim',
                        'url': 'http://muztv.net/mp3/Uzbek/Dildora%20Niyozova%20-%20Onajonim.mp3'
                    },
                ]
            }
        }
    

class TopMusics(BaseModel):
    musics: List[Music]
    