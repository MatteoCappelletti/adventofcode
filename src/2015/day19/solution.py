
def file_read():
    atoms = []
    replacements = []

    with open("./input.txt", 'r', encoding='utf-8') as file:
        for raw_line in file:
            line = raw_line.strip()

            if not line:
                continue

            if "=>" in line:
                starting, replacement = line.split("=>")
                replacements.append((starting.strip(), replacement.strip()))

            else:
                atom = ""
                for char in line:
                    if ord("A") <= ord(char) <= ord ("Z"):
                        if atom:
                            atoms.append(atom)
                        atom = char
                    else:
                        atom += char
                atoms.append(atom)

    return atoms, replacements

def first_star(atoms, replacements):
    molecules: set = {""}

    for i, atom in enumerate(atoms):
        for atom_to_replace, replacement in replacements:
            if atom == atom_to_replace:
                molecule = ""

                for concat_atom in atoms[:i]:
                    molecule += concat_atom

                molecule += replacement

                for concat_atom in atoms[(i+1):]:
                    molecule += concat_atom

                molecules.add(molecule)

    print(molecules)

    molecules_count = len(molecules) - 1 # '-1' for the empty initial string

    print("different molecules:", molecules_count)


def second_star():
    pass

if __name__ == "__main__":
    ATOMS, REPLACEMENTS = file_read()

    first_star(ATOMS, REPLACEMENTS)
    #second_star()
