class PIF:
    def __init__(self):
        self.__pairs = []

    def insert(self, token, position):
        self.__pairs.append((token, position))

    def __str__(self):
        text = ""
        for pair in self.__pairs:
            text += pair[0] + "->" + str(pair[1]) + "\n"
        return text
