def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
    except:
        return "Can't parse the data. Please enter name and phone number with a space"
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    try:
        name, phone = args
    except:
        return "Can't parse the data. Please enter name and phone number with a space"
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Name not found"


def show_phone(args, contacts):
    try:
        name = args[0]
    except:
        return "Can't parse the data."
    if name in contacts:
        return contacts[name]
    else:
        return "Name not found"


def show_all(contacts):
    all_list = ""
    for name, phone in contacts.items():
        all_list += f"{name}: {phone}\n"
    return all_list.removesuffix("\n")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
