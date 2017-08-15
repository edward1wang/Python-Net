# Python-Net

This is my first Python project. I will use this to learn Python and to create some Python scripts to improve our workflow. 

Currently this is a gap between our NetManager and ForeScout NAC system. If anyone (us, InfoSec, or Help Centre) wants to track down a wired connection, he/she has to look at NAC first to find the switch port information, then check NetManager for physical location information (building, room, and jack numbers). 

I am planning to create few Python scripts to do the following: 

	1. Analyze exported NetManager database records for all switch connections and re-format them into switch port description commands
	
	2. Update all switches with new port description commands
	
	3. Capture daily changes on NetManager data and apply switch port changes automatically

The end result: full detailed connection information can be found on ForeScout NAC. 
