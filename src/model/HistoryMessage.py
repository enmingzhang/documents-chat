# 历史消息
class HistoryMessage:
    def __init__(self, question_id, user_id, file_id, role, message, source):
        self.questionId = question_id
        self.user_id = user_id
        self.file_id = file_id
        self.name = role
        self.message = message
        self.source = source
