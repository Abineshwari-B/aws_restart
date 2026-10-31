import csv
import copy

# Create a vehicle dictionary with default values
myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}

# Create an empty list to store vehicle details
myInventoryList = []

# Open the CSV file
with open('car_fleet.csv') as csvFile:

    csvReader = csv.reader(csvFile, delimiter=',')

    lineCount = 0

    # Read each row from the CSV file
    for row in csvReader:

        # Display column names
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')
            lineCount += 1

        else:
            # Display vehicle details
            print(
                f'vin: {row[0]} make: {row[1]}, model: {row[2]}, '
                f'year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, '
                f'zeroSixty: {row[6]}, mileage: {row[7]}'
            )

            # Create a copy of the default vehicle dictionary
            currentVehicle = copy.deepcopy(myVehicle)

            # Assign CSV values to dictionary keys
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]

            # Add the vehicle dictionary to the inventory list
            myInventoryList.append(currentVehicle)

            lineCount += 1

    print(f'Processed {lineCount} lines.')


# Create another copy of the default vehicle dictionary
currentVehicle = copy.deepcopy(myVehicle)

# Display all vehicle properties
for myCarProperties in myInventoryList:

    for key, value in myCarProperties.items():

        print("{} : {}".format(key, value))

    print("-----")