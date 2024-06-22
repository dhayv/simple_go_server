from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Albums(BaseModel):
    id: str
    title: str
    artist: str
    price: float


albums = [
    {"id": "1", "title": "Blue Train", "artist": "John Coltrane", "price": 56.99},
    {"id": "2", "title": "Jeru", "artist": "Gerry Mulligan", "price": 17.99},
    {"id": "3", "title": "Sarah Vaughn and Clifford Brown", "artist": "Sarah Vaughn", "price": 39.99},
]


@app.get("/")
def main():
    return {"hello": "world"}


@app.get("/albums")
def getAlbum(id: int, album: Albums):
    return album


@app.post("/albums")
def postAlbum(id: int, album: Albums):
    

    return


@app.get("/albums/{id}")
def getAlbumById(id: int, album: Albums):
    return album.id


if __name__ == "__main__":
    main()
