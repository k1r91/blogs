import json
import aiohttp
from aiohttp import web
from logging import getLogger, StreamHandler, DEBUG

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

assert factorial(1) == 1
assert factorial(6) == 720

async def handler_factorial(request):
    value = int(request.query['value'])
    if value == 1:
        return web.json_response({'value': 1})

    url = '{}://{}{}'.format(request.scheme, request.host, request.path)

    async with aiohttp.ClientSession() as session:
        resp = await session.get(url, params={'value': value - 1})
        data = json.loads(await resp.text())
        return web.json_response({'value': value * int(data['value'])})

if __name__ == '__main__':
    app = web.Application()
    app.add_routes([web.get('/factorial', handler_factorial)])

    log = getLogger('aiohttp.access')
    log.setLevel(DEBUG)
    log.addHandler(StreamHandler())
    log_format = '%a %t "%r" %s %b "%{User-Agent}i" %Tfsec'

    web.run_app(app, port=8000, access_log=log, access_log_format=log_format)