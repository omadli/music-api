from typing import List
from pydantic import BaseModel, AnyHttpUrl


class Music(BaseModel):
    """Music model"""
    name: str
    url: AnyHttpUrl
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Doston Ergashev - O'shalar",
                "url" : "http://muztv.net/mp3/Uzbek/Doston%20Ergashev%20-%20O%27shalar.mp3"
            }
        }


class SearchResult(BaseModel):
    """Searched musics result model"""
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
    """Top 100 musics list model"""
    musics: List[Music]
    
    class Config:
        schema_extra = {
            "example": {
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
    