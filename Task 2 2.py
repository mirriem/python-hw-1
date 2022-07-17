a=input('Введіть рядок  ')
b=a[0:5]
print(b,"...")
a1=a.capitalize()
a2=a.lower()
if a[0]=='L':
    print(a2)
else:
    if a[0]=='l':
        print(a1)
    else:
        if a[0]=='U':
            print(a2)
        else:
            if a[0]=='u':
                print(a1)
            