from qdrant_client import QdrantClient

from src.config.QdrantConfig import QdrantConfig


class BaseVectorRepository:

    collection_name = None

    def __init__(self):
        self.qdrant_config = QdrantConfig().get_qdrant_config()
        self.collection_name = self.qdrant_config["collection"]
        self.host = self.qdrant_config["host"]
        self.port = self.qdrant_config["port"]

    def get_client(self):
        client = QdrantClient(host=self.host, port=self.port)
        return client
