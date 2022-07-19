num=int(input("Введіть число"))
def oddOrEven(num):
    x=num%2
    if x == 0:
        print('число', num, 'парне')
    else:
        print('число', num, 'не парне')
oddOrEven(num)