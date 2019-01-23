import numpy as np

class GameState:
    board = np.zeros((4,4))
    #(0,0)(0,1)(0,2)(0,3)
    #(1,0)(1,1)(1,2)(1,3)
    #(2,0)(2,1)(2,2)(2,3)
    #(3,0)(3,1)(3,2)(3,3)
    old_board = np.zeros((4,4))
    score = 0

    def is_game_over(self) -> bool:
        #check for zeros
        if (np.count_nonzero(self.board)==4*4):
            for i in range(4):
                for j in range(4):
                    if self.check_neighbourhood(i,j):
                        return False
            return True
        return False

    def check_neighbourhood(self, i: int, j: int) -> bool:
        #returns true if any neighouring cell has the same value
        if i+1<4 and self.board[i+1][j]==self.board[i][j]:
            return True
        if j+1<4 and self.board[i][j+1]==self.board[i][j]:
            return True
        if i-1>=0 and self.board[i-1][j]==self.board[i][j]:
            return True
        if j-1>=0 and self.board[i][j-1]==self.board[i][j]:
            return True
        return False

    def check_valid_move(self) -> bool:
        if np.array_equal(self.board,self.old_board):
            return False #not valid
        self.old_board=np.copy(self.board)
        return True #valid

    def spawn_number(self) -> None:
        possible_coordinates=np.where(self.board==0) #where no number exists
        if possible_coordinates[0].size>0:
            if possible_coordinates[0].size==1:
                index=0
            elif possible_coordinates[0].size>1:
                index=np.random.randint(0,possible_coordinates[0].size) #select random location
            (i,j)=(possible_coordinates[0][index-1],possible_coordinates[1][index-1])
            self.board[i][j]=np.random.randint(1,3) #random new number in [1,3[

    def left(self) -> None:
        for i in range(4): #for each line
            non_zero_indexes = np.nonzero(self.board[i])[0] #find values
            if len(non_zero_indexes)>0: #if line has values
                values=np.zeros(len(non_zero_indexes))
                ind=0
                for x in non_zero_indexes:
                    values[ind]=self.board[(i,x)]
                    ind+=1
                #print(self.mergeleftup(values))
                self.board[i] = self.mergeleftup(values)


    def right(self) -> None:
        for i in range(4): #for each line
            non_zero_indexes = np.nonzero(self.board[i])[0] #find values
            if len(non_zero_indexes)>0: #if line has values
                values=np.zeros(len(non_zero_indexes))
                ind=0
                for x in non_zero_indexes:
                    values[ind]=self.board[(i,x)]
                    ind+=1
                #print(self.mergeleftup(values))
                self.board[i] = self.mergeleftup(values[::-1])[::-1]

    def up(self) -> None:
        for j in range(4):
            non_zero_indexes=np.nonzero(self.board[:,j])[0]
            if len(non_zero_indexes)>0:
                values=np.zeros(len(non_zero_indexes))
                ind=0
                for x in non_zero_indexes:
                    values[ind]=self.board[(x,j)]
                    ind+=1
                #print(self.mergeleftup(values))
                self.board[:,j] = self.mergeleftup(values)

    def down(self) -> None:
        for j in range(4):
            non_zero_indexes=np.nonzero(self.board[:,j])[0]
            if len(non_zero_indexes)>0:
                values=np.zeros(len(non_zero_indexes))
                ind=0
                for x in non_zero_indexes:
                    values[ind]=self.board[(x,j)]
                    ind+=1
                #print(self.mergeleftup(values))
                self.board[:,j] = self.mergeleftup(values[::-1])[::-1]

    def mergeleftup(self, values:np.array) -> np.array:
        temp = 0
        array = np.zeros(4)
        i=0
        while(i in range(values.size)):
            if i+1<len(values):
                if values[i] == values[i+1]:
                    array[temp] = values[i]+1
                    self.score+= array[temp]
                    temp+= 1
                    i+= 1
                else:
                    array[temp] = values[i]
                    temp+= 1
            else:
                array[temp] = values[i]
                temp+= 1
            i+=1
        return np.concatenate((array,np.zeros(4-len(array))),axis=0)

    def playgamemanual(self) -> int:
        self.spawn_number()
        #print(self.check_valid_move())
        while not self.is_game_over():
            self.turnmanual()
        print(self.board)
        print(self.score)
        return self.score

    def turnmanual(self) -> None:
        print(self.board)
        while(True):
            self.getmovemanual()
            if self.check_valid_move():
                break
        self.spawn_number()

    def getmovemanual(self) -> None:
        commands = {"l":self.left,"r":self.right, "u":self.up, "d":self.down}
        while(True):
            cmd=input("enter your move:")
            if cmd in commands:
                break
        commands[cmd]()



#    def turn(self) -> None:
#        getmove()
#        spawn_number()


#    def playgame(self) -> int:
#        while not is_game_over:
#            turn()
#        return score
