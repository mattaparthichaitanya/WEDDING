import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import seaborn as sns
atmpl = 10
otmpl = 16
# Simulated function to calculate current_profit_or_loss
def calculate_profit_or_loss():
    # Replace this with your actual profit/loss calculation logic
    return (atmpl + otmpl) * 15

# Create initial chart and data
sns.set(style='whitegrid')
fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot(x_data, y_data, color='blue', label='Profit/Loss')
ax.set_xlabel('Time')
ax.set_ylabel('Profit/Loss')
ax.set_title('Real-Time Profit/Loss Data')
ax.legend()

timestamps = []

# Define update function
def update(frame):
    current_profit_or_loss = calculate_profit_or_loss()
    timestamps.append(time.time())
    y_data.append(current_profit_or_loss)
    
    # Limit the number of data points displayed on the chart (adjust as needed)
    max_data_points = 100
    if len(y_data) > max_data_points:
        y_data.pop(0)
        timestamps.pop(0)
    
    line.set_data(timestamps, y_data)
    ax.relim()
    ax.autoscale_view()
    
    return line,

# Create animation
animation = FuncAnimation(fig, update, frames=range(100), interval=1000, cache_frame_data=False)

# Save the animation as a GIF file
animation.save('profit_loss_animation.gif', writer='imagemagick', fps=1)

# Display the chart
plt.show()
