familyMemebers = ['Emmanuel', 'Adaobi', 'Chidubem', 'sochikamuma']

for member in familyMemebers:
    print(f'{member} is a member of this family')

print()
print('********** case two ***************')

for member in range(0, len(familyMemebers)):
    print(f'{familyMemebers[member]} is a member of this family')

print()
print('********** three ***************')

index = 0
while index < len(familyMemebers):
    print(f'{familyMemebers[index]} is a member of this family')
    index = index + 1
