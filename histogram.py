import pandas as pd
import matplotlib.pyplot as plt

# Data extracted from the rough histogram for Rabail (Before)
# Approximate values based on the text representation:
# W1: 30, W2: 0, W3: 10, W4: 0, W5: 0, W6: 40, W7: 40, W8: 40, W9: 80, W10: 80, W11: 50, W12: 60, W13: 20
data = {
    'Week': ['W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8', 'W9', 'W10', 'W11', 'W12', 'W13'],
    'Hours': [30, 0, 10, 0, 0, 40, 40, 40, 80, 80, 50, 60, 20]
}
df = pd.DataFrame(data)

# Create the bar chart
plt.figure(figsize=(12, 6))
plt.bar(df['Week'], df['Hours'], color='darkblue')

# Set the title and labels
plt.title('Rabail (Before) Hours per Week', fontsize=14)
plt.xlabel('Week', fontsize=12)
plt.ylabel('Hours', fontsize=12)

# Set y-axis limits to match the text representation
plt.ylim(0, 85) # Slight buffer above 80
plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80])

# Add horizontal grid lines for better readability
plt.grid(axis='y', linestyle='-', alpha=0.7)

# Save the plot
plt.savefig('rabail_before_histogram.png')

print("rabail_before_histogram.png")