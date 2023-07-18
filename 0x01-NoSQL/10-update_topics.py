#!/usr/bin/env python3
"""my docs"""


def update_topics(mongo_collection, name, topics):
    """updates an entry"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
