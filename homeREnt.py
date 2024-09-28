rent=int(input("Enter your hostel rent="))
food =int(input("Enter the amount of food ordered="))
electricity_spend =int(input("Enter the total of electricity  spend ="))
charge_per_unit =int(input("enter the charge per unit="))
person =int(input("Enter the  number of person living in room and flat"))
total_bill = electricity_spend * charge_per_unit
output = (food + rent + total_bill) //person 
print ("Each person will pay =", output)
