import uvicorn

from starlette.applications import Starlette
from starlette.responses import JSONResponse

from datastore import Datastore

bad_urls = set(["123.123.123.123:80/malware/234234/3",
                "234.234.234.234:555/virus/there?",
                "345.345.345.345:774/virus/here?please=no",
                "345.345.345.345:774/virus/here?please=yes",
                "maps.google.co.uk/index.html"])

app = Starlette(debug=True)
datastore = Datastore()

@app.on_event("startup")
async def start_datastore():
    await datastore.connect()
    #TODO: Don't do this here, we'll overwrite stuff other
    # things write
    for url in bad_urls:
        await datastore.set_bad_url(url)

@app.on_event("shutdown")
async def stop_datastore():
    await datastore.disconnect()

@app.route('/')
async def homepage(request):
        return JSONResponse({}, status_code=204)

@app.route('/urlinfo/1/{hostname_port}/{path_query:path}')
async def get_is_url_bad(request):

        hostname_port = request.path_params['hostname_port']
        path = request.path_params['path_query']

        url = hostname_port + "/" + path

        response = await datastore.get_is_url_bad(url)

        if response:
            return JSONResponse({url:response}, status_code=200)
        else:
            return JSONResponse({}, status_code=204)

if __name__ == '__main__':
        uvicorn.run(app, lifespan='on', host='0.0.0.0', port=8000)

