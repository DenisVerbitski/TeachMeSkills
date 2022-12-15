def names_gen(file_names: str, letter: str ):
    with open(file_names, mode='r') as file:
        for line in file:
            if line.startswith(letter):
                yield line


name_with_letter = names_gen('unsorted_names.txt', 'A')

print(next(name_with_letter))