from collections import Counter
from bs4 import BeautifulSoup

#Etape 1
def compter_occurrences(texte):
    # Diviser le texte en mots
    mots = texte.split()

    # Utiliser Counter pour compter les occurrences de chaque mot
    occurrences = Counter(mots)

    # Trier les occurrences par le nombre d'occurrences (du plus élevé au plus bas)
    occurrences_triees = occurrences.most_common()

    return occurrences_triees

# Exemple d'utilisation
phraseprojet = "Le soleil brille dans un ciel bleu, et les oiseaux chantent joyeusement."
#résultat Etape 1
resultat = compter_occurrences(phraseprojet)


#Etape 2
def supprimer_mots_parasites(occurrences, mots_parasites):
    # Filtrer les occurrences pour exclure les mots parasites
    occurrences_filtrees = [(mot, occ) for mot, occ in occurrences if mot not in mots_parasites]

    return occurrences_filtrees

# Exemple d'utilisation
mots_parasites = ['je', 'à','le', 'la','les', 'un','une', 'de','des', 'tu','il', 'elle','on', 'nous','vous', 'ils','elles','et','Le']

#résultat etape 2
resultat_filtre = supprimer_mots_parasites(resultat, mots_parasites)
#print(resultat_filtre)

#Etape 3
def lire_mots_parasites_de_txt(nom_fichier):
    mots_parasites = []

    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier_txt:
            # Lire chaque ligne du fichier texte
            lignes = fichier_txt.readlines()
            # Ajouter chaque mot de la ligne à la liste des mots parasites
            for ligne in lignes:
                mots_parasites.extend(ligne.strip().split())
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du fichier texte : {e}")

    return mots_parasites

# Exemple d'utilisation
fichier_parasite_txt = 'parasite.txt'
mots_parasites_txt = lire_mots_parasites_de_txt(fichier_parasite_txt)
resultat_filtre_txt = supprimer_mots_parasites(resultat, mots_parasites_txt)

# Résultat Etape 3:
#print(resultat_filtre_txt)

#Etape 4

def supprimer_balises_html(html):
    # Utiliser BeautifulSoup pour analyser le HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Extraire le texte sans balises
    texte_sans_balises = soup.get_text()

    return texte_sans_balises


# Exemple d'utilisation
html_input = "<p>Ceci est un <b>exemple</b> de <a href='#'>texte</a> HTML.</p>"
resultatetape4 = supprimer_balises_html(html_input)

#résultat Etape 4
#print(resultatetape4)

#Etape 5
def extraire_valeurs_attribut(html, nom_balise, nom_attribut):
    # Utiliser BeautifulSoup pour analyser le HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Trouver toutes les balises avec le nom spécifié
    balises = soup.find_all(nom_balise)

    # Extraire les valeurs de l'attribut spécifié
    valeurs_attribut = [balise.get(nom_attribut) for balise in balises if balise.has_attr(nom_attribut)]

    return valeurs_attribut


# Exemple d'utilisation
html_input = """
<html>
  <body>
    <p class="exemple">Premier paragraphe</p>
    <p class="exemple">Deuxième paragraphe</p>
    <p>Paragraphe sans classe</p>
  </body>
</html>
"""

nom_balise = 'p'
nom_attribut = 'class'

#Résultat Etape 5
resultat = extraire_valeurs_attribut(html_input, nom_balise, nom_attribut)
#print(resultat)


print(resultat_filtre)
