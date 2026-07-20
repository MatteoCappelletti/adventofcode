
def file_read():
    row = ""

    with open("./input.txt", 'r', encoding='utf-8') as file:
        for line in file:
            row = line.strip()

    return row

def first_star(password: str):
    print(next_accepted_password(password))

def next_accepted_password(password: str):
    test_password = password

    while True:
        if second_req(test_password) and first_req(test_password) and third_req(test_password):
            break

        test_password = next_test_password(test_password)

    return test_password

def next_test_password(password: str):
    forming_password = ""

    for i, char in enumerate(reversed(password)):
        real_i = len(password) - 1 - i

        next_char = ord(char) + 1
        if next_char <= ord("z"):
            forming_password = password[:real_i] + chr(next_char) + ("a" * i)
            return forming_password

    return password

def first_req(password: str):
    for num in range(ord("a"), (ord("z") - 1), 1):
        group = chr(num) + chr(num + 1) + chr(num + 2)

        if group in password:
            return True

    return False

def second_req(password: str):
    if "i" in password.lower() or "o" in password.lower() or "l" in password.lower():
        return False
    return True

def third_req(password: str):
    counter = 0

    for num in range(ord("a"), (ord("z") + 1), 1):
        pair = chr(num) + chr(num)

        if pair in password:
            counter += 1

            if counter >= 2:
                return True

    return False

def second_star(password: str):
    print(next_accepted_password(next_test_password(next_accepted_password(password))))

if __name__ == "__main__":
    PASSWORD = file_read()

    #first_star(PASSWORD)
    second_star(PASSWORD)
