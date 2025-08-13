import re

def is_valid_email(email):
    pattern = (r"^(?![_.-])[a-zA-Z0-9._%+-]+(?<![_.-])@"      # Local part
               r"(?!-)[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*"        # Domain
               r"\.[A-Za-z]{2,}$")                             # TLD
    return re.match(pattern, email) is not None

if __name__ == "__main__":
    email = input("Enter an email address: ")
    if is_valid_email(email):
        print("Valid email address.")
    else:
        print("Invalid email address.")