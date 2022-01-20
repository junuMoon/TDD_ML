import numpy as np

def sigmoid(x, scale=3):
    return (1 / (1 + np.exp(-x))) * scale