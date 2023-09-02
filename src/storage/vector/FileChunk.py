from qdrant_client.http.models import MatchValue
from qdrant_client.models import Filter, FieldCondition

from src.storage.vector.BaseVectorRepository import BaseVectorRepository


# 文件分片向量的crud 和相似查询
class FileChunk(BaseVectorRepository):

    # 获得所有的collection 数组
    def get_collections(self):
        return self.get_client().get_collections()

    # 统计collection中的point总数
    def count_collection(self):
        result = self.get_client().count(self.collection_name)
        return result

    # 根据id获得point
    def get_point(self, id: int):
        file_filter = Filter(
            must=[FieldCondition(key="id", match=MatchValue(value=id))]
        )
        result = self.get_client().scroll(self.collection_name, scroll_filter=file_filter, with_payload=True, limit=1)
        return result

    def count_file_points(self, file_id: int):
        file_filter = Filter(
            must=[FieldCondition(key="metadata.file_id", match=MatchValue(value=file_id))]
        )
        result = self.get_client().count(self.collection_name, scroll_filter=file_filter, with_payload=True, limit=100)
        return result

    # 获得文件的向量数组
    def get_file_points(self, file_id: int):
        file_filter = Filter(
            must=[FieldCondition(key="metadata.file_id", match=MatchValue(value=file_id))]
        )

        result = self.get_client().scroll(self.collection_name, scroll_filter=file_filter, with_payload=True,
                                          limit=100, )
        return result

    # 删除向量
    def delete_points(self, file_id: int):
        file_filter = Filter(
            must=[FieldCondition(key="metadata.file_id", match=MatchValue(value=file_id))]
        )
        self.get_client().delete(self.collection_name, points_selector=file_filter)

    # 保存向量
    def save_points(self, points):
        self.get_client().upsert(self.collection_name, points=points, wait=True)
        return True

    # 搜索相似向量
    def search_points(self, file_id: int, vector):
        file_filter = Filter(
            must=[FieldCondition(key="metadata.file_id", match=MatchValue(value=file_id))]
        )
        self.get_client().search(self.collection_name, query_vector=vector, query_filter=file_filter)
        return

