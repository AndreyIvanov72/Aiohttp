from aiohttp import web
import uuid
from datetime import datetime

app = web.Application()

ads = []

async def create_ad(request):
    data = await request.json()
    ad_id = str(uuid.uuid4())  
    data['id'] = ad_id  
    data['created_at'] = datetime.now().isoformat() 
    ads.append(data)
    return web.json_response({"message": "Объявление создано", "id": ad_id, "datetime":data['created_at']})

async def get_ad(request):
    ad_id = request.match_info['ad_id']
    ad = next((ad for ad in ads if ad.get('id') == ad_id), None)
    if ad:
        return web.json_response(ad)
    else:
        return web.json_response({"message": "Объявление не найдено"}, status=404)

async def update_ad(request):
    ad_id = request.match_info['ad_id']
    data = await request.json()
    ad = next((ad for ad in ads if ad.get('id') == ad_id), None)
    if ad:
        ad.update(data)
        return web.json_response({"message": "Изменения успешно внесены"})
    else:
        return web.json_response({"message": "Объявление не найдено"}, status=404)

async def delete_ad(request):
    ad_id = request.match_info['ad_id']
    ad = next((ad for ad in ads if ad.get('id') == ad_id), None)
    if ad:
        ads.remove(ad)
        return web.json_response({"message": f"Объявление № {ad_id} успешно удалено"})
    else:
        return web.json_response({"message": "Объявление не найдено"}, status=404)

async def get_all_ads(request):
    return web.json_response(ads)

app.router.add_post('/ad', create_ad)
app.router.add_get('/ad/{ad_id}', get_ad)
app.router.add_put('/ad/{ad_id}', update_ad)
app.router.add_delete('/ad/{ad_id}', delete_ad)
app.router.add_get('/ads', get_all_ads)

if __name__ == '__main__':
    web.run_app(app)