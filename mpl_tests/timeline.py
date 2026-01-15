import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Example: Project time process  

# 1. Prepare the data
events = [
    ("Project Kickoff", "2023-01-19"),
    ("First Prototype", "2023-03-21"),
    ("Beta Testing", "2023-06-15"),
    ("Final Review", "2023-08-07"),
    ("Product Launch", "2023-11-27")
]

# Convert strings to datetime objects
names = [e[0] for e in events]
dates = [datetime.strptime(e[1], "%Y-%m-%d") for e in events]

# 2. Set vertical levels for labels (alternating to avoid overlap)
levels = [1, -1, 1, -1, 1]

# 3. Create plot
fig, ax = plt.subplots(figsize=(10, 4), constrained_layout=True)
ax.set_title("Project timeline process for a simple product", fontsize=16, pad=20)

# Central horizonal baseline
ax.axhline(0, color="black", linewidth=2, zorder=1)

# Vertical stems and markers
ax.vlines(dates, 0, levels, color="lightblue", linewidth=1.5) # Baseline dots
ax.scatter(dates, [0]*len(dates), color="darkblue", s=100, zorder=3) # Baseline dots
ax.scatter(dates, levels, color="skyblue", s=50, zorder=3) # Tip dots

# 4. Annotate events
for i, (name, date) in enumerate(zip(names, dates)):
    ax.annotate(name, xy=(date, levels[i]),
                xytext=(0,5 if levels[i] > 0 else -15),
                textcoords="offset points",
                ha="center", va="bottom" if levels[i] > 0 else "top",
                fontsize=12, fontweight='bold')

# 5.- Format the X-axis dates    
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.xticks(rotation=45)

# 6.- Clean up the UI
ax.get_yaxis().set_visible(False) # Hide Y-axis
for spine in ["left", "top", "right"]:
    ax.spines[spine].set_visible(False) # Remove border spines

ax.margins(y=0.2) # add some padding

plt.show()