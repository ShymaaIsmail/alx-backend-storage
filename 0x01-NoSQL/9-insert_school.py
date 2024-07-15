#!/usr/bin/env python3
"""Insert school document"""


def insert_school(mongo_collection, **kwargs):
    """Insert school document"""
    new_school = {}
    if kwargs:
        for attr_name, value in kwargs.items():
            new_school[attr_name] = value
        mongo_collection.insert_one(new_school)
    return new_school['_id']
    