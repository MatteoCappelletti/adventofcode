
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

def second_star(atoms, replacements):
    final_molecule = get_molecule(atoms)

    molecule = "e"

    #steps = create_molecule(replacements, molecule, final_molecule, 0)
    steps = disassembly(replacements, atoms, 0)

    print("steps:", steps)

def create_molecule(replacements: list, molecule: str, final_molecule: str, steps: int):
    # se la molecola creata è uguale a quella finale, return steps
    if molecule == final_molecule:
        return steps

    atoms = get_atoms(molecule) if molecule != "e" else ["e"]
    final_atoms = get_atoms(final_molecule)

    if len(atoms) > len(final_atoms):
        return 0

    for replaceable_atom, replacement in replacements:
        for i, atom in enumerate(atoms):
            if atom == replaceable_atom:
                test_atoms = atoms[:i] + [replacement] + atoms[(i+1):]

                molecule = get_molecule(test_atoms)

                final_steps = create_molecule(replacements, molecule, final_molecule, (steps + 1))

                if final_steps is not None and final_steps > 0:
                    return final_steps

    return 0

def get_atoms(molecule: str) -> list:
    atoms = []

    atom = ""
    for char in molecule:
        if ord("A") <= ord(char) <= ord ("Z"):
            if atom:
                atoms.append(atom)
            atom = char
        else:
            atom += char
    atoms.append(atom)

    return atoms

def get_molecule(atoms: list) -> str:
    final_molecule = ""
    for atom in atoms:
        final_molecule += atom
    return final_molecule

def disassembly(replacements: list, molecule: list, steps: int): #second star: try 2
    if molecule == "e":
        return steps

    atoms = get_atoms(molecule)

    for reversed_i, atom in reversed(atoms):
        for replaceable_atom, replacement in replacements:
            if replacement.endswith(atom):
                i = len(atoms) - 1 - reversed_i

                pre_atoms = atoms[:i] + [replaceable_atom]

                pre_molecule = get_molecule(pre_atoms)

                final_steps = disassembly(replacements, pre_molecule, (steps + 1))

                if final_steps is not None:
                    return final_steps

    for i in range(len(molecule) - 1, -1, 1): # last -> first
        test = molecule[i:]

        endswith_found = False

        for replaceable_atom, replacement in replacements:
            if replacement.endswith(test):
                endswith_found = True

    return None

if __name__ == "__main__":
    ATOMS, REPLACEMENTS = file_read()

    #first_star(ATOMS, REPLACEMENTS)
    second_star(ATOMS, REPLACEMENTS)
