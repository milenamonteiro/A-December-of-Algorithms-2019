import re

def is_valid_email(email):
    match = re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)
    if match is None:
        return "This email is invalid!"
    else:
        return "This email is valid!"
