from datetime import datetime

'''
Creating a empty list for storing values 
bills for renting process
returing for returning process
'''
bills=[]
returnbill = []

#Giving user option to implement it
def select_Option():
    print()
    print("Select the desired option.")
    print("(1) Press '1' for renting the land ")
    print("(2) Press '2' for returning the land ")
    print("(3) Press '3' for exit")
    op = input("Enter the desired option: ")
    
    #Typecast string to int 'op'
    try:
        if op.isdigit():
            op = int(op)
            if op == 1:
                rent()
            elif op == 2:
                return_()
            elif op == 3:
                exit_()
            else:
                print("Invalid option! Please enter a number between 1 and 3.")
                select_Option()
        else:
            print("Invalid input! Please enter a number.")
            select_Option()
    except Exception as e:
        print("Error occurred:", e)
        print("Please try again.")
        select_Option()

        
#Table to display available lands
def desc():
    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("KITTA NO.\t CITY\t\t\t DIRECTION\t ANNA\t\t COST\t\t Status")
    print("-------------------------------------------------------------------------------------------------------------------------------")

def rent():
    from Read import displayLand
    from Write import displayLandStatus,printingBillintxt
    from Main import d
    desc()
    displayLand()
    
    #Extractiong all the keys values of d in a list to a veri
    veri=list(d.keys())
    
    while True:
        try: 
            #Asking user's input
            vali_id= input("Enter Desired Land's Kitta no: ")
            
            #Verifiying whether the vali_id is in the veri list or not
            if vali_id in veri:
                print("----------------------------------------------------------------")
                print("Land Kitta no. Found!!")
                print("----------------------------------------------------------------")
                break
            else:
                print("----------------------------------------------------------------")
                print("Invalid Land Kitta no!!")
                print("----------------------------------------------------------------")
        except:
            print("----------------------------------------------------------------")
            print("Land Kitta no must be in numberr!!")
            print("----------------------------------------------------------------")
    #Checking the land status if we can rent or not
    if d[vali_id]['status']=="Available":
        try: 
            print("----------------------------------------------------------------")
            custName= str(input("Enter your Name: "))
            print("----------------------------------------------------------------")
            print()
                    
        except:
            print("----------------------------------------------------------------")
            print("Enter your name alphabetically!!")
            print("----------------------------------------------------------------")
        
        while True:
            try:
                print("----------------------------------------------------------------")
                custPhno= input("Enter your Phone Number: ")
                print("----------------------------------------------------------------")
                print()
                #Length of the custPhno must be 10 while renting
                if len(custPhno)!=10:
                    print("----------------------------------------------------------------")
                    print("The phone number should be atleast 10 digits.")
                    print("----------------------------------------------------------------")
                else:
                    print("----------------------------------------------------------------")
                    print("\t\t\tSuccess!!")
                    print("----------------------------------------------------------------")  
                    break   
            except:
                print("----------------------------------------------------------------")
                print("The phone number should be in numberr!")
                print("----------------------------------------------------------------")
            
        while True:        
            try:
                desiredAana=int(input("Enter the land's aana you are desired to rent: "))
                selected_item=d[vali_id]
                #Comparing the aana with the land's 
                #You cannot take greater or smaller aana of land you should completely rent whole one
                if(selected_item['aana']==desiredAana):
                    print("----------------------------------------------------------------")
                    print("\t\t\tSuccess!!")
                    print("----------------------------------------------------------------")
                    break
                else:
                    print("----------------------------------------------------------------")
                    print("You can only rent whole landd!!")
                    print("----------------------------------------------------------------")
            except:
                print("----------------------------------------------------------------")
                print("Enter only numbers correct month value!!")
                print("----------------------------------------------------------------")
            
        try:
            desiredMonth=int(input("Enter the month you desired to rent up to: "))
            print()
        except:
            print("----------------------------------------------------------------")
            print("Enter only numbers correct month value!!")
            print("----------------------------------------------------------------")


        selected_item=d[vali_id]
        totalcost=selected_item['price']*desiredMonth
        grandTotal=0
        time=datetime.now()
        #Storing the inputs to bills list 
        bills.append({'vali_id':vali_id,
                'city':selected_item['city'],
                'direction':selected_item['direction'],
                'aana':selected_item['aana'],
                'desiredMonth':desiredMonth,
                'totalCost':totalcost,
                'Name':custName,
                'Phno':custPhno,
                'desiredAana':desiredAana,
                'desiredMonth':desiredMonth
                })
        #Changing the status of land to "Not Available"
        displayLandStatus(vali_id)
        
        print("----------------------------------------------------------------")
        #Want to rent more?
        while True:
            rent_choice=input("Do you want to rent more lands?(yes/no)").lower()
            if rent_choice=="yes":
                print()
                print("*********************USE THE SAME NAME AND PHONE NUMBER*********************")
                print()
                
                rent()
            elif rent_choice=="no":
                #Printing the invoice to console or terminal and text file
                printRentingBills(bills,grandTotal,time)
                printingBillintxt(custName, custPhno, bills,time)
                #Also displaying message
                print("Rented Successfully!!")
                break
            else:
                print("Input correctly!")
            
    else:
        print("----------------------------------------------------------------")
        print("The land is not available at the moment!!")
        print("----------------------------------------------------------------")
        rent()
    #Calling the function for next steps
    select_Option()

#This function prints the invoice of renting on an terminal or console
def printRentingBills(bills,grandTotal,time):
    print()
    print("Printing bill: ")
    print()
    print("____________________________________________________________________________________________________________________________________________________________________________________")
    print("\t\t\t\t\t\t\t\t\t\t\tLand Rental Service")
    print("")
    print("\t\t\t\t\t\t\t\t\t\tDhumbharahi, Kathmandu | Ph. no. 98876543210")
    print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print()
    print("\nLand Owner: "+ str(bills[0]['Name']))
    print("\nLand Owner Phone Number: "+ str(bills[0]['Phno']))
    print("\nLand Renting Date: "+str(time))
    print()
    print()
    print("\nLand Details: ")
    print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\nKitta no. \t\t\t City \t\t\t Direction \t\t\t Aana \t\t\t Rented Month \t\t\t Total Price")
    print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    #Extracting inputs and datas from bills list 
    for each in bills:
        print("\n"+str(each['vali_id'])+"\t\t\t\t"+str(each['city'])+"\t\t\t"
              +str(each['direction'])+"\t\t\t\t"+str(each['aana'])+"\t\t\t\t"+
              str(each['desiredMonth'])+"\t\t\t"+str(each['totalCost']))
        grandTotal+=each['totalCost']
    print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Grand Total")
    #Grand total cost
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"+str(grandTotal))
    print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n\t\t\t\t\t\t\t\t\t\tThank you for visiting us!")
    print("\n\t\t\t\t\t\t\t\t\tLooking for giving more services to you in future.")
    print("\n____________________________________________________________________________________________________________________________________________________________________________________")

#This function is used to return the land that has been rented
def return_():
    from Write import displayLandStatusReturn, printingBillintxtforReturn
    from Read import displayLand
    from Main import d
    print()
    desc()
    displayLand()
    verifi = list(d.keys())
    while True:
        try:
            vali_no = input("Enter Land's Kitta no: ")
            if vali_no in verifi:
                print("Kitta no is found!")

                if d[vali_no]['status'] == "Available":
                    print("----------------------------------------------------------------")
                    #Using formatted String to print the message
                    print(f"Land Kitta no. {vali_no} cannot be returned!! Check the details carefully!!")
                    print("----------------------------------------------------------------")
                    return_()

                elif d[vali_no]['status'] == "Not Available":
                    print()
                    while True:
                        try:
                            returnName = input("Enter your Name that was on Rented Invoice: ")
                            found = False
                            for bill in bills:
                                if bill['Name'] == returnName:
                                    found = True
                                    break
                            if found:
                                print("----------------------------------------------------------------")
                                print("Customer Found!!")
                                print("----------------------------------------------------------------")
                                break
                            else:
                                print("----------------------------------------------------------------")
                                print("Customer Not Found!! Error!!!")
                                print("----------------------------------------------------------------")
                        except:
                            print("----------------------------------------------------------------")
                            print("Error! Please enter a valid name.")
                            print("----------------------------------------------------------------")
                    
                    while True:
                        try:
                            print()
                            returnPhno = input("Enter your Phone Number that was on Rented Invoice: ")
                            #Checking the phone number with the rented used phone number and similarly lenght of the number
                            if returnPhno == bills[0]['Phno'] and len(returnPhno) == 10:
                                print("----------------------------------------------------------------")
                                print("Customer Phone Number confirmed!!")
                                print("----------------------------------------------------------------")
                                break
                            else:
                                print("----------------------------------------------------------------")
                                print("Customer Phone Number isn't correct. Check your Invoice again!")
                                print("----------------------------------------------------------------")
                        except:
                            print("----------------------------------------------------------------")
                            print("Error! Please enter a valid phone number.")
                            print("----------------------------------------------------------------")

                    while True:
                        try:
                            print()
                            rentedMonth = input("How many months did you intend to rent the land for? ")
                            #Typecast string to int rentedMonth
                            if rentedMonth.isdigit():
                                rentedMonth = int(rentedMonth)
                                #Also verifiying the desiredMonth to rent with rented invoice's
                                if rentedMonth == bills[0]['desiredMonth']:
                                    print("----------------------------------------------------------------")
                                    print("Yes, same as on Rented Invoice!")
                                    print("----------------------------------------------------------------")
                                    break
                                else:
                                    print("----------------------------------------------------------------")
                                    print("Doesn't match with Rented Invoice!")
                                    print("----------------------------------------------------------------")
                            else:
                                print("----------------------------------------------------------------")
                                print("Rented months must be in number!!")
                                print("----------------------------------------------------------------")
                        except:
                            print("----------------------------------------------------------------")
                            print("Error! Please enter a valid number of months.")
                            print("----------------------------------------------------------------")
                    
                    while True:
                        try:
                            print()
                            #Same typecast string input to integer actualRentedMonth
                            actualRentedMonth = input("How many months did you actually rent for? ")
                            if actualRentedMonth.isdigit():
                                actualRentedMonth = int(actualRentedMonth)
                                #Fine procedures
                                if actualRentedMonth > rentedMonth:
                                    print("----------------------------------------------------------------")
                                    print("Ok! You will get fined 30% per month for not returning in time.")
                                    print("----------------------------------------------------------------")
                                    break
                                elif actualRentedMonth < rentedMonth:
                                    print("----------------------------------------------------------------")
                                    print("Ok! Although you returned earlier than the date on Rented Invoice, you will have to pay the same.")
                                    print("*******************************************************************")
                                    print("For any queries, you can get help from our Customer Support.\n\t\t\t 01xxxxxx6")
                                    print("*******************************************************************")
                                    print("----------------------------------------------------------------")
                                    break
                                else:
                                    print("----------------------------------------------------------------")
                                    print(f"Ok! You have returned the land on exact time. Thank you, {returnName}!")
                                    print("----------------------------------------------------------------")
                                    print("----------------------------------------------------------------")
                                    break
                            else:
                                print("----------------------------------------------------------------")
                                print("Error! Please enter a valid number of months.")
                                print("----------------------------------------------------------------")
                        except:
                            print("----------------------------------------------------------------")
                            print("Error! Please enter a valid number of months.")
                            print("----------------------------------------------------------------")
            else:
                print("----------------------------------------------------------------")
                print("Invalid Land Kitta no!!")
                print("----------------------------------------------------------------")
        except:
            print("----------------------------------------------------------------")
            print("Land Kitta no must be a number!!")
            print("----------------------------------------------------------------")
    
        #Initializing the values
        fineMonth = 0
        grandTotalreturn = 0

        current_time = datetime.now()

        #Changing the status to "Available"
        displayLandStatusReturn(vali_no)

        #Fine process
        if actualRentedMonth > rentedMonth:
            fineMonth = actualRentedMonth - rentedMonth

        selected_item = d[vali_no]
        grandTotalreturn = selected_item['price'] * actualRentedMonth
        fine = (fineMonth * 0.3 * grandTotalreturn)

        #Appending every returned land's details to returnbill list
        returnbill.append({'name': returnName,
                        'phno': returnPhno,
                        'desiredMonth': rentedMonth,
                        'actualMonth': actualRentedMonth,
                        'direction': selected_item['direction'],
                        'kitta_no': vali_no,
                        'city': selected_item['city'],
                        'aana': selected_item['aana'],
                        'price': grandTotalreturn,
                        'fine': fine})  
        while True:
            try:
                return_choice = input("Do you want to return more lands?(yes/no): ").strip().lower()
                if return_choice == 'yes':
                    return_()
                elif return_choice == 'no': 
                    #Printing the invoice of returning lands
                    printReturingBills(returnbill, current_time)
                    printingBillintxtforReturn(returnbill)
                    break
                else:
                    print("Enter yes or no! Its so simple bro. (SKILL ISSUE)")

            except Exception as e:
                print("Exception occurred", e)
        select_Option()


# Function to print the return invoice
def printReturingBills(returnbill, current_time):
    print()
    grandTotalreturnwithfine = 0
    grandTotal = 0
    fineTotal = 0
    print("Printing Returning invoice: ")
    print()
    print("____________________________________________________________________________________________________________________________________________________________________________________")
    print("\t\t\t\t\t\t\t\t\t\t\tLand Rental Service")
    print("")
    print("\t\t\t\t\t\t\t\t\t\tDhumbharahi, Kathmandu | Ph. no. 98876543210")
    print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print()
    print("\nLand Owner: " + str(returnbill[0]['name']))
    print("\nLand Owner Phone Number: " + str(returnbill[0]['phno']))
    print("\nLand Returning Date: " + str(current_time))
    print()
    print("\nLand Details: ")
    print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\nKitta no. \t\t City \t\t\t Direction \t\t Aana \t\t Rented Month \t\t Actual Month \t\t Total Price\t\t Fine")
    print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for returnbilleach in returnbill:    
        print("\n" + str(returnbilleach['kitta_no']) + "\t\t\t" + str(returnbilleach['city']) + "\t\t"
              + str(returnbilleach['direction']) + "\t\t" + str(returnbilleach['aana']) + "\t\t\t" 
              + str(returnbilleach['desiredMonth']) + "\t\t\t" + str(returnbilleach['actualMonth']) + 
              "\t\t\t" + str(returnbilleach['price']) + "\t\t" + str(returnbilleach['fine']))
        grandTotal += returnbilleach['price']
        fineTotal += returnbilleach['fine']

    grandTotalreturnwithfine = grandTotal + fineTotal

    print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Grand Total")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(grandTotalreturnwithfine))
    print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n\t\t\t\t\t\t\t\t\t\tThank you for visiting us!")
    print("\n\t\t\t\t\t\t\t\t\tLooking for giving more services to you in future.")
    print("\n____________________________________________________________________________________________________________________________________________________________________________________")
    
#Function to exit the program and display approiate message before exiting
def exit_():
    import sys
    sys.exit("Thank you!! For Using the Application! Have a great day :)")