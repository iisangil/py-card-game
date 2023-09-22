import pygame

from enum import Enum
from .models import Deck, Pile, Player


class GameState(Enum):
  PLAYING = 0
  SNAPPING = 1
  ENDED = 2


class GameEngine:

  def __init__(self):
    self.deck = Deck()
    self.deck.shuffle()

    self.player1 = Player("Player 1", pygame.K_q, pygame.K_w)
    self.player2 = Player("Player 2", pygame.K_o, pygame.K_p)

    self.pile = Pile()
    self.state = GameState.PLAYING

    self.deal()
    self.currentPlayer = self.player1

    self.result = {}

  def deal(self):
    half = self.deck.length() // 2
    for _ in range(0, half):
      self.player1.draw(self.deck)
      self.player2.draw(self.deck)

  def switchPlayer(self):
    if self.currentPlayer == self.player1:
      self.currentPlayer = self.player2
    else:
      self.currentPlayer = self.player1

  def winRound(self, player):
    self.state = GameState.SNAPPING
    player.hand.extend(self.pile.popAll())

  def play(self, key):
    if not key or self.state == GameState.ENDED:
      return

    snapCaller = None
    nonSnapCaller = None
    isSnap = self.pile.isSnap()

    if key == self.player1.snapKey:
      snapCaller = self.player1
      nonSnapCaller = self.player2
    elif key == self.player2.snapKey:
      snapCaller = self.player2
      nonSnapCaller = self.player1

    if isSnap and snapCaller:
      self.winRound(snapCaller)
      self.result = {
          "winner": snapCaller,
          "isSnap": isSnap,
          "snapCaller": snapCaller
      }
      return

    if not isSnap and nonSnapCaller:
      self.winRound(nonSnapCaller)
      self.result = {
          "winner": nonSnapCaller,
          "isSnap": isSnap,
          "snapCaller": snapCaller
      }
      return

    if len(self.player1.hand) == 0:
      self.result = {
          "winner": self.player2,
      }
      self.state = GameState.ENDED
      return

    if len(self.player2.hand) == 0:
      self.result = {
          "winner": self.player1,
      }
      self.state = GameState.ENDED
      return

    if key == self.currentPlayer.flipKey:
      self.pile.add(self.currentPlayer.play())
      self.switchPlayer()
      return
