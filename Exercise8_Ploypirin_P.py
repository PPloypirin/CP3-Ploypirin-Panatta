U = input("Username : ")
P = input("Password : ")
if U == "Funny" and P == "F3432":
	print("Welcome to Everthing Jingabell Shop\n" +'\t\t\t\t🥰💕☺️')
	print('---- Top 5 Best seller product ----')
	print('EJMB01: Mouse Bluetooth      750 THB')
	print('EJMP02: Mouse Pad            330 THB')
	print('EJKB03: Keyboard Bluetooth 1,200 THB')
	print('EJSI04: Stylus for ipad      950 THB')
	print('EJCI05: Case Ipad Pro11    2,190 THB')
	print('-----------------------------------')
	EJMB01 = 750
	EJMP02 = 330
	EJKB03 = 1200
	EJSI04 = 950
	EJCI05 = 2190
	SelectProduct = input('Your items : ')
	QuantityProduct = int(input('Quantity   : '))
	if SelectProduct == 'Mouse Pad':
		print('--------- Total Your Order --------')
		print(SelectProduct,'x',QuantityProduct,'Qty. =', QuantityProduct*EJMP02,'\t\tTHB')
		vat = 7
		print('Vat 7%             =',(QuantityProduct*EJMP02)*(vat/100),'\t\tTHB')
		print('Grand Total        =',(QuantityProduct*EJMP02)+(QuantityProduct*EJMP02)*(vat/100), '\tTHB')
	elif SelectProduct == 'Mouse Bluetooth':
		print('--------- Total Your Order --------')
		print(SelectProduct,'x',QuantityProduct,'Qty. =', QuantityProduct*EJMB01,'THB')
		vat = 7
		print('Vat 7% =',(QuantityProduct*EJMB01)*(vat/100),'THB')
		print('Grand Total =',(QuantityProduct*EJMB01)+(QuantityProduct*EJMB01)*(vat/100), 'THB')
	elif SelectProduct == 'Keyboard Bluetooth':
		print('--------- Total Your Order --------')
		print(SelectProduct,'x',QuantityProduct,'Qty. =', QuantityProduct*EJKB03,'THB')
		vat = 7
		print('Vat 7% =',(QuantityProduct*EJKB03)*(vat/100),'THB')
		print('Grand Total =',(QuantityProduct*EJKB03)+(QuantityProduct*EJKB03)*(vat/100), 'THB')
	elif SelectProduct == 'Stylus for ipad':
		print('--------- Total Your Order --------')
		print(SelectProduct,'x',QuantityProduct,'Qty.=', QuantityProduct*EJSI04,'THB')
		vat = 7
		print('Vat 7%                  =',(QuantityProduct*EJSI04)*(vat/100),'THB')
		print('Grand Total             =',(QuantityProduct*EJSI04)+(QuantityProduct*EJSI04)*(vat/100), 'THB')
	else:
		print('--------- Total Your Order --------')
		print(SelectProduct,'x',QuantityProduct,'Qty.=', QuantityProduct*EJSI04,'THB')
		vat = 7
		print('Vat 7%                  =',(QuantityProduct*EJCI05)*(vat/100),'THB')
		print('Grand Total             =',(QuantityProduct*EJCI05)+(QuantityProduct*EJCI05)*(vat/100), 'THB')
	print('--------- 😊 Thank you 😊 --------')
else:
	print("Login error")

