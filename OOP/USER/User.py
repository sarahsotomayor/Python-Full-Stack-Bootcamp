class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

sachiko = User("Sachiko", "Nguyen", "sn@gmail.com", "20")
orlando = User("Orlando", "S", "j.o.s@gmail.com", "56")
chata = User("Isabel", "M", "nana@yahoo.com", "80")

def display_info(self):
    print(self.first_name)
    print(self.last_name)
    print(self.email)
    print(self.age)
    print(self.is_rewards_member)
    print(self.gold_card_points)

#test
#display_info(sachiko)

def enroll(self):
    self.is_rewards_member = True
    self.gold_card_points = 200

#test
#enroll(sachiko)
#display_info(sachiko)

def spend_points(self, amount):
    self.gold_card_points = self.gold_card_points - amount

enroll(sachiko)
spend_points(sachiko, 50)
enroll(orlando)
spend_points(orlando, 80)

display_info(sachiko)
display_info(orlando)
display_info(chata)



