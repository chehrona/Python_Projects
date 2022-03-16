# First way to write CSV files
# import csv
#
# def writes_csv(filename, inputs):
#     with open(filename, "w") as fileinput:
#         writer = csv.writer(fileinput)
#         header = ["name", "address", "age"]
#         writer.writerow(header)
#         for entry in inputs:
#             # print(entry)
#             tupleToList = []
#             tupleToList = list(entry)
#             # print(tupleToList)
#             writer.writerow(tupleToList)
# writes_csv("names.csv", [("George", "4312 Abbey Road", 22), ("John", "54 Love Ave", 21)])

# Second way to write CSV files
def writes_csv(filename, inputs):
    with open(filename, "w") as fileinput:
        header = "name, address, age\n"
        fileinput.write(header)
        for entry in inputs:
            tupleToList = list(entry)
            for item in tupleToList:
                intToStr = str(tupleToList[2])
                tupleToList[2] = intToStr
            listToStr = ",".join(tupleToList)
            fileinput.write(listToStr + "\n")
writes_csv("names_2.csv", [("George", "4312 Abbey Road", 22), ("John", "54 Love Ave", 21)])
