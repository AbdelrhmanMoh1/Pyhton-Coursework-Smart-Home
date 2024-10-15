#Task 1
class SmartPlug:
    
    def __init__(self, consumptionRate):
        self.switchedOn = False
        self.consumptionRate = consumptionRate

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn
        
    #retrieve the value of switch status   
    def getSwitchStatus(self):
        return self.switchedOn
    
    #retrieve the value ConsumptionRate 
    def getConsumptionRate(self):
        return self.consumptionRate

    def setConsumptionRate(self, rate):
        if 0 <= rate <= 150:
            self.consumptionRate = rate
        else:
            print("Invalid consumption rate.")
            print("Please provide a value between 0 and 150.")

    def __str__(self):
        if self.switchedOn:
            status = "ON"
        else:
            status = "OFF"
        
        output = f"SmartPlug: switchedOn: {status}  "
        output +=  f", consumptionRate={self.consumptionRate}"
        return output 


def testSmartPlug():
    # Create an instance of SmartPlug with a consumption rate of 45
    plug = SmartPlug(45)

    # Toggle the status of the plug
    plug.toggleSwitch()

    # Print the value of switchedOn
    print("Switched On:", plug.getSwitchStatus())

    # Print the value of consumptionRate, set it to a new valid value, and then print it again
    print("Consumption Rate:", plug.getConsumptionRate())
    plug.setConsumptionRate(50)
    print("New Consumption Rate:", plug.getConsumptionRate())

    print(plug)


#testSmartPlug()

#Task 2
class SmartFridge:
    
    def __init__(self):
        self.switchedOn= False
        self.temperature= 3
        
    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn
        
    def getSwitchStatus(self):
        return self.switchedOn
    
    def getTemperature(self):
        return self.temperature
    
    def setTemperature(self,temp):
        if temp in [1,3,5]:
            self.temperature = temp
        else:
            print("Invalid Temperature")
            
    def __str__(self):
        if self.switchedOn:
            status = "ON"
        else:
            status = "OFF"
        
        output= f"SmartFridge: switchedOn: {status}"
        output+= f", temperature={self.temperature}"
        return output
    

def testSmartFridge():
    fridge = SmartFridge()
    fridge.toggleSwitch()
    
    print("Switch on:", fridge.getSwitchStatus())
    print("Temperature:", fridge.getTemperature())
    
    fridge.setTemperature(5)
    print("New Temperature:", fridge.getTemperature())
    
    print(fridge)

#testSmartFridge()

#Task 3
class SmartHome:
    
    def __init__(self):
        self.device= []
        
    def getDevice(self):
        return self.device
    
    def getAdevice(self,index):
        if 0 <= index <= 3:
            return self.device[index]
        else:
            print("Invalid")
            
    def removeDevice(self,index):
        if 0 <= index <=3:
            del self.device[index]
        else:
            print("Invalid")
            
    
    def addDevice(self,device):
        self.device.append(device)
        
    def toggleSwitch(self,index):
        if 0 <= index <= 3:
            self.device[index].toggleSwitch()
        else:
            print("Invalid")
            
    def devicesOn(self):
        for device in self.device:
            device.switchedOn= True
            
    def devicesOff(self):
        for device in self.device:
            device.switchedOn= False        
    
    def __str__(self):
        output = "ALL DEVICES\n"
        num = 1
        
        for device in self.device:
            output += f"Device {num} : {device}\n"
            num += 1
        return output 
        
def testSmartHome():
    myHome = SmartHome()
    
    plug1 = SmartPlug(45)
    plug2 = SmartPlug(45)
    customDevice = SmartFridge()
    
    plug1.toggleSwitch()
    plug1.setConsumptionRate(50)
    plug2.setConsumptionRate(150)
    customDevice.setTemperature(3)
    
    myHome.addDevice(plug1)
    myHome.addDevice(plug2)
    myHome.addDevice(customDevice)
    
    myHome.toggleSwitch(1)
    print(myHome)
    
    print("After all devices are On")
    myHome.devicesOn()
    print(myHome)
    
    print("After removing one device")
    myHome.removeDevice(0)
    print(myHome)
testSmartHome()    
    
    
        
        
        
        
        
