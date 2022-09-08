import os

db_URI = os.getenv('DATABASE_URL', 'postgresql://localhost:5432/firesell1')
secret = os.getenv('SECRET', 'fanatstic_apps_and_where_to_find_them')

#postgresql-silhouetted-08098