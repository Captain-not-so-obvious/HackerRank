def imprime_tapete_de_porta(N):
    M = 3 * N
    bem_vindo = "WELCOME"
    linha_central = (N // 2)
    for i in range(N):
        if i == linha_central:
            padrao = bem_vindo.center(M, "-")
            print(padrao)
        else:
            num_padrao = (i * 2 + 1) if i < linha_central else ((N - 1 - i) * 2 + 1)
            padrao = ".|." * num_padrao
            padrao = padrao.center(M, "-")
            print(padrao)

N = 7
imprime_tapete_de_porta(N)
