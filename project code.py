# 1. Read the data from the spreadsheet
import csv
with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        print(dict(row))

# 2. Collect all of the sales from each month into a single list
import csv
with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    sales = []
    for row in spreadsheet:
        sale = int(row['sales'])
        sales.append(sale)
        print(sale)

# 3. Output the total sales across all months
total = sum(sales)
print('Total sales: {}'.format(total))

#ext: find the average
average = total/len(sales)
print('average: {}'.format(average))


# ext: months with the highest and lowest sales
import csv
with open('sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    sales = []
    for row in spreadsheet:
        sale = int(row['sales'])
        sales.append(sale)
highest_sale = max(sales)
print('Highest sale: {}'.format(highest_sale))

lowest_sale = min(sales)
print('Lowest sale: {}'.format(lowest_sale))