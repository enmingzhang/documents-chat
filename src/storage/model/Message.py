# 对话消息, 如果是答案 需要设置question_id
from datetime import datetime

from sqlalchemy import Integer, Column, DateTime, String
from sqlalchemy.orm import declarative_base

# 基础类
Base = declarative_base()

class Message(Base):
    __tablename__ = "ai_question"

    # 对于必须插入的字段，采用nullable=False进行约束，它相当于NOT NULL
    id          = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    user_id     = Column(Integer, index=True, nullable=False, comment="用户id")
    file_id     = Column(Integer, index=True, nullable=False, comment="文件id")
    role        = Column(String,  index=False, nullable=False, comment="角色")
    message      = Column(String,  index=False, nullable=False, comment="角色")
    source      = Column(String,  index=False, nullable=False, comment="角色")
    create_time = Column(DateTime, default=datetime.now,  comment="创建时间")
    update_time = Column(DateTime, onupdate=datetime.now, comment="最后更新时间")

    def __init__(self):
        self.id = None
        self.message = None
        self.create_time = None
        self.file_id = None
        self.user_id = None
        self.source = None

    def __str__(self):
        return f"object : <id:{self.message} name:{self.message}>"

    def to_dict(self):
        # 将类实例转换为字典
        data = {"id":      self.id,
                "user_id": self.user_id,
                "file_id": self.file_id,
                "role":    self.role,
                "message": self.message,
                "source":  self.source,
                "create_time": self.create_time.__str__()
                }
        return data
