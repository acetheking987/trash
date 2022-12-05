#text = input("enter text: ")
text = open("raw\\text.txt").read()
current = 0
index = 0
output = ""

for character in text:
    unicode = ord(character)
    diff = unicode - current
    if diff > 0:
        output += f"+0;"
        output += f"i0:{unicode}:{(index*4)+3};"
        output += f"g{index*4};"
        output += f"c0;"
        index += 1
    elif diff < 0:
        output += f"-0;"
        output += f"i0:{unicode}:{(index*4)+3};"
        output += f"g{index*4};"
        output += f"c0;"
        index += 1
    else:
        output += f"c0;"
        output += f";"
        output += f";"
        output += f";"
        index += 1
    current = unicode

#print(output)
open("output.txt", "w").write(output.replace(";", ";\n"))