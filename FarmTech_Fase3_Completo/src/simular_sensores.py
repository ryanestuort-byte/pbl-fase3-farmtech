"""
FarmTech Solutions - Fase 3
Simulação de dados de sensores agrícolas.

Este script gera o arquivo dados/dados_sensores_fase2.csv,
que pode ser importado no Oracle SQL Developer.
"""

import csv
import random
from datetime import datetime, timedelta

random.seed(42)

culturas = ["Soja", "Milho"]
inicio = datetime(2026, 5, 1, 8, 0, 0)

with open("../dados/dados_sensores_fase2.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo, delimiter=";")
    escritor.writerow([
        "id", "data_hora", "cultura", "umidade", "fosforo_p",
        "potassio_k", "ph", "temperatura", "status_irrigacao"
    ])

    for i in range(1, 81):
        cultura = random.choice(culturas)
        umidade = round(random.uniform(35, 80), 2)
        fosforo_p = random.randint(18, 60)
        potassio_k = random.randint(20, 75)
        ph = round(random.uniform(5.2, 7.2), 2)
        temperatura = round(random.uniform(20, 34), 2)

        status_irrigacao = "Ligada" if umidade < 50 or temperatura > 30 else "Desligada"
        data_hora = inicio + timedelta(hours=i)

        escritor.writerow([
            i, data_hora.strftime("%Y-%m-%d %H:%M:%S"), cultura,
            umidade, fosforo_p, potassio_k, ph, temperatura, status_irrigacao
        ])

print("Arquivo CSV gerado com sucesso!")
