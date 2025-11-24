# Projeto Educacional: Simulação Segura de Malware (Python)

Este projeto demonstra, **de forma 100% segura e ética**, o funcionamento básico de dois tipos de malware — *ransomware* e *keylogger* — utilizando apenas simulações controladas e sem qualquer comportamento malicioso real.

## Estrutura do Projeto

```
malware-simulado-full/
├─ README.md
├─ create_test_files.py
├─ simulate_ransomware.py
├─ simulate_keylogger.py
├─ sample_keystrokes.txt
├─ sandbox/
├─ backup/
├─ outbox/
├─ ransom_note.txt
└─ images/
   ├─ overview.png
   ├─ ransomware_flow.png
   └─ keylogger_flow.png
```

## Uso rápido

1. `python create_test_files.py`
2. `python simulate_ransomware.py encrypt`
3. `python simulate_ransomware.py restore`
4. `python simulate_keylogger.py generate`
5. `python simulate_keylogger.py send`

## Segurança
- Execute apenas em VMs/sandbox.
- Código é intencionalmente não-destrutivo.

## Imagens
As imagens no diretório `images/` são ilustrações em estilo blueprint para apresentação.
