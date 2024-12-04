import re

class Day4Solution:
    def __init__(self):
        self.fileName = "day4.txt"
        self.data = ""
        self.counter = 0

    def parseFileContents(self):
        self.data = open(self.fileName).read()
        self.parsedData = self.data.splitlines()

    def solvePart1(self):
        # Horizontals
        for line in self.parsedData:
            horizontalXMAS = re.findall("XMAS", line)
            horizontalSAMX = re.findall("SAMX", line)
            self.counter += len(horizontalXMAS) + len(horizontalSAMX)
        # Verticals
        for i in range(len(self.parsedData)):
            tempVerticalString = ""
            for j in range(len(self.parsedData)):
                tempVerticalString += self.parsedData[j][i]

            verticalXMAS = re.findall("XMAS", tempVerticalString) 
            verticalSAMX = re.findall("SAMX", tempVerticalString) 
            self.counter += len(verticalXMAS) + len(verticalSAMX)
        # Top Left Diagonals
        for i in range(len(self.parsedData) - 1, -1, -1):
            tempTopLeftDiagonalStringFirstHalf = ""
            adding = True
            row = i
            column = 0
            while adding:
                if row > len(self.parsedData) - 1 or column > len(self.parsedData) - 1:
                    adding = False
                else:
                    tempTopLeftDiagonalStringFirstHalf += self.parsedData[row][column]
                    row += 1
                    column += 1
            firstHalfTopLeftDiagonalXMAS = re.findall("XMAS", tempTopLeftDiagonalStringFirstHalf) 
            firstHalfTopLeftDiagonalSAMX = re.findall("SAMX", tempTopLeftDiagonalStringFirstHalf) 
            self.counter += len(firstHalfTopLeftDiagonalXMAS) + len(firstHalfTopLeftDiagonalSAMX)
        
        for j in range(1, len(self.parsedData)):
            tempTopLeftDiagonalStringSecondHalf = ""
            adding = True
            column = j
            row = 0
            while adding:
                if row > len(self.parsedData) - 1 or column > len(self.parsedData) - 1:
                    adding = False
                else:
                    tempTopLeftDiagonalStringSecondHalf += self.parsedData[row][column]
                    row += 1
                    column += 1
            secondHalfTopLeftDiagonalXMAS = re.findall("XMAS", tempTopLeftDiagonalStringSecondHalf) 
            secondHalfTopLeftDiagonalSAMX = re.findall("SAMX", tempTopLeftDiagonalStringSecondHalf) 
            self.counter += len(secondHalfTopLeftDiagonalXMAS) + len(secondHalfTopLeftDiagonalSAMX)

        # Top Right Diagonals
        for i in range(len(self.parsedData) - 1, -1, -1):
            tempTopRightDiagonalStringFirstHalf = ""
            adding = True
            row = i
            column = len(self.parsedData) - 1
            while adding:
                if row > len(self.parsedData) - 1 or column < 0:
                    adding = False
                else:
                    tempTopRightDiagonalStringFirstHalf += self.parsedData[row][column]
                    row += 1
                    column -= 1
            firstHalfTopRightDiagonalXMAS = re.findall("XMAS", tempTopRightDiagonalStringFirstHalf) 
            firstHalfTopRightDiagonalSAMX = re.findall("SAMX", tempTopRightDiagonalStringFirstHalf) 
            self.counter += len(firstHalfTopRightDiagonalXMAS) + len(firstHalfTopRightDiagonalSAMX)

        for j in range(len(self.parsedData) - 2, -1, -1):
            tempTopRightDiagonalStringSecondHalf = ""
            adding = True
            column = j
            row = 0
            while adding:
                if row > len(self.parsedData) - 1 or column < 0:
                    adding = False
                else:
                    tempTopRightDiagonalStringSecondHalf += self.parsedData[row][column]
                    row += 1
                    column -= 1

            secondHalfTopRightDiagonalXMAS = re.findall("XMAS", tempTopRightDiagonalStringSecondHalf) 
            secondHalfTopRightDiagonalSAMX = re.findall("SAMX", tempTopRightDiagonalStringSecondHalf) 
            self.counter += len(secondHalfTopRightDiagonalXMAS) + len(secondHalfTopRightDiagonalSAMX)

        return f"Part 1 Solution: {self.counter}"

    def solvePart2(self):
        self.counter = 0
        for i in range(1, len(self.parsedData) - 1):
            for j in range(1, len(self.parsedData) - 1):
                if self.parsedData[j][i] == "A":
                    if self.parsedData[j - 1][i - 1] == "M" and self.parsedData[j - 1][i + 1] == "M" and self.parsedData[j + 1][i - 1] == "S" and self.parsedData[j + 1][i + 1] == "S":
                        self.counter += 1
                    elif self.parsedData[j - 1][i - 1] == "S" and self.parsedData[j - 1][i + 1] == "S" and self.parsedData[j + 1][i - 1] == "M" and self.parsedData[j + 1][i + 1] == "M":
                        self.counter += 1
                    elif self.parsedData[j - 1][i - 1] == "M" and self.parsedData[j - 1][i + 1] == "S" and self.parsedData[j + 1][i - 1] == "M" and self.parsedData[j + 1][i + 1] == "S":
                        self.counter += 1
                    elif self.parsedData[j - 1][i - 1] == "S" and self.parsedData[j - 1][i + 1] == "M" and self.parsedData[j + 1][i - 1] == "S" and self.parsedData[j + 1][i + 1] == "M":
                        self.counter += 1
                else:
                    pass
        return f"Part 2 Solution: {self.counter}"

    def run(self):
        self.parseFileContents()
        part1Solution = self.solvePart1()
        part2Solution = self.solvePart2()
        print(part1Solution)
        print(part2Solution)

        

solution = Day4Solution()
solution.run()