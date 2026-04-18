import networkx as nx
import matplotlib.pyplot as plt

# Initialisation du graphe
metro = nx.Graph()

# Création des stations, liens et temps de trajet 

# Ligne Nord
ligne_nord = [
    ("Ouanaminthe", "Fort-Liberté", 15),
    ("Fort-Liberté", "Limonade", 12),
    ("Limonade", "Cap-Haïtien", 10),
    ("Cap-Haïtien", "Gonaïves", 45),
    ("Gonaïves", "Saint-Marc", 30),
    ("Saint-Marc", "Port-au-Prince", 40)
]

# Ligne Sud
ligne_sud = [
    ("Port-au-Prince", "Carrefour", 10),
    ("Carrefour", "Léogâne", 15),
    ("Léogâne", "Grand-Goâve", 10),
    ("Grand-Goâve", "Petit-Goâve", 8),
    ("Petit-Goâve", "Miragoâne", 12),
    ("Miragoâne", "Les Cayes", 40),
    ("Les Cayes", "Port-Salut", 15),
    ("Les Cayes", "Jérémie", 60)
]
# Ligne Est/Centre
ligne_est = [
    ("Belladère", "Hinche", 25),
    ("Hinche", "Mirebalais", 20),
    ("Mirebalais", "Port-au-Prince", 35),
    ("Port-au-Prince", "Pétion-Ville", 15),
    ("Pétion-Ville", "Kenscoff", 12),
    ("Pétion-Ville", "Jacmel", 50)
]

# Ajout des lignes au graphe
for ligne in [ligne_nord, ligne_sud, ligne_est]:
    metro.add_weighted_edges_from(ligne)

# Calcul de l'itinéraire optimal

def calculer_trajet(depart, arrivee):
    try:
        # Utilisation de l'algorithme de Dijkstra (poids = temps)
        temps_total = nx.shortest_path_length(metro, source=depart, target=arrivee, weight='weight')
        chemin = nx.shortest_path(metro, source=depart, target=arrivee, weight='weight')
        
        print(f" Trajet de '{depart}' à '{arrivee}' :")
        print(f" Temps estimé : {temps_total} minutes")
        print(f" Itinéraire : {' ➔ '.join(chemin)}")
    except nx.NetworkXNoPath:
        print("Aucun chemin trouvé.")

# Affichage des lignes
print(f"Nombre de stations créées : {metro.number_of_nodes()}")
calculer_trajet("Port-au-Prince", "Jacmel")

# Visualisation graphique
plt.figure(figsize=(12, 9))
pos = nx.spring_layout(metro)
nx.draw(metro, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=8)
labels = nx.get_edge_attributes(metro, 'weight')
nx.draw_networkx_edge_labels(metro, pos, edge_labels=labels)
plt.title("Plan du Réseau de Métro Simplifié")
plt.show()