class Cart():
    def __init__ (self, contents=[]):
        self.contents= contents
    
    def thanksForShopping(self):
            '''Thanks user for shopping and prints order'''
            print('Thank you for shopping with us, you have ordered:')
            compiled_cart={}
            for content in self.contents:
                if content in compiled_cart.keys():
                    continue
                else:
                    item_count= self.contents.count(content)
                    compiled_cart[content]=item_count
            for key,value in compiled_cart.items():
                print(f"{key.title()} : {value}")

    def showContents(self):
        '''shows user contents of cart'''
        print('You have this in your cart:')
        compiled_cart={}
        for content in self.contents:
            if content in compiled_cart.keys():
                    continue
            else:
                item_count= self.contents.count(content)
                compiled_cart[content]=item_count
        for key,value in compiled_cart.items():
            print(f"{key.title()} : {value}")
    
    def addToCart(self):
        '''adds items to cart'''
        add_item= input("What would you like to add?")
        amount= input("How many would you like?")
        while self.contents.count(add_item.lower())<int(amount):
            self.contents.append(add_item.lower())

    def removeFromCart(self):
        '''removes items from cart'''
        del_item= input("What would you like to delete?")
        amount= input("How many would you like, total?")
        while self.contents.count(del_item.lower())>int(amount):
            self.contents.remove(del_item.lower())

        

my_cart= Cart()

def run_cart():
    shopping= True
    while shopping==True:
        response= input("What would you like to do? 'see cart','add to cart', 'remove from cart', or 'quit'?")
        if response== 'see cart':
            my_cart.showContents()
        elif response== 'add to cart':
            my_cart.addToCart()
        elif response== 'remove from cart':
            my_cart.removeFromCart()
        elif response== 'quit':
            my_cart.thanksForShopping()
            shopping= False
        else:
            print("Invalid input, please try again.")

run_cart()
