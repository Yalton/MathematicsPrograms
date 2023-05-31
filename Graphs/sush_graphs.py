import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Use seaborn styles for more appealing plots
sns.set()

# Read the CSV data
df = pd.read_csv('data.csv')

# Remove the '%' from the 'Base Resistance' column and convert it to float
df['Base Resistance'] = df['Base Resistance'].str.rstrip('%').astype('float') / 100.0

# Create a subplot
fig, ax1 = plt.subplots()

# Plot 'Rock Mass' against 'Base Instability' as a scatter plot
scatter = ax1.scatter(df['Rock Mass'], df['Base Instability'], color='blue', label='Base Instability')
ax1.set_xlabel('Rock Mass')
ax1.set_ylabel('Base Instability', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Create a second y-axis that shares the same x-axis
ax2 = ax1.twinx()

# Plot 'Rock Mass' against 'Base Resistance' as a line plot
line = ax2.plot(df['Rock Mass'], df['Base Resistance'], color='red', label='Base Resistance')
ax2.set_ylabel('Base Resistance', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Add a title to the plot
plt.title('Rock Mass vs Base Instability and Base Resistance')

# Add legend
plots = scatter + line
labels = [p.get_label() for p in plots]
ax1.legend(plots, labels, loc=0)

# Save the plot as a PNG image
plt.savefig('plot.png', dpi=300)

# Show the plot
plt.show()
