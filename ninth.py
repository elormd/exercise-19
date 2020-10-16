print('A one bedroom in the bay area is listed $599,000')
print('Enter your first offer on the house.')
offer =  abs(int(input()))
print('Enter your best offer on the house.')
Best = abs(int(input()))
print('How much more do you want to offer each time?')
increment = abs(int(input()))
offer_accepted = False
while offer <= Best:
    if offer >= 650000:
        offer_accepted = True
        print('Your offer of', offer, 'has been accepted!')
        break
        if offer < 650000:
            print('We are sorry, your offer of', offer, 'has not been accepted')
            offer += increment