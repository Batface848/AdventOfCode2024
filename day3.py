import re

def mul(num1, num2):
    return num1 * num2

class Day3Solution:
    def __init__(self):
        self.fileName = "day3.txt"
        self.result = 0
        self.data = ""

    def parseFileContents(self):
        self.data = open(self.fileName).read()

    def solvePart1(self):
        muls = re.findall("mul\([0-9]+,[0-9]+\)", self.data)
        for m in muls:
            self.result += eval(m)

        return f"Part 1 Solution: {self.result}"

    def solvePart2(self):
        self.result = 0
        muls = re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", self.data)
        status = True
        for m in muls:
            if m == "do()":
                status = True
            elif m == "don't()":
                status = False
            else:
                if status:
                    self.result += eval(m)

        return f"Part 2 Solution: {self.result}"

    def run(self):
        self.parseFileContents()
        part1Solution = self.solvePart1()
        part2Solution = self.solvePart2()
        print(part1Solution)
        print(part2Solution)

        

solution = Day3Solution()
solution.run()