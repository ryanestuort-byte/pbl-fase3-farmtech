[README.md](https://github.com/user-attachments/files/28025046/README.md)
# FarmTech Solutions - Fase 3

Projeto desenvolvido para o PBL da Fase 3 do curso de Inteligência Artificial da FIAP.

## Objetivo

Importar os dados coletados pelos sensores agrícolas da Fase 2 para um banco de dados relacional Oracle, realizar consultas SQL, documentar o processo e apresentar o funcionamento em vídeo.

## Estrutura do repositório

```text
FarmTech_Fase3_Completo/
├── dados/
│   ├── dados_sensores_fase2.csv
│   └── produtos_agricolas.csv
├── sql/
│   └── consultas_farmtech.sql
├── src/
│   └── simular_sensores.py
├── dashboard/
│   ├── app.py
│   └── requirements.txt
├── notebooks/
│   └── SeuNome_RMxxxx_fase3_cap1.ipynb
├── docs/
│   └── prints/
└── video/
    └── roteiro_video.md
```

## Dados utilizados

O arquivo `dados/dados_sensores_fase2.csv` contém dados simulados de sensores agrícolas:

- Umidade do solo;
- Fósforo;
- Potássio;
- pH;
- Temperatura;
- Status da irrigação;
- Cultura monitorada.

## Passos realizados no Oracle SQL Developer

1. Abrir o Oracle SQL Developer.
2. Criar uma nova conexão com os dados da FIAP:
   - Usuário: RM do aluno;
   - Senha: data de nascimento no formato DDMMYY;
   - Host: oracle.fiap.com.br;
   - Porta: 1521;
   - SID: ORCL.
3. Clicar em `Tabelas (Filtrado)`.
4. Selecionar `Importa Dados`.
5. Escolher o arquivo `dados_sensores_fase2.csv`.
6. Definir o nome da tabela como `FARMTECH_SENSORES`.
7. Conferir as colunas.
8. Finalizar a importação.
9. Executar as consultas SQL do arquivo `sql/consultas_farmtech.sql`.

## Consultas SQL utilizadas

Consulta geral:

```sql
SELECT * FROM FARMTECH_SENSORES;
```

Consulta de irrigação ligada:

```sql
SELECT ID, DATA_HORA, CULTURA, UMIDADE, TEMPERATURA, STATUS_IRRIGACAO
FROM FARMTECH_SENSORES
WHERE STATUS_IRRIGACAO = 'Ligada';
```

Média dos sensores por cultura:

```sql
SELECT
    CULTURA,
    ROUND(AVG(UMIDADE), 2) AS MEDIA_UMIDADE,
    ROUND(AVG(FOSFORO_P), 2) AS MEDIA_FOSFORO,
    ROUND(AVG(POTASSIO_K), 2) AS MEDIA_POTASSIO,
    ROUND(AVG(PH), 2) AS MEDIA_PH,
    ROUND(AVG(TEMPERATURA), 2) AS MEDIA_TEMPERATURA
FROM FARMTECH_SENSORES
GROUP BY CULTURA;
```

## Prints obrigatórios

Coloque na pasta `docs/prints/` os prints das seguintes etapas:

1. Conexão criada no Oracle SQL Developer;
2. Importação do arquivo CSV;
3. Tabela criada/importada;
4. Consulta `SELECT * FROM FARMTECH_SENSORES`;
5. Consultas adicionais funcionando.

## Como executar o script Python

Entre na pasta `src` e execute:

```bash
python simular_sensores.py
```

## Como executar a dashboard

Entre na pasta `dashboard` e instale as dependências:

```bash
pip install -r requirements.txt
```

Depois execute:

```bash
streamlit run app.py
```

## Programa Ir Além - Dashboard

A dashboard apresenta:

- Visualização de umidade;
- Níveis de fósforo, potássio e pH;
- Status da irrigação;
- Sugestão de irrigação baseada nos dados.

## Programa Ir Além - Machine Learning

O notebook `notebooks/SeuNome_RMxxxx_fase3_cap1.ipynb` contém:

- Análise exploratória;
- Pelo menos 5 gráficos;
- Perfil ideal de solo/clima para 3 culturas;
- 5 modelos preditivos;
- Comparação de performance.

## Vídeo demonstrativo

O vídeo deve ter até 5 minutos e mostrar:

1. Organização do repositório;
2. Arquivo CSV da Fase 2;
3. Importação no Oracle SQL Developer;
4. Consultas SQL funcionando;
5. Dashboard ou notebook, caso utilize o Ir Além.

## Integrantes

- Nome: RYAN PABLO CORREA DE PAULA E MATHEUS KAUÃ DA SILVA
- RM: RM570587 E RM569379
