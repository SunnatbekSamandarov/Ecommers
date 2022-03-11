from django.db import connection
from .models import Category,Product

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
    ]

def dictfetchone(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return dict(zip([col[0] for col in desc], cursor.fetchone()))

def get_category():
    with connection.cursor() as cursor:
        cursor.execute("""
        select name from products_category
        """)
        data = dictfetchall(cursor)
    return data
def get_product():
    with connection.cursor() as cursor:
        cursor.execute("""
        select * from products_product as p
        ORDER BY p.created_date DESC 
        """)
        data = dictfetchall(cursor)
    return data
