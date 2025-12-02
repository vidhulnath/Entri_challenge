## print the prime numbers from a range of number from the given input
while True:
    
    n1= input('Enter The First Number\t: ')
    if n1.lower()== 'q':
         break
    n1 = int(n1)
    n2= int(input('Enter The Second Number\t: '))

    p = []



    if n1 < 2:
        print('First number should be greater than 1\n')
    elif n1 > n2:
        print('Second number should be greater than Fisrt number\n')
    else:
        for i in range(n1,n2+1):
            for j in range(2,int(i ** 0.5)+1):
                if i%j == 0:
                    break
            else:
                p.append(i)
        if len(p)>0:

            print(f'Prime Numbers Between {n1} and {n2} are {p}')
            print(f'There are {len(p)} prime numbers between {n1} and {n2}.\n')
        else:
            print('There is No prime Numbers in the Given Range.\n')
    print('Enter q to exit.\n')