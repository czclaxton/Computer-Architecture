PRINT_BEEJ = 1
HALT = 2

memory = [
    PRINT_BEEJ,
    PRINT_BEEJ,
    PRINT_BEEJ,
    PRINT_BEEJ,
    PRINT_BEEJ,
    HALT
]

pc = 0
running = True


while running:
    instruction = memory[pc]

    if instruction == PRINT_BEEJ:
        print("BEEJ!")

    elif instruction == HALT:
        running = False

    else:
        print(f"Error at index {pc}")

    pc += 1
