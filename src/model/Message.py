# 对话消息, 如果是答案 需要设置question_id
class Message:

    def __init__(self, question_id, user_id, file_id, role, message, source):
        self.questionId = question_id
        self.user_id = user_id
        self.file_id = file_id
        self.name = role
        self.message = message
        self.source = source
