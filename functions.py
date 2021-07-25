from pip._vendor.colorama import init, Fore
init()


def nameInitialExtractor(firstName, lastName, upper=False):
    firstName = firstName[0:1]
    lastName = lastName[0:1]
    if upper:
        firstName.upper()
        lastName.upper()
    return firstName + '.' + lastName


def inputCollector(message):
    return input(f'Please enter {message}: ')


first_Name = inputCollector('first name')
last_Name = inputCollector('last name')

nameInitials = nameInitialExtractor(lastName=last_Name, firstName=first_Name)

print(f'{Fore.RED } your initials are {nameInitials}')
