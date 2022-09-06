from datetime import datetime
anonasc = int(input('digite o ano do nascimento' ))
mesnasc = int(input('digite o mÊs do nascimento' ))
dianasc = int(input('digite o dia do nascimento' ))
nome = input('digite o nome do cliente ')
datanasc = datetime(anonasc, mesnasc, dianasc)
dataatual = datetime.now()
idadecliente = dataatual - datanasc

dias = idadecliente.days
anos, dias = dias // 365, dias % 365
meses, dias = dias // 30, dias % 30
endereço = input('digite o endereço ')
fone = input('digite o telefone ')

print('cliente:{}\nidade do cliente: {} anos,{} meses e {} dias\nEndereço: {}\nFone:'.format(nome, anos, meses, dias, endereço, fone))