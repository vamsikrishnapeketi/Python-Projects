import pandas       

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict) #gives a dictionary

temp_list = data["temp"].to_list()
print(temp_list) #converts the temp col to a list

print(data["temp"].mean()) #to calculate the avg/mean of the 

print(f"The maximum temperature in the week is {data["temp"].max()}") #here we can write both data["temp"] or data.temp 

print(data[data.day == "Monday"]) #used to print the entire row of the table.

print(data[data.temp == data.temp.max()]) #to get the row with max temperature

monday = data[data.day == "Monday"]
print(monday.temp[0]) # to get the temp of monday 


#to create a dataframe just use pandas.Dataframe(dict) 
new_dataframe = pandas.DataFrame(data_dict)

#to iterate thorough the pandas dataframe
for (index, row) in new_dataframe.iterrows():
    print(row)#this will iterate rowise 
    print(row.condition)