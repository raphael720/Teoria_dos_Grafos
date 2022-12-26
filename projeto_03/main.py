import os
from grafos import Graph
from naive_random import Naive_Random
from kager import Kager
from funcoes_aux import *

if __name__ == "__main__":

    pasta_entrada = "in"

    pasta_out = 'out'

    pasta_minha_saida = "my_out"

    pasta_plots = "my_plots"

    if not os.path.isdir(pasta_minha_saida):
        os.mkdir(pasta_minha_saida)
    
    if not os.path.isdir(pasta_plots):
        os.mkdir(pasta_plots)

    arquivos_entrada = os.listdir(pasta_entrada)

    path_corte_out = os.path.join(pasta_minha_saida, "cortes_minimos.txt")

    N_inter = 100 # numero de interações
    N_exec = 200 # numero de execuções

    for arquivo in arquivos_entrada:

        path = os.path.join(pasta_entrada, arquivo)
        path_out = os.path.join(pasta_out, arquivo)

        grafo = Graph()
        grafo.fit(path)

        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- Resultados das iteraçẽs -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        
        print(f"Nome do grafo: {grafo.get_nome()}")

        heuristic_random = Kager()
        ingenuo = Naive_Random()

        lista_cortes_heuristic = executor(model=heuristic_random, n_inter=N_inter, n_exec=N_exec, graph=grafo)
        lista_cortes_ingenuo = executor(model=ingenuo, n_inter=N_inter, n_exec=N_exec, graph=grafo)

        corte_minimo = ler_corte_arquivo(path_out)
        corte_minimo_Kager = menor_corte(lista_cortes=lista_cortes_heuristic)
        corte_minimo_naive = menor_corte(lista_cortes=lista_cortes_ingenuo)

        print(f"O corte minimo é: {corte_minimo}")
        print(f"O corte minimo para o Kager é: {corte_minimo_Kager}")
        print(f"O corte minimo para o Naive é: {corte_minimo_naive}")
      
        prob_kager = calcule_prob(lista=lista_cortes_heuristic, corte_minimo=corte_minimo, n_exec=N_exec)
        prob_naive = calcule_prob(lista=lista_cortes_ingenuo, corte_minimo=corte_minimo, n_exec=N_exec)
        x = eixo_x_plot(n_inter=N_inter)

        #print(f"As probabilidades kager: {prob_kager}")
        #print(f"As probabilidades naive: {prob_naive}")

        escreve_arquivo(path=path_corte_out, name_graph=grafo.get_nome(), corte_minimo=[corte_minimo_Kager, corte_minimo_naive])

        full_path_plot = os.path.join(pasta_plots, f"{grafo.get_nome()}.png")

        salve_plots(path_out=full_path_plot, eixo_x=x, probs=[prob_kager, prob_naive])

        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
