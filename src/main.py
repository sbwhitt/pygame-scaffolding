from game import Game
from pygame.display import set_caption

if __name__ == '__main__':
    set_caption('game')
    g = Game()
    g.on_execute()
