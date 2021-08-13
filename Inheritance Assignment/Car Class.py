
class Car:
    Make = 'Dodge'
    Model = 'Ram 1500'
    Year = '2017'

class Company(Car):
    LastTuneUp = 'Jan 12th, 2021'
    VehicleFleetNumber = '12'

class Retired(Car):
    RetiredDate = 'Oct 5th, 2008'
    Reason = 'Cracked Engine Block'
    VehicleFleetNumber = '2'

class Sold(Car):
    BillingInvoiceNumber = '231548'
    DateOfSale = 'Mar 27th, 2020'
