import random
from math import floor
from grafos import Graph

class Kager:
    def __init__(self) -> None:
      self.super_vert = dict()
      self.lista_vert_aux = list()
      self.lista_aresta_aux = list()

    def fit(self, grafo: Graph):
        self.lista_vert_aux = grafo.vertices.copy()
        self.lista_aresta_aux = grafo.arestas.copy()

        fired_vert1, fired_vert2 = 0, 0

        while len(self.lista_vert_aux) > 2:
            super_vertex = max(self.lista_vert_aux) + 1

            # pegano uma aresta random e colocando os vertices no novo super vertice
            aresta_random = random.randrange(len(self.lista_aresta_aux))
            current_edge = self.lista_aresta_aux.pop(aresta_random)

            fired_vert1, fired_vert2 = current_edge[0], current_edge[1]
            #print(f"Os vertices que vao ser retirados da lista: {fired_vert1} e {fired_vert2}")

            # adicioando o super vertice na lista de vertices
            self.lista_vert_aux.append(super_vertex)

            self.super_vert[f"{super_vertex}"] = []
            self.super_vert[f"{super_vertex}"].append(current_edge[0])
            self.super_vert[f"{super_vertex}"].append(current_edge[1])
            #print(f"Nosso current super vertice: {super_vertex}")

            # removendo os vertices da lista de vertices
            self.lista_vert_aux.pop(self.lista_vert_aux.index(fired_vert1))
            self.lista_vert_aux.pop(self.lista_vert_aux.index(fired_vert2))

            self.atualizacao_arestas(fired_vert1, fired_vert2, super_vertex)

            self.atuaizando_super_vertices(fired_vert1, fired_vert2, super_vertex)
            
            #print(f"\Current edges: {self.lista_aresta_aux}\n")
            #print(f"Lista Current de super vertices: {super_vert}")

    def atuaizando_super_vertices(self, fired_vert1, fired_vert2, super_vertex):
        #atualizando a lista de super vertices
        if str(fired_vert1) in self.super_vert.keys():
            aux_lista_verte_1 = self.super_vert[f"{fired_vert1}"]
            aux_lista_verte_2 = self.super_vert[f"{super_vertex}"]
            self.super_vert[f"{super_vertex}"] = aux_lista_verte_1 + aux_lista_verte_2
            del self.super_vert[f"{fired_vert1}"]

        if str(fired_vert2) in self.super_vert.keys():
            aux_lista_verte_1 = self.super_vert[f"{fired_vert2}"]
            aux_lista_verte_2 = self.super_vert[f"{super_vertex}"]
            self.super_vert[f"{super_vertex}"] = aux_lista_verte_1 + aux_lista_verte_2
            del self.super_vert[f"{fired_vert2}"]

    def atualizacao_arestas(self, fired_vert1, fired_vert2, super_vertex):
        # atualizando as arestas
        for i in range(len(self.lista_aresta_aux)):
            if self.lista_aresta_aux[i][0] == fired_vert1 or self.lista_aresta_aux[i][0] == fired_vert2:
                vert_aux = self.lista_aresta_aux[i][1]
                self.lista_aresta_aux[i] = (super_vertex, vert_aux)

            elif self.lista_aresta_aux[i][1] == fired_vert1 or self.lista_aresta_aux[i][1] == fired_vert2:
                vert_aux = self.lista_aresta_aux[i][0]
                self.lista_aresta_aux[i] = (vert_aux, super_vertex)

        # atualizando a lista de arestas
        new_lista = []
        for edge in self.lista_aresta_aux:
            if edge == (fired_vert1, fired_vert2) or edge == (fired_vert2, fired_vert1):
                continue
            elif edge == (super_vertex, fired_vert1) or edge == (fired_vert1, super_vertex):
                continue
            elif edge == (super_vertex, fired_vert2) or edge == (fired_vert2, super_vertex):
                continue
            else:
                new_lista.append(edge)

        self.lista_aresta_aux = new_lista

    def get_arestas(self):
        return self.lista_aresta_aux

    def get_num_arestas(self):
        return floor(len(self.lista_aresta_aux) / 2)

    def get_vertices(self):
        return self.lista_vert_aux
