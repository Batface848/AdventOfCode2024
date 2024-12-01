class Day1Solution:
    def __init__(self):
        self.fileName = "day1.txt"
        self.leftList = []
        self.rightList = []

    def parseFileContents(self):
        contents = open(self.fileName).read().splitlines()
        for line in contents:
            splitLine = line.split("   ")
            self.leftList.append(int(splitLine[0]))
            self.rightList.append(int(splitLine[1]))

    def solvePart1(self):
        sortedLeftList = sorted(self.leftList)
        sortedRightList = sorted(self.rightList)
        distances = []
        for i in range(1000):
            distances.append(abs(sortedLeftList[i] - sortedRightList[i]))
        
        sumOfDistances = sum(distances)

        return f"Part 1 Solution: {sumOfDistances}"

    def solvePart2(self):
        similarities = []
        for number in self.leftList:
            similarityScore = number * self.rightList.count(number)
            similarities.append(similarityScore)

        sumOfSimilarities = sum(similarities)
        return f"Part 2 Solution: {sumOfSimilarities}"

    def run(self):
        self.parseFileContents()
        part1Solution = self.solvePart1()
        part2Solution = self.solvePart2()
        print(part1Solution)
        print(part2Solution)

        

solution = Day1Solution()
solution.run()