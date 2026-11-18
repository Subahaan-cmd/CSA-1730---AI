# Experiment 20: Feed Forward Neural Network (with backpropagation) learning XOR
import numpy as np

np.random.seed(1)

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(a):
    return a * (1 - a)


input_size, hidden_size, output_size = 2, 4, 1
W1 = np.random.uniform(-1, 1, (input_size, hidden_size))
b1 = np.zeros((1, hidden_size))
W2 = np.random.uniform(-1, 1, (hidden_size, output_size))
b2 = np.zeros((1, output_size))

lr = 0.5
epochs = 10000

for epoch in range(epochs):
    # Forward pass
    hidden = sigmoid(X @ W1 + b1)
    output = sigmoid(hidden @ W2 + b2)

    # Error
    error = y - output

    # Backward pass
    d_output = error * sigmoid_derivative(output)
    d_hidden = (d_output @ W2.T) * sigmoid_derivative(hidden)

    # Update weights
    W2 += hidden.T @ d_output * lr
    b2 += np.sum(d_output, axis=0, keepdims=True) * lr
    W1 += X.T @ d_hidden * lr
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * lr

    if epoch % 2000 == 0:
        print(f"Epoch {epoch:5d}  Loss (MSE): {np.mean(error ** 2):.6f}")

print("\nFinal predictions:")
output = sigmoid(sigmoid(X @ W1 + b1) @ W2 + b2)
for inp, out, target in zip(X, output, y):
    print(f"  Input {inp} -> {out[0]:.4f} (rounded {round(out[0])}), expected {target[0]}")
