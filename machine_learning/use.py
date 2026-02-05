import joblib
model = joblib.load("rating.joblib")
print(model.predict([
    "Estragou depois de uma semana de uso.",
    "Produto maravilhoso, super satisfeito!",
    "O produto é bom, mas a entrega demorou um pouco",
]*333))
