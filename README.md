# 🐕 Dog Walker Live Tracking App

**A real-time web application to track a dog walker’s location, route, and distance.**

---

## ✨ Features
- 📍 Live location tracking
- 🗺️ Route visualization
- 📏 Distance calculation
- 🔁 WebSocket-based updates

---

## 🏗️ Tech Stack
### Backend
- FastAPI
- Uvicorn
- WebSockets

### Frontend
- HTML, CSS, JavaScript
- Leaflet.js (OpenStreetMap)

---

## 📂 Project Structure
```text
dog-tracker/
│
├── backend/
│   ├── main.py              # FastAPI backend
│   ├── requirements.txt     # Python dependencies
│   └── frontend/
│       ├── owner.html       # Owner dashboard
│       └── walker.html      # Walker live tracking page
│
└── README.md
```
---

## 🔁 How it works

1. The **walker** opens `walker.html`
2. The browser requests location permission
3. The walker’s location is sent via WebSocket
4. The **owner** opens `owner.html`
5. The owner receives live updates on the map
6. Route and total distance are updated in real time

The owner’s location is **never shared with the walker**.

---

## ▶️ Running Locally

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 2️⃣ Start the backend server
```bash
python -m uvicorn main:app --reload
```

Server will start at: 

http://127.0.0.1:8000

### 3️⃣ Open the frontend

Open these files directly in your browser:

frontend/walker.html

frontend/owner.html

⚠️ The backend must be running before opening the frontend.

---

## 🚀 Future Improvements

-🔐 Authentication (Owner ↔ Walker pairing)

-📊 Walk history and analytics

-🧠 AI insights (pace analysis, alerts)

-📱 Mobile-friendly UI

-🌐 Google Maps integration

-🐕 Support for multiple walkers and dogs



## 👤 Author

Sukhleen Kaur
Software Engineer | Python | FastAPI | Real-time Systems
