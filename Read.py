#This function is used to display the information of lands
def displayLand():
    from Main import d
    file = open("land.txt", "r")
    for line in file:
    
            print(line.replace(",", "\t\t"))
            parts = line.strip().split(",")
        
            #Extracting information from parts
            land_id = parts[0]
            city = parts[1]
            direction = parts[2]
            aana = int(parts[3])
            cost = float(parts[4])
            status = parts[5]
            
            #Creating a dictionary to store the property details
            property_details = {
                "city": city,
                "direction": direction,
                "aana": aana,
                "price": cost,
                "status": status
            }
            
            #Using land_id as a key to access property_details
            d[land_id] = property_details
            
    file.close()
    print()