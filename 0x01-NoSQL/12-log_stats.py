#!/usr/bin/env python3
"""Provide some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    ngnx = client.logs.nginx
    spc = " " * 4
    print(f"{ngnx.count_documents({})} logs")
    print("Methods:")
    print(f"{spc}method GET: {ngnx.count_documents({'method': 'GET'})}")
    print(f"{spc}method POST: {ngnx.count_documents({'method': 'POST'})}")
    print(f"{spc}method PUT: {ngnx.count_documents({'method': 'PUT'})}")
    print(f"{spc}method PATCH: {ngnx.count_documents({'method': 'PATCH'})}")
    print(f"{spc}method DELETE: {ngnx.count_documents({'method': 'DELETE'})}")
    count = ngnx.count_documents({'path': '/status', 'method': 'GET'})
    print(f"{count} status check")
