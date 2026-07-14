# Ciphers in Python

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-informational)

Implementações próprias de cifras clássicas e modernas em Python, com uma interface web em Flask para cifrar um texto e ver o resultado da versão simétrica (AES adaptado para texto) e assimétrica (RSA) lado a lado.

> ⚠️ **Uso educacional.** As implementações de AES e RSA aqui são feitas do zero para estudo do funcionamento dos algoritmos — não foram auditadas e não devem ser usadas para proteger dados reais. Para produção, use bibliotecas de criptografia estabelecidas (ex.: `cryptography`, `PyNaCl`).

## Como funciona

### Cifra AES baseada em texto

Adaptação do AES tradicional (que opera sobre bytes) para operar diretamente sobre um estado de **16 letras**, trocando a operação `SubBytes` por `SubBigrams`. Algoritmo baseado na implementação em C# de [n1k0m0](https://github.com/n1k0m0/AES-and-Text-Based-AES).

```
AES original (estado de 16 bytes)          Esta implementação (estado de 16 letras)
────────────────────────────────           ─────────────────────────────────────────
plaintext                                   plaintext
   ↓                                           ↓
AddRoundKey (Key Expansion inicial)         AddRoundKey (Key Expansion inicial)
   ↓                                           ↓
SubBytes      ┐                             SubBigrams    ┐
   ↓          │                                ↓          │
ShiftRows     │                             ShiftRows     │
   ↓          │ 9, 11 ou 13 rounds             ↓          │ 9 rounds
MixColumns    │                             MixColumns    │
   ↓          │                                ↓          │
AddRoundKey   ┘                             AddRoundKey   ┘
   ↓                                           ↓
SubBytes      ┐                             SubBigrams    ┐
   ↓          │ round final                    ↓          │ round final
ShiftRows     │ (sem MixColumns)            ShiftRows     │ (sem MixColumns)
   ↓          │                                ↓          │
AddRoundKey   ┘                             AddRoundKey   ┘
   ↓                                           ↓
CipherText                                  CipherText
```

### Cifra assimétrica (RSA)

Implementação didática do RSA: geração de `n`, `phi(n)`, escolha do expoente público `e` e cálculo da chave privada `d` via inverso modular, usados para cifrar/decifrar a mensagem convertida em blocos ASCII/binário.

## Como usar

1. Criar e ativar um ambiente virtual, depois instalar as dependências:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Rodar o servidor em modo desenvolvimento:

   ```bash
   flask --app src/app.py --debug run
   # ou
   python3 -m flask --app ./src/app.py --debug run
   ```

3. Acessar `http://localhost:5000`, digitar um texto (apenas letras) e ver o resultado cifrado em AES-baseado-em-texto e em RSA.

## Testes

```bash
python3 -m src.ciphers.tests
```
