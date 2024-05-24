# models.py

import datetime
import uuid

class Ad:
    def __init__(self, title, description, owner):
        self.id = uuid.uuid4().hex  # Генерация уникального идентификатора
        self.title = title
        self.description = description
        self.created_at = datetime.datetime.now()
        self.owner = owner

    def update(self, title=None, description=None, owner=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if owner:
            self.owner = owner
# Хранилище для объявлений. В реальном приложении это будет база данных.
ads = {}