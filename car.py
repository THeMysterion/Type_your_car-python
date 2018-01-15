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
        return self.__car_name
    
    def get_color(self):
        return self.__color
    
    def get_cost(self):
        return self.__cost
    
def main():

    name = raw_input('Car name: ')
    color = raw_input('Car color: ')
    cost = raw_input('Car cost: ')

    mycar = Car(name, color, cost)
	
    print('You car is: {}, color: {}, cost: {}'.format(mycar.get_name(), mycar.get_color(), mycar.get_cost()))
    
main()
