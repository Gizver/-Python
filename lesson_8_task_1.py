# На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?

n = int(input('Сколько встретилось друзей: '))
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        b.append(int(j>i))
    a.append(b)
summ=0
for el in a:
    summ+=sum(el)
print(f'Было сделано {summ} рукопожатий')