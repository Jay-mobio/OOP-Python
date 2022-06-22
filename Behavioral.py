import abc

class ThreeDaysTrip(object):
    @abc.abstractmethod
    def transport(self):
        pass
    
    @abc.abstractmethod
    def day1(self):
        pass
    
    @abc.abstractmethod
    def day2(self):
        pass

    @abc.abstractmethod
    def day3(self):
        pass

    @abc.abstractmethod
    def back_to_home(self):
        pass

   
    def iternary(self):
        print("The trip is started")
        self.transport()
        self.day1()
        self.day2()
        self.day3()
        self.back_to_home()
        print("The trip is over")

class South(ThreeDaysTrip):
    def transport(self):
        print("Go by train and check in to hotel")
    
    def day1(self):
        print("Day-1 : Enjoy the hotel beach whole day")
    
    def day2(self):
        print("Day-2 : Visit historical places")

    def day3(self):
        print("Day-3 : Go on shopping with your family")

    def back_to_home(self):
        print("Check out fromhotel and go back to your home")

class South(ThreeDaysTrip):
    def transport(self):
        print("Go by train and check in to hotel")
    
    def day1(self):
        print("Day-1 : Go to highted place and enjoy snow activities")
    
    def day2(self):
        print("Day-2 : Go on river rafting")

    def day3(self):
        print("Day-3 : Go on shopping with your family")

    def back_to_home(self):
        print("Check out fromhotel and go back to your home")


if __name__ =="__main__":
    place = input("Enter the place you want ot go : ")
    if place == "North":
        trip = North()
        trip.iternary()
    
    elif place == 'South':
        trip = South()
        trip.iternary()
    else:
        print("Option not available")

