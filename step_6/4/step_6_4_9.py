from collections import namedtuple

Game = namedtuple('Game', 'name developer publisher')

ExtendedGame = namedtuple('ExtendedGame',(*Game._fields,'release_date', 'price'))

game = ExtendedGame(1,2,3,4,5)
print(game)