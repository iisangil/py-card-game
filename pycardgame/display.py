import pygame

from .engine import GameState


def renderGame(window, engine):
  cardBack = pygame.image.load("images/BACK.png").convert_alpha()
  cardBack = pygame.transform.scale(cardBack, (int(238 * 0.8), int(332 * 0.8)))

  window.fill((15, 0, 169))
  font = pygame.font.SysFont("comicsans", 60, True)

  window.blit(cardBack, (100, 200))
  window.blit(cardBack, (700, 200))

  text = font.render(f"{str(len(engine.player1.hand))} cards", True,
                     (255, 255, 255))
  window.blit(text, (100, 500))

  text = font.render(
      str(len(engine.player2.hand)) + " cards", True, (255, 255, 255))
  window.blit(text, (700, 500))

  topCard = engine.pile.peek()
  if topCard:
    window.blit(topCard.image, (400, 200))

  if engine.state == GameState.PLAYING:
    text = font.render(engine.currentPlayer.name + " to flip", True,
                       (255, 255, 255))
    window.blit(text, (20, 50))

  if engine.state == GameState.SNAPPING:
    result = engine.result
    if result["isSnap"]:
      message = f"Winning Snap! by {result['winner'].name}"
    else:
      message = f"False Snap! by {result['snapCaller'].name}. {result['winner'].name} wins!"
    text = font.render(message, True, (255, 255, 255))
    window.blit(text, (20, 50))

  if engine.state == GameState.ENDED:
    result = engine.result
    message = f"Game Over! {result['winner'].name} wins!"
    text = font.render(message, True, (255, 255, 255))
    window.blit(text, (20, 50))
