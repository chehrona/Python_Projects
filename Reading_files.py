def reads_csv(filename):
    with open(filename, "r") as fileinput:
        listOfStrLists = []
        outputFile = dict()
        listOutputFile = []
        for line in fileinput:
            splittedLineList = line.split(",")
            # Converts it to a string
            noSpace = line[:-1]
            strToList = noSpace.split(",")
            listOfStrLists.append(strToList)
        key_name = listOfStrLists[0][0]
        key_address = listOfStrLists[0][1]
        key_age = listOfStrLists[0][2]
        for entry in listOfStrLists:
            if "name" in entry:
                continue
            outputFile[key_name] = entry[0]
            outputFile[key_address] = entry[1]
            outputFile[key_age] = entry[2]
            listOutputFile.append(outputFile)
        print(listOutputFile)
reads_csv("names.csv")
