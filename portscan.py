import socket
import portlist
import time
import os

print("PORTSCAN - V1")

def port_scan():
    ip = input("Insira o IP do alvo: ")
    lista_portas = portlist.escolher_listaDePortas()
    print("Iniciando scan no IP: ", ip)
    time.sleep(4)
    print("Lista de portas escolhidas:\n", lista_portas,"\n")
    time.sleep(4)
    os.system("cls")

    print("Aguarde o scan...")
    for porta in range(1,100):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        if (sock.connect_ex((ip,porta)) == 0):
            print("[+] Porta TCP Aberta:",porta)
            sock.close()

port_scan()