from lab3.SymbolTable import HashTable
from lab3.pif import PIF
from lab3.scanner import Scanner

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
