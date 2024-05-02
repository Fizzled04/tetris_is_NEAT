from settings import *
from sys import exit
from game import Game
from score import Score
from preview import Preview

class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Tetris')
        
        # Components
        self.game = Game()
        self.score = Score()
        self.preview = Preview()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            # Display
            self.display_surface.fill(GREY)
            
            # Components
            self.game.run()
            self.score.run()
            self.preview.run()
            
            # Game updating
            pygame.display.update()
            self.clock.tick()
            
if __name__ == '__main__':
    main = Main()
    main.run()