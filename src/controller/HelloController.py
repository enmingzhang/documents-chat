import json
from typing import Union

from fastapi import APIRouter

from src.storage.model import BaseRepository
from src.storage.model.File import File
from src.storage.model.Message import Message

router = APIRouter()


@router.get("/")
def read_root():
    fileList = BaseRepository.session.query(File).all()
    msgList = BaseRepository.session.query(Message).all()

    file_list_dict = []
    for f in fileList:
        file_list_dict.append(f.to_dict())

    return msgList


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
