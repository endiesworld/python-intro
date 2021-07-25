name = input('please enter you name: ')
print(f'welcome to python class, {name}')

country = input('Please enter the country of use: ')
print(f'ooh, you are from {country.upper()}')
if country.upper() == 'NIGERIA':
    state = input('please enter your current state ')
    if state.upper() == 'LAGOS':
        meetRequirement = True
    elif state.upper() == 'OGUN' or state.upper() == 'IBADAN':
        meetRequirement = True
    elif state.upper() in ('ABIA', 'IMO', 'ANAMBRA', 'EBONYI', 'ENUGU'):
        meetRequirement = True
    else:
        meetRequirement = False
else:
    meetRequirement = False

if meetRequirement:
    gender = input('Please enter your gender: ')
    age = input('Please enter your age: ')

else:
    print('We regret to inform you that we cannot proceed further with you')

if meetRequirement and gender == 'male' and age <= 35:
    print('You will be a great man in Jesus name')

elif meetRequirement and gender == 'female' and age <= 30:
    print('You will be a great woman in Jesus name')

elif meetRequirement and gender == 'female' and age <= 30:
    print('You will be a great woman in Jesus name')

else:
    print('We regret to inform you that we cannot proceed further with you')
