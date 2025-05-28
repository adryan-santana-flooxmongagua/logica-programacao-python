frase = 'aaaaoootesadrtgfhjykugftdrctycufikblnkatuwfevdukylhijkqw'

i = 0
qtap = 0
letap = ''

while i < len(frase):
    leatt = frase[i]

    if leatt == ' ':
        i += 1
        continue

    qttadt = frase.count(leatt)

    if qtap <= qttadt:
        qtap = qttadt
        letap = leatt

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letap}" que apareceu '
    f'{qtap}x'
)
