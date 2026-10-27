import pandas as pd

# 1. Importer le fichier CSV
df = pd.read_csv(r"C:\Users\aymen\Downloads\qualite_industrielle.csv")

print("Fichier importé avec succès !")


# 2. Explorer la structure et les données
print("\n--- Structure du fichier ---")
print(df.info())

print("\n--- Les 5 premières lignes ---")
print(df.head())

print("\n--- Dimensions du fichier ---")
print("Nombre de lignes :", df.shape[0])
print("Nombre de colonnes :", df.shape[1])

print("\n--- Statistiques descriptives ---")
print(df.describe())


# 3. Vérifier les valeurs manquantes et les doublons
print("\n--- Valeurs manquantes ---")
print(df.isnull().sum())

print("\n--- Nombre de lignes en double ---")
print(df.duplicated().sum())


# 4. Identifier les principales variables liées à la qualité
variables_qualite = [
    "Produit",
    "Ligne_Production",
    "Nb_Defauts",
    "Taux_Defauts_pct",
    "Dimension_mm",
    "Poids_g",
    "Temperature_C",
    "Nb_Non_Conformites",
    "Temps_Controle_min",
    "Cout_Non_Qualite_DH",
    "Resultat"
]

print("\n--- Variables liées à la qualité ---")
print(df[variables_qualite].head())


# 5. Nettoyer les données si nécessaire
df_nettoye = df.dropna().drop_duplicates().copy()

print("\n--- Vérification après nettoyage ---")
print("Lignes avant nettoyage :", len(df))
print("Lignes après nettoyage :", len(df_nettoye))


# 6. Sauvegarder le fichier nettoyé
df_nettoye.to_csv(
    "qualite_industrielle_nettoyee.csv",
    index=False
)

print("\nFichier nettoyé sauvegardé avec succès !")