from game import Game

def get_user_menu_choice():
    """
    Affiche un menu simple, obtient le choix de l'utilisateur avec validation
    et retourne le choix. Pas de boucle ici.
    
    Retourne: le choix de l'utilisateur ('1', '2', ou 'q')
    """
    print("\n=== PIERRE-PAPIER-CISEAUX ===")
    print("1. Jouer à une nouvelle partie")
    print("2. Afficher les scores")
    print("q. Quitter")
    
    choice = input("Votre choix: ").lower().strip()
    return choice

def print_results(results):
    """
    Affiche les résultats des jeux joués de manière conviviale
    et remercie l'utilisateur d'avoir joué.
    
    Paramètre:
    - results: dictionnaire contenant les résultats {win: x, loss: y, draw: z}
    """
    print("\n" + "="*40)
    print("      RÉSUMÉ DE VOS PARTIES")
    print("="*40)
    
    total_games = results['win'] + results['loss'] + results['draw']
    
    if total_games == 0:
        print("Aucune partie jouée.")
    else:
        print(f"Nombre total de parties: {total_games}")
        print(f"Victoires: {results['win']}")
        print(f"Défaites: {results['loss']}")
        print(f"Matchs nuls: {results['draw']}")
        
        if total_games > 0:
            win_percentage = (results['win'] / total_games) * 100
            print(f"Pourcentage de victoires: {win_percentage:.1f}%")
    
    print("\nMerci d'avoir joué au pierre-papier-ciseaux !")
    print("À bientôt ! 👋")

def main():
    """
    Fonction principale qui gère:
    1. L'affichage répété du menu jusqu'à ce que l'utilisateur quitte
    2. La création d'objets Game et l'enregistrement des résultats
    3. L'affichage des résultats finaux
    """
    # Dictionnaire pour stocker les résultats des parties
    results = {'win': 0, 'loss': 0, 'draw': 0}
    
    print("Bienvenue dans le jeu Pierre-Papier-Ciseaux !")
    
    while True:
        # 1. Affichage du menu et récupération du choix
        choice = get_user_menu_choice()
        
        # Validation du choix de l'utilisateur
        if choice == '1':
            # 2. L'utilisateur choisit de jouer
            print("\n--- NOUVELLE PARTIE ---")
            game = Game()  # Créer un nouvel objet Game
            game_result = game.play()  # Appeler la fonction play()
            
            # Enregistrer le résultat dans le dictionnaire
            results[game_result] += 1
            
        elif choice == '2':
            # Afficher les scores actuels
            print_results(results)
            
        elif choice == 'q':
            # 3. L'utilisateur choisit de quitter
            print_results(results)
            break
            
        else:
            print("Choix invalide. Veuillez choisir 1, 2 ou q.")

# Point d'entrée du programme
if __name__ == "__main__":
    main()