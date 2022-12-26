
import os
from searches import ShortestPathGraph

def calcula_excentrencidade(graph):
    short_path = ShortestPathGraph()

    excentri = [None] * graph.num_vertice
    distancias = [None] * graph.num_vertice

    for vert in range(graph.num_vertice):
        distancia = short_path.start(graph, vert)
        excentri[vert] = max(distancia)
        distancias[vert] = distancia

    return excentri, distancias

# É a minima excentricidade de um vértice
def calcula_raio(excentrencidade, nome_grafo):
    raio = min(excentrencidade)
    
    print(f"O Raio do {nome_grafo} é: {raio}")
    return raio

# É a maxima excentricidade de um vértice
def calcula_diametro(excentrencidade, nome_grafo):
    diametro = max(excentrencidade)

    print(f"O Diâmetro do {nome_grafo} é: {diametro}")
    return diametro

def calcular_distancia_media(dist, nome_grafo, n):
    sum_distances =  [sum(array) for array in dist] 
    distancia_media = sum(sum_distances) / (n * (n-1))

    print(f"A Distancia media do {nome_grafo} é: {distancia_media}")
    return distancia_media

def escreve_distancias(path, distan, raio, diametro, nome_grafo):
    new_path = os.path.join(path, f"{nome_grafo}.txt")
    with open(new_path, 'w') as arquivo:
        arquivo.write(f"{nome_grafo}:\n")
        arquivo.write(f"O Raio é: {raio}\n")
        arquivo.write(f"O Diâmetro é: {diametro}\n")
        arquivo.write(f"O Distancia media é: {distan}\n")