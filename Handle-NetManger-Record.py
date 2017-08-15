#!/usr/bin/env python
# coding=utf-8


"""  Task 1: Analyze exported NetManager database records for all switch connections and re-format them into switch port description commands


"""

# Function: Switch-Port-Numbers (#Switch, #Port)
#Return: #Switch-Number and #Port-Number
	
		# Switch type 1: 3524		
			
		# Switch type 2: 4000/4005 with CatOS
			
		# Switch type 3: 3550
			
		# Switch type 4: 2960
			
		# Switch type 5: 3750
			
		# Switch type 6: 3850
	
# End of Function: Switch-Port-Numbers (#Switch, #Port)
	
# Function: Switch-Conf-Command (#Switch-Number, #Port-Number)
# Return: #Switch-Conf-Command
	
		# Switch type 1: 3524		
			
		# Switch type 2: 4000/4005 with CatOS
			
		# Switch type 3: 3550
			
		# Switch type 4: 2960
			
		# Switch type 5: 3750
			
		# Switch type 6: 3850
	
# End of Function: Switch-Conf-Command (#Switch-Number, #Port-Number)
		
# Function: Handle-Record 
# Process the records from connections.txt. 
		
    # Find and open file:connections.txt
		
    # Process every record from connections.txt
		
    # Read the record
		
        # If the record is not for switch connection (starting with Sxxx), skip to the next record. 
		
	# Split the record to a list:
	#(#Switch,#Port,#Building,#Facility,#RoomNumber,#Extension,#Jack Number,#CampusUnit)
		
	# Process #Switch and #Port to get the proper Switch and Port number
	# Call: Switch-Port-Numbers (#Switch, #Port)
	# Return: #Switch-Number and #Port-Number
		
	# Check if the #Switch-Number.cfg file has been opened for appending
		
	# If not, open it
		
	# If #Switch-Number is not the same as last record, 
		
	    #Close current switch configuration file
	    #Open a new siwtch configuraiton file: #Switch-Number.cfg
		
	# Format the switch interface configuration command based on the switch type
	# Call: Switch-Conf-Command (#Switch-Number, #Port-Number)
	# Return: #Switch-conf-Command
					
	# Appending the following line to the #Switch-Number.cfg file: 
	# interface #Port-Number
	# description #Switch-Conf-Command 
	
# End of Function: Handle-Record 
