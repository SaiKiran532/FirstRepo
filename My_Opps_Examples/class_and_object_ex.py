# The below code explains about creation of Class and Objects ( Here, I took Mobile details as example).
# class Name should always start with Capital letter.
class Mobile:
    # __init__ method used to initialize variables using self keyword.
    def __init__(self, Brand, Ram, Storage, Battery, FCamera, BCamera):
        self.Brand = Brand
        self.Ram = Ram
        self.Storage = Storage
        self.Battery = Battery
        self.FCamera = FCamera
        self.BCamera = BCamera

    def display_mobile_details(self):
        print(self.Brand + " Details:")
        print("Ram:", self.Ram)
        print("Storage:", self.Storage)
        print("Battery:", self.Battery)
        print("Camera:")
        print("FrontCamera:", self.FCamera)
        print("BackCamera:", self.BCamera)
        print("----------------------------")


# object creation
# Here we are taking mobile names as objects
iQOO = Mobile("iQOO", "8GB", "128GB, 256GB", "5000mAh", "16mp", "50mp + 2mp")
NothingPhone = Mobile("NothingPhone", "8GB, 12GB", "128GB, 256GB", "5000mAh", "32mp", "50mp + 50mp")
SumsangGalaxy = Mobile("SumsungGalaxy", "8GB", "128GB, 256GB", "5000mAh", "13mp", "200mp + 8mp + 2mp")

# calling class method using object to display the mobile details
iQOO.display_mobile_details()
NothingPhone.display_mobile_details()
SumsangGalaxy.display_mobile_details()



