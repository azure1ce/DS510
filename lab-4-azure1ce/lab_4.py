# Lab 4
# Replace "WRITE CODE HERE" with your python code and remove the "pass" statement


# ----------------- Question 1 -----------------
def analyze_climate_data(filename: str) -> (int, int, float, float, float, float):
    # open file under samelocation by using open() can use except to catch the error if happened
    file = open(filename,"r")
    #use for line in file to read each line of this file
    #input:
    #min temp, max temp, hum percentage, precipitation inches
    #output:
    #total days recorded = len(list) need count any raw list
    #days with precipitation = list () need calculate precipitation
    #lowest temperature = list.min() need count temp
    #highest temperature = list.max() need count temp
    #mean humidity = list.mean() need count humidity
    #mean precipitation = list.mean() need count precipitation
    minTempList = list()
    maxTempList = list()
    humList = list()
    preciList = list()
    preciDays = 0
    for line in file:
        stripLine = line.rstrip().split(",")
        if line.startswith("Minimum"):
            continue
        #got 0,    1,        2,              3
        #min temp, max temp, hum percentage, precipitation inches
        minTempList.append(float(stripLine[0]))
        maxTempList.append(float(stripLine[1]))
        humList.append(float(stripLine[2]))
        preciList.append(float(stripLine[3]))
        if float(stripLine[3]) > 0:
            preciDays += 1
    file.close()
    return len(minTempList), preciDays,min(minTempList), max(maxTempList), round(sum(humList)/len(humList),2), round(sum(preciList)/len(preciList),2)
    
#

# invoke the function with relevant args of your choice
#analyze_climate_data("weather_1.csv") 


# ----------------- Question 2 -----------------
def rainfall_prediction(filename: str) -> (int, int):
    file = open(filename,"r")
    predictRainyDays = 0
    realRainyDays = 0
    for line in file:
        stripLine = line.rstrip().split(",")
        if line.startswith("Minimum"):
            continue
        #got 0,    1,        2,              3
        #min temp, max temp, hum percentage, precipitation inches
        elif (float(stripLine[1]) - float(stripLine[0])) > 10 and float(stripLine[2]) > 50:
            predictRainyDays += 1
            if float(stripLine[3]) > 0:
                realRainyDays += 1
        elif float(stripLine[3]) == 0:
            realRainyDays += 1
    file.close()
    return predictRainyDays,realRainyDays

# invoke the function with relevant args of your choice
#rainfall_prediction("weather_2.csv") 


# ----------------- Question 3 -----------------
def export_weather_predictions(source_file: str, destination_file: str) -> None:
    sourceFile = open(source_file,"r")
    exportFile = open(destination_file,"a")
    for line in sourceFile:
        stripLine = line.rstrip().split(",")
        if line.startswith("Minimum"):
            exportFile.write(line.rstrip()+(",Forecast")+"\n")
            continue
        #got 0,    1,        2,              3
        #min temp, max temp, hum percentage, precipitation inches
        elif (float(stripLine[1]) - float(stripLine[0])) > 10 and float(stripLine[2]) > 50:
            #there is a predict rainy day
            #predictRainyDays += 1
            exportFile.write(line.rstrip()+(",rainy")+"\n")
        else:
            exportFile.write(line.rstrip()+(",sunny")+"\n")
    sourceFile.close()
    exportFile.close()
    return None

# invoke the function with relevant args of your choice
# WRITE CODE HERE
