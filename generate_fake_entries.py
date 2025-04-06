from db import get_connection
from datetime import datetime
from faker import Faker
import random

fake = Faker()
conn = get_connection()
cursor = conn.cursor()

entries_by_lang = {
    'en': "I feel anxious and need help managing stress.",
    'et': "Tunen end rahutuna ja vajan tuge.",
    'lt': "Jaučiu nerimą ir ieškau pagalbos.",
    'lv': "Es izjūtu satraukumu un nepieciešams atbalsts.",
    'ru': "Чувствую тревогу и нуждаюсь в поддержке."
}

cursor.execute("SELECT id, email, language_preference FROM users")
users = cursor.fetchall()

for user_id, email, lang in users:
    cursor.execute("SELECT 1 FROM entries WHERE user_id = %s", (user_id,))
    if cursor.fetchone():
        continue  # already has entry

    text = (entries_by_lang[lang] + " More detail. ") * 20
    text = text[:1000]
    created_at = datetime.now()

    cursor.execute("""
        INSERT INTO entries (user_id, content, language_code, created_at)
        VALUES (%s, %s, %s, %s)
    """, (user_id, text, lang, created_at))

conn.commit()
cursor.close()
conn.close()
print(" Entries inserted for users who had none.")
