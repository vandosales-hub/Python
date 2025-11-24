# simulate_keylogger.py
# Simula um keylogger de forma ética: não captura teclas do sistema.
# Em vez disso, lê eventos de exemplo de sample_keystrokes.txt e grava em keylog_sim.txt
# "Envio" é simulado salvando em ./outbox/

import os
import time
from datetime import datetime
import argparse

SAMPLES = "sample_keystrokes.txt"
OUTBOX = "outbox"
KEYLOG = "keylog_sim.txt"
os.makedirs(OUTBOX, exist_ok=True)

def generate_keylog(from_sample=True):
    if not os.path.exists(SAMPLES):
        print(f"{SAMPLES} não encontrado. Crie um arquivo com eventos de exemplo.")
        return
    with open(SAMPLES, "r", encoding="utf-8") as s, open(KEYLOG, "a", encoding="utf-8") as k:
        for line in s:
            timestamp = datetime.utcnow().isoformat() + "Z"
            k.write(f"{timestamp} - {line.strip()}\n")
            # Sleep curto para simular tempo (mas sem comportamentos furtivos)
            time.sleep(0.05)
    print(f"Log de simulação gerado: ./{KEYLOG}")

def simulate_send():
    # Em vez de enviar por email, salvamos uma cópia no outbox (sem rede)
    if not os.path.exists(KEYLOG):
        print("Nenhum keylog gerado. Execute a geração primeiro.")
        return
    dest = os.path.join(OUTBOX, f"keylog_copy_{int(time.time())}.txt")
    with open(KEYLOG, "r", encoding="utf-8") as s, open(dest, "w", encoding="utf-8") as d:
        d.write(s.read())
    print(f"Arquivo 'enviado' salvo em {dest}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulação segura de keylogger (não intrusivo)")
    parser.add_argument("action", choices=["generate", "send"], help="generate/send")
    args = parser.parse_args()

    if args.action == "generate":
        generate_keylog()
    elif args.action == "send":
        simulate_send()
