import time
import statistics

def particao(vet, menor, maior):
    inicio_particao = time.time()
    
    pivo = vet[maior]
    i = menor
    for j in range(menor, maior):
        if vet[j] <= pivo:
            vet[i], vet[j] = vet[j], vet[i]
            i += 1
    
    vet[i], vet[maior] = vet[maior], vet[i]
    
    fim_particao = time.time()
    print(f"Tempo particao (tam = {maior-menor+1}): {fim_particao - inicio_particao:.6f}s")
    
    return i

def quickselect(vet, menor, maior, k):
    inicio_quickselect = time.time()
    
    if menor == maior:
        return vet[menor]
    
    pivo_i = particao(vet, menor, maior)
    
    if k == pivo_i:
        return vet[k]
    elif k < pivo_i:
        resultado = quickselect(vet, menor, pivo_i - 1, k)
    else:
        resultado = quickselect(vet, pivo_i + 1, maior, k)
    
    fim_quickselect = time.time()
    print(f"Tempo quickselect (tam = {maior-menor+1}): {fim_quickselect - inicio_quickselect:.6f}s")
    
    return resultado

def encontrar_mediana(vet):
    copia_vetor = vet.copy()
    n = len(copia_vetor)
    
    inicio_total = time.time()
    
    if n % 2 == 1:
        mediana = quickselect(copia_vetor, 0, n - 1, n // 2)
    else:
        esq = vet.copy()
        dir = vet.copy()
        esq = quickselect(esq, 0, n - 1, (n // 2) - 1)
        dir = quickselect(dir, 0, n - 1, n // 2)
        mediana = (esq + dir) / 2
    
    fim_total = time.time()
    
    print(f"\nTempo total: {fim_total - inicio_total:.6f} segundos")
    print(f"Mediana = {mediana}")
    
    return mediana

teste = [3, 1, 4, 1, 5, 9, 2, 6, 8]
encontrar_mediana(teste)
#print(f"Mediana (verificação): {statistics.median(teste)}")