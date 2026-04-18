import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import greedy_modularity_communities


G = nx.Graph()

# Création des utilisateurs U1 à U20
users = [f"U{i}" for i in range(1, 21)]
G.add_nodes_from(users)

#  Communauté A : U1 à U7 
comm_A = [
    ("U1","U2"),("U1","U3"),("U1","U4"),
    ("U2","U3"),("U2","U5"),
    ("U3","U6"),("U4","U5"),
    ("U5","U6"),("U6","U7"),("U4","U7")
]

#  Communauté B : U8 à U14 
comm_B = [
    ("U8","U9"),("U8","U10"),
    ("U9","U10"),("U9","U11"),
    ("U10","U12"),("U11","U12"),
    ("U11","U13"),("U12","U14"),
    ("U13","U14")
]

#  Communauté C : U15 à U20 
comm_C = [
    ("U15","U16"),("U15","U17"),
    ("U16","U17"),("U16","U18"),
    ("U17","U19"),("U18","U19"),
    ("U18","U20"),("U19","U20")
]

#  Ponts entre communautés 
bridges = [
    ("U3","U9"),
    ("U6","U12"),
    ("U11","U16")
]

# Ajout de toutes les relations
G.add_edges_from(comm_A + comm_B + comm_C + bridges)


# 2. Personnes les plus influentes (centralité de degré)
degrees = dict(G.degree())
max_degree = max(degrees.values())

influents = [u for u, d in degrees.items() if d == max_degree]

print("=== Utilisateurs les plus influents ===")
print(f"Degré maximal : {max_degree}")
print("Influents :", influents)


# 3. Calcul du degré de chaque utilisateur
print("\n=== Degré de chaque utilisateur ===")
for user, deg in degrees.items():
    print(f"{user} → degré = {deg}")


# 4. Détection des communautés (méthode greedy)
communities = greedy_modularity_communities(G)
print("\n=== Communautés détectées ===")
for i, comm in enumerate(communities, start=1):
    print(f"Communauté {i} :", sorted(list(comm)))

# 5. Visualisation du graphe
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G, seed=42)

nx.draw(
    G, pos,
    with_labels=True,
    node_color="blue",
    node_size=600,
    font_size=9,
    edge_color="black"
)

plt.title("TD1 — Réseau social intelligent")
plt.show()
