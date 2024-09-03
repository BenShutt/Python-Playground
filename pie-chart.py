"""
Example plotting a pie chart with Matplotlib and NumPy
"""

import matplotlib.pyplot as plt
import numpy as np

# Number of random numbers to generate
SAMPLE_SIZE = 100

# Size of the plotted figure
FIGURE_SIZE = (10, 7)

# Callable used by autopct when plotting.
# The percentage argument is reverted to get the count.
def autopct(size):
    def callable(percentage):
        print(percentage)
        value = int(round(size * percentage / 100.0))
        return '{v:d} ({p:.1f}%)'.format(v = value, p = percentage)
    return callable

if __name__ == "__main__":
    # Random numbers in the range [1, 3]
    data = np.random.randint(low=1, high=4, size=SAMPLE_SIZE)

    # Map to a dictionary by counting
    dict = {}
    for number in data:
        dict[number] = dict.get(number, 0) + 1
    
    # Sort by key
    sortedDict = sorted(dict.items())

    # Map to key only
    labels = [x[0] for x in sortedDict]

    # Map to value only
    counts = [x[1] for x in sortedDict]

    # Draw chart
    figure = plt.figure(figsize=FIGURE_SIZE)
    plt.pie(counts, labels=labels, autopct=autopct(SAMPLE_SIZE))
    plt.show()