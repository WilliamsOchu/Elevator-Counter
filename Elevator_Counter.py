## Elevator Counter
## This program will yield an elevator counter to show how many steps up or down you will be going 

def elevator():
    # Initiate the variables for entry and exit 
    entry=int(input("Entry Floor: "))
    exit=int(input("Exit Floor: "))
    count=entry
    
    # Initiate a variable to show the direction 
    direction=""
    
    if entry < exit:
        direction=direction+"You are Going Up!!!"
        print(direction)
        
        # Now initiate a count loop
        while count<exit:
            remaining_steps=exit-count
            print("You are now on floor " + str(count) + " you have " + str(remaining_steps) + " floors before destination")
            count=count+1
        if count==exit:
            print("We have arrived at your destintion floor: " + "\033[1m" + str(count) + "!!!" + "\033[0m")
    
    ## Now let us setup a downward movement
    
    if entry>exit:
        direction=direction+"We are going Down!!!"
        print(direction)    
        
        # We initiate a count loop for dwonward movement
        while count>exit:
            remaining_steps=count-exit
            print("You are now on floor " + str(count) + " you have " + str(remaining_steps) + " floors before destination")
            count=count-1
        if count==exit:
            print("We have arrived at your destination floor: " + "\033[1m" + str(count) + "!!!" + "\033[0m") 
            
elevator()  
        
    
    
    
