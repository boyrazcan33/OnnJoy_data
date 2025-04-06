import random
import bcrypt
from faker import Faker
from db import get_connection
from datetime import datetime

fake = Faker()
colors = ["Sapphire", "Ruby", "Emerald", "Ivory", "Amber", "Violet", "Scarlet", "Pearl", "Lilac", "Turquoise"]
animals = ["Fox", "Fawn", "Wolf", "Swan", "Panther", "Dove", "Tiger", "Owl", "Hummingbird", "Leopard"]
languages = ['en', 'et', 'lt', 'lv', 'ru']

conn = get_connection()
cursor = conn.cursor()

for i in range(1000):
    email = f"user{i}@example.com"
    cursor.execute("SELECT 1 FROM users WHERE email = %s", (email,))
    if cursor.fetchone():
        continue  # skip if email exists

    raw_password = "password123"
    password_hash = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    anon_username = f"{random.choice(colors)}{random.choice(animals)}{random.randint(100,999)}"
    language = random.choice(languages)
    created_at = datetime.now()
    last_entry_at = created_at
    jwt_token = None
    timezone = "UTC"
    ip_address = fake.ipv4()

    cursor.execute("""
        INSERT INTO users (email, password_hash, anon_username, language_preference, created_at, last_entry_at, jwt_token, timezone, ip_address)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (email, password_hash, anon_username, language, created_at, last_entry_at, jwt_token, timezone, ip_address))

conn.commit()
cursor.close()
conn.close()
print(" 1000 users inserted with hashed passwords.")
