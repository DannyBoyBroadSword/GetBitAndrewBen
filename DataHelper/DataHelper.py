import glob



def dataHeap(name):
    name_buffer = []
    f = open(name,'r')
    for lines in f:
        name_buffer.append(lines)
    people = name_buffer[0]
    people = people.split(',')
    winner = name_buffer[-1]
    winner = winner.split(',')
    try:
        print(str(people.index(winner[0]))+",")
    except:
        print("Not in List")
        
   
    #print("Starting five " + str(name_buffer[0])+ "Guess who won: " +str(name_buffer[-1]))
winners_index =[]

for names in glob.glob("/Users/andrewhennessy/Desktop/GetBitDAta/*.txt"):
    name_buffer = []
    f = open(names,'r')
    for lines in f:
        name_buffer.append(lines)
    people = name_buffer[0]
    people = people.split(',')
    winner = name_buffer[-1]
    winner = winner.split(',')
    try:
        winners_index.append(people.index(winner[0]))
    except:
        print("Not in List")

    

        
