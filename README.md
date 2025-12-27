#🐕 **Dog Walker Live Tracking App (MVP)**

A real-time web application that allows a dog owner to track their dog walker’s live location, route, and distance covered during a walk.
Built as a scalable MVP with modern web technologies and real-time communication.

##✨**Features**

📍 Live location tracking of the dog walker

🗺️ Interactive map using OpenStreetMap (Leaflet)

🧭 Route visualization (polyline of the path taken)

📏 Distance covered calculation

🔁 Real-time updates using WebSockets

👥 Separate Owner and Walker views

⚡ Built with FastAPI (ASGI) for scalability

##🏗️ **Tech Stack**
###Backend

FastAPI – ASGI web framework

Uvicorn – ASGI server

WebSockets – real-time communication

###Frontend

HTML / CSS / JavaScript

Leaflet.js – interactive maps (OpenStreetMap)

Browser Geolocation API

###Hosting (planned / supported)

Railway / Render / Fly.io

Supports WebSocket-compatible hosting


##📂 Project Structure

dog-tracker/
│
├── backend/
│   ├── main.py              # FastAPI backend with WebSocket logic
│   ├── requirements.txt     # Python dependencies
│   └── frontend/
│       ├── owner.html       # Owner dashboard
│       └── walker.html      # Walker live tracking page
│
└── README.md


##🔁 **How it works (High-level)**

The walker opens walker.html

Browser requests location permission

Location is sent continuously via WebSocket

The owner opens owner.html

Receives walker’s live location

Sees route and distance updated in real time

Backend acts as a WebSocket relay

Walker → Backend → Owner

Owner location is never sent to the walker

##▶️ **Running Locally**
1️⃣ Install dependencies

```bash
pip install -r requirements.txt

2️⃣ Start the backend server

```bash
python -m uvicorn main:app --reload

Server runs at:

http://127.0.0.1:8000


3️⃣ Open frontend

Open these files directly in your browser:

frontend/walker.html

frontend/owner.html

⚠️ Make sure the backend is running before opening the frontend.


🌍 Hosting Notes

Backend must be hosted on a platform that supports ASGI + WebSockets

Frontend can be:

Served by the backend

Or hosted separately (Netlify, Vercel, etc.)

WebSocket URL should be updated to the hosted backend domain



🚀 Future Improvements (Planned)

🔐 Authentication (Owner ↔ Walker pairing)

📊 Walk history & analytics

🧠 AI insights (pace, walk quality, alerts)

📱 Mobile-friendly UI

🌐 Google Maps integration

🐕 Multiple dogs / walkers support



👤 Author

Sukhleen Kaur
Software Engineer | Python | FastAPI | Real-time Systems
