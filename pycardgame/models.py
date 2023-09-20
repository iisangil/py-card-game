import pygame
import random

from enum import Enum


class Suits(Enum):
  CLUB = 0
  SPADE = 1
  HEART = 2
  DIAMOND = 3


class Card:
  suit = None
  value = None
  image = None

  def __init__(self, suit, value):
    self.suit = suit
    self.value = value
    self.image = pygame.image.load(
        f"images/{self.suit.name}-{str(self.value)}.svg")


class Deck:
  cards = []

  def __init__(self):
    for suit in Suits:
      for value in range(1, 14):
        self.cards.append(Card(suit, value))

  def shuffle(self):
    random.shuffle(self.cards)

  def deal(self):
    return self.cards.pop()

  def length(self):
    return len(self.cards)


class Pile:
  cards = []

  def add(self, card):
    self.cards.append(card)

  def peek(self):
    if (len(self.cards) > 0):
      return self.cards[-1]

    return None

  def popAll(self):
    return self.cards

  def clear(self):
    self.cards = []


class Player:
  hand = []
  flipKey = None
  snapKey = None
  name = None

  def __init__(self, name, flipKey, snapKey):
    self.flipKey = flipKey
    self.snapKey = snapKey
    self.name = name

  def draw(self, deck):
    self.hand.append(deck.deal())

  def play(self):
    return self.hand.pop(0)
