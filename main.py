import csv
import json



with open('words1.csv', 'a', newline='') as file:
    fieldnames = ['Frequency','Dutch Word', 'English Word']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Frequency': '3', 'Dutch Word': 'niuew', 'English Word': 'new'})

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
        jsonFile.write(jsonString)
       

csvFilePath = 'word_list2.csv'
jsonFilePath = 'word_list2.json'

csv_to_json(csvFilePath,jsonFilePath)




