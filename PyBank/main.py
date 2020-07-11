import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #Stepping past the header row
    csv_header = next(csvreader)

    
    #Declaring a row counting integer i.
    i = 0

    #Declaring a net profit counting float.
    netProfit=0.0

    #Creating a list of monthly changes in monthly profit.
    changeList = [] 

    #All the data in a list of lists.
    dataList = []

    #Variables for keeping track of the rows corresponding
    #to maximum and minimum change in monthly profits.

    maxIndex = 0 
    minIndex = 0
    
    #Variables for maximum and minimum changes in monthly profit.

    maxChange = 0.0
    minChange = 0.0


    #Defining variable for change in monthly income
    change = 0.0

    for row in csvreader:
        
        dataList.append(row)

        #The final value of i should be the number of months represented in
        #the data.
        i+=1

        #Storing the current month's profit.
        monthProfit = float(row[1])

        #Calculate the change in profit from the previous month. Note
        #that it was not made clear in the instructions whether "Average
        # change in Profit/Losses" refers to average change in total
        #from month to month, which would be simply total profit divided
        #by number of months, or average monthly change in monthly
        #profit, where we have to calculate all the monthly changes in
        #the second column, and then find the average change. The example
        #analysis provided makes it clear that the latter is the aim.
        if i>1:
            
            #Keeping track of the max/min change indices.
            if monthProfit - prevProfit > maxChange:
                maxIndex = i-1 #correction for choosing i as row number
                maxChange = monthProfit - prevProfit
            if monthProfit - prevProfit < minChange:
                minIndex = i-1
                minChange = monthProfit - prevProfit
            
            change =  monthProfit - prevProfit
            
            #Yes, I have redundant lists. I imagine numpy will enable 
            #a more efficient technique later in the course.
            changeList.append(change)
            dataList[i-1].append(change) 
            #^^^Now dataList has date, profit, and change 

            

        netProfit+=monthProfit

        #Storing this months profit as last month's profit for the next
        #loop.
        prevProfit = monthProfit

    
    #Printing the output, with some strategic math and rounding.
    #Storing the strings in variables.
    line1 ="Financial Analysis"
    line2 = "----------------------------"
    line3 = f"Total Months: {len(dataList)}"
    line4 = f"Total: ${round(netProfit,2)}"
    line5 = f"Average Change: ${round(sum(changeList)/len(changeList),2)}"
    line6 = f"Greatest Increase in Profits: {dataList[maxIndex][0]} (${round(dataList[maxIndex][2])})"
    line7 = f"Greatest Decrease in Profits: {dataList[minIndex][0]} (${round(dataList[minIndex][2])})"
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)
    print(line6)
    print(line7)

    #Creating text file and writing in the results.
    textOut = open("analysis/results.txt", "w+")
    textOut.write(line1 + "\r")
    textOut.write(line2 + "\r")
    textOut.write(line3 + "\r")
    textOut.write(line4 + "\r")
    textOut.write(line5 + "\r")
    textOut.write(line6 + "\r")
    textOut.write(line7 + "\r")

