
import hashlib

def file_read():
    with open("./input.txt", 'r', encoding='utf-8') as file:
        for line in file:
            pass

def first_star(secret_key):
    num = 1

    while True:
        combined_key = secret_key + str(num)

        res = hashlib.md5(combined_key.encode())
        hash_value = res.hexdigest()

        if hash_value == ("00000" + hash_value[5:]):
            print(f"lowest num to combine [{num}]")
            break

        num += 1

def second_star(secret_key):
    num = 1

    while True:
        combined_key = secret_key + str(num)

        res = hashlib.md5(combined_key.encode())
        hash_value = res.hexdigest()

        if hash_value == ("000000" + hash_value[6:]):
            print(f"lowest num to combine [{num}]")
            break

        num += 1

if __name__ == "__main__":
    SECRET_KEY = "bgvyzdsv"

    #first_star(SECRET_KEY)
    second_star(SECRET_KEY)
