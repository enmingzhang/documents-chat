from abc import ABC, abstractmethod

# 文件解析器 接口
class FileParse(ABC):
    @abstractmethod
    def load_file(self):
        pass

    @abstractmethod
    def extract_text(self, arg):
        pass
