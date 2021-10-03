if __name__ == '__main__':
    pokemon =('picachu', 'charmander', 'bulbasaur')

    print(pokemon[1])

    starter1 = pokemon[0]
    starter2 = pokemon[1]
    starter3 = pokemon[2]

#Is i in my name
    my_name = tuple('Brendan')
    'i' in my_name

#counting
    for N in range(2,11):
        print(N)

#counting up 
    M = 2
    B = 11
    while M < B:
        print(M)
        M += 1

#string print

    starter_string = 'This is a simple string'
    for x in starter_string:
        print(x)

#nesseded loop
    nested_loopset = ('this', 'is', 'a', 'simple', 'set')
    i = 0
    while i < len(nested_loopset):
        print(nested_loopset[i] *3)
        i += 1 