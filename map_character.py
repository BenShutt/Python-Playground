letters = "abcdefghijklmnopqrstuvwxyz"

def map_character(character):    
    i = next(i for i, letter in enumerate(letters) if letter == character)
    mapped_index = len(letters) - i - 1
    return letters[mapped_index]

print("Performing mapping:")
for letter in letters:
    print(f"{letter} -> {map_character(letter)}") 
    
characters = input("Input: ")
mapped_characters = [map_character(character) for character in characters]
output = "".join(mapped_characters)
print(f"Output: {output}")
    