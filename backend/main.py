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
walk_states = {}


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
                walk_states.setdefault(walk_id, "stopped")
                print(f"{role} joined walk {walk_id}")
            elif data["type"] == "status":
                # Use walk_id from message data to ensure consistency
                msg_walk_id = data.get("walk_id", walk_id)
                walk_states[msg_walk_id] = data["state"]

                owner_ws = walk_sessions.get(msg_walk_id, {}).get("owner")
                if owner_ws:
                    await owner_ws.send_json(data)
            elif data["type"] == "location":
                # Use walk_id from message data to ensure consistency
                msg_walk_id = data.get("walk_id", walk_id)
                
                # Debug logging
                print(f"Location update for walk_id: {msg_walk_id}, state: {walk_states.get(msg_walk_id)}, owner_connected: {msg_walk_id in walk_sessions and 'owner' in walk_sessions.get(msg_walk_id, {})}")
                
                if walk_states.get(msg_walk_id) != "started":
                    print(f"Ignoring location update - walk not started for {msg_walk_id}")
                    continue  # ignore stray GPS updates

                owner_ws = walk_sessions.get(msg_walk_id, {}).get("owner")
                if owner_ws:
                    print(f"Forwarding location to owner for {msg_walk_id}")
                    await owner_ws.send_json(data)
                else:
                    print(f"No owner connected for walk_id {msg_walk_id}")


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