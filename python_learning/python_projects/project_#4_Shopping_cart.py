class Store:
    def __init__(self):
        self.stock = {}
    
    def add_to_stock(self, P_name, product):
        self.stock[P_name] = product

    def stock_details(self):
        if not self.stock:
            print("Stock is empty")
        else:
            for key, values in self.stock.items():
                print(key ,":", values)
                
    def get_stock_info(self,p_name, quantity):
        if p_name in self.stock and self.stock[p_name]["Quantity"] >= quantity:
            return True
        else:
            return False
    def get_cost(self, p_name, quantity):
        cost_per = self.stock[p_name]["Per"]
        cost = (quantity/cost_per) * self.stock[p_name]["Cost"]
        return cost
class cart:
    def __init__(self):
        self.cart = {}
    
    def add_to_cart(self,obj, P_Name, quntity):
        if obj.get_stock_info(P_Name, quntity):
            obj.stock[P_Name]["Quantity"] -= quntity
            self.cart[P_Name] = quntity
            print(f"{P_Name} added to cart")
        else:
            print(f"Not enough {P_Name} in stock")
    def remove_from_cart(self,P_Name):
        if P_Name in self.cart:
            del self.cart[P_Name]
        else:
            print("Item not found in cart")

    def get_bill(self):
        Total = 0
        for key, value in self.cart.items():
            cost = s.get_cost(key, value)
            Total += cost
        print(f"Your total bill is {Total}")
    

class customer:
    def __init__(self, C_ID):
        self.C_ID = C_ID
        self.my_cart = cart()
        

    def shoping(self, obj, product, Quantity):
        self.my_cart.add_to_cart(obj, product, Quantity)

    def get_bill(self):
        self.my_cart.get_bill()


s = Store()
s.add_to_stock("Egg", {"P_ID":"E1", "Cost":6, "Per":1, "Quantity":30})
# p.stock_details()
# c = cart()
# c.add_to_cart(p, "Egg", 2)
# p.stock_details()
# print(c.get_bill())
cos1 = customer("cos_1")
cos1.shoping(s, "Egg", 8)
cos1.get_bill()

cos2 = customer("cos_2")
cos2.shoping(s, "Egg", 10)
cos2.get_bill()
cos1.get_bill()

while True:
    print("+++++ Welcome to our shopping mall")
    
    print("1.Go to shoping")
    print("2.stock details")
    print("3.cart details")
    print("4.To get bill")
    print("5.Exit")

    choice = int(input("Enter your choice(1 to 5) : "))
    if choice == 1:
        name = input("Please enetr customer name :")
        C_ID = input("Please enetr customer ID :")
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        break
    else:
        print("Invalid choice!")


