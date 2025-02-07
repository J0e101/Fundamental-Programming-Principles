#A simple calculator program *(+,-,*,/) only

fig1 = int(input("Enter first figure: "))
oper = input("Enter second figure: ")
fig2 = int(input("Enter operand(+,-,/,*): "))

if oper == "+" :
    print(fig1 + fig2)
    print("Goodbye")
elif oper == "-" :
    print(fig1 - fig2)
    print("Goodbye")
elif oper == "/" :
    print(fig1, fig2)
    print("Goodbye")
else :
    print(fig1 * fig2)
    print("Goodbye")





