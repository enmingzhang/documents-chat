import os

import yaml


# 向量数据库配置
class QdrantConfig:
    def __init__(self, config_file):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        fullpath = os.path.join(script_dir, config_file)
        with open(fullpath, 'r') as f:
            self.config = yaml.safe_load(f)

    def get_qdrant_config(self):
        return self.config['qdrant']


# 创建配置对象
config = QdrantConfig('application.yaml')

# 获取数据库配置
qdrant_config = config.get_qdrant_config()
print(qdrant_config['host'])  # 输出: localhost
print(qdrant_config['port'])  # 输出: 6300
