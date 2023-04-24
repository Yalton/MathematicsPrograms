class cubans: 
    length = None
    weight = None 

    def __init__(self):
         self.length = 0.175 # Length stored as Km
         self.weight = 75 # Weight stored as Kg
        
    def convert(self, amount, desiredConversion):
        if(desiredConversion == 1): 
            converted_amount = amount / self.length
        elif(desiredConversion == 2): 
            converted_amount = amount / self.weight
        return converted_amount
    
if __name__ == "__main__":
    calc = cubans()
    print(f"  ____      _                    ____      _            _       _                  \n  / ___|   _| |__   __ _ _ __    / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __      \n | |  | | | | '_ \ / _` | '_ \  | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|     \n | |__| |_| | |_) | (_| | | | | | |__| (_| | | (__| |_| | | (_| | || (_) | |        \n  \____\__,_|_.__/ \__,_|_| |_|  \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|        \n                                                                             ")
    desiredConversion = int(input("Please selected desired conversion\n\t1: Length\n\t2: Weight:\n\t->"))
    if(desiredConversion == 1): 
        amount = float(input("Please enter the length (in Km) that you would like converted to cubans\n\t ->"))
    elif(desiredConversion == 2): 
        amount = amount = float(input("Please enter the weight (in Kg) that you would like converted to cubans\n\t ->"))
    
    print("Value in cubans is", calc.convert(amount, desiredConversion), "cubans")