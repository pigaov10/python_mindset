 # -*- coding: utf-8 -*-

class Carta:
  def __init__(self, valor, naipe):
    self.valor = valor
    self.naipe = naipe
  
  def __repr__(self):
    return '<%s de %s>' % (self.valor, self.naipe)

zape = Carta('4', 'paus')
print zape

zape = Carta('5', 'copas')
print zape

class Baralho:
  naipes = 'copas ouros espadas paus'.split()
  valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
  
  
  def __init__(self):
    self.cartas = [Carta(v, n) for v in self.valores
                   			   for n in self.naipes]
b = Baralho()
print b.cartas
