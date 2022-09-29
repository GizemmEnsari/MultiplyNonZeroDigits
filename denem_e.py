

class calc:
    allResults = []
    allNumbers = []

    def __init__(self , number):
        self.sum = 0
        self.temp = 0
        self.number = str(number)
        self.eachDigit = []
        calc.allNumbers.append(number)
        self.firstStep()

    def firstStep(self): # make an array with all the non zero numbers

        for i in range(len(self.number)):
            if int(self.number[i]) != 0:
                self.eachDigit.append(int(self.number[i]))
        self.secondStep()

    def secondStep(self): #multiply all the numbers in the eachDigit array

        self.temp = self.eachDigit[0]
        for i in range(len(self.eachDigit)-1):
            self.temp = self.temp * self.eachDigit[i+1]
            if i == len(self.eachDigit)-1:
                self.lastStep()


    def lastStep(self):  # store and return the final answer
        self.eachDigit = []
        if int(self.temp) < 10:
            calc.allResults.append(self.temp)
            return self.temp
        else:
            for i in range(len(str(self.temp))):
                self.eachDigit.append(int(str(self.temp)[i]))

            self.secondStep()

x = calc(808)
print(x)







# 808 -> 64 -> 24 = 8