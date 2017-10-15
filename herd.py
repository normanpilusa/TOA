

def selected(total_feed, total_water, pc, ps, pg, fc, fs, fg, wc, ws, wg):
	#Maximum per animal type
	max_cattle = int(total_feed//pc) #This is integer division
	max_sheep = int(total_feed//ps)
	max_goats = int(total_feed//pg)

	#Store optimal animal combination into array
	animals = ""
	max_profit = 0

	#Select cattle
	for cattle in range (max_cattle):
		#Select sheep
		for sheep in range (max_sheep):
			#Select goats
			for goats in range(max_goats):
				feed = cattle*fc + sheep*fs + goats*fg
				water = cattle*wc + sheep*ws + goats*wg
				profit = cattle*pc + sheep*ps + goats*pg
				
				if feed > total_feed or water > total_water:
					break #Exceed available resources
				elif profit > max_profit :
					max_profit = profit
					animals = str(cattle) +" "+ str(sheep) +" "+  str(goats)+"\n" #Resets the selected animals
	return animals

	
if __name__ == '__main__':
	#Get the string of animal profits
	profits = raw_input()
	profits = profits.split(' ')
	
	#Gets string of feed
	feed = float(raw_input())
	
	#Gets string of animal feeds
	feeds = raw_input()
	feeds = feeds.split(' ')
	
	#Gets string of water
	water = float(raw_input())
	
	#Gets string of animal waters
	waters = raw_input()
	waters = waters.split(' ')
	
	optimal = selected(feed, water, float(profits[0]), float(profits[1]), float(profits[2]), float(feeds[0]), float(feeds[1]), float(feeds[2]), float(waters[0]), float(waters[1]), float(waters[2]),)
	
	print optimal