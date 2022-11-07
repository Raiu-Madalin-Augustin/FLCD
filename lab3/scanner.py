import re


def is_identifier(elem):
    return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9])*$', elem) is not None


def is_constant(elem):
    return re.match(r'^(0|[+-]?[1-9][0-9]*)$|^\'.*\'$', elem) is not None


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
            for i in range(17):
                self.__reserved_words.append(f.readline().strip())
            for i in range(17):
                self.__operators.append(f.readline().strip())
            for i in range(13):
                separator = f.readline().strip()
                if separator == 'space':
                    self.__separators.append(" ")
                else:
                    self.__separators.append(separator)

    def is_operator(self, elem):
        for o in self.__operators:
            if elem in o:
                return True
        return False

    def get_line_tokens(self, line):
        token = ''
        tokens = []
        i = 0
        while i < len(line):
            if line[i] == '\'':
                token, tokens, i = self._string(token, tokens, line, i)
            elif self.is_operator(line[i]):
                token, tokens, i = self._operator(token, tokens, line, i)
            elif line[i] in self.__separators:
                token, tokens, i = self._separator(token, tokens, line, i)
            else:
                token += line[i]
                i += 1
        if len(token) > 0:
            tokens.append(token)
        return tokens

    @staticmethod
    def _string(token, tokens, line, i):
        if len(token) > 0:
            tokens.append(token)
        token = '\''
        end_string = False
        i += 1
        while i < len(line) and not end_string:
            if line[i] == '\'':
                end_string = True
            token += line[i]
            i += 1
        tokens.append(token)
        token = ''

        return token, tokens, i

    def _operator(self, token, tokens, line, i):
        if len(token) > 0:
            tokens.append(token)
        token = ''
        while i < len(line) and self.is_operator(line[i]):
            token += line[i]
            i += 1
        tokens.append(token)
        token = ''
        return token, tokens, i

    @staticmethod
    def _separator(token, tokens, line, i):
        if len(token) > 0:
            tokens.append(token)
        token = line[i]
        i += 1
        tokens.append(token)
        token = ''
        return token, tokens, i
