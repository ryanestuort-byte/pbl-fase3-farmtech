# Roteiro para vídeo demonstrativo - até 5 minutos

Olá, meu nome é [SEU NOME], RM [SEU RM], e este é o projeto FarmTech Solutions da Fase 3.

Neste projeto, o objetivo foi utilizar os dados coletados por sensores agrícolas da Fase 2 e importar essas informações para um banco de dados Oracle.

Primeiro, vou mostrar a organização do repositório. Na pasta dados, temos o arquivo dados_sensores_fase2.csv, que contém informações como umidade, fósforo, potássio, pH, temperatura, cultura e status da irrigação.

Na pasta sql, temos o arquivo consultas_farmtech.sql, com as consultas utilizadas no Oracle SQL Developer.

Agora, no Oracle SQL Developer, foi criada a conexão com o banco da FIAP. Em seguida, utilizei a opção de importar dados, escolhi o arquivo CSV e criei a tabela FARMTECH_SENSORES.

Após a importação, executei a consulta SELECT * FROM FARMTECH_SENSORES para confirmar que os dados foram carregados corretamente.

Também foram feitas consultas adicionais, como a verificação dos registros com irrigação ligada, a média dos sensores por cultura e os registros com baixa umidade.

Como parte opcional do projeto, também foi criada uma dashboard em Python usando Streamlit. Nela é possível visualizar os níveis de umidade, pH, fósforo, potássio e o status da irrigação, além de receber uma sugestão automática sobre a necessidade de irrigação.

Por fim, o projeto também possui um notebook de Machine Learning com análise exploratória, gráficos, identificação de perfil ideal para culturas e comparação entre modelos preditivos.

Esse foi o projeto FarmTech Solutions da Fase 3. Obrigado.
