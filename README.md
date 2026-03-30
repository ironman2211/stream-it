# 🚀 Torrent Streaming App

A full-stack **Torrent Streaming Platform** that lets you stream videos directly from torrents while they download.

---

## 📌 Features

* ⚡ Add torrent via magnet link
* 📊 Real-time download stats (speed, peers, progress)
* 🎬 Stream video before full download
* 📁 File selection inside torrents
* 🔄 Automatic video conversion (FFmpeg)
* 🌐 Web UI (React)

---

## 🏗️ Project Roadmap

### 🧱 Phase 1: Backend Foundation (FastAPI MVP) ✅

**Goal:** Basic API + mock torrent system

* [x] Setup FastAPI project
* [x] Create project structure
* [x] Health check API
* [x] Add torrent (mock)
* [x] List torrents
* [x] Simulated progress

**Output:**

* [x] `/api/torrents` working
* [x] Swagger docs

---

### ⚙️ Phase 2: Real Torrent Engine 🔥

**Goal:** Integrate real torrent handling

**Tech:** `libtorrent`

* [x] Install libtorrent
* [x] Initialize torrent session
* [x] Add magnet link support
* [x] Fetch metadata
* [x] Track progress, peers, speed
* [x] Store torrents in memory

**Output:**

* [ ] Real downloading
* [ ] Live stats

---

### 📂 Phase 3: File Management

* [ ] List files in torrent
* [ ] Select file
* [ ] Prioritize video files
* [ ] Sequential downloading

**Output:**

* [ ] `/files` API
* [ ] `/select` API

---

### 🎬 Phase 4: Streaming Engine 🔥🔥

* [ ] `/stream/{torrent_id}/{file_id}` API
* [ ] HTTP Range Requests
* [ ] Partial file streaming
* [ ] Buffering logic

**Output:**

* [ ] Stream before download completes

---

### 🎥 Phase 5: Media Processing

**Tech:** `FFmpeg`

* [ ] Detect formats
* [ ] Convert to MP4
* [ ] Subtitle support

---

### 🌐 Phase 6: Frontend (React UI)

* [ ] Magnet input UI
* [ ] Torrent list
* [ ] Progress dashboard
* [ ] Video player
* [ ] File selector

---

### ⚡ Phase 7: Optimization

* [ ] Smart buffering
* [ ] Disk I/O optimization
* [ ] Bandwidth control
* [ ] Connection pooling

---

### 🔐 Phase 8: Production Features

* [ ] JWT authentication
* [ ] Multi-user support
* [ ] Database persistence
* [ ] Background workers
* [ ] Logging & monitoring

---

### ☁️ Phase 9: Deployment

**Tech:** Docker, Nginx, AWS/GCP

* [ ] Dockerize backend
* [ ] Reverse proxy setup
* [ ] Deploy API
* [ ] CDN for streaming

---

### 🧠 Phase 10: Advanced Features (Optional)

* [ ] Torrent search
* [ ] Peer-assisted streaming
* [ ] Mobile app
* [ ] HLS streaming

---

## 📊 Current Status

```
Phase 1 ✅ Completed
Phase 2 🔥 In Progress
```

---

## ⚙️ Tech Stack

* **Backend:** FastAPI
* **Torrent Engine:** libtorrent
* **Streaming:** HTTP Range Requests
* **Media Processing:** FFmpeg
* **Frontend:** React
* **Deployment:** Docker, Nginx

---

## 🚀 Getting Started

### 1. Clone Repo

```bash
git clone https://github.com/yourusername/torrent-streaming-app.git
cd torrent-streaming-app
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Server

```bash
uvicorn app.main:app --reload
```

### 4. Open API Docs

```
http://127.0.0.1:8000/docs
```

---

## 📁 Project Structure

```
app/
├── main.py
├── routes/
├── services/
├── models/
└── core/
```

---

## 🧑‍💻 Contributing

Pull requests are welcome. For major changes, open an issue first.

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.
Do not use it to download or distribute copyrighted content illegally.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

