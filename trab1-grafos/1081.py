def visitar(v, s):
    x = " "
    global t, n
    if marca[v] == 1:
        return

    t = t + 1
    marca[v] = 1

    for w in range(n):
        if mat[v][w] == 1 and marca[w] == 0:
            if w == len(marca):
                print(x * s, f"{v}-{w} pathR(G,{w})", end="") #delete tis
                visitar(w, s + 1)
            else:
                print(x * s, f"{v}-{w} pathR(G,{w})")
                visitar(w, s + 1)

        elif mat[v][w] == 1 and marca[w] == 1:
            print(x * s, f"{v}-{w}")

    return


##################################


casos = int(input())
for i in range(casos):
    print(f"Caso {i+1}:")
    n, e = input().split(" ")
    n = int(n)
    e = int(e)

    mat = [[0] * n for i in range(n)]

    for i in range(e):
        a, b = input().split(" ")
        a = int(a)
        b = int(b)
        mat[a][b] = 1

    marca = n * [0]
    t = 0
    espacos = 1
    visitar(0, espacos)

    for j in range(len(marca)):
        if marca[j] != 1:
            print()
            visitar(j, espacos)
    print()

# cat input.txt | py 1081.py
