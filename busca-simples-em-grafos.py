def visitar(v):
    global t, n
    if marca[v] == 1:
        return
    t = t + 1
    print("visitando o vértice", v, "no tempo", t)
    marca[v] = 1
    for w in range(n):
        if mat[v][w] == 1 and marca[w] == 0:
            visitar(w)
    return


n = input("Entre com o número de vértices: ")
n = int(n)
#mat = [[0] * n for i in range(n)]


# mat = [[0, 1, 0, 0, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 1], [1, 0, 0, 1, 0]]

mat = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
]

for i in range(n):
    print("inserir linha", i, "da matriz:")
    vet = input().split(" ")
    linha = [int(valor) for valor in vet]
    mat[i] = linha

marca = n * [0]
t = 0

visitar(0)

if t == n:
    print("Grafo conexo")
else:
    print("Grafo desconexo")
