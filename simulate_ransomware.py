# simulate_ransomware.py
# Simulação segura:
# - copia arquivos do ./sandbox para ./backup
# - sobrescreve os originais com uma mensagem clara "ENCRYPTED (SIMULATION)"
# - permite restaurar a partir do backup

import os
import shutil
import argparse
from datetime import datetime

SANDBOX = "sandbox"
BACKUP = "backup"
RANSOM_NOTE = "ransom_note.txt"

os.makedirs(SANDBOX, exist_ok=True)
os.makedirs(BACKUP, exist_ok=True)

def create_ransom_note():
    now = datetime.utcnow().isoformat() + "Z"
    note = (
        "=== NOTA DE RESGATE (SIMULAÇÃO) ===\n\n"
        "Seus arquivos foram 'criptografados' (simulação).\n"
        "Isto é um exercício educativo. Para restaurar, execute o script de restauração.\n\n"
        f"Timestamp: {now}\n"
        "Esta nota NÃO representa código malicioso real.\n"
    )
    with open(RANSOM_NOTE, "w", encoding="utf-8") as f:
        f.write(note)
    print(f"Nota de resgate simulada gerada em ./{RANSOM_NOTE}")

def simulate_encrypt():
    files = [f for f in os.listdir(SANDBOX) if os.path.isfile(os.path.join(SANDBOX, f))]
    if not files:
        print("Nenhum arquivo no sandbox. Execute create_test_files.py primeiro.")
        return
    for fname in files:
        src = os.path.join(SANDBOX, fname)
        dst_backup = os.path.join(BACKUP, fname)
        shutil.copy2(src, dst_backup)  # backup seguro
        # sobrescreve o arquivo original com uma mensagem não-destrutiva
        with open(src, "w", encoding="utf-8") as f:
            f.write("=== ARQUIVO ENCRIPTADO (SIMULAÇÃO) ===\n")
            f.write("Conteúdo removido propositalmente para a simulação. Backup disponível em ./backup\n")
    create_ransom_note()
    print("Simulação de 'criptografia' concluída. Backups em ./backup")

def restore():
    files = [f for f in os.listdir(BACKUP) if os.path.isfile(os.path.join(BACKUP, f))]
    if not files:
        print("Nenhum backup encontrado em ./backup")
        return
    for fname in files:
        src = os.path.join(BACKUP, fname)
        dst = os.path.join(SANDBOX, fname)
        shutil.copy2(src, dst)
    print("Restauração concluída a partir de ./backup")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulação segura de ransomware")
    parser.add_argument("action", choices=["encrypt", "restore", "note"], help="Ação: encrypt/restore/note")
    args = parser.parse_args()
    if args.action == "encrypt":
        simulate_encrypt()
    elif args.action == "restore":
        restore()
    elif args.action == "note":
        create_ransom_note()
