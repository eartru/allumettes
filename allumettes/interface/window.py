import pygame
from os.path import dirname
from os.path import abspath
from os.path import join
from interface.utils import blit_text


class Window(object):

    def __init__(self, IA):
        self.IA = IA

    def start(self, width, height):
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Notre jeu des allumettes')

        self.game_ended = False
        self.set_image()
        self.set_text()
        while not self.game_ended:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.handle_key(event.key)

    def stop(self):
        self.game_ended = True

    def set_image(self, nb_match=0):
        main_dir = abspath(dirname(dirname(abspath(__file__))))
        image_dir = join(main_dir, 'images')
        image = pygame.image\
            .load(join(image_dir, 'allumettes_300x200.png'))\

        self.window.blit(image, (0, 0))
        pygame.display.flip()

    def set_text(self, text="Bienvenue\n sur le jeu\n des allumettes!"):
        self.reset_text()
        pygame.font.init()
        font = pygame.font.Font(pygame.font.get_default_font(), 15)
        blit_text(self.window, text, (150, 0), font)
        pygame.display.update()

    def handle_key(self, event_key):
        if event_key == pygame.K_q:
            self.stop()
        else:
            self.set_text(
                'Vous avez appuyé\n'
                'sur la touche {}\n'
                'appuyer sur la Q\n'
                'pour quitter le jeu'.format(
                    chr(event_key).upper()
                )
            )

    def reset_text(self):
        pygame.draw.rect(self.window, (0, 0, 0), [150, 0, 150, 300], 0)
        pygame.display.flip()
