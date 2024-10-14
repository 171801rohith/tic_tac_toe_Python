from Board import Boards


class Work:
    board = Boards()
    count = 0
    i = 0

    def check_win(self):
        for i in range(0, len(self.board.coord), 3):
            if (
                self.board.coord[i]
                == self.board.coord[i + 1]
                == self.board.coord[i + 2]
            ):
                return True

        for i in range(3):
            if (
                self.board.coord[i]
                == self.board.coord[i + 3]
                == self.board.coord[i + 6]
            ):
                return True

        if self.board.coord[0] == self.board.coord[4] == self.board.coord[8] != " ":
            return True

        if self.board.coord[2] == self.board.coord[4] == self.board.coord[6] != " ":
            return True

        return False

    def start(self):
        self.board.showB()
        for self.i in range(0, len(self.board.coord)):
            if not( self.check_win) and (int(self.i) % 2 == 0):
                self.board.PutX()
                self.count = 1
            elif not( self.check_win) and (int(self.i) % 2 != 0):
                self.board.PutO()
                self.count = 2
            else:
                break

        if self.i == len(self.board.coord) - 1:
            print("Draw")
        elif self.count == 1:
            print("X wins")
        elif self.count == 2:
            print("O wins")
