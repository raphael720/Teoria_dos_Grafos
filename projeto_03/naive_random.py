# -*- coding: utf-8 -*-
import random
import numpy as np
from grafos import Graph

class Naive_Random:
  def __init__(self):
    self.lista_super_esquerda = []
    self.lista_super_direita = []
    self.aresta_corte = list()

  def fit(self, grafo: Graph):
    self.lista_super_esquerda = []
    self.lista_super_direita = []
    self.aresta_corte = list()

    lista_vert_aux = grafo.vertices
    valor_random = 0

    for vert in lista_vert_aux:
      valor_random = 2 * np.random.random() -1
      if valor_random > 0:
        self.lista_super_esquerda.append(vert)
        continue
      self.lista_super_direita.append(vert)

    # se a alguma das lista estiver vazia
    if len(self.lista_super_esquerda) == 0:
      vertice_random = random.randrange(len(self.lista_super_direita))
      self.lista_super_esquerda.append(self.lista_super_direita.pop(vertice_random))

    elif len(self.lista_super_direita) == 0:
      vertice_random = random.randrange(len(self.lista_super_esquerda))
      self.lista_super_direita.append(self.lista_super_esquerda.pop(vertice_random))

    for i in self.lista_super_esquerda:
      for j in self.lista_super_direita:
        if grafo.matriz[i][j] == 1:
          self.aresta_corte.append((i, j))
  
  def get_arestas(self):
    return self.aresta_corte

  def get_num_arestas(self):
    return len(self.aresta_corte)