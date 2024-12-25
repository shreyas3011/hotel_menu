#define the menu of restrorent

menu={ "burger":50,
      "pizza":100,
      "coffie":50,
      "sandwitch":80,
      "nuddles":100

}
print("welcome to python restro")
print("MENU :\nburger:50$\npizza;100$\ncoffie:50$\nsandwitch:80$\nnuddles:100$")


total_order=0

item_1=input("enter the name of item you want to eat=")
if item_1 in menu:
    total_order+=menu[item_1]
    print(f"your {item_1} is added to your order")

else:
    print(f"your ordered {item_1} is not avialble")


another_order=input("do you want to add another item?(yes/no)")
if another_order=="yes":
    item_2=input("enter the name ofsecond order =")
    if item_2 in menu:
        total_order+=menu[item_2]
        print(f"your {item_2} added to order")
    else:
        print(f"your {item_2} is not avialble")

another_order=input("do you want add another order? (yes/no)")
if another_order=="yes":
    item_3=input("enter the name of 3rd order =")
    if item_3 in menu :
        total_order+=menu[item_3]
        print(f"your {item_3} is added to order")

    else:
        print("your order {item_3} is not avilable")



print(f"your total bill is : {total_order}")
    