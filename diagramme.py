import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/aymen/Downloads/qualite_industrielle.csv")


# 1. Répartition des résultats
resultats = df["Resultat"].value_counts()

plt.figure(figsize=(7, 5))
plt.pie(
    resultats.values,
    labels=resultats.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Répartition des contrôles qualité")
plt.show()


# 2. Taux moyen de défauts par produit
taux_defauts = df.groupby("Produit")["Taux_Defauts_pct"].mean()

plt.figure(figsize=(8, 5))
plt.bar(taux_defauts.index, taux_defauts.values)
plt.title("Taux moyen de défauts par produit")
plt.xlabel("Produit")
plt.ylabel("Taux de défauts (%)")
plt.show()


# 3. Nombre de défauts et coût de non-qualité
plt.figure(figsize=(8, 5))
plt.scatter(
    df["Nb_Defauts"],
    df["Cout_Non_Qualite_DH"]
)
plt.title("Défauts et coût de non-qualité")
plt.xlabel("Nombre de défauts")
plt.ylabel("Coût de non-qualité (DH)")
plt.show()