from src.service.file.impl.PDFParser import PDFParser
import unittest

# pdf 解析器测试用例
class TestPDFParser(unittest.TestCase):
    def test_extract_text(self):
        # 创建一个PDFParser对象并加载文件
        parser = PDFParser("/Users/enming/PycharmProjects/documents-chat/test/parser/20230517-中信建投-医药行业深度研究·中期策略：复苏、创新、中医药，三箭齐发的副本.pdf")
        parser.load_file()

        # 提取文本内容
        text = parser.extract_text()

        # 将文本写入文件
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(text)

        # 读取写入的文件内容并进行断言
        with open("output.txt", "r", encoding="utf-8") as file:
            output_text = file.read()

        self.assertEqual(text, output_text)


if __name__ == "__main__":
    unittest.main()
