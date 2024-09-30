print ("Hello World")
print(round(38/6.9,3))

email_cliente = input('email:')
verifica_1 = email_cliente.find('@')
verifica_2 = email_cliente.find ('gmail')
verifica_3 = email_cliente.find ('hotmail')
verifica_4 = email_cliente.find ('.')

if verifica_1 > 0 and verifica_2 > 0 and verifica_4 >0 or verifica_1 > 0 and verifica_3 > 0 and verifica_4 > 0 :
    print ("Email Válido")

else :
    print ('Email não Válido')


drinks = ['coffee','tea', ' orange juice','soda']
dinner = ['Pizza','Hamburger','Hotdog','pudding','spaghetti']
dessert =["Ice cream", "cake"]

food = [drinks,dinner,dessert] 
drinks.pop(2)
print (drinks)
print(f"I would like {drinks[2]} for drink,{dinner[3]} to eat and {dessert[0]} like dessert")

 