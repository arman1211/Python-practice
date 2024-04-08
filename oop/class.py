class Calculator:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        return None
    def add (self,num1,num2):
        return num1+num2

mycalc = Calculator('casio',991)

print(mycalc.brand,mycalc.model,mycalc.add(23,45))