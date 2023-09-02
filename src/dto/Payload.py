# 向量中的payload对象
class Payload:

    def __int__(self, id: int, user_id: int, file_id: int, title: str, type: str, create_time: str):
        self.id = id
        self.user_id = user_id
        self.file_id = file_id
        self.title = title
        self.type = type
        self.create_time = create_time

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "file_id": self.file_id,
            "title": self.title,
            "type": self.type,
            "create_time": self.create_time,
        }
