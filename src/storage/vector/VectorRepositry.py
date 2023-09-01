from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter, FieldCondition, MatchValue

from src.config.QdrantConfig import QdrantConfig

qdrant_config = QdrantConfig().get_qdrant_config()

collection_name = qdrant_config["collection"]

# 查询集合
client = QdrantClient(host=qdrant_config["host"], port=qdrant_config["port"])


query_filter = Filter(must=[FieldCondition(key="metadata.file_id", match=MatchValue(value=10935))])

result = client.scroll(collection_name, scroll_filter=query_filter)

# 打印查询结果
print(result)
