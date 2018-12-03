import pygame
from os.path import dirname
from os.path import abspath
from os.path import join
import time

from interface.utils import blit_text


class Window(object):

    def __init__(self, game):
        self.game = game

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

    def set_image(self, nb_match=16):
        self.reset_image()
        main_dir = abspath(dirname(dirname(abspath(__file__))))
        image_dir = join(main_dir, 'images')
        image = pygame.image\
            .load(join(
                image_dir, 'allumettes_{}_300x200.png'.format(nb_match))
            )

        self.window.blit(image, (0, 0))
        pygame.display.flip()

    def set_text(self, text="Bienvenue\n sur le jeu\n des allumettes!"):
        self.reset_text()
        pygame.font.init()
        font = pygame.font.Font(pygame.font.get_default_font(), 15)
        blit_text(self.window, text, (150, 0), font)
        pygame.display.update()

    def handle_key(self, event_key):
        if event_key == pygame.K_a:
            self.stop()
        elif chr(event_key) in ['&', 'q']:
            self.update_game(1)
        elif chr(event_key) in ['é', 'w']:
            self.update_game(2)
        elif chr(event_key) in ['"', 'e']:
            self.update_game(3)
        else:
            self.set_text(
                'Vous avez appuyé\n'
                'sur la touche {}\n'
                'appuyer sur la touche A\n'
                'pour quitter le jeu'.format(
                    chr(event_key).upper()
                )
            )

    def update_game(self, nb_match):
        self.game.player_removes(nb_match)
        if self.game.state.game_ended:
            self.show_victory_screen()

        self.set_image(nb_match=self.game.state.matches_left)
        self.set_text(
            "Vous avez retiré {} allumettes\n"
            "2 secondes l'ordinateur réfléchi"
            .format(self.game.state.matches_removed)
        )
        time.sleep(2)

        self.game.ia_removes()
        if self.game.state.game_ended:
            self.show_victory_screen()

        self.set_image(nb_match=self.game.state.matches_left)
        self.set_text(
            "L'ordinateur a retiré {} allumettes\n"
            "à vous de jouer"
            .format(self.game.state.matches_removed)
        )

    def reset_text(self):
        pygame.draw.rect(self.window, (0, 0, 0), [150, 0, 150, 300], 0)
        pygame.display.flip()

    def reset_image(self):
        pygame.draw.rect(self.window, (0, 0, 0), [0, 0, 150, 300], 0)
        pygame.display.flip()

    def show_victory_screen(self):
        self.reset_image()
        self.reset_text()
        text = '{} à gagné'.format(self.game.state.player)
        pygame.font.init()
        font = pygame.font.Font(pygame.font.get_default_font(), 30)
        blit_text(self.window, text, (100, 100), font)
        pygame.display.update()
        time.sleep(2)
        self.stop()
