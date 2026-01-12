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
# Auftrag 1: Erstelle ein Balkendiagramm für den Umsatz pro Kategorie.
# Dafür zuerst die Daten nach 'Category' gruppieren und die 'Sales' summieren.
# Dann die Funktion 'erstelle_diagramm' mit den richtigen Zutaten aufrufen.

# Auftrag 2: Erstelle ein Streudiagramm für den Zusammenhang von Umsatz und Profit.
# Dafür die Funktion 'erstelle_diagramm' mit dem originalen DataFrame 'df' und anderen Zutaten aufrufen.
def erstelle_diagramm(df, x, y, titel, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.bar(df[x], df[y], color='skyblue')
    plt.title(titel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
# Auftrag 1: Umsatz pro Kategorie
umsatz_pro_kategorie = df.groupby('Category')['Sales'].sum().reset_index()
erstelle_diagramm(
    umsatz_pro_kategorie,
    'Category',
    'Sales',
    'Umsatz pro Kategorie',
    'Kategorie',
    'Umsatz'
)
# Auftrag 2: Streudiagramm für Umsatz und Profit
def erstelle_streudiagramm(df, x, y, titel, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x], df[y], alpha=0.5, color='orange')
    plt.title(titel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.show()  
erstelle_streudiagramm(df, 'Sales', 'Profit', 'Zusammenhang von Umsatz und Profit', 'Umsatz', 'Profit') 

# Speichere beide Diagramme als PNG-Dateien
umsatz_pro_kategorie.to_csv('umsatz_pro_kategorie.csv', index=False)
plt.savefig('umsatz_pro_kategorie.png')
plt.close() 
plt.savefig('umsatz_profit_streudiagramm.png')
plt.close() 
# Hinweis: Die Diagramme werden direkt angezeigt und auch als PNG-Dateien gespeichert.