game_grid = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
letters = ['X', 'O']
count = 1
symbols = ''


def display_grid(game_grid):
      print(game_grid[1]+'|'+game_grid[2]+'|'+game_grid[3])
      print('-----')
      print(game_grid[4] + '|' + game_grid[5] + '|' + game_grid[6])
      print('-----')
      print(game_grid[7] + '|' + game_grid[8] + '|' + game_grid[9])
    

def take_input():
      first_letter = input('Player 1: choose between "X" or "O" :')
      first_letter = first_letter.upper()
      if first_letter == 'X':
            letters[0] = 'X'
            letters[1] = 'O'
            return
      elif first_letter == 'O':
            letters[0] = 'O'
            letters[1] = 'X'
            return
      else:
            print("X or O ?")
            take_input()


def display_input_on_grid():
      global count
      global symbols
      add = True
      while add:
            num = input('Choose the number 1 - 9:  ')
            if num.isdigit():
                  num = int(num)
                  if 0 < num < 10:
                        if game_grid[num] == ' ':
                              if count % 2 != 0:
                                    game_grid[num] = letters[0]
                                    symbols = letters[0]
                                    count += 1
                                    break
                              else:
                                    game_grid[num] = letters[1]
                                    symbols = letters[1]
                                    count += 1
                                    break
                        else:
                              print('Please choose another number')
                              continue
            print('Choose the number 1 - 9   ')


def winner(game_grid, symbol):
      global symbols
      if count % 2 != 0:
            symbol = letters[1]
            symbols = letters[1]
      else:
            symbol = letters[0]
            symbols = letters[0]

      if((game_grid[1] == symbol and game_grid[2] == symbol and game_grid[3] == symbol) or  
            (game_grid[4] == symbol and game_grid[5] == symbol and game_grid[6] == symbol) or  
            (game_grid[7] == symbol and game_grid[8] == symbol and game_grid[9] == symbol) or  
            (game_grid[1] == symbol and game_grid[4] == symbol and game_grid[7] == symbol) or  
            (game_grid[2] == symbol and game_grid[5] == symbol and game_grid[8] == symbol) or  
            (game_grid[3] == symbol and game_grid[6] == symbol and game_grid[9] == symbol) or  
            (game_grid[1] == symbol and game_grid[5] == symbol and game_grid[9] == symbol) or  
            (game_grid[7] == symbol and game_grid[5] == symbol and game_grid[3] == symbol)     
      ):
            return True
      else:
            if count % 2 != 0:
                  symbols = letters[0]
            else:
                  symbols = letters[1]
            return False


def next_game():
      char = input('One more game? Y/N :')
      char = char.upper()
      if char == 'Y' or char == 'N':
            return char
      else:
            print('Yes (Y) or No (N)?')
            next_game()


new_game = True
while new_game:
      game_grid = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
      symbols = ''
      take_input()                                                           
      play_game = True
      while play_game:
            if count < 10 and not (winner(game_grid, symbols)):
                  display_input_on_grid()                                         
                  display_grid(game_grid)                                           
                  if winner(game_grid, symbols):
                        if symbols == letters[0]:
                              print('Player 1 won')                        
                              count = 1
                              break
                        else:
                              print('Player 2 won')                          
                              count = 1
                              break
                  play_game = True
            elif count >= 10:
                  count = 1
                  print('Drawn')                                       
                  play_game = False
      one_more_game = next_game()                                            
      if one_more_game == 'Y':
            new_game = True
      else:
            new_game = False