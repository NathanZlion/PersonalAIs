class BaseRepo:
    """
    Base repository class that provides a common interface for all repositories.
    """

    def __init__(self):
        pass

    def get(self, id):
        raise NotImplementedError("Subclasses should implement this method.")

    def create(self, entity):
        raise NotImplementedError("Subclasses should implement this method.")

    def update(self, entity):
        raise NotImplementedError("Subclasses should implement this method.")

    def delete(self, id):
        raise NotImplementedError("Subclasses should implement this method.")
