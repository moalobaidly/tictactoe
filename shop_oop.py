"""its a class"""
class Item:
    sale = 0.8
    all = []
    """class representing item in a shop"""
    def __init__(self,name : str,price : float,quantity = 0):
        print(f"created {name}")
        self.name = name
        self.price = price
        self.quantity = quantity
        #actions
        Item.all.append(self)
    def total_amount(self):
        """d"""
        return self.price * self.quantity
    def randomfunc(self,days = 365):
        """"d"""
        return(f"{self.name} has a sale in {days} days")
    def sale_amount(self):
        """"h"""
        return (f"the sale price of {self.name} is {self.price*self.sale}")
    def __repr__(self):
        return (self.name)
        
    
item1 = Item("lattafa asad", 15, 30)
item2 = Item("club de nuit", 30, 10)
item3 = Item("sauvage", 60, 12)
item2.sale = 0.5

print("Welcome to the shop")
print(Item.all)