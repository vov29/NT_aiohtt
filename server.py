import aiohttp
from aiohttp import web
from datetime import datetime
ads = {}
ads_id = 1
async def create_ad(request):
    global ads_id
    data = await request.json()
    data_ads = {
        'id': ads_id,
        'header': data['header'],
        'discript': data['discript'],
        'date': datetime.now().isoformat(),
        'name': data['name']

    }
    ads[ads_id] = data_ads
    ads_id += 1
    return web.json_response(data_ads, status = 201)
async def get_ads(request):
    return web.json_response(list(ads.values()))
async def delete_ads(request):
    ads_user_id = int(request.match_info['id'])
    if ads_user_id in ads:
        del ads[ads_user_id]
        return web.json_response({'message': 'ads deleted'}, status = 200)
    return web.json_response({'error': 'smth goes wrong'}, status = 404)
r = web.Application()
r.router.add_post('/ads', create_ad)       
r.router.add_get('/ads', get_ads)
r.router.add_delete('/ads/{id}', delete_ads)
web.run_app(r, host = '127.0.0.1', port = 8080)