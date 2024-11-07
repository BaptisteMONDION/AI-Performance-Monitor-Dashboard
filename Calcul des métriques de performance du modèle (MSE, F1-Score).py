from sklearn.metrics import mean_squared_error, f1_score

# Exemple de valeurs prédictives et réelles
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]

# Calcul du MSE
mse = mean_squared_error(y_true, y_pred)
print(f"Mean Squared Error (MSE): {mse}")

# Calcul du F1-Score (pour une classification binaire)
y_true_class = [0, 1, 1, 0]
y_pred_class = [0, 1, 0, 0]
f1 = f1_score(y_true_class, y_pred_class)
print(f"F1-Score: {f1}")
