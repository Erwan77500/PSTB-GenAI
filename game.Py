import random

class Game:
    def get_user_item(self):
        """
        Demande à l'utilisateur de sélectionner un élément (pierre/papier/ciseaux).
        Continue à demander jusqu'à ce que l'utilisateur ait sélectionné un élément valide.
        Retourne l'élément sélectionné.
        """
        valid_items = ['pierre', 'papier', 'ciseaux']
        
        while True:
            user_choice = input("Choisissez votre élément (pierre/papier/ciseaux): ").lower().strip()
            
            if user_choice in valid_items:
                return user_choice
            else:
                print("Choix invalide. Veuillez choisir entre pierre, papier ou ciseaux.")
    
    def get_computer_item(self):
        """
        Sélectionne pierre/papier/ciseaux au hasard pour l'ordinateur.
        Retourne l'élément sélectionné.
        """
        items = ['pierre', 'papier', 'ciseaux']
        return random.choice(items)
    
    def get_game_result(self, user_item, computer_item):
        """
        Détermine le résultat du match.
        
        Paramètres:
        - user_item: l'objet choisi par l'utilisateur (pierre/papier/ciseaux)
        - computer_item: l'objet choisi par l'ordinateur (pierre/papier/ciseaux)
        
        Retourne: 'win', 'draw' ou 'loss'
        """
        # Match nul si les deux joueurs ont le même élément
        if user_item == computer_item:
            return 'draw'
        
        # Conditions de victoire pour l'utilisateur
        winning_conditions = {
            'pierre': 'ciseaux',    # pierre bat ciseaux
            'papier': 'pierre',     # papier bat pierre
            'ciseaux': 'papier'     # ciseaux bat papier
        }
        
        if winning_conditions[user_item] == computer_item:
            return 'win'
        else:
            return 'loss'
    
    def play(self):
        """
        Fonction principale du jeu appelée de l'extérieur de la classe.
        
        1. Récupère l'objet de l'utilisateur
        2. Obtient un objet aléatoire pour l'ordinateur
        3. Détermine les résultats du jeu
        4. Affiche le résultat
        5. Retourne le résultat sous forme de chaîne
        """
        # 1. Récupérer l'élément de l'utilisateur
        user_item = self.get_user_item()
        
        # 2. Obtenir un élément aléatoire pour l'ordinateur
        computer_item = self.get_computer_item()
        
        # 3. Déterminer le résultat du jeu
        result = self.get_game_result(user_item, computer_item)
        
        # 4. Afficher la sortie du jeu
        if result == 'win':
            print(f"Vous avez choisi {user_item}. L'ordinateur a sélectionné {computer_item}. Vous gagnez !")
        elif result == 'draw':
            print(f"Vous avez choisi {user_item}. L'ordinateur a sélectionné {computer_item}. Vous avez fait match nul !")
        else:  # result == 'loss'
            print(f"Vous avez choisi {user_item}. L'ordinateur a sélectionné {computer_item}. Vous perdez !")
        
        # 5. Retourner le résultat
        return result