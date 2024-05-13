#Importing
import random
from datetime import datetime
from Main import d


def displayLandStatus(vali_id):
    #Opening the file in read mode
    file_path = "land.txt"
    file= open(file_path, "r")
    lines = file.readlines()

    #Update the status of land with the given vali_id
    for i, line in enumerate(lines):
        parts = line.strip().split(",")
        if parts[0] == vali_id:
            parts[-1] = "Not Available"  #As Status is in last -1 was used to access it
            lines[i] = ",".join(parts) + "\n"

    #Writing the updated content back to land.txt file
    file= open(file_path, "w")
    file.writelines(lines)
    file.close()

def printingBillintxt(custName,custPhno,bills,time):
    from Main import d
    random_number=random.randint(1,99999999)
    grandTotalRent=0
    file_bill= open("rent_invoice/"+str(random_number)+"_"+custName.replace(' ', '_')+".txt", "w")
    file_bill.write("\t\t\t\t\t\t\tRENT INVOICE\n\n")
    file_bill.write("Name: " + custName + "\n")
    file_bill.write("Phone number: " + custPhno + "\n")
    file_bill.write("Invoice ID NO:"+str(random_number))
    file_bill.write("\nID\t\tDistrict\tDirection\t\tAnna\t\tPrice\t\tMonths\n")
    file_bill.write("---------------------------------------------------------------------------------------------------------------\n")

    for item in bills:
        vali_id = item['vali_id']
        months = item['desiredMonth']
        district = d[vali_id]['city']
        direction = d[vali_id]['direction']
        anna = d[vali_id]['aana']
        price_per_month = float(d[vali_id]['price'])
        price = price_per_month * months

        file_bill.write(str(vali_id) + "\t\t" + district + "\t" + direction + "\t\t\t" + str(anna) + "\tRs." + str(price) + "\t\t" + str(months) + "\n")
        grandTotalRent += price 

    file_bill.write("---------------------------------------------------------------------------------------------------------------\n")
    file_bill.write("Net Total: Rs" + str(grandTotalRent) + "\n")
    file_bill.write("Invoice Generated: "+str(time)+"\n")
    file_bill.write("---------------------------------------------------------------------------------------------------------------\n")
    file_bill.close()

def displayLandStatusReturn(vali_no):
    # Open the file in read mode
    file_path = "land.txt"
    file= open(file_path, "r")
    lines = file.readlines()

    #Update the status of the land with the given ID
    for i, line in enumerate(lines):
        parts = line.strip().split(",")
        if parts[0] == vali_no:
            parts[-1] = "Available" 
            lines[i] = ",".join(parts) + "\n"

    # Write the updated content back to the file
    file= open(file_path, "w")
    file.writelines(lines)
    file.close()
        
def printingBillintxtforReturn(returnbill):
    #Inializing the variable before use
    random_number = random.randint(1, 999999999)
    grandTotalReturn = 0
    fine_total=0
    overGrandTotalReturn = 0

    #File path and name to create the file
    file_bill= open("return_invoice/" + str(random_number) + "_" + returnbill[0]['name'].replace(' ', '_') + ".txt", "w")
    file_bill.write("\t\t\t\t\t\t\t RETURN INVOICE\n\n")
    file_bill.write("Name: " + returnbill[0]['name'] + "\n")
    file_bill.write("Phone number: " + returnbill[0]['phno'] + "\n")
    file_bill.write("Invoice ID NO:"+str(random_number))
    file_bill.write("\nID\t\tDistrict\tAana\t\tDesired Month\tActual Rented Months\t\tPrice per month\t\tFine\n")
    file_bill.write("-------------------------------------------------------------------------------------------------------------------------------------------\n")
    #Extracting the values from returnbill list
    for item in returnbill:
        vali_id = item['kitta_no']
        months = item['desiredMonth']
        finalmonths = item['actualMonth']
        city = d[vali_id]['city']
        aana = d[vali_id]['aana']
        price_per_month = float(d[vali_id]['price'])
        price = price_per_month * finalmonths
        fine = item['fine']
        grandTotalReturn+=item['price']
        fine_total+=item['fine']
        
        #Printing in invoice
        file_bill.write(str(vali_id) + "\t\t" + str(city) + "\t" + str(aana) + "\t\t\t" + str(
            months) + "\t\t\t" + str(finalmonths) + "\t\tRs." + str(price) + "\t\t" + str(fine) + "\n")
    #Calculation of total cost
    overGrandTotalReturn = grandTotalReturn + fine_total

    time = datetime.now()
    file_bill.write("-------------------------------------------------------------------------------------------------------------------------------------------\n")
    file_bill.write("Net Total: Rs" + str(overGrandTotalReturn) + "\n")
    file_bill.write("Invoice Generated: " + str(time) + "\n")
    file_bill.write("---------------------------------------------------------------------------------------------------------------\n")
    file_bill.close()