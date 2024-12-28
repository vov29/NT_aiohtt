import aiohttp, asyncio
url = 'http://127.0.0.1:8080/ads'
create_ad = [

    {"header":"Сделаю ремонт",
     "discript": "Быстро и качественно",
     "date": "10 декабря 2024",
     "name": "Боря"},
    {"header":"Пропала собака",
     "discript": "Черная немецкая овчарка",
     "date": "11 декабря 2024",
     "name": "Алена"}

]
async def create_ads():
    async with aiohttp.ClientSession() as session:
        for i in create_ad:
            async with session.post(url, json = i) as response_post:
                print(response_post.status)
                print(await response_post.json())
        print()
        async with session.get(url) as response_get:
            print(response_get.status)
            print(await response_get.json())
        ads_id = 1
        async with session.delete(f'{url}/{ads_id}') as response_delete:
            if response_delete.status == 200:
                response_data = await response_delete.json()
                print(response_data.get('message', 'ads deleted'))
            else:
                print('Объявление не удалено', await response_delete.text())
asyncio.run(create_ads())                