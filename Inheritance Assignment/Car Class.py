
# Creates original Car class
class Car:
    Make = 'Dodge'
    Model = 'Ram 1500'
    Year = '2017'

# Creates Company Car child class
class Company(Car):
    LastTuneUp = 'Jan 12th, 2021'
    VehicleFleetNumber = '12'

# Creates Retired Car child class
class Retired(Car):
    RetiredDate = 'Oct 5th, 2008'
    Reason = 'Cracked Engine Block'
    VehicleFleetNumber = '2'

# Creates a non-company Sold Car child class. This child class does not
# need the VehicleFleetNumber attribute so it was not included in the parent
# Car class
class Sold(Car):
    BillingInvoiceNumber = '231548'
    DateOfSale = 'Mar 27th, 2020'
