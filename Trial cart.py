import math

print("Hello User, Welcome to the Online Market ! Please Login to shop further")
print("Please note you may select upto 10 items only at a time")

user = input("Enter username : ")
while user == "" :
    print("Please enter your username to continue")
    user = input("Enter username : ")
print(f"Welcome {user} ")

item1 = input("Enter first item on the list : ")
#
price1 = float(input("Enter the price of the item : "))
#
quant1 = int(input("Enter the quantity : "))
#
type1 = input("Enter type of item (F for food , B for beverage , O for other) : ")

while type1 == "" :
    print("It is mandatory to select item type!")
    type1 = input("Enter type of item (F for food , B for beverage , O for other) : ")
if type1 == "F" :
    gst1 = price1 + 1.10
    bill1 = quant1 * gst1 
    print(f"You bought {quant1} {item1}. Your bill for item 1 is {bill1} ")
elif type1 == "B" :
    gst1 = price1 + 0.70
    bill1 = quant1 * gst1 
    print(f"You bought {quant1} {item1}. Your bill for item 1 is {bill1} ")
elif type1 == "O" :
    gst1 = price1 + 0.90
    bill1 = quant1 * gst1 
    print(f"You bought {quant1} {item1}. Your bill for item 1 is {bill1} ")
    exit()
else :
    print("You failed to select a valid item type. Bill Failed")

ques1 = input("Do you wish to proceed further (Y for yes / N for no) : ")
if ques1 == "Y" :
    item2 = input("Enter second item on the list : ")
    price2 = float(input("Enter the price of the item : "))
    quant2 = int(input("Enter the quantity : "))
    type2 = input("Enter type of item (F for food , B for beverage , O for other) : ")
    while type2 == "" :
        print("It is mandatory to select food type!")
        type2 = input("Enter type of item (F for food , B for beverage , O for other) : ")
    if type2 == "F" :
        gst2 = price2 + 1.10
        bill2 = quant2 * gst2 
        print(f"You bought {quant2} {item2}. Your bill for item 2 is {bill2} ")
    elif type2 == "B" :
        gst2 = price2 + 0.70
        bill2 = quant2 * gst2
        print(f"You bought {quant2} {item2}. Your bill for item 2 is {bill2} ")
    elif type2 == "O" :
        gst2 = price2 + 0.90
        bill2 = quant2 * gst2 
        print(f"You bought {quant2} {item2}. Your bill for item 2 is {bill2} ")
    else :
        print("You failed to select a valid item type. Bill Failed")
elif ques1 == "" or "N" :
    print(f"Thank you, your final bill {bill1}")
    exit()

ques2 = input("Do you wish to proceed further (Y for yes / N for no) : ")
if ques2 == "Y" :
    item3 = input("Enter third item on the list : ")
    price3 = float(input("Enter the price of the item : "))
    quant3 = int(input("Enter the quantity : "))
    type3 = input("Enter type of item (F for food , B for beverage , O for other) : ")
    while type3 == "" :
        print("It is mandatory to select food type!")
        type3 = input("Enter type of item (F for food , B for beverage , O for other) : ")
    if type3 == "F" :
        gst3 = price3 + 1.10
        bill3 = quant3 * gst3 
        print(f"You bought {quant3} {item3}. Your bill for item 3 is {bill3} ")
    elif type3 == "B" :
        gst3 = price3 + 0.70
        bill3 = quant3 *gst3
        print(f"You bought {quant3} {item3}. Your bill for item 3 is {bill3} ")
    elif type3 == "O" :
        gst3 = price3 + 0.90
        bill3 = quant3 * gst3 
        print(f"You bought {quant3} {item3}. Your bill for item 3 is {bill3} ")
    else :
        print("You failed to select a valid item type. Bill Failed")
elif ques2 == "" or "N" :
    print(f"Thank you, your final bill {bill1+bill2}")
    exit()

ques3 = input("Do you wish to proceed further (Y for yes / N for no) : ")
if ques3 == "Y" :
    item4 = input("Enter fourth item on the list : ")
    price4 = float(input("Enter the price of the item : "))
    quant4 = int(input("Enter the quantity : "))
    type4 = input("Enter type of item (F for food , B for beverage , O for other) : ")
    while type4 == "" :
        print("It is mandatory to select food type!")
        type4 = input("Enter type of item (F for food , B for beverage , O for other) : ")
    if type4 == "F" :
        gst4 = price4 + 1.10
        bill4 = quant4 * gst4 
        print(f"You bought {quant4} {item4}. Your bill for item 4 is {bill4} ")
    elif type4 == "B" :
        gst4 = price4 + 0.70
        bill4 = quant4 * gst4
        print(f"You bought {quant4} {item4}. Your bill for item 4 is {bill4} ")
    elif type4 == "O" :
        gst4 = price4 + 0.90
        bill4 = quant4 * gst4 
        print(f"You bought {quant4} {item4}. Your bill for item 4 is {bill4} ")
    else :
        print("You failed to select a valid item type. Bill Failed")
elif ques3 == "" or "N" :
    print(f"Thank you, your final bill {bill1+bill2+bill3}")
    exit()

ques4 = input("Do you wish to proceed further (Y for yes / N for no) : ")
if ques4 == "Y" :
    item5 = input("Enter fifth item on the list : ")
    price5 = float(input("Enter the price of the item : "))
    quant5 = int(input("Enter the quantity : "))
    type5 = input("Enter type of item (F for food , B for beverage , O for other) : ")
    while type5 == "" :
        print("It is mandatory to select food type!")
        type5 = input("Enter type of item (F for food , B for beverage , O for other) : ")
    if type5 == "F" :
        gst5 = price5 + 1.10
        bill5 = quant5 * gst5 
        print(f"You bought {quant5} {item5}. Your bill for item 5 is {bill5} ")
    elif type5 == "B" :
        gst5 = price5 + 0.70
        bill5 = quant5 * gst5
        print(f"You bought {quant5} {item5}. Your bill for item 5 is {bill5} ")
    elif type5 == "O" :
        gst5 = price5 + 0.90
        bill5 = quant5 * gst5 
        print(f"You bought {quant5} {item5}. Your bill for item 5 is {bill5} ")
    else :
        print("You failed to select a valid item type. Bill Failed")
elif ques4 == "" or "N" :
    print(f"Thank you, your final bill {bill1+bill2+bill3+bill4}")
    exit()

ques5 = input("Do you wish to proceed further (Y for yes / N for no) : ")
if ques5 == "Y" :
    item6 = input("Enter sixth item on the list : ")
    price6 = float(input("Enter the price of the item : "))
    quant6 = int(input("Enter the quantity : "))
    type6 = input("Enter type of item (F for food , B for beverage , O for other) : ")
    while type6 == "" :
        print("It is mandatory to select food type!")
        type6 = input("Enter type of item (F for food , B for beverage , O for other) : ")
    if type6 == "F" :
        gst6 = price6 + 1.10
        bill6 = quant6 * gst6 
        print(f"You bought {quant6} {item6}. Your bill for item 6 is {bill6} ")
    elif type6 == "B" :
        gst6 = price6 + 0.70
        bill6 = quant6 * gst6
        print(f"You bought {quant6} {item6}. Your bill for item 6 is {bill6} ")
    elif type6 == "O" :
        gst6 = price6 + 0.90
        bill6 = quant6 * gst6 
        print(f"You bought {quant6} {item6}. Your bill for item 6 is {bill6} ")
    else :
        print("You failed to select a valid item type. Bill Failed")
elif ques5 == "" or "N" :
    print(f"Thank you, your final bill {bill1+bill2+bill3+bill4+bill5}")
    exit()

ques6 = input("Do you wish to proceed further (Y for yes / N for no) : ")
if ques6 == "Y" :
    item7 = input("Enter seventh item on the list : ")
    price7 = float(input("Enter the price of the item : "))
    quant7 = int(input("Enter the quantity : "))
    type7 = input("Enter type of item (F for food , B for beverage , O for other) : ")
    while type7 == "" :
        print("It is mandatory to select food type!")
        type7 = input("Enter type of item (F for food , B for beverage , O for other) : ")
    if type7 == "F" :
        gst7 = price7 + 1.10
        bill7 = quant7 * gst7 
        print(f"You bought {quant7} {item7}. Your bill for item 7 is {bill7} ")
    elif type7 == "B" :
        gst7 = price7 + 0.70
        bill7 = quant7 * gst7
        print(f"You bought {quant7} {item7}. Your bill for item 7 is {bill7} ")
    elif type7 == "O" :
        gst7 = price7 + 0.90
        bill7 = quant7 * gst7 
        print(f"You bought {quant7} {item7}. Your bill for item 7 is {bill7} ")
    else :
        print("You failed to select a valid item type. Bill Failed")
elif ques6 == "" or "N" :
    print(f"Thank you, your final bill {bill1+bill2+bill3+bill4+bill5+bill6}")
    exit()

ques7 = input("Do you wish to proceed further (Y for yes / N for no) : ")
if ques7 == "Y" :
    item8 = input("Enter eighth item on the list : ")
    price8 = float(input("Enter the price of the item : "))
    quant8 = int(input("Enter the quantity : "))
    type8 = input("Enter type of item (F for food , B for beverage , O for other) : ")
    while type8 == "" :
        print("It is mandatory to select food type!")
        type8 = input("Enter type of item (F for food , B for beverage , O for other) : ")
    if type8 == "F" :
        gst8 = price8 + 1.10
        bill8 = quant8 * gst8 
        print(f"You bought {quant8} {item8}. Your bill for item 8 is {bill8} ")
    elif type8 == "B" :
        gst8 = price8 + 0.70
        bill8 = quant8 * gst8
        print(f"You bought {quant8} {item8}. Your bill for item 8 is {bill8} ")
    elif type8 == "O" :
        gst8 = price8 + 0.90
        bill8 = quant8 * gst8 
        print(f"You bought {quant8} {item8}. Your bill for item 8 is {bill8} ")
    else :
        print("You failed to select a valid item type. Bill Failed")
elif ques7 == "" or "N" :
    print(f"Thank you, your final bill {bill1+bill2+bill3+bill4+bill5+bill6+bill7}")
    exit()

ques8 = input("Do you wish to proceed further (Y for yes / N for no) : ")
if ques8 == "Y" :
    item9 = input("Enter ninth item on the list : ")
    price9 = float(input("Enter the price of the item : "))
    quant9 = int(input("Enter the quantity : "))
    type9 = input("Enter type of item (F for food , B for beverage , O for other) : ")
    while type9 == "" :
        print("It is mandatory to select food type!")
        type9 = input("Enter type of item (F for food , B for beverage , O for other) : ")
    if type9 == "F" :
        gst9 = price9 + 1.10
        bill9 = quant9 * gst9 
        print(f"You bought {quant9} {item9}. Your bill for item 9 is {bill9} ")
    elif type9 == "B" :
        gst9 = price9 + 0.70
        bill9 = quant9 * gst9
        print(f"You bought {quant9} {item9}. Your bill for item 9 is {bill9} ")
    elif type9 == "O" :
        gst9 = price9 + 0.90
        bill9 = quant9 * gst9 
        print(f"You bought {quant9} {item9}. Your bill for item 9 is {bill9} ")
    else :
        print("You failed to select a valid item type. Bill Failed")
elif ques8 == "" or "N" :
    print(f"Thank you, your final bill {bill1+bill2+bill3+bill4+bill5+bill6+bill7+bill8}")
    exit()

ques9 = input("Do you wish to proceed further (Y for yes / N for no) : ")
if ques9 == "Y" :
    item10 = input("Enter tenth item on the list : ")
    price10 = float(input("Enter the price of the item : "))
    quant10 = int(input("Enter the quantity : "))
    type10 = input("Enter type of item (F for food , B for beverage , O for other) : ")
    while type10 == "" :
        print("It is mandatory to select food type!")
        type10 = input("Enter type of item (F for food , B for beverage , O for other) : ")
    if type10 == "F" :
        gst10 = price10 + 1.10
        bill10 = quant10 * gst10 
        print(f"You bought {quant10} {item10}. Your bill for item 10 is {bill10} ")
    elif type10 == "B" :
        gst10 = price10 + 0.70
        bill10 = quant10 * gst10
        print(f"You bought {quant10} {item10}. Your bill for item 10 is {bill10} ")
    elif type10 == "O" :
        gst10 = price10 + 0.90
        bill10 = quant10 * gst10 
        print(f"You bought {quant10} {item10}. Your bill for item 10 is {bill10} ")
    else :
        print("You failed to select a valid item type. Bill Failed")
elif ques9 == "" or "N" :
    print(f"Thank you, your final bill {bill1+bill2+bill3+bill4+bill5+bill6+bill7+bill8+bill9}")
    exit()

print(f"Thank you {user} for shopping with us. Your final bill is {bill1+bill2+bill3+bill4+bill5+bill6+bill7+bill8+bill9+bill10}")


