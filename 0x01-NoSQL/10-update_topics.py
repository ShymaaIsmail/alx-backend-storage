#!/usr/bin/env python3
"""Update topics of a document"""


def update_topics(mongo_collection, name, topics):
    """Update topics of a document"""
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
