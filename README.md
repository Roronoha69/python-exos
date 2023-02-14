# Exercices ludiques en python

Vous trouverez ici un ensemble d'exercices permettant de pratiquer python mais également découvrir quelques pans annexes de l'informatique en général.
Ces exercices sont issus d'un livre réalisé par Pascal Lafourcade et Malika More.

## Exercice : A ski
Décryptez le message stocké dans le fichier `files/a_ski.txt`.

Après avoir compris la technique de codage utilisé, saurez-vous implémenter un programme en python permettant de le déchiffrer?

> Ici vous allez découvrir la manipulation de fichiers, la conversion de str en int et quelques méthodes natives du langage python. 

## Exercice cryptarithme
Chaque lettre de l'opération représente un chiffre différent entre 0 et 9. Ecrivez un programme permettant de déterminer la valeur de chaque lettre pour que l'opération soit correcte, sachant que le premier chiffre de chaque nombre ne peut être un `0`.
> SEND + MORE = MONEY

> HUIT + HUIT = SEIZE

> UN + UN + ONZE = TREIZE

> CINQ + CINQ + VINGT = TRENTE

Saurez-vous implémenter un script python permettant de trouver les chiffres associés aux lettres?

Vous avez le fichier `files/cryptarithme.txt` à votre disposition si vous le souhaitez. 

> Cet exercice implique l'utilisation de boucles imbriquées.

## Exercice: Compter comme un shadok
> Pour compte les matins, les Shadoks ont un système de numérotation basé uniquement sur les syllabes suivantes : 
>GA, BU, ZO et MEU.
>Voici par exemple un nombre shadok : BU MEU ZO MEU GA GA

Saurez-vous programmer un convertisseur de nombre shadoks  en nombres décimaux pour découvrir quel est le nombre caché derrière le fichier `files/shadoks.txt` et ainsi découvrir la date de diffusion du premier épisode de cette série culte?

> Cet exercice implique la compréhension des bases en mathématiques.

## Exercice : Stéganographie
Le principe de stéganographie est d'utiliser une technique pour passer un message secret d'une manière dissimulée tout en restant lisible pour celui qui sait comment trouver. 
Au sein du fichier `stegano.png` se cache un texte secret. Chaque pixel a été très légèremet modifié.
Il faut extraire le bit de poids faible de chaque couleur de chaque pixel.
Puis d'en refaire des octets de 8 bits.

Exemple: 
```python
pixel = image[0][0]
r = red(pixel) % 2
g = green(pixel) % 2
b = blue(pixel) % 2
a = alpha(pixel) % 2 

pixel1 = image[1][0]
r1 = red(pixel1) % 2
g1 = green(pixel1) % 2
b1 = blue(pixel1) % 2
a1 = alpha(pixel1) % 2 

first_letter = chr(bin2dec(''.join((r,g,b,a,r1,g1,b1,a1))))
```
Vous aurez très probablement besoin d'utiliser PIL.
```shell
pip install pillow
```

## Exercice : Canaux cachés
La fonction fournie dans le fichier `files/canaux_caches.py` permets de vérifier si
un code saisi est contenu dans la variable essai

Saurez-vous écrire un programme qui permets à votre ordinateur à coup sûr en moins de 3 minutes de découvrir le code PIN saisi par l'utilisateur ? 
L'ordinateur ne doit pas utiliser la variable pin mais uniquement la méthode checkpin.
La fonction checkpin fournie ne dois pas être modifiée.