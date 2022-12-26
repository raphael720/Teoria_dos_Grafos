from grafos import Graph
import matplotlib.pyplot as plt

def executa_modelo(model, n_inter: int, graph: Graph) -> list:
    array_minimo = [None] * n_inter

    for i in range(n_inter):
        model.fit(graph)
        array_minimo[i] = model.get_num_arestas()

    return min(array_minimo)

def executor(model, n_inter: int, n_exec: int, graph: Graph) -> list:
    cortes_minimos = list()

    for inter in range(10, n_inter+10, 10):
        lista_aux = []
        for _ in range(n_exec):
            lista_aux.append(executa_modelo(model, inter, graph))
        cortes_minimos.append(lista_aux)

    return cortes_minimos

def menor_corte(lista_cortes:list) -> int:
    menor_das_listas = [min(lista) for lista in lista_cortes]
    return min(menor_das_listas)


def calcule_prob(lista:list, corte_minimo:int, n_exec:int) -> list:
    probabilidades = list()
    for i in range(len(lista)):
        count = 0
        for item in lista[i]:
            if item == corte_minimo:
                count += 1
        probabilidades.append(count / n_exec)

    return probabilidades

def eixo_x_plot(n_inter:int):
    return [i for i in range(10, n_inter+10, 10)]

def salve_plots(path_out:str, eixo_x:list[int], probs:list) -> None:

    plt.plot(eixo_x, probs[0], label="Kager")
    plt.plot(eixo_x, probs[1], label="Naive")
    plt.legend(loc="upper right")
    plt.xlabel("Numero de Iterações")
    plt.ylabel("A probabilidade")

    plt.savefig(path_out, format="png")
    plt.clf()
    plt.cla()
    plt.close()

def escreve_arquivo(path:str, name_graph:str, corte_minimo:list[int]) -> None:
    with open(path, 'a') as file:
        file.write(f"{name_graph}:\n")
        file.write(f"Corte minimo Kager: {corte_minimo[0]}\n")
        file.write(f"Corte minimo Naive: {corte_minimo[1]}\n\n")

def ler_corte_arquivo(path: str) -> int:
    file = open(path, 'r')
    corte_minimo = int(file.readline())
    file.close()
    return corte_minimo
