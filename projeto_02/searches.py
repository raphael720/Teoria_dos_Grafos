#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 12:00:15 2022

@author: raphael720
"""

class DepthFirstSeach:

    def start(self, graph):
        self._t = 0
        self.PE = [0] * graph.num_vertice #profundidade de entrada
        self.PS = [0] * graph.num_vertice #profundidade de saida
        self.PAI = [None] * graph.num_vertice #arvore de profundidade
        self.result = []
        # escolhendo o vertece raiz de busca
        raiz = 0
        self._dpf(graph, raiz)
        return self.result

    def _dpf(self, graph, v):
        self._t += 1
        self.PE[v] = self._t
        vizinhos_v = graph.lista[v]
        for w in vizinhos_v:
            if self.PE[w] == 0:
                self.PAI[w] = v
                if w > v:
                    self.result.append([v, w, '0,0,255'])
                else:
                    self.result.append([w, v, '0,0,255'])
                self._dpf(graph, w)
            elif self.PS[w] == 0 and w != self.PAI[v]:
                if w > v:
                    self.result.append([v, w, '255,0,0'])
                else:
                    self.result.append([w, v, '255,0,0'])
        self._t += 1
        self.PS[v] = self._t

class BreadthFirstSearch:

    def start(self, graph):
        self._t = 0
        self.fila_auxiliar = [] #fila auxiliar para a busca
        self.nivel = [0] * graph.num_vertice #o nivel de cada arvore
        self.L = [0] * graph.num_vertice #os indices dos vertices na busca
        self.PAI = [None] * graph.num_vertice #arvore de profundidade
        self.result = []
        
        raiz = 0
        self.fila_auxiliar.append(raiz)
    
        while len(self.fila_auxiliar) != 0:
            v = self.fila_auxiliar.pop(0) # pegando o primerio elemento da fila
            self._t += 1
            self.L[v] = self._t
            vizinhos_v = graph.lista[v]
            for w in vizinhos_v:
                if self.L[w] == 0:
                    self.PAI[w] = v
                    self.nivel[w] = self.nivel[v] + 1
                    self._t += 1
                    self.L[w] = self._t
                    self.fila_auxiliar.append(w)
                    if w > v:
                        self.result.append([v, w, '0,0,255'])
                    else:
                        self.result.append([w, v, '0,0,255'])
                        
                elif self.nivel[w] == self.nivel[v]:
                    if self.PAI[w] == self.PAI[v] and w in self.fila_auxiliar:
                        if w > v:
                            self.result.append([v, w, '255,0,0'])
                        else:
                            self.result.append([w, v, '255,0,0'])

                    elif self.PAI[w] != self.PAI[v] and w in self.fila_auxiliar:
                        if w > v:
                            self.result.append([v, w, '255,255,0'])
                        else:
                            self.result.append([w, v, '255,255,0'])
                     
                elif self.nivel[w] == self.nivel[v] + 1:
                    if w > v:
                        self.result.append([v, w, '0,255,0']) 
                    else:
                        self.result.append([w, v, '0,255,0']) 

        return self.result

class ShortestPathGraph:
    def start(self, graph, root=0):
        self._t = 0
        self.fila_auxiliar = [] #fila auxiliar para a busca
        self.nivel = [0] * graph.num_vertice #o nivel de cada arvore
        self.L = [0] * graph.num_vertice #os indices dos vertices na busca
        self.PAI = [None] * graph.num_vertice #arvore de profundidade
        
        raiz = root
        self.fila_auxiliar.append(raiz)
    
        while len(self.fila_auxiliar) != 0:
            v = self.fila_auxiliar.pop(0) # pegando o primerio elemento da fila
            self._t += 1
            self.L[v] = self._t
            vizinhos_v = graph.lista[v]
            for w in vizinhos_v:
                if self.L[w] == 0:
                    self.PAI[w] = v
                    self.nivel[w] = self.nivel[v] + 1
                    self._t += 1
                    self.L[w] = self._t
                    self.fila_auxiliar.append(w)

        return self.nivel

