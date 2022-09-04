import re
import aiohttp
import asyncio
# from pprint import pprint
from bs4 import BeautifulSoup
from .random_user_agent import rand


class MuzTv:
    def __init__(self) -> None:
        self.url = 'http://muztv.net/'
        self.headers = {
            'Accept': '*/*',
            'Connection': 'keep-alive',
            "User-Agent": rand()
        }
        self.s = None
        
    async def start(self):
        self.s : aiohttp.ClientSession = aiohttp.ClientSession()
    
    
    async def close(self):
        await self.s.close()
    
    async def getPage(self, url: str) -> BeautifulSoup:
        if not url.startswith(self.url):
            url = self.url + url
        try:
            resp: aiohttp.ClientResponse = await self.s.get(url, headers=self.headers)
            if resp.status != 200:
                return print(f"Bunday sahifa mavjud emas!\n {url}")
            txt = await resp.text()
            return BeautifulSoup(txt, 'html.parser')
        except Exception as e:
            return print(e)
    
    async def details(self, url):
        bs: BeautifulSoup = await self.getPage(url)
        if bs is None:
            return
        
        mcont = bs.find('div', attrs={'id': "m-cont"})
        fmain = mcont.find('div', attrs={'class': "fmain"})
        
        res = {}
        
        res['name'] = fmain.find('h1').text.strip()
        ul = fmain.find('ul', attrs={'class': 'finfo'})
        # res['category'] = ul.find('a').text.strip()
        res['url'] = fmain.find('a', attrs={'class': "fbtn fx-row fx-middle fdl"})['href']
        
        return res
    
    
    async def search(self, query: str, page=1):
        resp: aiohttp.ClientResponse = await self.s.post(
            self.url,
            params={
                'do': 'search',
                'subaction': 'search',
                'search_start': page,
                'full_search': 0,
                'result_from': (page-1)*20 + 1,
                'story': query
            },
            headers=self.headers
        )
        if resp.status != 200:
            return
        
        bs = BeautifulSoup(await resp.text(), 'html.parser')
        NOT_FOUNT_TEXT = "К сожалению, поиск по сайту не дал никаких результатов. Попробуйте изменить или сократить Ваш запрос."
        mcont = bs.find('div', attrs={'id': "mcont"})
        if not NOT_FOUNT_TEXT in mcont.text:
            mcont = mcont.find('div', attrs={'id': "m-cont"})
            form = mcont.find('div', attrs={'class': "berrors"})
            txt = form.text
            n = re.search(r"По Вашему запросу найдено ([0-9]+) ответов", txt).group(1)
            res = {'count': int(n)}
            
            musics = mcont.find_all('div', attrs={'class': "play-item fx-row fx-middle js-item"})
            musics_list = [
                {
                    'name': x['data-title'], 
                    'url': x['data-track']
                } for x in musics]
            res['musics'] = musics_list
            return res
                
        else:
            return
        
        
    async def top(self):
        bs: BeautifulSoup = await self.getPage('top.html')
        if bs is not None:
            mcont = bs.find('div', attrs={'id': 'm-cont'})
            musics = mcont.find_all('div', {'class': "play-item fx-row fx-middle js-item"})
            return [
                {
                    'name': x['data-title'], 
                    'url': x['data-track']
                } for x in musics
                ]
            

# async def main():
#     m = MuzTv()
#     await m.start()
    
#     # print(await m.details("mp3/23775-alisher-zokirov-osha-kun.html"))
#     # pprint(await m.search("Yulduz Usmonova"))
#     pprint(await m.top())
    
    
#     await m.close()
    
# if __name__ == '__main__':
#     asyncio.run(main())
    