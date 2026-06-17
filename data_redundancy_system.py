def process_data(input_data):
    words = input_data.split()

    unique = []
    duplicates = []

    # Load existing database
    try:
        with open("database.txt", "r") as f:
            existing_data = f.read().split()
    except:
        existing_data = []

    for word in words:
        if word in existing_data or word in unique:
            duplicates.append(word)
        else:
            unique.append(word)

    # Append only unique data to database
    with open("database.txt", "a") as f:
        for word in unique:
            f.write(word + " ")

    return unique, duplicates