from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
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
walk_sessions = {}



@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    role = None
    walk_id = None

    try:
        while True:
            data = await ws.receive_json()

            if data["type"] == "register":
                role = data["role"]
                walk_id = data["walk_id"]

                if walk_id not in walk_sessions:
                    walk_sessions[walk_id] = {}

                walk_sessions[walk_id][role] = ws
                print(f"{role} joined walk {walk_id}")

            elif data["type"] in ("location", "status"):
                if walk_id in walk_sessions:
                    owner_ws = walk_sessions[walk_id].get("owner")
                    if owner_ws:
                        await owner_ws.send_json(data)

                        
            elif data["type"] == "walk_stopped":
                owner_ws = walk_sessions.get(walk_id, {}).get("owner")
                if owner_ws:
                    await owner_ws.send_json({"type": "walk_stopped"})

    except WebSocketDisconnect:
        if walk_id and walk_id in walk_sessions:
            walk_sessions[walk_id].pop(role, None)
            if not walk_sessions[walk_id]:
                walk_sessions.pop(walk_id)
        print("Disconnected")

# Serve frontend files
frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")
#app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
app.mount("/static", StaticFiles(directory=frontend_path), name="static")



@app.get("/")
def landing_page():
    return FileResponse(os.path.join(frontend_path, "index.html"))

@app.get("/owner")
def owner_page():
    return FileResponse(os.path.join(frontend_path, "owner.html"))

@app.get("/walker")
def walker_page():
    return FileResponse(os.path.join(frontend_path, "walker.html"))