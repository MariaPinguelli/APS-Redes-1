def validarCampos(ipAddr, netMask, saida):
  escritoIP = 0
  escritoMask = 0
  if(len(ipAddr) != 4):
    print("Erro: Quantidade de números do endereço de IP está errada, o número deve ter exatamente 4 números!\n")
    saida.write("\n\t\"ipValido\": false,")
    escritoIP = 1
  else:
    print("Quantidade de números do endereço IP: OK")
    saida.write("\n\t\"ipValido\": true,")
    escritoIP = 1
  if(len(netMask) != 4):
    print("Erro: Quantidade de números da máscara de rede está errada, o número deve ter exatamente 4 números!\n")
    saida.write("\n\t\"mascaraValida\": false,")
    escritoMask = 1
  else:
    print("Quantidade de números da máscara de rede: OK\n")
    saida.write("\n\t\"mascaraValida\": true,")
    escritoMask = 1
    
  flagIp = 0
  for num in ipAddr:
    if(num > 255 or num < 0):
      print("O número ", num, "do endereço IP não está no intervalo de 0 á 255")
      saida.write("\n\t\"ipValido\": false,")
  
  if(flagIp == 0 and escritoIP == 0):
    print("Endereço IP: OK")
    saida.write("\n\t\"ipValido\": true,")
      
  flag = 0
  for num in netMask:
    if(num > 255 or num < 0):
      print("Erro: O número ", num, "da Máscara de Rede não está no intervalo de 0 á 255")
      saida.write("\n\t\"mascaraValida\": false,")
      flag = 1
  if(flag == 0 and escritoMask == 0):
    print("Máscara de Rede: OK")
    saida.write("\n\t\"mascaraValida\": true,")

  print("\n")

def verificaID(ipAddr, netMask, saida):
  print("Verificando o netID e o hostID, da máscara ...")
  if(ipAddr[0] >= 0 and ipAddr[0] <= 127):
    print("NetID = 8\nHostID = 24")
    saida.write("\n\t\"netID\": 8,")
    saida.write("\n\t\"hostID\": 24,")

  if(ipAddr[0]) >= 128 and int(ipAddr[0] <= 191):
    print("NetID = 16\nHostID = 16")
    saida.write("\n\t\"netID\": 16,")
    saida.write("\n\t\"hostID\": 16,")

  if(ipAddr[0]) >= 192 and int(ipAddr[0] <= 223):
    print("NetID = 24\nHostID = 8")
    saida.write("\n\t\"netID\": 24,")
    saida.write("\n\t\"hostID\": 8,")

  if(ipAddr[0] >= 224 and ipAddr[0] <= 239):
    print("Máscara: Endereçamento Multicast")
    saida.write("\n\t\"netID\": '',")
    saida.write("\n\t\"hostID\": '',")

  if(ipAddr[0] >= 240 and ipAddr[0] <= 255):
    print("Máscara: Reservado para futuro uso")
    saida.write("\n\t\"netID\": '',")
    saida.write("\n\t\"hostID\": '',")

  print("\n")

def verificaClasse(ipAddr, netMask, saida):
  if(ipAddr[0] >= 0 and ipAddr[0] <= 127):
    print("Classe do Endereço IP: Classe A")
    saida.write("\n\t\"ipClasse\": \"Classe A\",")
    return[1,7,24]

  if(ipAddr[0] >= 128 and ipAddr[0] <= 191):
    print("Classe do Endereço IP: Classe B")
    saida.write("\n\t\"ipClasse\": \"Classe B\",")
    return[2,14,16]

  if(ipAddr[0] >= 192 and ipAddr[0] <= 223):
    print("Classe do Endereço IP: Classe C")
    saida.write("\n\t\"ipClasse\": \"Classe C\",")
    return[3,21,8]

  if(ipAddr[0] >= 224 and ipAddr[0] <= 239):
    print("Classe do Endereço IP: Classe D")
    saida.write("\n\t\"ipClasse\": \"Classe D\",")
    return[4,28]
  if(ipAddr[0] >= 240 and ipAddr[0] <= 255):
    print("Classe do Endereço IP: Classe E")
    saida.write("\n\t\"ipClasse\": \"Classe E\",")
    return[4,28]
  print("\n")

def ipDaRede(ipAddr, netMask, saida):
  ipRede = []
  for i in range(4):
    ipRede.append(ipAddr[i] & netMask[i])
  print("IP da Rede:", ipRede[0],'.',ipRede[1],'.',ipRede[2],'.',ipRede[3])
  saida.write("\n\t\"ipRede\": \""+ str(ipRede[0])+"."+str(ipRede[1])+"."+str(ipRede[2])+"."+str(ipRede[3])+"\",")
  return ipRede

def ipBroadcast(ipAddr, netMask, saida):
  ipBroad = []
  for i in range(4):
    ipBroad.append(ipAddr[i] | (0b11111111-netMask[i]))
  saida.write("\n\t\"ipBroadcast\": \""+ str(ipBroad[0])+"."+str(ipBroad[1])+"."+str(ipBroad[2])+"."+str(ipBroad[3])+"\",")
  return ipBroad

def qtdHosts(netMask, saida):
  for i in range(4):
    netMask[i] = format(netMask[i], '08b')
    netMask[i] = list(netMask[i])

  somaBit = 0
  for i in range(4):
    for j in range(8):
      if(netMask[i][j] == '1'):
        somaBit+=1

  if(somaBit < 31):
    print("Quantidade máxima de hosts na rede:",str(pow(2, 32-somaBit)-2))
    saida.write("\n\t\"qtdHosts\": "+str(pow(2, 32-somaBit)-2)+",")
  else:
    saida.write("\n\t\"qtdHosts\": 1,")
    

def faixaValida(ipRede, ipBroad, saida):
  ipRede[3] = ipRede[3]+1
  ipBroad[3] = ipBroad[3]-1
  print("A faixa de IPs válidos é de", ipRede,"até",ipBroad)
  saida.write("\n\t\"menorIp\":\""+str(ipRede)+"\",")
  saida.write("\n\t\"maiorIp\":\""+str(ipBroad)+"\",")

def ipReservado(ipAddr, classe, saida):
  contNetID_um = 0
  contHostID_um = 0
  contNetID_zero = 0
  contHostID_zero = 0
  listaSimples = []
  backup = ipAddr.copy()

  if(len(classe) != 2):
    for i in range(4):
      ipAddr[i] = format(ipAddr[i], '08b')
      ipAddr[i] = list(ipAddr[i])

    for i in range(4):
      for j in range(8):
        listaSimples.append(ipAddr[i][j])
    

    for i in range(classe[0]+1,classe[1]+classe[0]):
      if(listaSimples[i] == '1'):
        contNetID_um+=1
      else:
        contNetID_zero+=1
    print("\n")

    for i in range(32-classe[2],len(listaSimples)):
      if(listaSimples[i] == '1'):
        contHostID_um+=1
      else:
        contHostID_zero+=1

    if(backup == [0,0,0,0]):
      print("IP reservado: Endereço de origem inicial")
      saida.write("\n\t\"ipReservado\": true")
    elif(backup == [1,1,1,1]):
      print("IP reservado: Broadcast limitado (rede local)")
      saida.write("\n\t\"ipReservado\": true")
    elif(contHostID_um == classe[2] and contNetID_um == classe[1]):
      print("IP reservado: Broadcast direcionado para a rede")
      saida.write("\n\t\"ipReservado\": true")
    elif(contHostID_zero == classe[2] and contNetID_zero == classe[1]):
      print("IP reservado: Endereço de rede")
      saida.write("\n\t\"ipReservado\": true")
    elif(backup[0] == 127):
      print("IP reservado: endereço de loopback")
      saida.write("\n\t\"ipReservado\": true")
    else:
      print("Este IP não está reservado.")
      saida.write("\n\t\"ipReservado\": false")
    