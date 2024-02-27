from datetime import datetime
Username = input('Enter your name :')
phonenumber = input("Enter your mobile number : ")

itemlist = '''
===================================================
list of groceries with their prices in Rs/quantity:
===================================================
1.Rice (1 kg)                  - Rs 60
2.Wheat Flour (1 kg)           - Rs 40
3.Sugar (1 kg)                 - Rs 45
4.Sunflower Oil (1 liter)      - Rs 120
5.Milk (1 liter)               - Rs 60
6.Eggs (dozen)                 - Rs 80
7.Bread (loaf)                 - Rs 30
8.Coffee Powder (250g)         - Rs 100
----------------------------------------------------
'''
print(itemlist)

# Declaration
price = 0
pricelist = []
totalprice = 0
Finalprice = 0
ilist = []
qlist = []
plist = []

items = {'rice': 60,'wheat flour': 40,'sugar': 45,'sunflower oil': 120,'milk': 60,
         'eggs': 80,'bread': 30,'coffee powder': 100}


while True:
    item = input("Enter 1 to add items (enter done to finish shopping) : ").lower()
    if item == "done":
        print("Thank You For Shopping")
        break
    if item in items:
        quantity = int(input(f"Enter quantity of {item}: "))
        price = quantity * items[item]
        pricelist.append((item, quantity, items[item], price))
        totalprice += price
        ilist.append(item)
        qlist.append(quantity)
        plist.append(price)            
    else:
        print("Selected item is not available. Sorry for the inconvenience.")  
if totalprice > 0:
            tax = (totalprice * 12) / 100
            finalamount = tax + totalprice

            print(25 * "=", "Supermarket", 25 * "=")
            print(15 * " ", "Address : Machilipatname,krishna,AP")
            print(63*"=")
            print("Date:", datetime.now())
            print("Name :", Username)
            print("Mobile No :",phonenumber)
            print(75 * "-")
            print("sno", 10 * " ", 'items', 8 * " ", 'quantity', 8 * " ", 'price')
            for i in range(len(pricelist)):
                print(i, 6 * ' ', 5 * ' ', ilist[i], 12 * ' ', qlist[i], 12 * " ", plist[i])
            print(75 * "-")
            print(50 * " ", 'Total amount:', 'Rs', totalprice)
            print(50 * " ", "Tax amount:", 3*"",'Rs', tax)
            print(75 * "-")
            print(50 * " ", 'Final amount:', 'Rs', finalamount)
            print(75 * "-")
            print(20 * " ", "Thank you & Visit again")
            print(75 * "-")
          

           
       
