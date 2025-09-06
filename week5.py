class Airbnb:
  def __init__(self, name, location, price):
    self.name = name
    self.location = location
    self.price = price
    
  def display_info(self):
    print(f"Name: {self.name}, Location: {self.location}, Price: ${self.price}")  
    
    
if __name__ == "__main__":
  airbnb=Airbnb("Cozy Cottage", "New York", 100)
  airbnb.display_info()
  airbnb=Airbnb("Cozy Cottage", "New York", 150)
  airbnb.display_info()
    
class sercetAirbnb(Airbnb):
  def __init__(self, name, location, price, secret_code):
    super().__init__(name, location, price)
    self.secret_code = secret_code
    
  def display_info(self):
    super().display_info()
    print(f"Secret Code: {self.secret_code}")
    
  def reveal_secret(self, code):
    if code == self.secret_code:
      print("Access Granted: Here is the secret information!")
    else:
      print("Access Denied: Incorrect secret code.")
      

if __name__ == "__main__":
  secret_airbnb=sercetAirbnb("Hidden Gem", "Los Angeles", 200, "XYZ123")
  secret_airbnb.display_info()  secret_airbnb.reveal_secret("XYZ123")
  