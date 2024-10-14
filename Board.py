class Boards:
    coord = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def showB(self):
        print(self.coord[0], "|", self.coord[1], "|", self.coord[2])
        print("==========")
        print(self.coord[3], "|", self.coord[4], "|", self.coord[5])
        print("==========")
        print(self.coord[6], "|", self.coord[7], "|", self.coord[8])

    def PutX(self):
        inX = input("For Player 'X': Enter a number which is only shown in board : ")
        if inX in self.coord:
            self.coord[int(inX) - 1] = "x"
        self.showB()

    def PutO(self):
        inO = input("For Player 'O': Enter a number which is only shown in board : ")
        self.coord[int(inO) - 1] = "o"
        self.showB()
