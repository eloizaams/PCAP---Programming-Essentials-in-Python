file_name = input("Nome do arquivo: ")

try:
    with open(file_name, "rt") as file:
        char_dict = {chr(x): 0 for x in range(ord('A'), ord('Z')+1)}
        for line in file:
            for ch in line:
                if 'a' <= ch <= 'z':
                    ch = ch.upper()
                if 'A' <= ch <= 'Z':
                    char_dict[ch] += 1
except FileNotFoundError:
    print("Erro ao abrir o arquivo.")
    exit()

for key, value in char_dict.items():
    if value > 0:
        print(key, " -> ", value)