MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

        
def all_setting(choice):   
    global resources
    if resources['water']>=MENU[choice]['ingredients']['water']:       
         resources['water']-=MENU[choice]['ingredients']['water']
    else:
        return ( "Not enough water")
    if choice != 'espresso' and resources['milk']>=MENU[choice]['ingredients']['milk']:  
        resources['milk']-=MENU[choice]['ingredients']['milk']
    elif choice!='espresso':
        return ( "Not enough milk")
    if resources['coffee']>=MENU[choice]['ingredients']['coffee']:  
       resources['coffee']-=MENU[choice]['ingredients']['coffee']
    else:
         return ("Not enough coffee")
    return 1
def money_taking(choice):
    global profit
    print("Please insert coins")
    quarters=int(input("How many quarters : "))*0.25
    dimes=int(input("How many dimes : "))*0.1
    nickles=int(input("How many nickles : "))*0.05
    pennies=int(input("How many pennies : "))*0.01
    coins=quarters+dimes+nickles+pennies
    
    if(coins>=MENU[choice]['cost']):
        profit+=MENU[choice]['cost'] 
        print(f"Here is ${round(coins-MENU[choice]['cost'],2)} in change.")
        print(f"Here is your {choice} ☕.Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")
  
  
def coffee_game(): 
    global profit
    k=True
    while k:
        choice=input("what would you like ? ('espresso', 'latte','cappuccino':" )
        if choice=='off':
            k=False
        elif choice=='report':
            for i in resources:
                print(i, ":" ,resources[i])
            print(f"Money : ${profit}")
        elif choice in  ['espresso','latte','cappuccino']:
            result=all_setting(choice)
            if result ==1:
                  money_taking(choice)
            else:
                print(result)
        else:
            print("Please enter correct input.")
coffee_game()        
         
         