people = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

# CREATE
def add_person(person_list, person):
    allowed_keys = {"id", "name", "email"}
    person = {k: v for k, v in person.items() if k in allowed_keys}
    person_list.append(person)
    print(f"Added: {person}\n")

# READ
def get_all_people(person_list):
    print("All People:")
    for person in person_list:
        print(person)
    print()

def get_person_by_id(person_list, person_id):
    for person in person_list:
        if person["id"] == person_id:
            print(f"Found: {person}\n")
            return person
    print(f"No person found with ID {person_id}\n")
    return None

# UPDATE
def update_person(person_list, person_id, updated_info):
    allowed_keys = {"name", "email"}  # don't allow id to be updated
    updated_info = {k: v for k, v in updated_info.items() if k in allowed_keys}
    for person in person_list:
        if person["id"] == person_id:
            person.update(updated_info)
            print(f"Updated: {person}\n")
            return
    print(f"No person found with ID {person_id}\n")

# DELETE
def delete_person(person_list, person_id):
    for person in person_list:
        if person["id"] == person_id:
            person_list.remove(person)
            print(f"Deleted person with ID {person_id}\n")
            return
    print(f"No person found with ID {person_id}\n")

# Example usage:
add_person(people, {"id": 3, "name": "Ben", "email": "ben@example.com"})

get_all_people(people)

get_person_by_id(people, 2)

update_person(people, 3, {"email": "ben@newmail.com", "age": 30})  # age ignored

delete_person(people, 1)

get_all_people(people)
