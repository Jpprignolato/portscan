def escolher_listaDePortas():
    top_portas10 = [21,22,23,25,80,110,139,443,445,3389]
    top_portas20 = [135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
    top_portas50 = [3389,5060,5666,5900,6001,8000,8008,8080,8443,8888,10000,32768,49152,49154]

    print("Selecione uma Lista de Portas: ")
    print("1 - Lista top 10")
    print("2 - Lista top 20")
    print("3 - Lista top 50")
    resposta = input("\n>>> ")

    lista_escolhida = []

    if (resposta == '1'):   
        lista_escolhida = top_portas10
        return lista_escolhida
    elif(resposta == '2'):
        lista_escolhida = top_portas20
        return lista_escolhida
    else:
        lista_escolhida = top_portas50
        return lista_escolhida
