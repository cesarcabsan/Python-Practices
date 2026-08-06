import matplotlib.pyplot as plt
import matplotlib.patches as patches

''''''''''
# Making a basic generic logo with bbox 
logo_text = plt.text(0.5, 0.5, 'Key Point', fontsize=40, color='blue', ha='center', va='center',
                     bbox=dict(boxstyle='circle', facecolor='green', alpha=0.5))

plt.axis('off') 
plt.show()
'''''''''


# With the patches library
fig, ax = plt.subplots()
ax.set_aspect('equal')

circle = patches.Circle((0.5, 0.5), 0.5, color='red', alpha=0.5)
ax.add_patch(circle)

ax.text(0.5, 0.5, 'Logo made with patches library', color='purple', ha='center', va='center', fontsize=13, fontweight='bold')

plt.xlim(0, 1)
plt.ylim(0, 1)
plt.axis('off')  
plt.show()