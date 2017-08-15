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
		
	Switch Type 1: 
		S753,3,72,South Residence (Complex B),0,Unknown/Undefined,321B,,0-01-23,0013,Student Housing Services
		
	Switch Type 2: 
		S1130_3,33,142,Rozanski Hall,0,Unknown/Undefined,107,,01-02-B33,0080,Office of Registrarial Services
		
	Switch Type 3: 
		S1236,14,35,Zoology Annex #2,0,Unknown/Undefined,101,,0A-A27,0158,Biological Science-Dean's Office
		
	Swith Type 4: 
		S1302_2,21,21,Zavitz Hall,0,Unknown/Undefined,313,,1A-D05,0064,CCS-Networking Services
		
	Switch Type 5: 
		S1482_1,46,7,Creelman Hall,0,Unknown/Undefined,SRVR,,2A-A40,0014,Hospitality Services
		
	Switch Type 6: 
		S1522_1,48,180,East Residence,310,Dundas,317,72083,,0013,Student Housing Services
		
	Switch Type 7: 
		S1611_2,7,140,Science Complex,0,Unknown/Undefined,4464,,4B-C07,0158,Biological Science-Dean's Office
		
		
	
Task 2: Update all switches with new port description commands


Task 3: Capture daily changes on NetManager data and apply switch port changes automatically

