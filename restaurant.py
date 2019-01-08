rez = 3 #number of months in advance reservation was made
choice = "veg"

if rez >= 2:
    print ("you may enter!")

    if choice == "mix":
        print ("you get a mix of meats and vegetables")
    elif choice == "meat":
        print ("you get meat")
    elif choice == "veg":
        print ("you get veg")
    else: print ("you will eat air")

else: print ("Sorry, you didn't make a reservation at least two months ago.")
