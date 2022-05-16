import csv
import json



with open('words.csv', 'r', newline='') as file:
    fieldnames = ['Dutch Word', 'English Word','Row_Number']
    writer = csv.DictWriter(file, fieldnames=fieldnames)


def csv_to_json(csvFilePath,jsonFilePath):
    data = {}


    with open(csvFilePath, encoding='utf-8') as csvfile:
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvfile) 
        
        #convert each csv row into python dict
        for rows, i in zip(csvReader, range(1,5001)):
            data[i] = rows
        
        
    #convert python data to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonFile:
        jsonString = json.dumps(data, indent=4)
        jsonFile.write(jsonString)
       

csvFilePath = 'words.csv'
jsonFilePath = 'word_list.json'

csv_to_json(csvFilePath,jsonFilePath)




