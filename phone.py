class Phone:
    """ This is a phone class that can be used for inheritance purposes"""
    def __init__(self, phone_number, color):
        self.phone_number = phone_number
        self.color = color

    def __str__(self):
        return f"This phone belongs to {self.phone_number}"
    
    def call(self, other_number):
        print(f"Calling number: {other_number}")

    def test(self, other_number, message):
        print(f'Sending text to {other_number}')
        print(message)
    
    def open_app(self, app_name):
        print(f"Opening {app_name}")

class Android(Phone):
    def __init__(self, phone_number, color):
        super().__init__(phone_number, color)
        self.passcode = None
        self.battery = 50
    
    def __str__(self):
        return f"Android phone that belongs to number {self.phone_number}"
    
    def set_passcode(self, passcode):
        self.passcode = passcode

    def unlock_phone(self, passcode):
        if passcode == self.passcode:
            print('Phone unlocked')
    def view_batter_life(self):
        print(f'Battery life: {self.battery}')

    def charge_phone(self, charging_amount):
        self.battery += charging_amount

        if self.battery > 100:
            self.battery = 100
    
    def view_phone_number(self):
        print(f"Phone Number: {self.phone_number}")


class IPhone(Phone):
  def __init__(self, phone_number, color):
    super().__init__(phone_number, color)
    self.fingerprint = None

  def set_fingerprint(self, fingerprint):
    self.fingerprint = fingerprint

  def unlock(self, fingerprint=None):
    if (fingerprint == self.fingerprint):
      print("Phone unlocked because no fingerprint has not been set.")

    if (fingerprint == self.fingerprint):
      print("Phone unlocked. Fingerprint matches.")
    else:
      print("Phone locked. Fingerprint doesn't match.")


    
my_phone = IPhone('555-555-5555', 'Blue')

my_phone.set_fingerprint('fingerprint')
my_phone.unlock(fingerprint='fingerprint')