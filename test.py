search = [-50,-78,-70,-65,-80,-55]

B1A = [-46,-78,-72,-70,-81,-59]#, 'b1a')
B1B = [None,-82,-85,None,-76,-55]#, 'b1b')
B1C = [None,None,None,-78,None,-58]#,'b1c')
B2A = [None,-88,None,None,None,-60]#, 'b2a')
B2B = [None,-78,-79,-80,-80,-59]#, 'b2b')

atual = ([], 0,'')

for vetor in [B1A, B1B, B1C, B2A, B2B]:
    quantidade = 0

    for valor in search:
        if valor in vetor:
            quantidade += 1

    if quantidade > atual[1]:
        atual = [vetor, quantidade]

busca = search
resultado = atual[0]
matchs = atual[1]
#local = atual[2]


print("Busca: {}".format(busca))
print("Resultado: {}".format(resultado))
print("Matchs: {}".format(matchs))
#print("Local: {}".format(local))
