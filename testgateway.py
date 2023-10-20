from mlflow.gateway import query, set_gateway_uri

set_gateway_uri(gateway_uri="http://localhost:7000")

response = query(
    "chat",
    {"messages": [{"role": "user", "content": "What is the best day of the week?"}]},
)

print(response)