    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    output = ''
    print('[', end='')
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    output += '[{0}, {1}, {2}], '.format(i,j,k)
    output = output.rstrip(' ,')+']'
    print(output)
