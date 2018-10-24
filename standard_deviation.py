from math import sqrt
from random import randint

#Calculates the standard deviation
list = [10,12,13,14,15,16,17,18]


def standard_deviation(list):
    mean = sum(list)/len(list)
    variance = 0
    standardard_deviation = 0
    for i in list:
        variance += pow(i - mean,2)
    print('%.2f' % sqrt(variance))

#standard_deviation(list)

#[] Pick a grade in middleschool level (6-8)
#[] Pick a grade in highschool level (9-12)
#[] Random sample a class name
#[] 40 students from highschool

# middleschool = [6,7,8]
# highschool = [9,10,11,12]
# temp_names = []
# class_names = ["Andromeda","Aries","Athena","Artemis","Achillis","Antigone","Atlas","Aura"]

# 7 Atlas
seven_atlas = [
"Bun Sok Chhay",
"Chhun Vortanakchanmani",
"Da Ravid",
"Ear Chhang Hout",
"Heang Watanak Sathyar",
"Hok Heng Seng",
"Hong Lainey",
"Ivy Janine",
"Molina Alamis",
"Khean Khun Devin",
"Kourn Chhay Huy",
"Lin Zhibin",
"Ly Mei Jing",
"Peng Phalsovatheka",
"Real Moun Somealear",
"Siep Tharithysal",
"Sim Song Sak",
"Sok Deesovann",
"Taing Chungseng",
"Taing Lyzang",
"Tang Chayhak",
"Tanheang Ketteya",
"Vuth Sedhika Henry",
"Wang Kimshien",
"Yin Janet"
]

# 8 Athena
eight_athena = [
"Chea Sopanhala",
"Chhen Pengleap",
"Deng Reach Sambat",
"Eath Eav Thean",
"Fernandez Aleeyah Charis",
"Kong Oscar",
"Kuch Sok Ketya",
"La Seav Hong",
"Lim Chanthida",
"Lim Vyrack Sathya",
"Meng Sandora",
"Ngov Lyping",
"Phay Pitou",
"San Puthika",
"Sen Solyjenny",
"Serey Socheata",
"Sok Lita",
"Taing Kheng Long",
"Tauch Lisa",
"Tea Sihon",
"Top Rithy Sorajati",
"Vich Sethsobotrey",
"Zhong Ihoung"
]
#===<For middle school>===#
#print("Grade %s %s" % (middleschool[randint(0,len(middleschool)-1)],class_names[randint(0,len(class_names)-1)]) )

#===<For highschool>===#
#print("Grade %s %s" % (highschool[randint(0,len(highschool)-1)],class_names[randint(0,len(class_names)-1)]) )

#===<For names>===#
# for i in range(10):
#     print(seven_atlas[randint(0,len(seven_atlas)-1)])
#
# list1 = []
# i=0
# while i < 10:
#     name = eight_athena[randint(0,len(eight_athena)-1)]
#     if name not in list1:
#         list1.append(name)
#         i += 1
# for i in list1:
#     print(i)

list2 = []
j=0
while j < 10:
    name = seven_atlas[randint(0,len(seven_atlas)-1)]
    if name not in list2:
        list2.append(name)
        j += 1
for j in list2:
    print(j)


###===<7 Atlas Class>===###
# Kourn Chhay Huy
# Chhun Vortanakchanmani
# Wang Kimshien
# Ivy Janine
# Siep Tharithysal
# Yin Janet
# Da Ravid
# Heang Watanak Sathyar
# Taing Lyzang
# Tanheang Ketteya

###===<8 Athena Class>===###
# Lim Chanthida
# Lim Vyrack Sathya
# Chhen Pengleap
# Tauch Lisa
# Sen Solyjenny
# Top Rithy Sorajati
# Sok Lita
# Zhong Ihoung
# Kuch Sok Ketya
# Vich Sethsobotrey

#===<AP Human Geo>===#
# Phalkunvuthe Peng
# Pisedh Eng
# Rattanakun Sith
# Sandra Peang
# Young Ju Wi
# Justine Rellin
# Leesy Heng
# Miangaly Randrianasoavina
