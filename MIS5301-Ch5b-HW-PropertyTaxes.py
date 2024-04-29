#------------------------------------------------------------
#Name: John Ogun
#MIS 5301 
#Purpose: Property Tax Estimation Tool
#File: MIS5301-Ch5b-HW-PropertyTaxes.py
#------------------------------------------------------------

#Import Modules
import random


def isfloat(value):
    try: 
        float(value) 
        return True
    except: 
        return False
##def main():
##
##    for i in range(0, 5):
##        num = random.randrange(1,25)
##        print('randrange:', num)
##    
##main() 




#Global Constants


#MAIN---------------------------------------------------------------------------------------
def main():
    

    #initialize variables
    indent1 = (' ' * 3)
    indent2 = (' ' * 6)
    indent3 = ('-' * 70)
    indent4 = (' ' * 2)
    
    #header lines
    display_company_banner()
    app_title = f'{"Welcome to the Residential Property Tax Estimation Tool!":^72}'
    display_application_title(app_title)
    print()

    #INPUT-----------------------------------------------------
    #Get user input comment line
    #test
    #address = '123 rolling hills'
    #bulg_sqft = 3300
    #land_front = 133.33
    #land_depth = 175.55
    #exempt_code = 'H'
    
    address = str(input('    Enter property address: '))
    
    bulg_sqft = input('    Enter building size (sqft): ')
    while not bulg_sqft.isdigit():
        print('   >> building size (sqft) is invalid. Please enter a number')
        bulg_sqft = input('\n    Enter building size (sqft): ')
    bulg_sqft = int(bulg_sqft)

    land_front = input('    Enter land effective front (ft): ')
    while not isfloat(land_front):
        print('    >> Land effective front is invalid. Please enter a number.')
        land_front = input('\n    Enter land effective front: ')
    land_front = float(land_front)

    land_depth = input('    Enter land effective depth (ft): ')
    while not isfloat(land_depth):
        print('    >> Land effective depth is invalid. Please enter a number. ')
        land_depth = input('\n    Enter land effective depth: ')
    land_depth = float(land_depth)

##    y = False  # Initialize the flag as False
##
##    while not y:
##        exempt_code = input('Enter exemption code - (H)omestead, (O)ver 65, or (N)one: ').upper()
##        if exempt_code in ['H', 'O', 'N']:
##            y = True
##        else:
##             print('Invalid input. Please enter (H) for Homestead, (O) for Over 65, or (N) for None.')
##
### At this point, the loop exits when a valid exemption code is entered.
### You can use the `exempt_code` variable for further processing.





    

    y = 'false'
    while y == 'false':
        exempt_code = input('    Enter exemption code - (H)omestead, (O)ver 65, or (N)one: ').upper()
        while not exempt_code.isalpha():
            print('    >> Exemption code is invalid. Please enter any of the alphabet - (H)omestead, (O)ver 65, or (N)one: ')
            exempt_code = input('\n    Enter Exemption code - (H)omestead, (O)ver 65, or (N)one: ').upper()
        exempt_code = str(exempt_code)
        if exempt_code == 'H' or exempt_code == 'O' or exempt_code == 'N':
            y = 'True'
        else:
            print('    >> Invalid alphabet entered. Kindly enter any of the alphabet - (H)omestead, (O)ver 65, or (N)one: ')
##                y = 'false'

    
    
    
##    address = input('Enter property address: ')
##    bulg_sqft = int(input('Enter building size: '))
##    land_front = float(input('Enter land effective front: '))
##    land_depth = float(input('Enter land effective depth: '))
##    exempt_code = input('Enter exemption code - (H)omestead, (O)ver 65, or (N)one: ').upper()

#PROCESS---------------------------------------------------
    bulg_value = bulg_sqft * 130.00
    land_sqft = land_front * land_depth
    land_acres = land_sqft / 43560
    land_value = land_acres * 100000

    #property_tax = (bulg_value + land_value) * 0.02
    #property_tax_exempt = property_tax - (property_tax * 0.15)
    num = random.randrange(100000,999999)
    
    get_exemption_name(exempt_code)
    calc_bulg_value(bulg_sqft)
    calc_land_square_footage(land_front, land_depth)
    calc_land_acres(land_sqft)
    calc_land_value(land_acres)
    property_tax, property_tax_exempt = calc_property_taxes(bulg_value, land_value, exempt_code)

    gen_confirmation_no()
    
##
    #OUTPUT----------------------------------------------------
    #Estimate Report Title
    print()
    print(indent1, indent3)
    print(indent1, f' {"Property Tax Estimate Report":^70}')
    print(indent1, indent3)
    print()
    print(indent1, '>>>> Report for property located at: ', address.title())
    print()
    
    #Estimate Report
    print(indent1, f'Building: {bulg_sqft:,} sqft')
    print()
    print(indent1, 'Land Info')
    print(f'{indent2} {"Front:":6}{land_front:10,.2f}{indent4} {"Depth:":5} {land_depth:7,.2f}')
    print(f'{indent2} {"Sqft:":6}{land_front * land_depth:10,.2f}{indent4} {"Acres:":5} {land_acres:7,.4f}')
    print()
    print(f'{indent1} {"Building market value:":28} {bulg_value:10,.2f}')
    print(f'{indent1} {"Land market value:":28} {land_value:10,.2f}')
    print(f'{indent1} {"Taxes w/Current Exemptions:":28} {property_tax_exempt:10,.2f} ({get_exemption_name(exempt_code)})')
    print(f'{indent1} {"Taxes w/o Exemptions:":28} {property_tax:10,.2f}')

    #Report Footer
    print(indent1, indent3)
    print(indent1, 'Estimate Confirmation No:', num)



    
    
##
##
##
###FUNCTIONS---------------------------------------------------------------------------------------
##
##
##
#FN1: Company banner
def display_company_banner():
    print('*' * 80)
    print(f' {"Victorino County Tax Assessor":^80}')
    print('*' * 80)
    #return display_company_banner
    print()  

#FN2: Application title
def display_application_title(app_title):
    print(app_title)
    return app_title
    print()

#FN3: Exemption name
def get_exemption_name(exempt_code):
    if exempt_code == 'H':
        exempt_name = 'Homestead'
    elif exempt_code == 'O':
        exempt_name = 'Over'
    elif exempt_code == 'N':
        exempt_name = 'None'
    else:
        exempt_name = 'invalid input, enter any of H, O, or N'
    return exempt_name
    
#FN4: Building value
def calc_bulg_value(bulg_sqft):
    bulg_value = bulg_sqft * 130.00
    return bulg_value

#FN5: Land sqft
def calc_land_square_footage(land_front, land_depth):
    land_sqft = land_front * land_depth
    return land_sqft

#FN6: Land acres
def calc_land_acres(land_sqft):
    land_acres = land_sqft / 43560
    return land_acres

#FN7: Land value
def calc_land_value(land_acres):
    land_value = land_acres * 100000
    return land_value

#FN8: Property taxes
def calc_property_taxes(bulg_value, land_value, exempt_code):
    property_tax = (bulg_value + land_value) * 0.02
    if exempt_code == 'H':
        property_tax_exempt = property_tax - (property_tax * 0.15)
    elif exempt_code == 'O':
        property_tax_exempt = property_tax - (property_tax * 0.20)
    else:
        property_tax_exempt = property_tax
         
    
    return property_tax, property_tax_exempt

#FN9: Confirmation number
def gen_confirmation_no():
    for i in range(0, 6):
        num = random.randrange(100000,999999)
        return num

main()
