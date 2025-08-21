from datetime import date
def add_item():
    it = item(input("Enter item name: "))
    items.append(it.name)
def show_items():
    if len(items) == 0:
        print("No items in the inventory.")
    else:
        print(items)
class store:
    def __init__(self,name):
        self.name="Sathwik Kirana Store"
class item:
    def __init__(self,name):
        self.name=name
        self.quantity=0
    def add_stock(self, quantity):
        self.quantity=self.quantity+quantity
    def remove_stock(self, qty):
        self.quantity=self.quantity-qty
        if self.quantity <10:
            print("Refill the stock soon for", self.name)
    def sell_item(self, qty, cust_ph_no):
        self.remove_stock(qty)
        sales[cust_ph_no]=qty
    def spoiled_item(self,qty):
        self.remove_stock(qty)
        d=date.today()
        spoiled_items[d]=qty
items=[]
sales={}
spoiled_items={}
k=1
while k:
    print("Stock management system:\n1. Show items: 1\n2. Add item: 2\n3. Add stock: 3\n4. Sell items: 4\n5. Throw spoiled items: 5\n6. Show sales: 6\n7. Show spoiled items: 7\n8. Exit: 8")
    n=int(input())
    match n:
        case 1:
            show_items()
        case 2:
            add_item()
        case 3:
            n=input("enter the item name to add to stock:")
            if n in items:
                p=items.index(n)
                items[p].add_stock(int(input("Enter quantity to add: ")))
        case 4:
            n=input("enter the item name to add to sell:")
            if n in items:
                n.sell_item(int(input("Enter quantity to sell: ")), input("Enter customer phone number: "))
        case 5:
            n=input("enter the item name to add to sell:")
            if n in items:
                n.spoiled_item(int(input("Enter quantity to throw: ")))
        case 6:
            print(sales)
        case 7:
            print(spoiled_items)
        case 8:
            k=0
            print("exiting system")
            
