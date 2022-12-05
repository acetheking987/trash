import sys

ARRAY = [0 for i in range(200)]
INDEX = -1

def main(code : str):
    global ARRAY, INDEX
    while INDEX < len(code.split(';')) - 1:
        try:
            INDEX += 1
            func = code.split(';')[INDEX]
            if func == '': continue
            elif func[0] == '+':
                ARRAY[int(func[1:])] += 1
            elif func[0] == '-':
                ARRAY[int(func[1:])] -= 1
            elif func[0] == '=':
                ARRAY[int(func[1:].split(":")[0])] = int(func[1:].split(":")[0])
            elif func[0] == 'p':
                print(ARRAY[int(func[1:])], end='')
            elif func[0] == '>':
                string = input()[0]
                try:
                    ARRAY[int(func[1:])] = int(string)
                except:
                    ARRAY[int(func[1:])] = ord(string)
            elif func[0] == 'c':
                print(chr(ARRAY[int(func[1:])]), end='')
            elif func[0] == 'i':
                if int(ARRAY[int(func[1:].split(":")[0])]) == int(func[1:].split(":")[1]):
                    INDEX = int(func[1:].split(":")[2]) - 1
            elif func[0] == 'g':
                INDEX = int(func[1:]) - 1
            elif func[0] == 'n':
                print("")
            else:
                print("Error: Unknown command '" + func[0] + "' at line " + str(INDEX + 1))
                sys.exit()
        except:
            print("Error: Unknown error at line " + str(INDEX + 1))
            sys.exit()

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        print('Usage:\ttrash -f <file>\n\ttrash <code>')
        sys.exit()
    if "-f" in args:
        args.remove("-f")
        with open(args[0]) as f:
            main(f.read().replace('\n', ''))
    else:
        main(args[0])