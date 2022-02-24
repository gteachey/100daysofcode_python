names_list = []
with open("Input/Names/invited_names.txt", "r") as get_names:
    for name in get_names.read().splitlines():
        names_list.append(name)
        print(name)

# Replace the [name] placeholder with the actual name.
with open("Input/Letters/starting_letter.txt", "r") as edit_letter:
    starting_letter = edit_letter.read()
    for name in names_list:
        changed_letter = starting_letter.replace("[name]", name)
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as write_letter:
            write_letter.writelines(changed_letter)
