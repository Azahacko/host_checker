import json
import os
import hashlib
import getpass

class PasswordManager:
    def __init__(self, file_path="passwords.json"):
        self.file_path = file_path
        self.users = {}
        self.load_data()
    
    def load_data(self):
        """Charge les données utilisateur depuis le fichier s'il existe."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as file:
                    self.users = json.load(file)
            except json.JSONDecodeError:
                print("Erreur lors de la lecture du fichier. Création d'un nouveau fichier.")
                self.users = {}
    
    def save_data(self):
        """Sauvegarde les données utilisateur dans le fichier."""
        with open(self.file_path, 'w') as file:
            json.dump(self.users, file)
    
    def hash_password(self, password):
        """Hache le mot de passe pour le stockage sécurisé."""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register(self, username, password):
        """Enregistre un nouvel utilisateur."""
        if username in self.users:
            print("Ce nom d'utilisateur existe déjà.")
            return False
        
        hashed_password = self.hash_password(password)
        self.users[username] = hashed_password
        self.save_data()
        print(f"Utilisateur {username} enregistré avec succès.")
        return True
    
    def login(self, username, password):
        """Vérifie les identifiants de l'utilisateur."""
        if username not in self.users:
            print("Nom d'utilisateur inconnu.")
            return False
        
        hashed_password = self.hash_password(password)
        if self.users[username] == hashed_password:
            print(f"Bienvenue, {username}!")
            return True
        else:
            print("Mot de passe incorrect.")
            return False

def main():
    manager = PasswordManager()
    
    while True:
        print("\n=== Gestionnaire de mots de passe ===")
        print("1. S'inscrire")
        print("2. Se connecter")
        print("3. Quitter")
        
        choice = input("Choisissez une option (1-3): ")
        
        if choice == "1":
            username = input("Entrez votre nom d'utilisateur: ")
            password = getpass.getpass("Entrez votre mot de passe: ")
            manager.register(username, password)
        
        elif choice == "2":
            username = input("Entrez votre nom d'utilisateur: ")
            password = getpass.getpass("Entrez votre mot de passe: ")
            manager.login(username, password)
        
        elif choice == "3":
            print("Au revoir!")
            break
        
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()