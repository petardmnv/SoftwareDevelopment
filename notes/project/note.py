from datetime import datetime


class Note:
    heading: str
    content: str
    created_at: datetime

    def __init__(self, heading, content):
        self.heading = heading
        self.content = content
        self.created_at = datetime.now()

