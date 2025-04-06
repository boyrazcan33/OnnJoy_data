from db import get_connection
from faker import Faker
import random
from datetime import datetime

fake = Faker()
conn = get_connection()
cursor = conn.cursor()

languages = ['en', 'et', 'lt', 'lv', 'ru']
bios_by_lang = {
    'en': "I help clients with stress, anxiety, and emotional growth.",
    'et': "Aitan klientidel toime tulla stressiga ja enesearenguga.",
    'lt': "Padedu įveikti stresą ir augti emociškai.",
    'lv': "Palīdzu cilvēkiem tikt galā ar stresu un trauksmi.",
    'ru': "Помогаю справляться со стрессом и тревожностью."
}

for i in range(50):
    email = f"therapist{i}@onnjoy.com"
    cursor.execute("SELECT id FROM therapists WHERE email = %s", (email,))
    result = cursor.fetchone()
    if result:
        therapist_id = result[0]
    else:
        password_hash = "securepass"
        full_name = fake.name()
        profile_pic = "https://placekitten.com/200/200"
        created_at = datetime.now()

        cursor.execute("""
            INSERT INTO therapists (email, password_hash, full_name, profile_picture_url, created_at)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id
        """, (email, password_hash, full_name, profile_pic, created_at))
        therapist_id = cursor.fetchone()[0]

    # Add 1–5 bios
    lang_count = random.randint(1, 5)
    chosen_langs = random.sample(languages, lang_count)

    for lang in chosen_langs:
        cursor.execute("""
            SELECT 1 FROM therapist_bios WHERE therapist_id = %s AND language_code = %s
        """, (therapist_id, lang))
        if cursor.fetchone():
            continue

        bio = (bios_by_lang[lang] + " More professional content.") * 30
        cursor.execute("""
            INSERT INTO therapist_bios (therapist_id, language_code, bio)
            VALUES (%s, %s, %s)
        """, (therapist_id, lang, bio[:2500]))

conn.commit()
cursor.close()
conn.close()
print(" Therapists + language bios inserted without duplicates.")
