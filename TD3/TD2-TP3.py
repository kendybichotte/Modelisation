import numpy as np

# MODELISATION DES DEUX SYSTEMES
# --- Système météo ---
etats_meteo = ["Soleil", "Pluie", "Nuage"]

# Matrice de transition météo
P_meteo = np.array([
    [0.7, 0.2, 0.1],   # Soleil : Soleil, Pluie, Nuage
    [0.4, 0.4, 0.2],   # Pluie  : Soleil, Pluie, Nuage
    [0.3, 0.3, 0.4]    # Nuage  : Soleil, Pluie, Nuage
])

# --- Système économie ---
etats_eco = ["Hausse", "Stable", "Baisse"]

# Matrice de transition économie
P_eco = np.array([
    [0.6, 0.3, 0.1],   # Hausse : Hausse, Stable, Baisse
    [0.2, 0.6, 0.2],   # Stable : Hausse, Stable, Baisse
    [0.1, 0.3, 0.6]    # Baisse : Hausse, Stable, Baisse
])


# FONCTIONS GENERIQUES
def simuler(P, X0, n):
    X = X0.copy()
    for _ in range(n):
        X = X @ P
    return X

def stationnaire(P):
    w, v = np.linalg.eig(P.T)
    i = np.argmin(np.abs(w - 1))
    T = v[:, i].real
    return T / T.sum()

def afficher(systeme, etats, Xn, T):
    print(f"\n=== {systeme} ===")
    print("États :", etats)
    print("Après 50 jours :", Xn.round(4))
    print("Stationnaire   :", T.round(4))
    print("Différence     :", (Xn - T).round(6))


# SIMULATION + DISTRIBUTION STATIONNAIRE
# Météo
X0_meteo = np.array([1, 0, 0])  # Soleil au jour 0
Xn_meteo = simuler(P_meteo, X0_meteo, 50)
T_meteo = stationnaire(P_meteo)

# Économie
X0_eco = np.array([0.5, 0.3, 0.2])  # Distribution initiale
Xn_eco = simuler(P_eco, X0_eco, 50)
T_eco = stationnaire(P_eco)

#COMPARAISON SIMULATION VS THEORIE
afficher("Météo", etats_meteo, Xn_meteo, T_meteo)
afficher("Économie", etats_eco, Xn_eco, T_eco)
print("\nConclusion : les distributions simulées convergent vers les distributions stationnaires.")
