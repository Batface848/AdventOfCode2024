class Day2Solution:
    def __init__(self):
        self.fileName = "day2.txt"
        self.data = []
        self.safeCount = 0
        self.clearData = []
        self.newFile = open("day2test2.txt", "w")

    def parseFileContents(self):
        contents = open(self.fileName).read().splitlines()
        for line in contents:
            splitLine = [int(item) for item in line.split(" ")]
            self.data.append(splitLine)

    def solvePart1(self):
        for level in self.data:
            safe = True
            differenceList = []
            for i in range(0, len(level) - 1):
                diff = level[i+1] - level[i]
                differenceList.append(diff)

            decreasing = False
            for index, d in enumerate(differenceList):
                if index == 0:
                    if d == 0:
                        safe = False
                        break
                    elif d < 0:
                        decreasing = True
                    else:
                        decreasing = False
                if abs(d) > 3 or abs(d) < 1:
                    safe = False
                    break
                elif decreasing and d >= 0 or not decreasing and d <= 0:
                    safe = False
                    break
                else:
                    safe = True

            if safe:
                # print(f"{self.data.index(level)}: {level}")
                self.safeCount += 1
            else:
                self.clearData.append(level)

        return f"Part 1 Solution: {self.safeCount}"

    def solvePart2(self):
        for level in self.clearData:
            levelSafe = False
            for i in range(len(level)):
                copiedLevel = level.copy()
                copiedLevel.pop(i)
                safe = True
                differenceList = []
                for i in range(0, len(copiedLevel) - 1):
                    diff = copiedLevel[i+1] - copiedLevel[i]
                    differenceList.append(diff)
                decreasing = False
                for index, d in enumerate(differenceList):
                    if index == 0:
                        if d == 0:
                            safe = False
                            break
                        elif d < 0:
                            decreasing = True
                        else:
                            decreasing = False
                    if abs(d) > 3 or abs(d) < 1:
                        safe = False
                        break
                    elif decreasing and d >= 0 or not decreasing and d <= 0:
                        safe = False
                        break
                    else:
                        safe = True

                if safe:
                    levelSafe = True
                    self.safeCount += 1
                    break
            if levelSafe:
                self.newFile.write(str(level) + "\n")


        return f"Part 2 Solution: {self.safeCount}"

    def run(self):
        self.parseFileContents()
        part1Solution = self.solvePart1()
        part2Solution = self.solvePart2()
        print(part1Solution)
        print(part2Solution)

        

solution = Day2Solution()
solution.run()