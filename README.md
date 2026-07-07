# Chiffrement-machine-ENIGMA
Machine de chiffrement ENIGMA en python (OOP) 
--Enigma--

Machine Enigma en Python, inspiree du film "The Imitation Game". Ce projet reproduit le fonctionnement de la machine de chiffrement utilisee par l'Allemagne pendant la Seconde Guerre mondiale, celle-la meme qu'Alan Turing et son equipe ont travaille a casser a Bletchley Park.

--Fonctionnement--

La machine chiffre un message en faisant passer chaque lettre a travers plusieurs etapes de substitution :


Le Plugboard echange certaines paires de lettres
Les 3 rotors appliquent chacun une substitution, en tournant a chaque lettre (comme un compteur kilometrique)
Le reflecteur renvoie le signal en sens inverse a travers les rotors
Le Plugboard re-echange les lettres en sortie

Le resultat : une meme lettre tapee deux fois de suite donne deux lettres chiffrees differentes, grace a la rotation des rotors.

Propriete du reflecteur : rechiffrer un message chiffre avec la meme configuration redonne le message original.

--Structure du code--

Le projet est construit en programmation orientee objet avec trois classes qui interagissent :

Rotor — gere le cablage, la rotation et le chiffrement dans les deux sens (aller et retour). Sert aussi pour le reflecteur (un rotor qui ne tourne pas).
Plugboard — echange des paires de lettres avant et apres le passage dans les rotors.
Enigma — assemble les composants et orchestre le parcours complet de chaque lettre.

Les cablages utilises sont ceux des rotors historiques I, II, III et du reflecteur B.

Les espaces et la ponctuation sont preserves. Seules les lettres A-Z sont chiffrees.

--Contexte--

Projet personnel de cryptographie, construit dans le cadre d'un apprentissage progressif allant du chiffre de Cesar jusqu'a la machine Enigma. L'objectif etait de pratiquer la POO en Python a travers un cas concret avec plusieurs classes qui interagissent.
