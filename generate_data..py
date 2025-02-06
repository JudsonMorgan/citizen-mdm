#!/usr/bin/env python
# coding: utf-8

# In[4]:


from faker import Faker
import json
import random

fake = Faker()
Faker.seed(42) 

def generate_health_data(num_records):
    health_data = []
    
    # Ensure unique citizen IDs by using range()
    citizen_ids = list(range(1, num_records + 1))
    random.shuffle(citizen_ids)  # Shuffle to add randomness
    
    for i in range(num_records):
        health_data.append({
            "citizen_id": citizen_ids[i],  # Use unique ID from shuffled list
            "name": fake.name(),
            "dob": fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat(),
            "gender": random.choice(["Male", "Female"]),
            "health_status": random.choice(["Healthy", "Sick", "Critical"])
        })
    
    return health_data

def generate_education_data(num_records):
    education_data = []
    
    citizen_ids = list(range(1, num_records + 1))
    random.shuffle(citizen_ids)
    
    for i in range(num_records):
        education_data.append({
            "citizen_id": citizen_ids[i],  # Use unique ID from shuffled list
            "name": fake.name(),
            "dob": fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat(),
            "gender": random.choice(["Male", "Female"]),
            "school_name": fake.company()
        })
    
    return education_data

# Save JSON files
with open("health.json", "w") as f:
    json.dump(generate_health_data(100000), f, indent=4)

with open("education.json", "w") as f:
    json.dump(generate_education_data(100000), f, indent=4)

print("JSON files generated successfully!")


# In[ ]:




