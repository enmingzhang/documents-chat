import os

import yaml


# 向量数据库配置
class MysqlConfig:
    def __init__(self, config_file):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        fullpath = os.path.join(script_dir, config_file)
        with open(fullpath, 'r') as f:
            self.config = yaml.safe_load(f)

    def get_db_config(self):
        return self.config['model']


# 创建配置对象
config = MysqlConfig('application.yaml')

# 获取数据库配置
db_config = config.get_db_config()
print(db_config['host'])  # 输出: localhost
print(db_config['port'])  # 输出: 6300
