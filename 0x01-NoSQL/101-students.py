#!/usr/bin/env python3
"""Returns all students sorted by average score"""
from pymongo import MongoClient


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    # Retrieve all students from the collection
    students = mongo_collection.find()
    # Calculate average score for each student
    student_scores = []
    for student in students:
        scores = [topic['score'] for topic in student.get('topics', [])]
        if scores:  # Avoid division by zero
            average_score = sum(scores) / len(scores)
        else:
            average_score = 0
        # Append student with the average score included
        student_scores.append({
            '_id': student['_id'],
            'name': student.get('name', ''),
            'averageScore': average_score
        })
    # Sort students by average score in descending order
    sorted_students = sorted(student_scores, key=lambda x: x['averageScore'],
                             reverse=True)
    return sorted_students
