class Boards:
    coord = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def showB(self):
        print()
        print("\t", self.coord[0], "\t|\t", self.coord[1], "\t|\t", self.coord[2])
        print("===================================================")
        print("\t", self.coord[3], "\t|\t", self.coord[4], "\t|\t", self.coord[5])
        print("===================================================")
        print("\t", self.coord[6], "\t|\t", self.coord[7], "\t|\t", self.coord[8])

    def PutX(self):
        inX = input("For Player 'X': Enter a number which is only shown in board : ")
        if(int(inX) > 9):
            print("\t!!!! NUMBERS ONLY SEEN IN BOARD ARE VALID !!!!!")
            self.PutX()
        if inX in self.coord:
            self.coord[int(inX) - 1] = "x"
        self.showB()

    def PutO(self):
        inO = input("For Player 'O': Enter a number which is only shown in board : ")
        if(int(inO) > 9):
            print("\t!!!! NUMBERS ONLY SEEN IN BOARD ARE VALID !!!!!")
            self.PutO()
        self.coord[int(inO) - 1] = "o"
        self.showB()
