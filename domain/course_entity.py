from uuid import uuid4, UUID

class Course:
    def __init__(self, name, description, category, kind, subscription_type, location, info):
        self.id = uuid4()
        self.name: str = name
        self.description: str = description
        self.category: str = category
        self.kind: str = kind
        self.subscription_type: list = subscription_type
        self.location: str = location
        self.info: dict = info