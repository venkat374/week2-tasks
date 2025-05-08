import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

print("Checking email validity:")
print(f"user@domain.com -> {is_valid_email('user@domain.com')}")
print(f"user@domain -> {is_valid_email('user@domain')}")
print(f"user.name@sub.domain.co -> {is_valid_email('user.name@sub.domain.co')}")