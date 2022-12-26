#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 11:58:20 2022

@author: raphael720
"""
import os
import numpy as np

class LerGraph:
    def __init__(self):
        self._num_vertice = 0
        self._num_arestas = 0
        self._arestas = []
        self._nome = None

    def cria_matriz(self, arquivo: str):
        self.get_nome_graph(arquivo)

        file = open(arquivo, 'r')
        num_vertice = int(file.readline())

        self.set_num_vertices(num_vertice)
        num_arestas = 0

        matriz = np.zeros((num_vertice, num_vertice), dtype = int)
        for i in range(num_vertice):
            line = file.readline()
            line = line.split()
            for j in range(num_vertice):
                value_int = int(line[j])
                if j > i and value_int == 1:
                    num_arestas += 1
                matriz[i][j] = value_int

        self.set_num_arestas(num_arestas)
        file.close()
        return matriz

    def cria_filas(self, arquivo: str):
        self.get_nome_graph(arquivo)
        file = open(arquivo, 'r')
        num_vertice = int(file.readline())
        self.set_num_vertices(num_vertice)
        
        filas = []
        for i in range(num_vertice):
            line = file.readline()
            line = line.split()
            fila = []
            for j in range(num_vertice):
                value_int = int(line[j])
                if value_int == 1:
                    fila.append(j)
                    self._arestas.append((i, j))

            filas.append(fila)
        file.close()
        return filas
  
    def pega_vertices(self):
        lista_vertices = [vert for vert in range(self.get_num_vertices())]
        return lista_vertices

    def get_arestas(self):
        return self._arestas

    def get_nome_graph(self, nome_arquivo: str):
        if self._nome == None:
            head, tail = os.path.split(nome_arquivo)
            nome = tail
            self.set_name(nome)

    def get_num_vertices(self):
        return self._num_vertice
    
    def set_num_vertices(self, numVert):
        if self._num_vertice == 0:
            self._num_vertice = numVert

    def get_num_arestas(self):
        return self._num_arestas
    
    def set_num_arestas(self, numArestas):
        if self._num_arestas == 0:
            self._num_arestas = numArestas
            
    def get_name(self):
        return self._nome
    
    def set_name(self, nome):
        if self._nome == None:
            self._nome = nome
