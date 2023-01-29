class Bulbs:    
    def __init__(self):
        self.state=False
    def on(self):
        self.state=True
    def off(self):
        self.state=False

class Red(Bulbs):    
    def __init__(self):
        super().__init__()

class Green(Bulbs):    
    def __init__(self):
        super().__init__()

class Yellow(Bulbs):    
    def __init__(self):
        super().__init__()
    

class TrafficLight:
    def __init__(self):
        self.color='red-green'
        self.red=Red()
        self.red.on()
        self.green=Green()
        self.green.on()
        self.yellow=Yellow()

    def check_state(self):
        return f"Red: {self.red.state} Green: {self.green.state} Yellow: {self.yellow.state}"
        
    def set_state(self,changeTo):
        transitions = self.color + ' to ' + changeTo        
        if transitions in ['red to green','green to yellow','yellow to red','red-green to red']:
            self.color=changeTo
            self.red.off()
            self.green.off()
            self.yellow.off()
            exec(f"self.{changeTo}.on()")
            return True

        elif changeTo =='red-green':
            self.color=changeTo
            self.red.on()
            self.green.on()
            self.yellow.off()
            return True

        else:
            print("Transition is invalid")
            return False
    

DanStr=TrafficLight()
print(DanStr.check_state())
DanStr.set_state('red')
print(DanStr.check_state())
DanStr.set_state('green')
print(DanStr.check_state())
DanStr.set_state('yellow')
print(DanStr.check_state())
DanStr.set_state('red-green')
print(DanStr.check_state())