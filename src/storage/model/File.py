from datetime import datetime

from sqlalchemy import (Column, Integer, String, Enum, DECIMAL, DateTime, Boolean)
from sqlalchemy.orm import declarative_base

# 基础类
Base = declarative_base()

class File(Base):
    __tablename__ = "file"
    # 对于必须插入的字段，采用nullable=False进行约束，它相当于NOT NULL
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    name = Column(String, index=True, nullable=False, comment="名称")
    create_time = Column(DateTime, default=datetime.now, comment="创建时间")
    update_time = Column(DateTime, onupdate=datetime.now, comment="最后更新时间")

    def __str__(self):
        return f"object : <id:{self.id} name:{self.name}>"

    def to_dict(self):
        # 将类实例转换为字典
        data = {"id": self.id, "name": self.name, "create_time": self.create_time.__str__()}
        return data

