#!/usr/bin/env python3
"""List all documents in mongo collection in python"""


def list_all(mongo_collection):
    """List all documents in mongo collection in python"""
    return mongo_collection.find()
