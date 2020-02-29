import numpy as np

#search = np.array([(-66,-76,-78,-62,-79,-81)]) #busca B6A retorna (B6B, B6C, e B10.5)
#search = np.array([(-73,-73,-77,-53,-70,-78)]) #busca B6B retorna (B6A, B6B, B6C, B10.5)
#search = np.array([(-70,-60,-61,-69,-78,-72)]) #busca B9B retorna (B9B)
search = np.array([(-100,-67,-63,-49,-53,-48)]) #busca WC-M retorna (WC-M)
#search = np.array([(-57,-63,-63,-64,-100,-100)]) #busca B10.2 retorna (B104)
#search = np.array([(-100,-72,-74,-59,-79,-100)]) #busca B8B retorna (B8A)

#Exemplo
#search = np.array([(-100,-67,-63,-49,-53,-48)])

B1A = np.array([(-46,-78,-72,-70,-81,-59)])
B1B = np.array([(-100,-82,-85,-100,-76,-55)])
B1C = np.array([(-100,-100,-100,-78,-100,-58)])
B1D = np.array([(-51,-64,-73,-67,-79,-56)])
B4A = np.array([(-77,-100,-84,-75,-72,-72)])
B4B = np.array([(-78,-81,-80,-72,-70,-67)])
B4C = np.array([(-76,-76,-81,-67,-62,-67)])
B5A = np.array([(-100,-76,-80,-67,-61,-69)])
B5B = np.array([(-100,-79,-80,-68,-59,-71)])
B6A = np.array([(-77,-81,-78,-62,-76,-80)])
B6B = np.array([(-68,-75,-76,-54,-73,-74)])
B6C = np.array([(-72,-73,-72,-62,-72,-75)])
B7A = np.array([(-100,-78,-78,-65,-74,-78)])
B7B = np.array([(-100,-81,-77,-69,-74,-76)])
B8A = np.array([(-100,-77,-75,-66,-81,-100)])    #B8A
B8B = np.array([(-82,-74,-76,-64,-80,-100)])     #B8B
B9A = np.array([(-73,-66,-62,-69,-76,-100)])     #B9A
B9B = np.array([(-70,-61,-63,-69,-78,-75)])      #B9B
B9C = np.array([(-70,-57,-75,-75,-100,-79)])     #B9C
B101 = np.array([(-63,-73,-70,-68,-100,-85)])     #B10.1
B102 = np.array([(-57,-70,-65,-70,-78,-81)])      #B10.2
B103 = np.array([(-56,-70,-67,-75,-100,-100)])    #B10.3
B104 = np.array([(-56,-65,-72,-72,-100,-100)])    #B10.4
B105 = np.array([(-64,-75,-78,-60,-76,-76)])      #B10.5
B11A = np.array([(-78,-52,-73,-73,-78,-76)])      #B11A
B11B = np.array([(-77,-58,-68,-74,-100,-78)])     #B11B
B11C = np.array([(-83,-67,-82,-78,-79,-79)])      #B11C
B12A = np.array([(-63,-56,-74,-77,-100,-83)])     #B12A
B12B = np.array([(-67,-63,-77,-79,82,-100)])      #B12B
B12C = np.array([(-72,-64,-77,-78,-100,-78)])     #B12C
WCM = np.array([(-100,-70,-68,-55,-53,-55)])     #WC-M
WCF = np.array([(-100,-76,-80,-78,-71,-60)])     #WC-F
C1 = np.array([(-100,-61,-69,-61,-61,-43)])     #C1
C2 = np.array([(-100,-48,-59,-53,-49,-52)])     #C2
C3 = np.array([(-67,-58,-60,-48,58,-57)])       #C3
C4 = np.array([(-55,-46,-57,-52,-54,-55)])      #C4
C5 = np.array([(-100,-48,-60,-58,-64,-57)])      #C5

candidatos = [B1A, B1B, B1C, B1D, B4A, B4B, B4C, B5A, B5B, B6A, B6B, B6C, B7A, B7B, B8A, B8B, B9A, B9B, B9C, B101, B102, B103, B104, B105, B11A, B11B, B11C, B12A, B12B, B12C, WCM, WCF, C1, C2, C3, C4, C5]
margem_erro = 10.0

distancias = candidatos[::] - search # Avalia a distância de cada vetor para o vetor de busca.
avaliar_dist = np.where(np.absolute(distancias) < margem_erro, True, False) # Localiza em quais posições dos vetores de distância a margem de erro é satisfeita.
vetores_aprovados = avaliar_dist.all(axis=2) # Marca Verdadeiro se toda a linha tem valores Verdadeiros.
posicao_aprovados = np.array(np.where(vetores_aprovados== True)[0]) # Grava a posição dos vetores dentro da margem de erro.

print("Busca: {}".format(search))
print("Resultado: ")
for x in posicao_aprovados:
    print(candidatos[x])
