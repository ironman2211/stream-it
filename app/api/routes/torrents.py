from http.client import HTTPException

from fastapi import APIRouter
from app.models.torrent import TorrentCreate
from app.services.torrent_engine import torrent_engine

router = APIRouter()

@router.post("/torrents")
def add_torrent(data: TorrentCreate):
    return torrent_engine.add_magnet(data.magnet_link)

@router.get("/torrents/{torrent_id}")
def get_status(torrent_id: str):
    status = torrent_engine.get_status(torrent_id)

    if not status:
        raise HTTPException(status_code=404, detail="Torrent not found")

    return status