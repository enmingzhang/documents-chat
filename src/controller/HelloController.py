import json
from typing import Union

from fastapi import APIRouter

from src.storage.model import BaseRepository
from src.storage.model.File import File
from src.storage.model.Message import Message
from src.storage.vector.FileChunk import FileChunk

router = APIRouter()


@router.get("/")
def read_root():
    fileList = BaseRepository.session.query(File).all()
    msgList = BaseRepository.session.query(Message).all()

    file_list_dict = []
    for f in fileList:
        file_list_dict.append(f.to_dict())

    return msgList

@router.get("/hello")
def read_root():

    hits, _offset = FileChunk().get_point_list(10935)
    print(len(hits))
    print(_offset)

    # for hit in hits:
    #     print(hit)

    return hits



@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
