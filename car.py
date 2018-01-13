class Car:
    def __init__(self, name, color, cost):
        self.__car_name = name
        self.__color = color
        self.__cost = cost
        
    ###
    
    def set_name(self, name):
        self.__name = name
        
    def set_color(self, color):
        self.__color = color
        
    def set_cost(self, color):
        self.__color = color
        
    ###
    
    def get_name(self):
        return self.__name
    
    def get_color(self):
        return self.__color
    
    def get_cost(self):
        return self.__cost
    
def main():

    name = input('Car name: ')
    color = input('Car color: ')
    cost = input('Car cost: ')

    mycar = car(name, color, speed)
    
main()