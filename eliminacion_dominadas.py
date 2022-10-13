import nashpy as nash
import numpy as np

game = np.array(
    [[0,-1,1],
    [1,0,-1],
    [-1,1,0]]
    )

response = nash.Game(game)
print(response)