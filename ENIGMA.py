# Machine ENIGMA en python inspirée du film "The imitation game"




###################### On commence par les parties séparées ######################  

class Rotor:


    """Cette classe contient l'alphabet normal, les 3 rotors qui vont mélanger les lettres et les méthodes qui vont chiffrer et dechiffrer """
    

    def __init__(self, cablage) -> str:
        self.cablage = cablage
        self.position = 0

    def tourner(self):
        self.position = (self.position +1) % 26
    
    def chiffrer(self, lettre) -> str:
        position = alphabet.find(lettre)
        nouvelle_position = (position + self.position) %26 
        nouvelle_lettre = self.cablage[nouvelle_position]
        return nouvelle_lettre

    def chiffrer_inverse(self, lettre) -> str:
        position = self.cablage.find(lettre)
        ancienne_position = (position - self.position) %26 
        ancienne_lettre = alphabet[ancienne_position]
        return ancienne_lettre

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    




class Plugboard:

    """ce tableau échange la lettre tapée avec une autre via des paires"""


    def __init__(self, paires):
        self.paires = paires
    
    def echanger(self,lettre):
        for paire in self.paires:
            if lettre == paire[0]:
                return paire[1]
            elif lettre == paire[1]:
                return paire[0]
        return lettre
    
paires = [("A", "M"), ("G", "T"), ("E", "K")]




###################### On assemble chaque partie dans la machine ######################

class Enigma:

    """Cette classe assemble tous les composants pour faire la machine """


    def __init__(self, rotorI, rotorII, rotorIII, reflecteur, plugboard):
        self.rotorI= rotorI
        self.rotorII = rotorII
        self.rotorIII= rotorIII
        self.reflecteur = reflecteur
        self.plugboard = plugboard
    
    def chiffrer_lettre(self, lettre) -> str :

        if lettre not in alphabet:
            return lettre
        
        else :
            self.rotorIII.tourner()

            if self.rotorIII.position == 0:
                self.rotorII.tourner()

            lettre = self.plugboard.echanger(lettre)

            lettre = self.rotorIII.chiffrer(lettre)
            lettre = self.rotorII.chiffrer(lettre)
            lettre = self.rotorI.chiffrer(lettre)

            lettre= self.reflecteur.chiffrer(lettre)

            lettre = self.rotorI.chiffrer_inverse(lettre)
            lettre = self.rotorII.chiffrer_inverse(lettre)
            lettre = self.rotorIII.chiffrer_inverse(lettre)

            lettre = self.plugboard.echanger(lettre)

            return lettre 
    
    def chiffrer_message(self,message) -> str :

        resultat = ""
        for lettres in message:
            resultat = resultat + self.chiffrer_lettre(lettres)
        return resultat

rotorI = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
rotorII = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE")
rotorIII = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO")
plugboard = Plugboard(paires)
reflecteur = Rotor("YRUHQSLDPXNGOKMIEBFZCWVJAT")  
enigma = Enigma(rotorI, rotorII, rotorIII, reflecteur, plugboard)




###################### Le programme principal ######################

print ("Veuillez écrire le message a chiffrer : ")
message_clair = input()
message_chiffre = enigma.chiffrer_message(message_clair.upper())
print(f"Le message chiffré est : {message_chiffre}")



       


        


