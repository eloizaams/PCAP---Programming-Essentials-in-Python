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

char_dict_order = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))

for key, value in char_dict_order.items():
    if value > 0:
        print(key, " -> ", value)