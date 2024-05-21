# Flowchart using Graphviz
from graphviz import Digraph

# Create a new directed graph
graph = Digraph()

# Add nodes
graph.node('A', 'Start')
graph.node('B', 'Step 1')
graph.node('C', 'Step 2')
graph.node('D', 'End')

# Add edges
graph.edge('A', 'B')
graph.edge('B', 'C')
graph.edge('C', 'D')

# Save and render the graph
graph.render('simple_algorithm', format='png', cleanup=True)

# Animated Visualization using Matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for visualization
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a figure and axis
fig, ax = plt.subplots()

# Update the plot in a loop to simulate algorithm steps
for i in range(len(x)):
    ax.plot(x[:i], y[:i], color='blue')
    ax.set_title(f'Step {i}')
    plt.pause(0.1)  # Pause for 0.1 seconds to see the plot update
    ax.cla()  # Clear the axis for the next plot

plt.show()

# Textual Visualization
# Example of printing intermediate steps
for i in range(5):
    print(f'Step {i}: {i * 2}')
