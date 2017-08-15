# Python-Net

This is my first Python project. I will use this to learn Python and to create some Python scripts to improve our workflow. 

Currently this is a gap between our NetManager and ForeScout NAC system. If anyone (us, InfoSec, or Help Centre) wants to track down a wired connection, he/she has to look at NAC first to find the switch port information, then check NetManager for physical location information (building, room, and jack numbers). 

I am planning to create few Python scripts to do the following: 

	1. Analyze exported NetManager database records for all switch connections and re-format them into switch port description commands
	
	2. Update all switches with new port description commands
	
	3. Capture daily changes on NetManager data and apply switch port changes automatically

The end result: full detailed connection information can be found on ForeScout NAC. 


Task 1: Analyze exported NetManager database records for all switch connections and re-format them into switch port description commands
	
	Format of CSV file exported from NetManager database: 
	
	[dawang@charybdis netmanager]$ pwd
		/home/ip-tracking/netmanager
	[dawang@charybdis netmanager]$ ls -lh 
		total 2.7M
		-rwxrwxrwx 1 root   root     2.5M Aug 15 06:00 connections.txt
		-rwxrwxrwx 1 root   root      200 Mar  4  2009 connection.txt.note
		-rw-r--r-- 1 root   root     5.4K Jan 26  2010 ITAdmins.csv
		-rw-rw-r-- 1 nsc    nsc      4.7K Aug 15 06:00 lanadmins.txt
		-rwxrwxrwx 1 root   root     188K Aug 15 06:00 switches.txt
		-rw-r--r-- 1 dawang ccsstaff   57 Mar 10  2009 test

	[dawang@charybdis netmanager]$ more connection.txt.note
		Switch,Port,Building,Facility,Room Number,Extension,Jack Number,Campus Unit
	
	[dawang@charybdis netmanager]$ more connections.txt 
		
	Switch Type 1: 3524
		S753,3,72,South Residence (Complex B),0,Unknown/Undefined,321B,,0-01-23,0013,Student Housing Services
		S653,9,180,East Residence,310,Dundas,231,72004,,0013,Student Housing Services
		S579,17,300,78 College Ave,427,78 College W.,18,226-971-1970,,300,Family Housing Services
		
		S726_RPC(240)_MainFloor#conf terminal
		S726_RPC(240)_MainFloor(conf)#int fa0/10
		S726_RPC(240)_MainFloor(conf)#description ?
  		LINE  A character string describing this interface

		
	Switch Type 2: WS-C4006 Software, Version NmpSW: 8.4(10)GLX
		S1130_3,33,142,Rozanski Hall,0,Unknown/Undefined,107,,01-02-B33,0080,Office of Registrarial Services
		
		S1130_ROZH(142)r144> (enable) set port name 3/33 Rozanski Hall,0,Unknown/Undefined,107,
		Name string must be less than 21 characters.
		
		
	Switch Type 3: C3550 Software (C3550-IPBASEK9-M), Version 12.2(35)SE5, RELEASE SOFTWARE (fc1)
	
		S1236,14,35,Zoology Annex #2,0,Unknown/Undefined,101,,0A-A27,0158,Biological Science-Dean's Office
		
		S1236_ZooAn#2(35)L2#conf terminal
		S1236_ZooAn#2(35)L2(config)#int fa0/14
		S1236_ZooAn#2(35)L2(config-if)#description ?
  		LINE  Up to 240 characters describing this interface
		
	Swith Type 4: WS-C2960S-48FPD-L 
	
		S1302_2,21,21,Zavitz Hall,0,Unknown/Undefined,313,,1A-D05,0064,CCS-Networking Services
		
		S1302_ZAV(21)1A#conf terminal 
		S1302_ZAV(21)1A(config)#int gi2/0/21
		S1302_ZAV(21)1A(config-if)#description ?
  		LINE  Up to 240 characters describing this interface
		
	Switch Type 5: C3750E Software (C3750E-IPBASEK9-M), Version 15.0(1)SE3, RELEASE SOFTWARE (fc1)
	
		S1482_1,46,7,Creelman Hall,0,Unknown/Undefined,SRVR,,2A-A40,0014,Hospitality Services
		
		S1482_CREEL(007)2A#conf terminal 
		S1482_CREEL(007)2A(config)#int gi1/0/46
		S1482_CREEL(007)2A(config-if)#description ?
  		LINE  Up to 200 characters describing this interface
		
	Switch Type 6: WS-C3850-48P 
		IOS-XE Software, Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Version 03.06.05E RELEASE SOFTWARE (fc2)
		S1522_1,48,180,East Residence,310,Dundas,317,72083,,0013,Student Housing Services
		S1611_2,7,140,Science Complex,0,Unknown/Undefined,4464,,4B-C07,0158,Biological Science-Dean's Office
		
		S1522_East_Dundas2-4#conf terminal 
		S1522_East_Dundas2-4(config)#int gi1/0/48
		S1522_East_Dundas2-4(config-if)#description ?
  		LINE  Up to 200 characters describing this interface
		
	Switch Type 7: 4948
		S1804,C3548-EN,00:02:16:4B:B9:40,192.168.132.107,Animal Science-Nutrition,033,Cabinet - Srv-C3 Grid - H3,70
	
	
	We will use the following information: 
		Building,Facility,Room Number,Jack Number,Campus Unit
	
	At following format for all IOS switches (up to 200 characters): 
	
Building:#Building,Facility:#Facility,RoomNumber:#RoomNumber,JackNumber:#JackNumber,CampusUnit:#CampusUnit,Comments:#CurrentDes
		
	At following format for CatOS switches (Name string must be less than 21 characters.)
		#RoomNumber,#JackNumber,#CurrentDes
		
		
		
	
	# Function: Switch-Port-Numbers (#Switch, #Port)
	#	Return: #Switch-Number and #Port-Number
	
		# Switch type 1: 3524		
			
		# Switch type 2: 4000/4005 with CatOS
			
		# Switch type 3: 3550
			
		# Switch type 4: 2960
			
		# Switch type 5: 3750
			
		# Switch type 6: 3850
	
	# End of Function: Switch-Port-Numbers (#Switch, #Port)
	
	# Function: Switch-Conf-Command (#Switch-Number, #Port-Number)
	# 	Return: #Switch-Conf-Command
	
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
			(#Switch,#Port,#Building,#Facility,#RoomNumber,#Extension,#Jack Number,#CampusUnit)
		
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
		
Task 2: Update all switches with new port description commands


Task 3: Capture daily changes on NetManager data and apply switch port changes automatically

