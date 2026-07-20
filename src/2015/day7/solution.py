
def file_read():
    instructions = []

    with open("./input.txt", 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split("->")

            final_wire = parts[1].strip()

            left = parts[0].strip()

            if "AND" in left:
                gate = create_gate(left, "AND")

            elif "OR" in left:
                gate = create_gate(left, "OR")

            elif "LSHIFT" in left:
                gate = create_gate(left, "LSHIFT")

            elif "RSHIFT" in left:
                gate = create_gate(left, "RSHIFT")

            elif "NOT" in left:
                wire = left.replace("NOT", "").strip()
                wire = int(wire) if wire.isnumeric() else wire.strip()
                gate = ("NOT", wire)

            else:
                if left.isnumeric():
                    gate = ("SET", int(left))
                else:
                    gate = ("SET", left)

            instructions.append((final_wire, gate))

    return instructions

def create_gate(string: str, operator: str):
    wire1, wire2 = string.split(operator)

    wire1 = wire1.strip()
    wire2 = wire2.strip()

    wire1 = int(wire1) if wire1.isnumeric() else wire1
    wire2 = int(wire2) if wire2.isnumeric() else wire2

    return (operator, wire1, wire2)

def first_star(instructions: list):
    wires = {}

    done_instructions = []

    while len(done_instructions) < len(instructions):

        previous_done_len = len(done_instructions)

        for i, instruction in enumerate(instructions):
            if i in done_instructions:
                continue

            wire, gate = instruction

            operator: str = gate[0]
            output: int | None = wires.get(wire)

            if operator == "SET":
                if isinstance(gate[1], int):
                    output = gate[1]
                    done_instructions.append(i)
                else:
                    value_input: int | None = wires.get(gate[1])
                    if value_input is not None:
                        output = value_input
                        done_instructions.append(i)

            elif operator == "AND":
                if isinstance(gate[1], int):
                    value_input1: int = gate[1]
                else:
                    value_input1: int | None = wires.get(gate[1])

                if isinstance(gate[2], int):
                    value_input2: int = gate[2]
                else:
                    value_input2: int | None = wires.get(gate[2])

                if value_input1 is not None and value_input2 is not None:
                    output = value_input1 & value_input2
                    done_instructions.append(i)

            elif operator == "OR":
                if isinstance(gate[1], int):
                    value_input1: int = gate[1]
                else:
                    value_input1: int | None = wires.get(gate[1])

                if isinstance(gate[2], int):
                    value_input2: int = gate[2]
                else:
                    value_input2: int | None = wires.get(gate[2])

                if value_input1 is not None and value_input2 is not None:
                    output = value_input1 | value_input2
                    done_instructions.append(i)

            elif operator == "LSHIFT":
                value_input1: int | None = wires.get(gate[1])
                shift: int = gate[2]

                if value_input1 is not None:
                    output = value_input1 << shift
                    done_instructions.append(i)

            elif operator == "RSHIFT":
                value_input1: int | None = wires.get(gate[1])
                shift: int = gate[2]

                if value_input1 is not None:
                    output = value_input1 >> shift
                    done_instructions.append(i)

            elif operator == "NOT":
                value_input: int | None = wires.get(gate[1])

                if value_input is not None:
                    output = int(bin(0b1111111111111111 ^ value_input), 2)
                    done_instructions.append(i)

            wires[wire] = output

        # if there are no new done instructions
        if previous_done_len == len(done_instructions):
            break

    for key, value in wires.items():
        if key in ["a"]:
            print(key, value)

def second_star(instructions):
    wires = {}
    done_instructions = []

    # first turn -> normal
    # second turn -> override b set value with first turn a value
    for i in range(2):

        wires = {}
        done_instructions = []

        while len(done_instructions) < len(instructions):

            previous_done_len = len(done_instructions)

            for i, instruction in enumerate(instructions):
                if i in done_instructions:
                    continue

                wire, gate = instruction

                operator: str = gate[0]
                output: int | None = wires.get(wire)

                if operator == "SET":
                    if isinstance(gate[1], int):
                        output = gate[1]
                        done_instructions.append(i)
                    else:
                        value_input: int | None = wires.get(gate[1])
                        if value_input is not None:
                            output = value_input
                            done_instructions.append(i)

                elif operator == "AND":
                    if isinstance(gate[1], int):
                        value_input1: int = gate[1]
                    else:
                        value_input1: int | None = wires.get(gate[1])

                    if isinstance(gate[2], int):
                        value_input2: int = gate[2]
                    else:
                        value_input2: int | None = wires.get(gate[2])

                    if value_input1 is not None and value_input2 is not None:
                        output = value_input1 & value_input2
                        done_instructions.append(i)

                elif operator == "OR":
                    if isinstance(gate[1], int):
                        value_input1: int = gate[1]
                    else:
                        value_input1: int | None = wires.get(gate[1])

                    if isinstance(gate[2], int):
                        value_input2: int = gate[2]
                    else:
                        value_input2: int | None = wires.get(gate[2])

                    if value_input1 is not None and value_input2 is not None:
                        output = value_input1 | value_input2
                        done_instructions.append(i)

                elif operator == "LSHIFT":
                    value_input1: int | None = wires.get(gate[1])
                    shift: int = gate[2]

                    if value_input1 is not None:
                        output = value_input1 << shift
                        done_instructions.append(i)

                elif operator == "RSHIFT":
                    value_input1: int | None = wires.get(gate[1])
                    shift: int = gate[2]

                    if value_input1 is not None:
                        output = value_input1 >> shift
                        done_instructions.append(i)

                elif operator == "NOT":
                    value_input: int | None = wires.get(gate[1])

                    if value_input is not None:
                        output = int(bin(0b1111111111111111 ^ value_input), 2)
                        done_instructions.append(i)

                wires[wire] = output

            # if there are no new done instructions
            if previous_done_len == len(done_instructions):
                break

        for key, value in wires.items():
            if key in ["a"]:
                for i, (wire, gate) in enumerate(instructions):
                    if wire == "b" and gate[0] == "SET":
                        instructions[i] = (wire, (gate[0], value))
                        break
                break

    for key, value in wires.items():
        if key in ["a"]:
            print(key, value)

if __name__ == "__main__":
    INSTRUCTIONS = file_read()

    #first_star(INSTRUCTIONS)
    second_star(INSTRUCTIONS)
