import numpy as np

search = [-50,-68,-70,-65,-78,-55]

B1A = [-46,-78,-72,-70,-81,-59]
B1B = [None,-82,-85,None,-76,-55]
B1C = [None,None,None,-78,None,-58]
B2A = [None,-88,None,None,None,-60]
B2B = [None,-78,-79,-80,-80,-59]
teste = [-51,-68,-70,-65,-78,-55]
result = []

for vetor in [B1A, B1B, B1C, B2A, B2B, teste]:
    #retorna true ou false se for igual
    #if np.array_equal(search,vetor):
    #    result = vetor

    if np.allclose(search,vetor):
        print(vetor)

    #print(result)
