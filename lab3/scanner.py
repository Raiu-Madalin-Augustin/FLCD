import re


class Scanner:
    def __init__(self):
        self.__reserved_words = []
        self.__separators = []
        self.__operators = []

    def get_separators(self):
        return self.__separators

    def get_reserved_words(self):
        return self.__reserved_words

    def get_operators(self):
        return self.__operators

    def get_all(self):
        return self.__operators + self.__separators + self.__reserved_words

    def read_tokens(self):
        with open('token.in', 'r') as f:
            for i in range(16):
                self.__reserved_words.append(f.readline().strip())
            for i in range(16):
                self.__operators.append(f.readline().strip())
            for i in range(12):
                separator = f.readline().strip()
                if separator == 'space':
                    self.__separators.append(" ")
                else:
                    self.__operators.append(separator)

    def is_constant(self, elem):
        return re.match(r'^(0|[+-]?[1-9][0-9]*)$|^\'.*\'$', elem) is not None

    def is_identifier(self, elem):
        return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9])*$', elem) is not None
