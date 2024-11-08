import paramiko

def ssh_connect(host, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # Autorise les nouvelles clés SSH
    client.connect(hostname=host, username=username, password=password)
    return client

# Exemple d'utilisation
host = 'monserveur.local'  # Adresse IP ou nom de domaine du serveur
username = 'user'
password = 'password'
client = ssh_connect(host, username, password)

# Commande à exécuter sur le serveur (par exemple, surveiller l'utilisation CPU)
stdin, stdout, stderr = client.exec_command('top -b -n 1 | grep "Cpu(s)"')
cpu_usage = stdout.read().decode('utf-8')
print("Usage du CPU:", cpu_usage)

client.close()
