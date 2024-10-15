from tkinter import *
from backend import *
from tkinter import simpledialog,messagebox


def setUpHome():
    myHome = SmartHome()
    
    print("Welcome to the Smart Home setup")
    
    for i in range(5):
        print(f"\nAdding Device {i + 1}")
        
        deviceMade = False
        # Prompt the user to choose device type
        while not deviceMade:
            deviceType = input("Enter device type (SmartPlug/SmartFridge): ").lower()
            
            if deviceType == "smartplug":
                    consumptionRate = input(f"Enter consumption rate for SmartPlug (0-150) {i + 1}: ")
                    if consumptionRate.isdigit():
                        consumptionRate = int(consumptionRate)
                        if 0 <= consumptionRate <= 150:
                            plug = SmartPlug(consumptionRate)
                            myHome.addDevice(plug)
                            deviceMade = True  
                        else:
                            print("Invalid consumption rate. Please enter a value between 0 and 150.")
                    else:
                            print("Invalid consumption rate.")

            elif deviceType == "smartfridge":
                    temperature = input(f"Enter temperature for SmartFridge (1, 3, 5) {i + 1}: ")
                    if temperature.isdigit():
                        temperature = int(temperature)
                        if temperature in [1, 3, 5]:
                            fridge = SmartFridge()
                            fridge.setTemperature(temperature)
                            myHome.addDevice(fridge)
                            deviceMade = True    
                        else:
                             print("Invalid")
                    else:
                        print("Invalid temperature rate. Please enter either 1, 3, or 5.")    
            else:
                print("Invalid device type. Please enter either 'SmartPlug' or 'SmartFridge'.")
        
    print("Smart Home setup complete")
    return myHome

#setUpHome()

# TASK 4

class SmartHomeSystem:
    
    def __init__(self, smartHome):
        self.smartHome = smartHome
        self.win = Tk()
        self.win.title("Smart Home System")
        self.mainFrame = Frame(self.win)
        self.mainFrame.grid(row=0, column=0, padx=10, pady=10)
    
    def addWidgets(self):
        allOnButton = Button(self.mainFrame, text="Turn on all", width=23, command=self.turnOnAll)
        allOnButton.grid(row=0, column=0, padx=(40,0), pady=(0,10))
        
        allOffButton = Button(self.mainFrame, text="Turn off all", width=23, command=self.turnOffAll)
        allOffButton.grid(row=0, column=1, padx=30, pady=(0,10))

        addButton = Button(self.mainFrame, text="Add Device", width=23, command=self.addDevice)
        addButton.grid(row=20, column=0, padx=(40,0), pady=(10,0))

        devices = self.smartHome.getDevice()
        for i in range(len(devices)):
            device = devices[i]
            label = Label(self.mainFrame, text=str(device))
            label.grid(row=i+1, column=0)

            toggleButton = Button(self.mainFrame, text="Toggle", width=13, command=lambda idx=i: self.toggleDevice(idx))
            toggleButton.grid(row=i+1, column=1, padx=(0,70), pady=5)

            editButton = Button(self.mainFrame, text="Edit", width=6, command=lambda idx=i: self.editDevice(idx))
            editButton.grid(row=i+1, column=1, padx=(120,0), pady=5)

            deleteButton = Button(self.mainFrame, text="Delete", width=8, command=lambda idx=i: self.deleteDevice(idx))
            deleteButton.grid(row=i+1, column=2, padx=(0,0), pady=5)
        
    def run(self):
        self.addWidgets()
        self.win.mainloop()
    
    def turnOnAll(self):
        self.smartHome.devicesOn()
        self.updateGUI()
    
    def turnOffAll(self):
        self.smartHome.devicesOff()
        self.updateGUI()
    
    def toggleDevice(self, index):
        self.smartHome.toggleSwitch(index)
        self.updateGUI()
    
    def addDevice(self):
        deviceType = simpledialog.askstring("Add Device", "Enter device type (SmartPlug/SmartFridge): ").lower()
        
        if deviceType == "smartplug":
            self.addSmartPlug()
        elif deviceType == "smartfridge":
            self.addSmartFridge()
        else:
            messagebox.showerror("Error", "Invalid device type. Please enter either 'SmartPlug' or 'SmartFridge'.")
    
    def addSmartPlug(self):
        consumptionRate = self.getValidConsumptionRate()
        if consumptionRate is not None:
            plug = SmartPlug(consumptionRate)
            self.smartHome.addDevice(plug)
            self.updateGUI()
    
    def getValidConsumptionRate(self):
        consumptionRate = simpledialog.askinteger("Add SmartPlug", "Enter consumption rate for SmartPlug (0-150): ")
        if consumptionRate is not None and 0 <= consumptionRate <= 150:
            return consumptionRate
        else:
            messagebox.showerror("Error", "Invalid consumption rate. Please enter a value between 0 and 150.")
            return None
    
    def addSmartFridge(self):
        temperature = self.getValidTemperature()
        if temperature is not None:
            fridge = SmartFridge()
            fridge.setTemperature(temperature)
            self.smartHome.addDevice(fridge)
            self.updateGUI()
    
    def getValidTemperature(self):
        temperature = simpledialog.askinteger("Add SmartFridge", "Enter temperature for SmartFridge (1, 3, 5): ")
        if temperature is not None and temperature in [1, 3, 5]:
            return temperature
        else:
            messagebox.showerror("Error", "Invalid temperature. Please enter either 1, 3, or 5.")
            return None
    
    def editDevice(self, index):
        device = self.smartHome.getAdevice(index)
        if device:
            self.editDeviceAttributes(device, index)
    
    def editDeviceAttributes(self, device, index):
        if "SmartPlug" in str(device):
            self.editSmartPlug(device, index)
        elif "SmartFridge" in str(device):
            self.editSmartFridge(device, index)
    
    def editSmartPlug(self, device, index):
        newConsumptionRate = self.getValidConsumptionRate()
        if newConsumptionRate is not None:
            device.setConsumptionRate(newConsumptionRate)
            self.updateGUI()
    
    def editSmartFridge(self, device, index):
        newTemperature = self.getValidTemperature()
        if newTemperature is not None:
            device.setTemperature(newTemperature)
            self.updateGUI()
    
    def deleteDevice(self, index):
        self.smartHome.removeDevice(index)
        self.updateGUI()
    
    def updateGUI(self):
        for widget in self.mainFrame.winfo_children():
            widget.destroy()
        self.addWidgets()

def test():
    smartHome = setUpHome()
    mySystem = SmartHomeSystem(smartHome)
    mySystem.run()

test()
