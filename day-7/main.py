import random

erros = [''' 
      _______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___ ''',
    ''' 
      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___ ''',
    ''' 
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |       
     |
    _|___ ''',
    ''' 
      _______
     |/      |
     |      (_)
     |      \|
     |       |
     |       
     |
    _|___ ''',
        ''' 
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |       
     |
    _|___ ''',
    ''' 
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___ ''',
    ''' 
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___ '''
]

print("Forca")

palavras = ['python','words','random']

palavra = random.choice(palavras)

contagem_acertos = 0
contagem_erros = 0
letras_achadas = ""

# bool para colocar no while em vez disso
while contagem_acertos < len(palavra):

    print(erros[contagem_erros])
    
    if contagem_erros >= 6:
        print("perdeu burro")
        break

    # com lista é mais bonito
    teste = ""
    for p in palavra:
        if p in letras_achadas:
            teste += p
        else:
            teste += "_"

    print(teste)

    escolha = str(input("\nEscolha uma letra: ")).lower()

    if escolha in palavra:
        letras_achadas += escolha
        contagem_acertos += 1
    else:
        contagem_erros += 1

print("\nPalavra certa: "+palavra)
print("Erros: "+ str(contagem_erros))
