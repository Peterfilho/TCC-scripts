
from __future__ import print_function

import numpy as np

none = 1e10

#lugares sem sinal algum foram preenchidos como -100

#search = np.array([-66,-76,-78,-62,-79,-81]) #busca B6A retorna B4C
#search = np.array([-73,-73,-77,-53,-70,-78]) #busca B6B retorna B11A
#search = np.array([-100,-56,-61,-71,-78,-72]) #busca B9B retorna WC-F
#search = np.array([-100,-67,-63,-49,-53,-48]) #busca WC-M retorna C5
#search = np.array([-57,-63,-63,-64,-100,-100]) #busca B10.2 retorna B12A
search = np.array([-100,-72,-74,-59,-79,-100]) #busca B8B retorna B5B

candidates = np.array([

        [-46,-78,-72,-70,-81,-59],      #B1A
        [-100,-82,-85,-100,-76,-55],    #B1B
        [-100,-100,-100,-78,-100,-58],  #B1C
        [-100,-88,-100,-100,-100,-60],  #B2A
        [-100,-78,-79,-80,-80,-59],     #B2B
        [-100,-100,-100,78,-77,-57],    #B3A
        [-100,-100,-100,-80,-80,-52],   #B3B
        [-77,-100,-84,-75,-72,-72],     #B4A
        [-78,-81,-80,-72,-70,-67],      #B4B
        [-76,-76,-81,-67,-62,-67],      #B4C
        [-100,-76,-80,-67,-61,-69],     #B5A
        [-100,-79,-80,-68,-59,-71],     #B5B
        [-77,-81,-78,-62,-76,-80],      #B6A
        [-68,-75,-76,-54,-73,-74],      #B6B
        [-72,-73,-72,-62,-72,-75],      #B6C
        [-100,-78,-78,-65,-74,-78],     #B7A
        [-100,-81,-77,-69,-74,-76],     #B7B
        [-100,-77,-75,-66,-81,-100],    #B8A
        [-82,-74,-76,-64,-80,-100],     #B8B
        [-73,-66,-62,-69,-76,-100],     #B9A
        [-70,-59,-63,-68,-81,-83],      #B9B
        [-70,-57,-75,-75,-100,-79],     #B9C
        [-63,-73,-70,-68,-100,-85],     #B10.1
        [-57,-70,-65,-70,-78,-81],      #B10.2
        [-56,-70,-67,-75,-100,-100],    #B10.3
        [-56,-65,-72,-72,-100,-100],    #B10.4
        [-64,-75,-78,-60,-76,-76],      #B10.5
        [-78,-52,-73,-73,-78,-76],      #B11A
        [-77,-58,-68,-74,-100,-78],     #B11B
        [-83,-67,-82,-78,-79,-79],      #B11C
        [-63,-56,-74,-77,-100,-83],     #B12A
        [-67,-63,-77,-79,82,-100],      #B12B
        [-72,-64,-77,-78,-100,-78],     #B12C
        [-100,-77,-80,-70,-57,-71],     #WC-M
        [-100,-76,-80,-78,-71,-60],     #WC-F
        [-100,-61,-69,-61,-61,-43],     #C1
        [-100,-48,-59,-53,-49,-52],     #C2
        [-67,-58,-60,-48,58,-57],       #C3
        [-55,-46,-57,-52,-54,-55],      #C4
        [-100,-48,-60,-58,-64,-57]      #C5
])

sum_residual_closest = 1e10
closest = []

for candidate in candidates:

    differences = (search.reshape(1,-1) - candidate.reshape(-1,1))

    indices = np.abs(differences).argmin(axis=0)

    residual = np.diagonal(differences[indices,])

    sum_residual = np.sum(np.abs(residual))

    if sum_residual < sum_residual_closest:

        sum_residual_closest = sum_residual

        closest = candidate

print("Procure esse vetor no codigo e veja o local comentado {}".format(closest))
