import networkx as nx
import matplotlib.pyplot as plt
import random



G = nx.Graph()

stations = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"
]
G.add_nodes_from(stations)

edges = [
    ("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "F"), 
    ("F", "G"), ("G", "H"), ("H", "I"), ("I", "J"), ("J", "A"),
    ("B", "E"), ("E", "H"), ("H", "C"), ("C", "F"), ("F", "I")
]
G.add_edges_from(edges)

for u, v in G.edges():
    G[u][v]['weight'] = random.randint(1, 5)

if __name__ == "__main__":
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()

    degree_dict = dict(G.degree())


    print(f"Кількість вершин: {num_nodes}")
    print(f"Кількість ребер: {num_edges}\n")

    print("Ступені вершин:")
    for node, degree in degree_dict.items():
        print(f"Вузол {node}: {degree}")

    print("\nВаги ребер:")
    for u, v, weight in G.edges(data="weight"):
        print(f"Ребро ({u} - {v}): Вага {weight}")


    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)  
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000, font_size=12)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, font_color='red')
    plt.title("Модель транспортної мережі міста з вагами ребер")
    plt.show()