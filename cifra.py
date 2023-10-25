#A cifra de Vigenère é um método de encriptação que usa um série de diferentes cifras de César baseadas em letras de uma senha

#Para fazer uso da cifra de Vigenère , devemos usar uma tabela de alfabetos.Essa tabela consiste no alfabeto escrito 26 vezes em diferentes linhas, cada um deslocado ciclicamente do anterior por uma posição. As 26 linhas correspondem às 26 possíveis cifras de César.

#EX: 
#Frase : 'Michael Jackson não morreu' --> upper()
#Chave : 'dahora' --> upper()


palavra_c_esp = input("Digite a palavra para ser criptografada: ").upper().split()
palavra = ''
for item in palavra_c_esp:
    palavra+=item
chave = input("Digite sua chave: ").upper()

key = chave
tamanho_palavra = len(palavra)

# Aqui e gero a chave da forma correta, de maneira que fique igual a 'dahoradahoradahoradahor', ou seja, com a mesma quantidade de caracteres que a frase inserida (Tirando os espaços)
while tamanho_palavra/len(key) > 1:
    key+=chave
key = key[:tamanho_palavra]
codificada = ''

# Gerando a palavra codificada, de acordo com o tamanho da palavra
# Pega o mod do índice de (ord(palavra[i])+ord(key[i]))
# Adiciona esse valor a 65 (Pois é onde começa o alfabeto em maiúsculo) para pegar o caracter que corresponde ao valor e concatenando à frase codificada
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

# No código de decodificação, basta, ao invés de usar ord(palavra[i])+ord(key[i]), usa ord(palavra[i])-ord(key[i])
for i in range(tamanho_palavra):
    decodificada+=chr(65+(ord(palavra[i])-ord(key[i]))%26)
print("A palavra codificada é: "+decodificada)