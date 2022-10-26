name = str(input('Digite um nome de pessoa completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em Maiúsculo: {}'.format(name.upper()))
print('Seu nome em minúsculo: {}'.format(name.lower()))
nameNS = name.split()
nameNSS = ''.join(nameNS)
print('O seu nome sem espaços têm {} letras'.format(len(nameNSS)))
name1 = name.split()
print('O seu primeiro é {}, e têm {} letras'.format(name1[0], len(name1[0])))




