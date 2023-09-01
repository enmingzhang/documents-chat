import os

import yaml


# 向量数据库配置
class QdrantConfig:
    def __init__(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        fullpath = os.path.join(script_dir, "application.yaml")
        with open(fullpath, 'r') as f:
            self.config = yaml.safe_load(f)

    def get_qdrant_config(self):
        return self.config['qdrant']

