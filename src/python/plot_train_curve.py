import pandas as pd
import matplotlib.pyplot as plt
import sys

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(sys.argv[1])

# Extract data from the DataFrame
epochs = df['epoch']
mse = df['mse']

# Plotting the training curve
plt.figure(figsize=(10, 6))
plt.plot(epochs, mse, label='Training MSE')
plt.title('Multivar. RNN Training Curve')
plt.xlabel('Epoch')
plt.ylabel('MSE')
plt.legend()
plt.grid(True)
plt.show()
