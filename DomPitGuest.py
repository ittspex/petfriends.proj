class Customers:
    def __init__(self,name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city


    def get_guest(self):
        return f'{self.name} {self.surname}, {self.city}'


customer_1 = Customers('Joe','Needls','New York City')
customer_2 = Customers('David','Beckham','Los Angeles')
customer_3 = Customers('Lasly','Fouls','Cansas City')

guest_list=[customer_1,customer_2,customer_3]


for guest in guest_list:
    print(guest.get_guest())