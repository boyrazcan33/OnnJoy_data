import random
from faker import Faker
from db import get_connection
from datetime import datetime, timedelta

fake = Faker()

# Connect to database
conn = get_connection()
cursor = conn.cursor()

# First, get all therapist IDs
cursor.execute("SELECT id FROM therapists")
therapist_ids = [row[0] for row in cursor.fetchall()]

if not therapist_ids:
    print("No therapists found in database. Please create therapists first.")
    cursor.close()
    conn.close()
    exit()

# Generate availability for each therapist
for therapist_id in therapist_ids:
    # Each therapist gets 10-20 available dates
    num_dates = random.randint(10, 20)
    
    # Generate dates in the next 60 days
    start_date = datetime.now().date()
    end_date = start_date + timedelta(days=60)
    
    # Create a list of possible dates
    delta = end_date - start_date
    possible_days = [start_date + timedelta(days=i) for i in range(delta.days)]
    
    # Randomly select available dates
    available_dates = random.sample(possible_days, min(num_dates, len(possible_days)))
    
    # Insert each availability record
    for avail_date in available_dates:
        created_at = datetime.now()
        
        cursor.execute("""
            INSERT INTO therapist_availability 
            (therapist_id, available_date, created_at)
            VALUES (%s, %s, %s)
        """, (therapist_id, avail_date, created_at))
        
        print(f"Added availability for therapist {therapist_id} on {avail_date}")

# Commit and close
conn.commit()
cursor.close()
conn.close()
print(f"Therapist availability created for {len(therapist_ids)} therapists.")