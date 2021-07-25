from functions import nameInitialExtractor

father = {}
father['firstName'] = 'Emmanuel'
father['lastName'] = 'Okoro'
father['age'] = 34
father['initials'] = nameInitialExtractor(
    'Emmanuel', 'Okoro', True)

mother = {}
mother['firstName'] = 'Adaobi'
mother['lastName'] = 'Okoro'

firstSon = {}
firstSon['firstName'] = 'Chidubem'
firstSon['lastName'] = 'Emmanuel'

family = [father, mother, firstSon]

family.append({
    'firstName': 'Sochikamuma',
    'lastName': 'Emmanuel'
})

print(family)
