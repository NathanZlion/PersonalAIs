from datetime import datetime
from json import JSONEncoder

from beanie import PydanticObjectId
from bson import ObjectId


class CustomJSONEncoder(JSONEncoder):
    """
    Custom JSON encoder that handles datetime objects.
    """

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.timestamp()

        if isinstance(obj, ObjectId):
            return str(obj)

        if isinstance(obj, PydanticObjectId):
            return str(obj)

        return super().default(obj)
