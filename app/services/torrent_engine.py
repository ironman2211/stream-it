import libtorrent as lt

class TorrentEngine:
    def __init__(self):
        # create session (core engine)
        self.session = lt.session()
        self.session.listen_on(6881, 6891)

        # store active torrents
        self.handles = {}

    def add_magnet(self, magnet_link: str):
        params = {
            "save_path": "./downloads/"
        }

        # add torrent
        handle = lt.add_magnet_uri(self.session, magnet_link, params)

        torrent_id = str(handle.info_hash())
        self.handles[torrent_id] = handle

        return {"torrent_id": torrent_id}

    def get_status(self, torrent_id: str):
        handle = self.handles.get(torrent_id)
        if not handle:
            return None

        s = handle.status()

        return {
            "name": s.name,
            "progress": round(s.progress * 100, 2),
            "download_rate": s.download_rate,
            "upload_rate": s.upload_rate,
            "peers": s.num_peers,
            "state": str(s.state),
        }

torrent_engine = TorrentEngine()