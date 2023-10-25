with open('resources/enc', 'r', encoding='utf-8') as file:
    flag = file.read()

print(flag.encode('utf-16-be'))