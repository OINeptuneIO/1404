def main():
    email_dict = {}
    while True:
        email = input("Email: ").strip()
        if email == "":  # If user enters a blank email, exit the loop
            break
        
        name = extract_name(email)
        prompt = f"Is your name {name}? (Y/n) "
        choice = input(prompt).strip().lower()
        if choice == 'n':
            name = input("Name: ").strip().title()  # Ask for the name if the default is not accepted
        
        email_dict[email] = name

    # Print out emails and names
    for email, name in email_dict.items():
        print(f"{name} ({email})")


def extract_name(email):
    """
    Extracts the name from the email address.
    """
    username = email.split('@')[0]  # Extract username part before '@'
    name_parts = username.split('.')  # Split username into parts
    name_parts = [part.capitalize() for part in name_parts]  # Capitalize each part
    name = ' '.join(name_parts)  # Join parts to form the name
    return name



main()