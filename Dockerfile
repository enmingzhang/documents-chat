FROM python:3.10

WORKDIR /root
COPY requirements.txt requirements.txt

RUN python -m pip install -i https://mirrors.cloud.tencent.com/pypi/simple/ -r requirements.txt

RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list.d/debian.sources && \
    sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list.d/debian.sources

WORKDIR /root/chat_backend

ENV WORKER_NUM=16
ENV MAIN_APP="main"
CMD ["bash", "start.sh"]
