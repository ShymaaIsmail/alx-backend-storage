#!/usr/bin/env python3
"""Provide some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    ngnx = client.logs.nginx
    print(f"{ngnx.count_documents({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {ngnx.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {ngnx.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {ngnx.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {ngnx.count_documents({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {ngnx.count_documents({'method': 'DELETE'})}")
    count = ngnx.count_documents({'path': '/status', 'method': 'GET'})
    print(f"{count} status check")
    # Get top 10 IPs
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = list(ngnx.aggregate(pipeline))
    print("IPs:")
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")
