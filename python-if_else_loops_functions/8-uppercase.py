# !/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        char = str[i]
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
