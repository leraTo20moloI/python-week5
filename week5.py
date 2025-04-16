#Defining the class

class iphone:
    def_init_(self,model,storage,battery):
    self.__model = model 
    self.__storage = Storage
    self.__battery = Battery
    self.__is_on = False
        
    def power_on(self):
            if not self.__is_on:
                self.__is_on =True
                print(f"{self.__model} is now ON.")
            else:
                print(f"{self.__model} is already ON.")
                
                def power_off(self):
                    If self.__is_on:
                    self.__is_on =False
                    print(f"{self.__model} is OFF.")
            else:
            print(f"{self.__model} is already OFF.")
                
            def check_battery(self):
                    print(f"{self.__model} has {self.__battery}mAh battery remaining.")
                    
                    def get_specs(self):
                        return f"iPhone {self.__model} - {self.__storage}GB Storage, {self.__battery}mAh Battery"


# Activity 2
 
 # Base class
class Vehicle:
    def move(self):
        pass
    
    # Subclasses
    class Car(Vehicle):
        def move(self):
            print("Driving")
            
            class Plane(Vehicle):
                def move(self):
                    print("Flying")
                    
                    class Boat(Vehicle):
                        def move(self):
                            print("Sailing")
                            
                            class Bike(Vehicle):
                                def move(self):
                                    print("Pedaling")
                                    
                                    # CREATE instances and call move()
                                    def main():
                                        vehicles = [
                                            
                                            Car(),
                                            Plane(),
                                            Boat(),
                                            Bike()
                                        ]
                                        
                                        for vehicle in vehicles:
                                            vehicle.move()
                                            
                                            if _name__ == "__main__":
                                                main()
