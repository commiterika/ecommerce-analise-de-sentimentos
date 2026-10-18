import os
import numpy as np
import pandas as pd

# Garantir reprodutibilidade
np.random.seed(42)
n = 100

# Opções de avaliação por cenário (para garantir coerência entre status, nota e texto)
REVIEWS_BY_STATUS = {
    "No Prazo": [
        ("Excelente produto, chegou super rápido!", 5),
        ("Gostei bastante, recomendo a todos!", 5),
        ("Chegou dentro do prazo e bem embalado.", 5),
        ("Muito bom, atendeu às expectativas.", 4),
        ("Produto atendeu o esperado, entrega dentro do prazo.", 4),
    ],
    "Atrasado": [
        ("O produto é bom, mas a entrega atrasou um pouco.", 3),
        ("Demorou mais do que o informado na compra.", 2),
        ("Péssimo atendimento, demorou demais para chegar.", 1),
        ("Entrega muito atrasada, fiquei insatisfeita.", 1),
    ],
    "Cancelado": [
        ("Pedido foi cancelado e o suporte não ajudou.", 1),
        ("Tive o pedido cancelado sem explicação razoável.", 1),
        ("Veio com defeito e acabei cancelando a compra.", 1),
        ("Atendimento horrível, cancelaram meu pedido.", 1),
    ],
}

# 1. Gerar atributos básicos
order_ids = [f"ORD-{1000 + i}" for i in range(n)]
customer_ids = [f"CUST-{np.random.randint(100, 999)}" for _ in range(n)]
order_dates = pd.date_range(start="2026-01-01", periods=n, freq="D")
delivery_statuses = np.random.choice(
    ["No Prazo", "Atrasado", "Cancelado"], size=n, p=[0.7, 0.2, 0.1]
)

delivery_days = []
review_ratings = []
review_texts = []

# 2. Atribuir dias de entrega, notas e textos de forma lógica
for status in delivery_statuses:
    if status == "No Prazo":
        # Entregas no prazo levam de 1 a 5 dias
        days = np.random.randint(1, 6)
    elif status == "Atrasado":
        # Entregas atrasadas levam de 6 a 15 dias
        days = np.random.randint(6, 16)
    else:
        # Cancelado não possui dias de entrega concluída
        days = None

    # Seleciona aleatoriamente um par (texto, nota) coerente com o status
    options = REVIEWS_BY_STATUS[status]
    text, rating = options[np.random.choice(len(options))]

    delivery_days.append(days)
    review_texts.append(text)
    review_ratings.append(rating)

# 3. Montar DataFrame
df = pd.DataFrame(
    {
        "order_id": order_ids,
        "customer_id": customer_ids,
        "order_date": order_dates,
        "delivery_status": delivery_statuses,
        "delivery_days": delivery_days,
        "review_rating": review_ratings,
        "review_text": review_texts,
    }
)

# Garantir que a pasta 'data' existe antes de salvar
os.makedirs("data", exist_ok=True)

# Salvar o CSV
output_path = "data/ecommerce_site_reviews.csv"
df.to_csv(output_path, index=False)

print(f"Base {output_path} base gerada com sucesso!")