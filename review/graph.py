import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------------------------------------------------------------------
# Graph Class, takes in a list of [0,0,0] (positve, negative, neutral) values, and labels for each ---
# product, then creates a graph using info -----------------------------------------------------------
# ----------------------------------------------------------------------------------------------------
class Graph:
  # Take in info, translate to how it will be used for display function
  def __init__(self, vals_list, labels):
    self.values = vals_list
    self.labels = labels

    self.positive = []
    self.neutral = []
    self.negative = []

    for spot in self.values:
      self.positive.append(spot[0])
      self.neutral.append(spot[1])
      self.negative.append(spot[2])

  # Display contents
  def display(self):
    products = self.labels
    x = np.arange(len(products))

    width = 0.2  # Width of each bar

    # Plotting
    plt.bar(x - width, self.positive, width, label='Positive')
    plt.bar(x, self.neutral, width, label='Neutral')          
    plt.bar(x + width, self.negative, width, label='Negative')

    # labels/legend
    plt.xticks(x, products) 
    plt.xlabel('Products')
    plt.ylabel('Reviews')
    plt.title('Review Chart')
    plt.legend()

    # Display
    plt.tight_layout()
    plt.show()
