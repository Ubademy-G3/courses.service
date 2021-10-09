class Course:
    """Course represents your collection of courses as an entity."""

    def __init__(
        self,
        id: str,
        name: str
    ):
        self.id = id
        self.name = name
