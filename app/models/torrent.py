from pydantic import BaseModel

class TorrentCreate(BaseModel):
    magnet_link: str
    
   