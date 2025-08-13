#!/usr/bin/env python3
"""List all documents from mongo collection"""


def list_all(mongo_collection):
    if mongo_collection is None:
        return []
    else:
        return list(mongo_collection.find())

if __name__ == "__main__":
    pass