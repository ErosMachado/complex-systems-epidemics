import matplotlib.pyplot as plt
import networkx as nx

# Criação do grafo
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
G.add_edges_from([
    (1, 2), (2, 3), (3, 4),  # Linha Turquesa
    (4, 7), (7, 8), (8, 9),  # Linha Rubi
    (4, 10),                 # Linha Jade
    (4, 11), (11, 12), (12, 13),  # Linha Coral
    (4, 5), (5, 6)           # Linha Cinza
])

# Conjuntos de arestas por linha
edges_turquoise = [(1, 2), (2, 3), (3, 4)]
edges_rubi = [(4, 7), (7, 8), (8, 9)]
edges_jade = [(4, 10)]
edges_coral = [(4, 11), (11, 12), (12, 13)]
edges_cinza = [(4, 5), (5, 6)]

# Layout dos nós
pos = nx.spring_layout(G, seed=42)  # Para consistência visual

# Cores do contorno dos nós
node_edge_colors = [
    'turquoise', 'turquoise', 'turquoise', 'black',
    'silver', 'silver', 'darkred', 'darkred', 'darkred',
    'limegreen', 'coral', 'coral', 'coral'
]

# Desenho do grafo com nós brancos e contornos coloridos
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color='white',          # Centro branco
    edgecolors=node_edge_colors, # Cor do contorno
    node_size=800,               # Tamanho dos nós
    linewidths=2,                # Largura do contorno
    font_size=10                 # Tamanho das etiquetas
)

# Desenho das arestas com cores personalizadas
nx.draw_networkx_edges(G, pos, edgelist=edges_turquoise, edge_color='turquoise', width=2)
nx.draw_networkx_edges(G, pos, edgelist=edges_rubi, edge_color='darkred', width=2)
nx.draw_networkx_edges(G, pos, edgelist=edges_jade, edge_color='limegreen', width=2)
nx.draw_networkx_edges(G, pos, edgelist=edges_coral, edge_color='coral', width=2)
nx.draw_networkx_edges(G, pos, edgelist=edges_cinza, edge_color='silver', width=2)

# Legenda das cidades
cities = [
    "1 - Mauá", "2 - Santo André", "3 - São Caetano", "4 - São Paulo",
    "5 - Osasco", "6 - Itapevi", "7 - Caieiras", "8 - Franco do Rocha",
    "9 - Jundiaí", "10 - Guarulhos", "11 - Ferraz de Vasconcelos",
    "12 - Suzano", "13 - Mogi das Cruzes"
]

city_handles = [
    plt.Line2D([0], [0],
               label=city, markersize=10) for city in cities
]

# Legenda das linhas de metrô
lines = {
    'turquoise': 'Turquesa',
    'silver': 'Cinza',
    'darkred': 'Rubi',
    'limegreen': 'Jade',
    'coral': 'Coral'
}



# Adicionar legendas
legend1 = plt.legend(handles=city_handles, loc="lower right", title="Cidades")
plt.gca().add_artist(legend1)  # Adicionar a legenda das cidades manualmente
plt.legend(handles=line_handles, loc="lower left", title="Linhas de Metrô")

# Ajustar e mostrar o grafo
plt.title("Grafo CPTM Resumido")
plt.tight_layout()
plt.show()
