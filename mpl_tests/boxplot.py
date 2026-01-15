import matplotlib.pyplot as plt

class_A = [50, 55, 58, 60, 62, 64, 66, 69, 70, 71, 72, 75, 76, 87, 98] # Outlier: 98
class_B = [55, 60, 62, 64, 66, 69, 70, 71, 72, 75, 76, 79, 89, 98, 98.3] # Outliers: 98, 98.3
class_C = [43.5, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 85, 99, 105]  # Outliers: 43.5, 105

data = [class_A, class_B, class_C]
 
plt.boxplot(data, vert=False, patch_artist=True, whis=1.5, showfliers=True, tick_labels=['Class A', 'Class B', 'Class C'], boxprops=dict(facecolor='skyblue'),
            flierprops=dict(marker='o', color='black', markersize=6), medianprops=dict(color='red', linewidth=2))

plt.title("Exam scores for three classes")
plt.xlabel("Exam scores")
plt.ylabel("Classes")
plt.tight_layout()
plt.show()