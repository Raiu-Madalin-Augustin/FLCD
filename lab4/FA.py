class FA:
    def __init__(self, filename):
        self.Q = {}
        self.E = {}
        self.q0 = {}
        self.F = {}
        self.T = {}
        self.read_input_file(filename)

    def read_input_file(self, filename):
        with open(filename) as f:
            self.Q = f.readline().strip().replace(" ", "")[3:-1].split(',')
            self.E = f.readline().strip().replace(" ", "")[3:-1].split(',')
            self.q0 = f.readline().strip().replace(" ", "")[4:-1].strip(',')
            self.F = f.readline().strip().replace(" ", "")[3:-1].split(',')

            f.readline()
            self.T = {}

            for line in f:
                if line != '}' and len(line) > 0:
                    pair = line.strip().replace(" ", "").split('->')[0].strip()[1:-1].split(",")
                    origin = pair[0]
                    path = pair[1]
                    target = line.strip().replace(" ", "").split('->')[1].strip()

                    if (origin, path) in self.T.keys():
                        self.T[(origin, path)].append(target)
                    else:
                        self.T[(origin, path)] = [target]

    def is_dfa(self):
        for key in self.T.keys():
            if len(self.T[key]) > 1:
                return False
        return True

    def is_accepted_by_fa(self, sequence):
        if self.is_dfa():
            start = self.q0
            for c in sequence:
                if (start, c) in self.T.keys():
                    start = self.T[(start, c)][0]
                else:
                    return False
            if start in self.F:
                return True

        return False

    def __str__(self):
        T = ""
        for (origin, path) in self.T.keys():
            T += "(" + str(origin) + "," + str(path) + ")" + "->" + str(self.T[(origin, path)]) + "\n"
        return "Q = " + str(self.Q) + "\n" + "E = " + str(self.E) + "\n" + "q0 = {" + str(
            self.q0) + "}\n" + "F = " + str(self.F) + "\n" + "T = {\n" + T + "\n"


x = FA("FA.in")
print(x)
