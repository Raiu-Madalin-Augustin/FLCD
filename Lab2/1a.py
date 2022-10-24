from Lab2.SymbolTable import HashTable

if __name__ == "__main__":
    table = HashTable(3)

    table.add("a")
    table.add("b")
    table.add("d")
    table.add("c")
    table.add("e")
    table.add("ee")

    table.add(2)
    table.add(1)
    table.add(4)
    table.add(5)

    print(table)

