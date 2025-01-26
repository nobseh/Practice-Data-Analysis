import re  # Import the 're' module for regular expressions

# Define the filename to read data from
filename = input("Enter the filename to search: ")

# Get the search term from the user and remove any leading/trailing spaces
search_term = input("Enter the search character(s): ").strip()

# Initialize an empty list to store words that match the search term
matching_words = []

# Open the file in read mode using 'with' to ensure proper file handling
with open(filename, "r") as fhand:
    for line in fhand:  # Iterate over each line in the file
        words = line.split()  # Split the line into a list of words
        for word in words:  # Iterate over each word in the line
            # Remove leading and trailing special characters (except '@') using regex
            cleaned_word = re.sub(r"^[^\w@]+|[^\w@]+$", "", word)

            # Check if the cleaned word contains the search term (case-insensitive)
            if search_term.lower() in cleaned_word.lower():
                matching_words.append(cleaned_word)  # Add the word to the matching list

# Print matching words as a numbered list
if matching_words:
    print("\nMatching words list:")
    for i, word in enumerate(matching_words, start=1):  
        print(f"{i}. {word}")  # Display words with numbering (starting from 1)

    # Print the total number of matching words found
    print(f"\nTotal words found: {len(matching_words)}")
else:
    # Display a message if no words match the search term
    print(f"\nNo words found containing '{search_term}'.")
