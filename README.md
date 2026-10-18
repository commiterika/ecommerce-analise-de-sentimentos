# Análise das Entregas de E-commerce e Avaliação de Sentimentos dos Clientes"


## 📌 Descrição do Projeto

Este projeto analisa o desempenho das entregas e a percepção dos clientes, de um e-commerce fictício. Buscando insights e feedbacks para melhorias.

O OBJETIVO é identificar gargalos logísticos e o impacto disso na visão do consumidor sobre o e-commerce.


## 🛠️ Tecnologias Utilizadas

- Python 3.13.16
- Pandas
- NumPy
- Matplotlib (pyplot)


## 📊 Principais Insights

#### 1. Pedidos Atrasados (23,0% do total)

* Problemas com SLA¹: O prazo regulamentar de entrega do e-commerce é de até 5 dias. No entanto, 60% dos pedidos atrasados levaram 11 dias ou mais para serem entregues, o que representa mais do que o dobro do tempo limite acordado.

* Impacto na Experiência (NPS²/CSAT³): Os atrasos geraram uma insatisfação crítica nos clientes, resultando em avaliações com nota mínima (1 ou 2 estrelas) e sentimento estremamente negativo para a quase todos dos casos registrados.

¹ Service Level Agreement: Acordo de Nível de Serviço.
² Net Promoter Score: Indice de Lealdade do Cliente.
³ Customer Satisfaction Score: Pontuação de Satisfação do Cliente.

#### 2. Pedidos Cancelados (8,0% do total)

Ao analisar a causa raiz dos cancelamentos nas avaliações e comentários, identificou-se um cenário dividido:

* 50,0% Cancelados pelos Clientes: Motivados por o produto ter chegado com defeito.
* 50,0% Cancelados pela Empresa (Interno): Pedidos cancelados diretamente pela empresa, sem justificativa clara.

### 💡 Recomendações:

1. Logística: Investigar as rotas e transportadoras responsáveis pelos pedidos com mais de 10 dias de entrega para renegociar SLAs ou trocar de parceiros operacionais.
2. Controle de Qualidade (QA): Revisar o processo de envio com fornecedores para diminuir o índice de produtos entregues com defeito.
3. Comunicação de Cancelamento: Implementar notificações automáticas e claras quando houver cancelamento por parte da empresa, evitando a sensação de descaso, ocasionado por cancelamentos sem explicação.

## 🚀 Como Executar

1. Clone o repositório: `git clone https://github.com/commiterika/ecommerce-analise-de-sentimentos`
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute o gerador de dados: `python src/generate_data.py`
4. Execute o notebook/script em `notebooks/da_and_sentiment.ipynb`
