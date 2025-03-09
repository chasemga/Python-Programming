def main():
    names_input = input("Enter list of names separated by spaces and commas:")
    
    names_list = names_input.split(",")
    
    formatted_names = []

    for names in names_list:
        names = names.strip()
        first, last = names.split(" ", 1)
        formatted_names.append(f"{last}, {first}")

    formatted_names.sort()

    print("Formatted names in alphabetical order:")
    for name in formatted_names:
        print(name)

main()
