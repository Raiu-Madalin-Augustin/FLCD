from lab3.SymbolTable import HashTable
from lab3.pif import PIF
from lab3.scanner import Scanner, is_identifier, is_constant

if __name__ == "__main__":
    ST = HashTable(10)
    pif = PIF()
    scanner = Scanner()

    program = "p1.txt"
    exception = ""
    scanner.read_tokens()
    print(scanner.get_all())

    with open(program, 'r') as f:
        line = f.readline()
        index_line = 1
        for line in f:
            tokens = scanner.get_line_tokens(line.strip())
            for i in range(len(tokens)):
                if tokens[i] in scanner.get_all():
                    if tokens[i] == ' ':
                        continue
                    pif.insert(tokens[i], (-1, -1))
                elif is_identifier(tokens[i]):
                    ST.add(tokens[i])
                    identifier = tokens[i]
                    pif.insert("identifier", ST.getIndex(identifier))
                elif is_constant(tokens[i]):
                    ST.add(tokens[i])
                    constant = tokens[i]
                    pif.insert("constant", ST.getIndex(constant))
                else:
                    exception += 'Lexical error --> ' + tokens[i] + ' - at line ' + str(index_line) + "\n"
            index_line += 1

    with open('PIF.out', 'w') as writer:
        writer.write(str(pif))

    with open('ST.out', 'w') as writer:
        writer.write(str(ST))

    if exception == '':
        print("Lexically correct!")
    else:
        print(exception)
