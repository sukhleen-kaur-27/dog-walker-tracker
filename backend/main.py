from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store all connected clients
clients = []

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    clients.append(ws)
    try:
        while True:
            data = await ws.receive_json()
            role = data.get("role")
            # Broadcast to all clients except the sender
            for client in clients:
                if client != ws:
                    # Only send owner location to owner page, not to walker
                    if role == "owner" and data.get("for_walker") != True:
                        continue
                    await client.send_json(data)
    except:
        clients.remove(ws)

# Serve frontend files
frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
