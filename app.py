import re
# DESAFIO 1
# Encontre a palavra simples
# Olá! sou uma frase simples
'''desafio1 = 'Olá! sou uma frase simples'
padrao = r'\bsimples\b'
result = re.findall(padrao, desafio1)
print(result)

#DESAFIO 2 
# Encontre todas as ocorrência de 23(os números juntos) e exatamente com esses valores
'''
'''dev123com
developer 123
dev = 123
dev = 1234
dev = 1337
dev = 9000'''

''''''
desafio2 = [
    'dev123com',
    'developer 123',
    'dev = 123',
    'dev = 1234',
    'dev = 1337',
    'dev = 9000'
]

padrao = r'23'

result = [texto for texto in desafio2 if re.search(padrao, texto)]

print(result)

# DESAFIO 3
'''
Encontre todos os valores onde o valor inicial é 2, porém o segundo valor você não conhece: ex: 23, 24,21, 26 etc..
dev123com
developer 123
dev = 123
dev = 1234
dev = 1337
dev = 9000
'''
desafio3 = [
    'dev123com',
    'developer 123',
    'dev = 123',
    'dev = 1234',
    'dev = 1337',
    'dev = 9000'
]

padrao = r'2\d'

result = [texto for texto in desafio3 if re.search(padrao, texto)]

print(result)

# DESAFIO 4
'''
Usando os cvalores a seguir, encontre os seguintes números por completo, usando regex
13.35.86
22.36.77
53.12.34
'''
desafio4 = [
    'dev123com',
    'developer 123',
    '13.35.86',
    '22.36.77',
    'dev = 123',
    'dev = 1234',
    'dev = 1337',
    '53.12.34',
    'dev = 9000',
]

padrao = r'\d\d\.\d\d\.\d\d'
result = [texto for texto in desafio4 if re.search(padrao, texto)]
print(result)

# DESAFIO 5
'''
Crie um regex para encontrar o seguinte padrão: Encontre apenas as combinações segundo o descrito abaixo
bah pular
tah encontrar
jah encontrar
nah encontrar
uai pular
'''
desafio5 = [
    'bah',
    'tah',
    'jah',
    'nah',
    'uai',
]

padrao = r'[tjn]ah'
result = [texto for texto in desafio5 if re.search(padrao, texto)]
print(result)

# DESAFIO 6
'''
Encontre a combinação de acordo com o descrito abaixo:
(123)1234-1235 encontrar
(123)1234-1235 encontrar
(129)1234-1235 pular
(129)1234-1235 pular
'''
desafio6 = [
    '(123)1234-1235',
    '(123)1234-1235',
    '(129)1234-1235',
    '(129)1234-1235',
]
padrao = r'[(]\d\d[3][)]\d\d\d\d[-]\d\d\d\d'
result = [texto for texto in desafio6 if re.search(padrao, texto)]
print(result)

# DESAFIO 7
'''
Usando regex, encontre apenas a sequência 1234 abaixo
1234 encontrar
6462 pular
Essa expressão r'[1-4]' não retornou somente a segquencia 1 a 4 retorou o 6462
então utilizei padrao = r'1234'
'''
desafio7 = [
    '1234',
    '6569',
    '6462'
]
padrao = r'1234'
result = [texto for texto in desafio7 if re.search(padrao, texto)]
print(result)

'''# DESAFIO 8 
# Usando regex, encontre apenas as letras iniciandos de p a v
'''
'''pqrstuv encontrar
wxyz pular
abcdefg pula'''

desafio8 = 'pqrstuv wxyz abcdefg'
padrao = r'[p-vP-V]\w+'
# Este padrão corresponde a uma letra que começa com 'p' a 'v' (maiúscula ou minúscula)
# seguida por zero ou mais caracteres de palavra (\w+).
result = re.findall(padrao, desafio8)
print(result)

# DESAFIO 9
''''
Crie um regex para encontrar tanto pizzas enviadas como pizza enviada
2 pizzas enviadas

1 pizza enviada

3 pizzas enviadas
'''
desafio9 = [
    "2 pizzas enviadas",
    "1 pizza enviada",
    "3 pizzas enviadas"
]

padrao = r'\b[pP]izza[s]?\b'

result = [texto for texto in desafio9 if re.search(padrao, texto)]

print(result)
