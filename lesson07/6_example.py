# Multiple inheritance: one class inherits from more than one parent

class Camera:
    def take_photo(self):
        print("Taking photo...")


class GPS:
    def get_location(self):
        print("Getting location...")


class SmartPhone(Camera, GPS):
    def browse_internet(self):
        print("Browsing the internet...")


if __name__ == '__main__':
    phone = SmartPhone()

    phone.take_photo()
    phone.get_location()
    phone.browse_internet()

    # isinstance
    print(isinstance(phone, SmartPhone))    # True
    print(isinstance(phone, GPS))           # True
    print(isinstance(phone, Camera))        # True

    # issubclass
    print(issubclass(SmartPhone, GPS))      # True
    print(issubclass(SmartPhone, Camera))   # True
