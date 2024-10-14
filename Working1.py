from Board import Boards


class Work1:
    board = Boards()
    i = 0
    count = 0

    def start(self):
        self.board.showB()
        for self.i in range(0, len(self.board.coord)):
            if not (
                (
                    self.board.coord[0] == self.board.coord[1]
                    and self.board.coord[1] == self.board.coord[2]
                )
                or (
                    self.board.coord[3] == self.board.coord[4]
                    and self.board.coord[4] == self.board.coord[5]
                )
                or (
                    self.board.coord[6] == self.board.coord[7]
                    and self.board.coord[7] == self.board.coord[8]
                )
                or (
                    self.board.coord[0] == self.board.coord[3]
                    and self.board.coord[3] == self.board.coord[6]
                )
                or (
                    self.board.coord[1] == self.board.coord[4]
                    and self.board.coord[4] == self.board.coord[7]
                )
                or (
                    self.board.coord[2] == self.board.coord[5]
                    and self.board.coord[5] == self.board.coord[8]
                )
                or (
                    self.board.coord[0] == self.board.coord[4]
                    and self.board.coord[4] == self.board.coord[8]
                )
                or (
                    self.board.coord[2] == self.board.coord[4]
                    and self.board.coord[4] == self.board.coord[6]
                )
            ) and (int(self.i) % 2 == 0):
                self.board.PutX()
                self.count = 1
            elif not (
                (
                    self.board.coord[0] == self.board.coord[1]
                    and self.board.coord[1] == self.board.coord[2]
                )
                or (
                    self.board.coord[3] == self.board.coord[4]
                    and self.board.coord[4] == self.board.coord[5]
                )
                or (
                    self.board.coord[6] == self.board.coord[7]
                    and self.board.coord[7] == self.board.coord[8]
                )
                or (
                    self.board.coord[0] == self.board.coord[3]
                    and self.board.coord[3] == self.board.coord[6]
                )
                or (
                    self.board.coord[1] == self.board.coord[4]
                    and self.board.coord[4] == self.board.coord[7]
                )
                or (
                    self.board.coord[2] == self.board.coord[5]
                    and self.board.coord[5] == self.board.coord[8]
                )
                or (
                    self.board.coord[0] == self.board.coord[4]
                    and self.board.coord[4] == self.board.coord[8]
                )
                or (
                    self.board.coord[2] == self.board.coord[4]
                    and self.board.coord[4] == self.board.coord[6]
                )
            ) and (int(self.i) % 2 != 0):
                self.board.PutO()
                self.count = 2

            else:
                break
            
            if(self.i == len(self.board.coord) - 1):
                self.count = 0

        if self.count == 0:
            print("Draw")
        elif self.count == 1:
            print("X wins")
        elif self.count == 2:
            print("O wins")
