#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from lerGrafos import LerGraph

class Graph:
    def __init__(self):
        self.matriz = np.array([])
        self.lista = np.array([])
        self.vertices = np.array([])
        self.arestas = np.array([])
        self.num_vertice = 0
        self.num_arestas = 0
        self._name = None

    def fit(self, path):
        ler_grafo = LerGraph()

        self.matriz = ler_grafo.cria_matriz(path)
        self.lista = ler_grafo.cria_filas(path)
        self.vertices = ler_grafo.pega_vertices()
        self.arestas = ler_grafo.get_arestas()

        self.num_vertice = ler_grafo.get_num_vertices()
        self.num_arestas = ler_grafo.get_num_arestas()
        self._name = ler_grafo.get_name()

    def escreve_nodes(self, file: str):
        for i in range(self.num_vertice):
            file.write(f"{i+1},{i+1}\n")
            
    def get_nome(self):
        return self._name