import csv
import json



with open('words.csv', 'r', newline='') as file:
    fieldnames = ['Dutch Word', 'English Word','Row_Number']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # writer.writeheader()
    # writer.writerow({'Frequency': '3', 'Dutch Word': 'niuew', 'English Word': 'new'})

def csv_to_json(csvFilePath,jsonFilePath):
    data = []


    with open(csvFilePath, encoding='utf-8') as csvfile:
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvfile) 
        print(csvReader)
        #convert each csv row into python dict
        for row in csvReader:
            data.append(row)
        # print(data)
        

    #convert python data to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonFile:
        jsonString = json.dumps(data, indent=4)
        # for i in jsonString:
        #     data[range(1,20)] = data["order_number"]
        #     data["order_number"] += 1
        jsonFile.write(jsonString)
       

csvFilePath = 'words.csv'
jsonFilePath = 'word_list.json'

csv_to_json(csvFilePath,jsonFilePath)




