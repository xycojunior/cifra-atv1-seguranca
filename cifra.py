palavra = input("Digite a palavra para ser criptografada: ").upper()
chave = input("Digite sua chave: ").upper()

key = chave
tamanho_palavra = len(palavra)

while tamanho_palavra/len(key) > 1:
    key+=chave
key = key[:tamanho_palavra]
codificada = ''

for i in range(tamanho_palavra):
    codificada+=chr(65+(ord(palavra[i])+ord(key[i]))%26)
print("A palavra codificada é: "+codificada)



palavra = input("Digite a palavra para ser decriptografada: ").upper()
chave = input("Digite sua chave: ").upper()

key = chave
tamanho_palavra = len(palavra)

while tamanho_palavra/len(key) > 1:
    key+=chave
key = key[:tamanho_palavra]

decodificada = ''

for i in range(tamanho_palavra):
    decodificada+=chr(65+(ord(palavra[i])-ord(key[i]))%26)
print("A palavra codificada é: "+decodificada)