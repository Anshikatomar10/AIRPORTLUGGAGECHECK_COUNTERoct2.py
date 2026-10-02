#AIRPORT LUGGAGE CHECK COUNTER :
#PROBLEM REQUIREMENTS ;1.THE MAIN LOOP :run continuously until an agent types "end" for the passenger's
#name.  #THE SAFE EXIT CHECK : accept the passenger's name as the string and check for "end" before asking 
#for any numbers .   
#THE VALIDATION LOOP : ask for the ticket class (first,business,or economy). If they type anything else ,use
#a while loop to repeatedly tell them "invalid class,try again" until they enter a valid option.
# LUGGAE MATH :
#promt for the luggage weight in kilograms .
#every class gets a free weight limit :first (40kg),business (30kg),economy(20kg).
#if the luggage is over the limit , charge a penalty fee of $15.00 per excess kg .
#DUAL ACCUMULATORS :track 2 thing across the entire day .
#total_penalty_revenue (sum of all excess weight fees charged),total_excess_weight (sum of all overweight kg
#  processed).  FINAL OUTPUT :when the main loop ends ,print both final totals seprately .
total_excess_weight = 0
total_penalty_revenue = 0 
#the main loop runs continuously until "end" is typed for the passenger's name .
while True:
    #take passenger's name as a string .
    flier_name = str(input("enter flier name (or enter 'end' to end the shift ) :"))
    #to make the loop end exactly when the user types "end" check for end before asking for any numbers .
    if flier_name.lower().strip() == "end":
        break
    # intialize allowed weight variable .
    weight_allowed = 0
    # now set up a loop that repeatedly asks for the ticket class until the entered class is valid .
    while True:
        flier_class = str(input("enter ticket class (first,business or economy)"))
        class_clean = flier_class.lower().strip()
        if class_clean =="first":
            weight_allowed = 40
            break
        elif class_clean == "business":
            weight_allowed = 30
            break
        elif class_clean == "economy":
            weight_allowed = 20 
            break
        else:
            print("invalid class, try again")

    #now take luggage weight as an input in float.
    actual_weight = float(input("enter luggage weight in kg")) 

    # calculate excess weigt if it exceeds the weight limit .
    if actual_weight > weight_allowed:
         excess_weight = actual_weight - weight_allowed
         penalty = excess_weight*15.00
    #update dual accumulators.
         total_excess_weight += excess_weight
         total_penalty_revenue += penalty
    else:
         excess_weight = 0
         penalty = 0
    print("your extra weight is :", excess_weight,"kg")
    print("your penalty is :$",penalty)
 #final output print both final output after the final loop ends .

print("total excess weight :",total_excess_weight, "kg")
print("total penalty revenue :$",total_penalty_revenue)        


     
           

