import uuid
import random

class TorrentManager:
    def __init__(self):
        self.torrents = {}

    def add_torrent(self, magnet_link: str):
        torrent_id = str(uuid.uuid4())
        torrent = {
            "id": torrent_id,
            "name": f"Torrent-{torrent_id[:5]}",
            "progress": 0,
            "download_speed": 0,
            "peers": 0,
        }
        self.torrents[torrent_id] = torrent
        return torrent

    def list_torrents(self):
        for t in self.torrents.values():
            t["progress"] = min(100, t["progress"] + random.uniform(1, 5))
            t["download_speed"] = random.randint(100, 500)
            t["peers"] = random.randint(1, 20)
        return list(self.torrents.values())

torrent_manager = TorrentManager()