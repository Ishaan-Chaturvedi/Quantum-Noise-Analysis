from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
def histogrammaker(result,key='meas'):
    counts = getattr(result[0].data.meas, key).get_counts()
    plot_histogram(counts)
    plt.show()

