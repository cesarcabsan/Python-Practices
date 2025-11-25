import matplotlib.pyplot as plt
import numpy as np

# Basic heatmap
plt.figure()
some_data = np.random.random((10,10))
plt.imshow(some_data, cmap='coolwarm', aspect='auto', origin='upper')
plt.colorbar(label='Insensity') 
plt.title("Basic Heatmap Example")


# Annotated heatmap
plt.figure() 
annotated_data = np.random.random((5,7))
plt.imshow(annotated_data, cmap='viridis', aspect='auto', origin='upper')
# Add text annotations to each cell
for i in range(annotated_data.shape[0]):
    for j in range(annotated_data.shape[1]):
        plt.text(j, i, f'{annotated_data[i,j]:.2f}', ha='center', va='center', color='red')

plt.colorbar(label='Values')
plt.title("Annotated Heatmap")


# Clustered heatmap
plt.figure()
data = np.random.random((8, 12))
# Creating clusters in a portion of the data
data[:, 3:6] += 1  
plt.imshow(data, cmap='winter', aspect='auto', origin='upper')
plt.colorbar(label='Intensity')
plt.title('Clustered Heatmap')

#add row and column labels (Optional)
plt.xticks(range(data.shape[1]), [f'Col {i}' for i in range(data.shape[1])])
plt.yticks(range(data.shape[0]), [f'Row {i}' for i in range(data.shape[0])])

# show both figures simultaneously
plt.show()