class Day5Solution:
    def __init__(self):
        self.fileName = "day5.txt"
        self.data = []
        self.totalMiddleNumbers = 0

    def parseFileContents(self):
        self.data = open(self.fileName).read().splitlines()
        self.updates = []
        self.updateRules = []
        self.pairs = []
        self.rules = []
        for i in range(0, 1176):
            self.updates.append(self.data[i])
        for j in range(1177, len(self.data)):
            self.updateRules.append(self.data[j])
        for pair in self.updates:
            p = [int(e) for e in pair.split("|")]
            self.pairs.append(p)
        for rule in self.updateRules:
            r = [int(r) for r in rule.split(",")]
            self.rules.append(r)

    def solvePart1(self):
        acceptedRules = []
        for rule in self.rules:
            accepted = True
            for pair in self.pairs:
                if pair[0] in rule and pair[1] in rule:
                    if rule.index(pair[0]) > rule.index(pair[1]):
                        accepted = False
                    else:
                        pass
                else:
                    pass
            if accepted:
                acceptedRules.append(rule)
        for rule in acceptedRules:
            middleNumber = rule[len(rule) // 2]
            self.totalMiddleNumbers += middleNumber

        return f"Part 1 Solution: {self.totalMiddleNumbers}"

    def solvePart2(self):
        self.totalMiddleNumbers = 0
        unacceptedRules = []
        newAcceptedRules = []
        for rule in self.rules:
            accepted = True
            for pair in self.pairs:
                if pair[0] in rule and pair[1] in rule:
                    if rule.index(pair[0]) > rule.index(pair[1]):
                        accepted = False
                    else:
                        pass
                else:
                    pass
            if not accepted:
                unacceptedRules.append(rule)

        for rule in unacceptedRules:
            newRule = []
            for _ in range(len(rule)):
                newRule.append(0)
            pairsRequired = []
            counters = {}
            for number in rule:
                counters[number] = 0
            print(counters)
            for pair in self.pairs:
                if pair[0] in rule and pair[1] in rule:
                    pairsRequired.append(pair)
            for pair in pairsRequired:
                if pair[1] in counters.keys():
                    counters[pair[1]] += 1
            for key, value in counters.items():
                newRule[value] = key

            newAcceptedRules.append(newRule)

        for rule in newAcceptedRules:
            middleNumber = rule[len(rule) // 2]
            self.totalMiddleNumbers += middleNumber


        return f"Part 2 Solution: {self.totalMiddleNumbers}"

    def run(self):
        self.parseFileContents()
        part1Solution = self.solvePart1()
        part2Solution = self.solvePart2()
        print(part1Solution)
        print(part2Solution)

        

solution = Day5Solution()
solution.run()
