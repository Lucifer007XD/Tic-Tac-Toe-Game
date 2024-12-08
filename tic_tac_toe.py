from typing import Union,Optional,Tuple,NewType,Set,Dict
from dataclasses import dataclass
import unittest
#Creating Type Token
@dataclass 
class X:
     pass
 
@dataclass
class O:
     pass

Token=Union[X,O]


# creating Cell as a Optional Token Type
Cell=Optional[Token]

#creating Row as Type Cell Tuple

Row = NewType("Row",Tuple[Cell,Cell,Cell])

# Creating Grid as Type Row tuple
Board = NewType("Board",Tuple[Row,Row,Row])


#Coordinates
@dataclass
class A:
     pass
@dataclass
class B:
     pass
@dataclass
class C:
     pass
axis=Union[A,B,C]

Cord=NewType("Cord",Tuple[axis,axis])


#Accessing the 
#Elements of the Grid Typed Dictionary Access Created
Access=NewType("Access",Dict[Cord,Cell])


#creating function to parse String to Token
def parseToken(value:str)->Token:
     match value:
          case "X"|"x":
               return X()
          case "O"|"o":
               return O()
          case _:
               return None
#Creating Function to getToken
def getToken()->Token:
     ask=parseToken(input("Enter the Valid Token: "))
     match ask:
          case X():
               return X()
          case O():
               return O()
          case _:
               print("Invalid Token")
               return getToken()

#creating function to parse String to CoordinateAxis value
def parseCoordinateAxis(value:str):
     match value:
          case "A"|"a":
               return A()
          case "B"|"b":
               return B()
          case "C"|"c":
               return C()
          case _:
               return None

#getting Coordinates
def getCoordinatesAxis()->axis:
          cordaxis=parseCoordinateAxis(input("Enter the coordinates: "))
          match cordaxis:
               case A():
                    return A
               case B():
                    return B
               case C():
                    return C
               case _:
                    print("Invalid Coordinate")
                    return getCoordinatesAxis()
               
     

def getCoordinates()->Cord:
     print("---Getting Horizontal Coordinates ---")
     hcord:axis=getCoordinatesAxis()
     print("\n")
     print("---Getting Vertical Coordinates---")
     vcord:axis=getCoordinatesAxis()
     print("\n")
     cord:Cord=(hcord,vcord)
     return cord


               
               


     

               


     

#Creating Board From Access Dictionary
def createBoard(ac:Access)->Board:
     row1=[None,None,None]
     row1[0]=ac[(A,A)]
     row1[1]=ac[(A,B)]
     row1[2]=ac[(A,C)]
     tuple(row1)
     row2=[None,None,None]
     row2[0]=ac[(B,A)]
     row2[1]=ac[(B,B)]
     row2[2]=ac[(B,C)]
     tuple(row2)
     row3=[None,None,None]
     row3[0]=ac[(C,A)]
     row3[1]=ac[(C,B)]
     row3[2]=ac[(C,C)]
     tuple(row3)
     bd:Board=(row1,row2,row3)
     return bd
                
def createAccess(bd:Board)->Access:
     ac:Access=dict()
     ac[(A,A)]=bd[0][0]
     ac[(A,B)]=bd[0][1]
     ac[(A,C)]=bd[0][2]
     ac[(B,A)]=bd[1][0]
     ac[(B,B)]=bd[1][1]
     ac[(B,C)]=bd[1][2]
     ac[(C,A)]=bd[2][0]
     ac[(C,B)]=bd[2][1]
     ac[(C,C)]=bd[2][2]
     return ac
# play Token
def playToken(tk:Token,bd:Board)->Board:
     ac:Access=createAccess(bd)
     cord:Cord=getCoordinates()
     if (ac[cord]== X() or ac[cord]==O()):
               print("Token Already Placed:Choose Another Spot")
               return bd
     else:
               ac[cord]=tk
               bd=createBoard(ac)
               return bd    

def playTokenByBot(tk:Token,bd:Board)->Board:
     access:Access=createAccess(bd)
     axiss=(A,B,C)

     for row in axiss:
          for column in axiss:
               if (access[(row,column)]==None):
                    access[(row,column)]=tk
                    return createBoard(access)
     





#check Winner
def checkDiagnal(ac:Access):
     if (ac[(A,A)]==ac[B,B] and ac[B,B]==ac[C,C]):
          match ac[(A,A)]:
               case X():
                    return X()
               case O():
                    return O()
               case _:
                    return None
     elif(ac[(A,C)]==ac[(B,B)] and ac[(A,C)]==ac[(C,A)]):
          match ac[(A,C)]:
               case X():
                    return X()
               case O():
                    return O()
               case _:
                    return None
     else:
          return None

def checkRow(ac:Access):
     if (ac[(A,A)]==ac[(A,B)] and ac[(A,B)]==ac[(A,C)]):
          match ac[(A,A)]:
               case X():
                    return X()
               case O():
                    return O()
               case _:
                    return None
     elif(ac[(B,A)]==ac[(B,B)] and ac[(B,B)]==ac[(B,C)]):
          match ac[(B,A)]:
               case X():
                    return X()
               case O():
                    return O()
               case _:
                    return None
     elif(ac[(C,A)]==ac[(C,B)] and ac[(C,B)]==ac[(C,C)]):
          match ac[(C,A)]:
               case X():
                    return X()
               case O():
                    return O()
               case _:
                    return None
     else:
          return None

def checkColumn(ac:Access):
     if (ac[(A,A)]==ac[(B,A)] and ac[(B,A)]==ac[(C,A)]):
          match ac[(A,A)]:
               case X():
                    return X()
               case O():
                    return O()
               case _:
                    return None
     elif(ac[(A,B)]==ac[(B,B)] and ac[(B,B)]==ac[(C,B)]):
          match ac[(A,B)]:
               case X():
                    return X()
               case O():
                    return O()
               case _:
                    return None
     elif(ac[(A,C)]==ac[(B,C)] and ac[(B,C)]==ac[(C,C)]):
          match ac[(A,C)]:
               case X():
                    return X()
               case O():
                    return O()
               case _:
                    return None
     else:
          return None
     
               
def checkWinner(ac:Access):
     match checkDiagnal(ac):
          case X():
               return X()
          case O():
               return O()
     match checkRow(ac):
          case X():
               return X()
          case O():
               return O()
     match checkColumn(ac):
          case X():
               return X()
          case O():
               return O()
     return None


#get Empty the board
def getEmptyBoard():
     row:Row=(None,None,None)
     board=(row,row,row)
     return board

def countTokenFilledCell(board:Board)->int:
     count=0
     for r in board:
          for e in r:
               if( e==X() or e==O()):
                    count+=1
     return count

def checkTieGame(board:Board)->bool:
     if (countTokenFilledCell(board)==9):
          return True
     else:
          return False
     


                    
                         
     
def displayBoard(board:Board):
     print("--------------Board----------------")
     print("--------------------")
     for i in board:
          for j in i:
               if( j==X()):
                         print("|  X  |",end="")
               elif(j==O()):
                         print("|  O  |",end="")
               else:
                         print("|     |",end="")
          print("\n--------------------")



def displayMenu():
     print("----Tic Tac Toe----")
     print("1. Player Vs Player")
     print("2. Player Vs CMP")
     print("3. Exit")

def main():
     playAgain=True
     while(playAgain):
          player1=None
          player2=None
          displayMenu()
          LastTurn:Cell=None
          gameTied=False
          Winner:Cell=None
          Loser:Cell=None
          gotWinner=False
          selectedPlay=input("Select the Option (1/2/3): ")
          board:Board=getEmptyBoard()
          access:Access=createAccess(board)
          match selectedPlay:
               case "1":
                    print("Player 1 Select the Token:-")
                    player1=getToken()
                    match player1:
                         case X():
                              player2=O()
                              print("--------------------\nToken\n--------------------\nPlayer 1: X\nPlayer 2: O\n------------------")
                         case O():
                              player2=X()
                              print("--------------------\nToken\n--------------------\nPlayer 1: O\nPlayer 2: X\n------------------")
                    while(gameTied==gotWinner):
                         displayBoard(board)
     
                         if(LastTurn==None or LastTurn==player2):
                              print("----------------\n-----Player 1 Turn----\n-----------------")
                              lastBoard=board
                              board=playToken(player1,board)
                              access=createAccess(board)
                              LastTurn=player1
                              while(lastBoard==board):
                                   board=playToken(player1,board)
                                   access=createAccess(board)
                                   LastTurn=player1

                         
                         elif(LastTurn==player1):
                              print("----------------\n-----Player 2 Turn----\n-----------------")
                              lastBoard=board
                              board=playToken(player2,board)
                              access=createAccess(board)
                              LastTurn=player2
                              while(lastBoard==board):
                                   board=playToken(player2,board)
                                   access=createAccess(board)
                                   LastTurn=player2
                         else:
                              print("bug")
                    




                        
                         match checkWinner(access):
                              case X():
                                   gotWinner=True
                                   displayBoard(board)
                                   Winner=X()
                                   Loser=O()
                              case O():
                                   gotWinner=True
                                   displayBoard(board)
                                   Winner=O()
                                   Loser=X()
                              case _:
                                   gotWinner=False
                         match checkTieGame(board):
                              case True:
                                   displayBoard(board)
                                   gameTied=True
                              case False:
                                   gameTied=False

                    
                    
               
               case "2":
                    print("Player 1 select token:-")
                    player1=getToken()
                    match player1:
                         case X():
                              bot=O()
                              print("--------------------\nToken\n--------------------\nPlayer 1: X\nPlayer 2: O\n------------------")
                         case O():
                              bot=X()
                              print("--------------------\nToken\n--------------------\nPlayer 1: O\nPlayer 2: X\n------------------")
                    while(gameTied==gotWinner):
                         displayBoard(board)
                         if( LastTurn==None or LastTurn==bot):
                              lastBoard=board
                              board=playToken(player1,board)
                              access=createAccess(board)
                              LastTurn=player1
                              while(lastBoard==board):
                                   board=playToken(player1,board)
                                   access=createAccess(board)
                                   LastTurn=player1

                         else:
                              board=playTokenByBot(bot,board)
                              access=createAccess(board)
                              LastTurn=bot
                         match checkWinner(access):
                              case X():
                                   gotWinner=True
                                   displayBoard(board)
                                   Winner=X()
                                   Loser=O()
                              case O():
                                   gotWinner=True
                                   displayBoard(board)
                                   Winner=O()
                                   Loser=X()
                              case _:
                                   gotWinner=False
                         match checkTieGame(board):
                              case True:
                                   gameTied=True
                              case False:
                                   gameTied=False
          
               case "3":
                    playAgain=False
                    print("Thank You For Playing \nNOTE:IF you want to play Run the Game Again")
                    return 0
               case _:
                    playAgain=True
                    print("Invalid Option")
          if(gotWinner):
               match Winner:
                    case X():
                         print("--------------------------\nResults\n--------------------------\nWinner: {} \nLoser: {}\n--------------------------".format("X","O"))
                    case O():
                         print("--------------------------\nResults\n--------------------------\nWinner: {} \nLoser: {}\n--------------------------".format("O","X"))
               
          if(gameTied):
               print("--------------------------\nResults\n--------------------------\nGAME TIED\n Lets have Another game To Decide the Winner\n--------------------------")
     



class TicTacToeTestCase(unittest.TestCase):
     def test_parseToken(self):
          x=parseToken("x")
          b=parseToken("b")
          self.assertEqual(x,X())
          self.assertEqual(b,None)
     def test_parseCoordinateAxis(self):
          a=parseCoordinateAxis("A")
          x=parseCoordinateAxis("X")
          self.assertEqual(a,A())
          self.assertEqual(x,None)
     def test_getEmptyBoard(self):
          row=(None,None,None)
          board=(row,row,row)
          self.assertEqual(board,getEmptyBoard())  
     def test_checkTieGame(self):
          row=(X(),O(),O())
          row1=(X(),O(),O())
          row2=(O(),X(),X())
          row3=(None,None,None)
          board=(row,row1,row2)
          self.assertTrue(checkTieGame(board))
          board1=(row1,row2,row3)
          self.assertFalse(checkTieGame(board1))

     def test_checkWinner(self):
          row=(X(),None,O())
          row1=(X(),O(),O())
          row2=(X(),None,None)
          board=(row,row1,row2)
          self.assertEqual(checkWinner(createAccess(board)),X())
     def test_checkDiagnal(self):
          row=(X(),O(),None)
          row1=(O(),X(),O())
          row2=(None,None,X())
          board=(row,row1,row2)
          self.assertEqual(checkDiagnal(createAccess(board)),X())
     def test_checkRow(self):
          row=(O(),O(),None)
          row1=(X(),X(),X())
          row2=(None,None,O())
          board=(row,row1,row2)
          self.assertEqual(checkRow(createAccess(board)),X())
    
     def test_checkColumn(self):
          row=(X(),None,O())
          row1=(X(),O(),O())
          row2=(X(),None,None)
          board=(row,row1,row2)
          self.assertEqual(checkColumn(createAccess(board)),X())
    
    



if __name__ == '__main__':
    unittest.main()








    
