import csv
import sys
import matplotlib.pyplot as plt
import unittest


# Retrieve the details for the top ranked song for a particular day 
def topRankerdSongPerDay():
    print("Top ranked song for a particular day\n")
    with open('charts.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)

        data = list(filter(lambda x: x[1]=='1', reader))

        param = input("Please enter a date. eg: 1958-10-20 : ")

        for d in data:
            if(d[0] == param):
                print("Top rank song on {} is {} by {}".format(d[0],d[2],d[3]))

# Retrieve the details of the artist with the most top ranked songs 
def artistWithMostTopRanked():
    print("Artist with the most top ranked songs: ")
    with open('charts.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)


        data = list(filter(lambda x: x[1]=='1', reader))

        artists = []
        for d in data:
            artists.append(d[3])

        most_artist = (sorted(artists, key=lambda x: artists.count(x), reverse=True)[0])    
        print(most_artist)

# Retrieve the details of the 10 songs with the longest number of weeks on the board
def songsWithTheLongestNumberOfWeeks():
    print("10 songs with the longest number of weeks on the board\n")
    with open('charts.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)

        data = []

        for d in reader:
            data.append(d) 

        data.pop(0)         

        data.sort(key=lambda x:int(x[6]),reverse=True)

        for d in data[0:10]:
            print("{} times - {} by {}".format(d[6], d[2], d[3]))  

# Retrieve the song that has moved the most in ranking on the board
def songThatHasMovedTheMostInRanking():
    print("Song that has moved the most in ranking on the board\n")
    with open('charts.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)

        data = []

        for d in reader:
            data.append(d) 

        data.pop(0)  

        newData = []

        for d in data:
            if d[4] and d[1]:
                d.append(int(d[4]) - int(d[1]))
                
                if d[7] > 0:
                    newData.append(d)

        sortedList = sorted(newData, key = lambda x: int(x[7]),reverse=True)

        for d in sortedList[0:10]:
            print("{} times moved the most in ranking - {} by {}".format(d[7], d[2], d[3]))          

# Visualise the top songs
def visualiseTheTopSongs():
    print("Visualise the top songs in a month\n")
    with open('charts.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)

        data = list(filter(lambda x: x[1]=='1', reader))

        year = input("Please enter a year. eg: 1958 : ")
        month = input("Please enter a month. eg: 06 : " )

        sorted_values = []

        for d in data:
            if(d[0].split("-")[0] == year and d[0].split("-")[1] == month):
                song = d[2] + d[3]
                sorted_values.append([song])
                print("Top rank song on {} is {} by {}".format(d[0],d[2],d[3])) 

        fig, ax = plt.subplots() 
        table = ax.table(cellText=sorted_values, loc='center') 

        #modify table
        table.auto_set_font_size(False)
        table.set_fontsize(14)
        table.scale(1.5,1.5)
        ax.axis('tight')
        ax.axis('off')

        #display table
        plt.show()

def main():
    print("COM709 Assessment -Designing and Developing Computer Programs")
    print("--------------------------------------------------------------")

    print("""
      1: Retrieve the details for the top ranked song for a particular day
      2: Retrieve the details of the artist with the most top ranked songs
      3: Retrieve the details of the 10 songs with the longest number of weeks on the board
      4: Retrieve the song that has moved the most in ranking on the board
      5: Visualise the top songs
      0: Exit \n""")

    param = input("Please select a option : ")

    match param:
        case "1":
            topRankerdSongPerDay()

        case "2":
            artistWithMostTopRanked()

        case "3":
            songsWithTheLongestNumberOfWeeks()
        
        case "4":
            songThatHasMovedTheMostInRanking()

        case "5":
            visualiseTheTopSongs()
        case _:
            print("Select Valid Option")


if __name__ == '__main__':
    main()
