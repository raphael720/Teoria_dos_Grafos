# -*- coding: utf-8 -*-

# Importações
import os
from grafos import Graph
from searches import BreadthFirstSearch, DepthFirstSeach
from escreverDistancias import *

def counting_sort(index, lista, max_vert): # complexidade O(n + k)
    k =  max_vert + 1 #len(lista)+1
    n = len(lista)
    c = [0] * k
    b = [None] * (n)
    
    for j in range(n):
        c[lista[j][index]] = c[lista[j][index]] + 1
        
    for i in range(1, k):
        c[i] = c[i] +  c[i-1]
        
    for j in range(n-1, -1, -1):
        b[c[lista[j][index]] -1] = lista[j]
        c[lista[j][index]] = c[lista[j][index]] -1
        
    return b

def escreve_arvore(lista, num_vert, file):
    # complexidade O(n + k), mas esse k vai ser assintoticamente igual ao n
    sorted_lista = counting_sort(1, lista, num_vert) # então complexidade O(n)
    sorted_lista = counting_sort(0, sorted_lista, num_vert) # então complexidade O(n)
    for v, w, cor in sorted_lista:
        linha = f"{v+1},{w+1},false," "'"+ cor +"'\n"
        file.write(linha)

def cria_arquivo_gdf(graph, path, tipo, resultado):
    if tipo == "depth":
        new_path = os.path.join(path, f"{graph.get_nome()}_dfs.gdf")
    elif tipo == "breadth":
        new_path = os.path.join(path, f"{graph.get_nome()}_bfs.gdf")
    
    with open(new_path, "w") as file:
        file.write("nodedef>name VARCHAR,label VARCHAR\n")
        graph.escreve_nodes(file)
        file.write("edgedef>node1 VARCHAR,node2 VARCHAR,directed BOOLEAN,color VARCHAR\n")
        escreve_arvore(resultado, graph.num_vertice, file)

if __name__ == "__main__":
    """# Organizando os arquivos"""
    
    # Nome da pasta onde vão ficar os arquivos .gdf
    pasta_out = "my_out"
    
    # Nome da pasta onde estão os arquivos de entrada
    pasta_in = "in"

    # Nome da pasta onde vão ficar os arquivos com as distancias
    pasta_out_txt = "my_out_txt"
    
    if not os.path.isdir(pasta_out):
        os.mkdir(pasta_out)

    if not os.path.isdir(pasta_out_txt):
        os.mkdir(pasta_out_txt)
    
    """# Criando os arquivos de cada Grafo"""
    
    arquivos = os.listdir(pasta_in)

    print("\nCriando os arquivos dos Grafos...")

    busca_largura = BreadthFirstSearch()
    busca_profundidade = DepthFirstSeach()
    
    for arquivo in arquivos:
        path = os.path.join(pasta_in, arquivo)
        
        grafo = Graph()
        grafo.fit(path)
        
        resultado_dfs = busca_profundidade.start(grafo)
        resultado_bfs = busca_largura.start(grafo)
        
        cria_arquivo_gdf(grafo, pasta_out, "depth", resultado_dfs)
        cria_arquivo_gdf(grafo, pasta_out, "breadth", resultado_bfs)
        
        excentrencidade, list_dist = calcula_excentrencidade(grafo)

        raio = calcula_raio(excentrencidade, grafo.get_nome())
        diametro = calcula_diametro(excentrencidade, grafo.get_nome())
        distancia_media = calcular_distancia_media(list_dist, grafo.get_nome(), grafo.num_vertice)

        escreve_distancias(pasta_out_txt, distancia_media, raio, diametro, grafo.get_nome())
        print()

    print("Arquivos criados!!!")

