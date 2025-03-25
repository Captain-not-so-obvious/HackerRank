def imprime_tapete_de_porta(N, M):
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

N, M = map(int, input().split())
if N % 2 == 0:
    print("Por favor, N deve ser um número ímpar.")
else:
imprime_tapete_de_porta(N, M)
