from fastapi import APIRouter
from app.models.torrent import TorrentCreate
from app.services.torrent_manager import torrent_manager

router = APIRouter()

@router.post("/torrents")
def add_torrent(data: TorrentCreate):
    return torrent_manager.add_torrent(data.magnet_link)

@router.get("/torrents")
def list_torrents():
    return torrent_manager.list_torrents()