TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

passwords = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

print('-' * 40)
print('Welcome to Karol text analyzer. Please log in: ')
user = input('Username: ')
if user not in passwords:
    print('wrong username')
    exit()

attempt = 0
password = str(input('Password: '))
while attempt < 2 and password != str(passwords[user]):
    print('wrong password')
    password = input('Password: ')
    if attempt == 1 and password != str(passwords[user]):
        print('Wrong password. All attempts used. Exiting program.')
        exit()
    attempt += 1
print('Welcome ', user)
print('-' * 40)
print('We have 3 texts to be analyzed.')
choice = int(input('Enter a number btw. 1 and 3 to select: '))
index = choice - 1

txt_an = TEXTS[index].split()
txt_len = len(txt_an)

print('There are', txt_len, 'words in the selected text')

titlecase = 0
uppercase = 0
lowercase = 0
numeric = 0
i = 0
while i < txt_len:
    if txt_an[i][0].isupper():
        titlecase += 1
    elif txt_an[i].isupper():
        uppercase += 1
    elif txt_an[i].islower():
        lowercase += 1
    elif txt_an[i].isnumeric():
        numeric += 1
    i += 1

delky = {}
i = 0
k = 0
max_delka = 0
while i < txt_len:
    leni = len(txt_an[i])
    if leni >= max_delka:
        max_delka = leni
    delky[leni] = []
    i += 1

k = 0
suma = 0
while k < txt_len:
    lenk = len(txt_an[k])
    delky[lenk].append(txt_an[k])
    if txt_an[k].isnumeric():
        suma = suma + int(txt_an[k])
    k += 1

print('-' * 40)
print('There are', titlecase, 'titlecase words')
print('There are', uppercase, 'uppercase words')
print('There are', lowercase, 'lowercase words')
print('There are', numeric, 'numeric strings')
print('-' * 40)

keylist = list(delky.keys())
k = 0
keylist.sort()

while k <= max_delka:
    if k in keylist:
         print(k, '*' * int(len(delky[k])), int(len(delky[k])))
         k += 1
    else:
        k += 1

print('-' * 40)
print('If we summed all the numbers in this text we would get: ', float(suma))
print('-' * 40)

