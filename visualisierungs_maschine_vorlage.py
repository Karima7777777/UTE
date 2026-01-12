# ----------------------------------------------------------------
# AI-Cooking-Rezept 8: Die Visualisierungs-Maschine
# Schritt 1: Werkzeuge importieren und Daten laden
# ----------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

# WICHTIG: Stelle sicher, dass die CSV-Datei im selben Ordner ist!
# Lade die Daten in einen DataFrame
df = pd.read_csv('superstore_daten.csv', encoding='latin-1')

# Wirf einen ersten Blick auf die Daten, um sie zu verstehen
print("Die ersten 5 Zeilen der Superstore-Daten:")
print(df.head())
print("\nÜbersicht der Datentypen und fehlenden Werte:")
df.info()


# HIER BEGINNT DEIN CODE FÜR DIE NÄCHSTEN SCHRITTE
# (Der Rest der Datei ist leer, damit Du hier arbeitest)