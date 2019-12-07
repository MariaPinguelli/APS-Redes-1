from funcoes import validarCampos, verificaID, verificaClasse, ipDaRede, ipBroadcast, qtdHosts, faixaValida, ipReservado
import json
import sys

def main():
  arquivo = {}
  with open((sys.argv[1]), "r") as f:
    arquivo = json.load(f)
  if arquivo == None:
    print("\nNão foi possível carregar o arquivo!\nExecute o código novamente passando o .json correto por parâmetro.\n")
  else:
    print("\nArquivo aberto!\n")

    ipAddr = arquivo["ipAddr"]
    netMask = arquivo["netMask"]

    print("Endereço de IP: ", ipAddr)
    print("Máscara de Rede:", netMask, "\n")

    ipAddr = ipAddr.split(".")
    netMask = netMask.split(".")

    for i in range(4):
      ipAddr[i] = int(ipAddr[i])
    for i in range(4):
      netMask[i] = int(netMask[i])
    with open('saida.json', 'w') as saida:
      saida.write("{")

      # a) Verificar se IPs e máscaras são válidas.
      validarCampos(ipAddr, netMask, saida)

      # b) Quantidade de bits da rede (netID) e quantidade de bits de host (hostID), da máscara.
      verificaID(ipAddr, netMask, saida)

      # c) Classe do IP.
      classe = verificaClasse(ipAddr, netMask, saida)

      # d) IP da rede.
      ipRede = ipDaRede(ipAddr, netMask, saida)

      # e) IP de broadcast.
      ipBroad = ipBroadcast(ipAddr, netMask, saida)

      # f) Quantidade de hosts na referida rede.
      qtdHosts(netMask, saida)

      # g) Faixa de máquinas válidas - que podem ser utilizadas pelos hosts.
      faixaValida(ipRede, ipBroad, saida)

      # h) Se o IP é em questão é reservado (privado, loopback, etc).
      ipReservado(ipAddr, classe, saida)
      
      saida.write("\n}")
      



if __name__ == "__main__":
  main()