from cryptography.fernet import Fernet

# Génération d'une clé symétrique (à faire une seule fois)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Chiffrement de données
text = "Données sensibles"
cipher_text = cipher_suite.encrypt(text.encode())
print(f"Texte chiffré: {cipher_text}")

# Déchiffrement des données
decrypted_text = cipher_suite.decrypt(cipher_text).decode()
print(f"Texte déchiffré: {decrypted_text}")
