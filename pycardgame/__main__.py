import pygame

from .display import renderGame
from .engine import GameEngine, GameState


def runGame():
  pygame.init()
  bounds = (1024, 768)
  window = pygame.display.set_mode(bounds)
  pygame.display.set_caption("PyCardGame")

  gameEngine = GameEngine()

  run = True
  while run:
    key = None
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

      if event.type == pygame.KEYDOWN:
        key = event.key

    gameEngine.play(key)
    renderGame(window, gameEngine)
    pygame.display.update()

    if gameEngine.state == GameState.SNAPPING:
      pygame.time.delay(3000)
      gameEngine.state = GameState.PLAYING
