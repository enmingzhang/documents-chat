
from fastapi import FastAPI
from src.controller.HelloController import router as hello_router
from src.controller.ChatController import router as chat_router

app = FastAPI()

# 加载各个子路由
app.include_router(hello_router)
app.include_router(chat_router)