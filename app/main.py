from starlette.applications import Starlette
from starlette.responses import JSONResponse
import uvicorn

bad_urls = set(["123.123.123.123",
                "234.234.234.234",
                "345.345.345.345"])
app = Starlette(debug=True)

@app.route('/')
async def homepage(request):
        return JSONResponse({'hello': 'world'})
@app.route('/url/{url}/')
async def homepage(request):
        url= request.path_params['url']
        return JSONResponse({url: url in bad_urls})



if __name__ == '__main__':
        uvicorn.run(app, host='0.0.0.0', port=8000)

