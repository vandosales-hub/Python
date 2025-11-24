# create_test_files.py
# Gera arquivos de teste dentro de ./sandbox
import os

SANDBOX = "sandbox"
os.makedirs(SANDBOX, exist_ok=True)

contents = [
    ("documento1.txt", "Este é um arquivo de teste. Conteúdo original A.\n"),
    ("documento2.txt", "Arquivo de demonstração. Conteúdo original B.\n"),
    ("imagem_simulada.jpg", "CONTEÚDO_BINÁRIO_SIMULADO\n"),
]

for name, text in contents:
    path = os.path.join(SANDBOX, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

print(f"Arquivos de teste criados em ./{SANDBOX}")
