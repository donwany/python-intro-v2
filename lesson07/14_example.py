class SmartHome:
    def __init__(self):
        self.lights = False
        self.temperature = 72
        self.doors_locked = False
        self.alarm = False

    def turn_on_lights(self):
        self.lights = True
        print("💡 Lights turned ON")
        return self

    def turn_off_lights(self):
        self.lights = False
        print("💡 Lights turned OFF")
        return self

    def set_temperature(self, temp):
        self.temperature = temp
        print(f"🌡️ Temperature set to {temp}°F")
        return self

    def lock_doors(self):
        self.doors_locked = True
        print("🔒 Doors locked")
        return self

    def unlock_doors(self):
        self.doors_locked = False
        print("🚪 Doors unlocked")
        return self

    def activate_alarm(self):
        self.alarm = True
        print("🚨 Alarm activated")
        return self

    def deactivate_alarm(self):
        self.alarm = False
        print("✅ Alarm deactivated")
        return self

    def good_night(self):
        self.lights = False
        self.doors_locked = True
        self.alarm = True
        self.temperature = 67
        print("🌙 Good night mode activated.")
        return self

    def is_secure(self):
        if self.doors_locked and self.alarm:
            print("✅ Home is secure.")
        else:
            print("⚠️ Warning: Home is not secure!")

        return self

    def status(self):
        print("\n===== SMART HOME STATUS =====")
        print(f"Lights: {'ON' if self.lights else 'OFF'}")
        print(f"Temperature: {self.temperature}°F")
        print(f"Doors Locked: {'Yes' if self.doors_locked else 'No'}")
        print(f"Alarm: {'Active' if self.alarm else 'Inactive'}")
        print("=============================")
        return self


if __name__ == '__main__':
    home = SmartHome().turn_on_lights().set_temperature(68).lock_doors().activate_alarm().status()
    home