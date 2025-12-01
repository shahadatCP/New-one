class Calculator:
    brand = 'CasioMS990'
    features = ['adding','subtracking','multiplying','dividing']


    def sum(self, num1, num2):
        ans = num1 + num2
        return ans
    
    def sub(self, num1, num2):
        ans = num1 - num2
        return ans
    
    def mult(sel, num1, num2):
        ans = num1 * num2
        return ans
    
    def div(self, num1, num2):
        ans = num1/num2
        return ans
    

print(Calculator().sum(12,10)) #we can directly use the class for print
my_calculator = Calculator()
print(my_calculator.sum(20,17))
print(my_calculator.sub(12,10))
print(my_calculator.mult(12,10))
print(my_calculator.div(120, 12))