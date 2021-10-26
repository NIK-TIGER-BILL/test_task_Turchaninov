from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title='Turchaninov_test_task',
    description='Test task for company Turchaninov'
)

templates = Jinja2Templates(directory='templates')


@app.get('/')
async def get(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    counter = 1
    try:
        while True:
            data = await websocket.receive_json()
            if data.get('message'):
                data['counter'] = counter
                counter += 1
                await websocket.send_json(data)
            else:
                print("error: don't find message in json data")
    except WebSocketDisconnect:
        pass
