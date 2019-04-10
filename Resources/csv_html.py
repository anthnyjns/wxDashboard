from prettytable import PrettyTable
x = PrettyTable()

from prettytable import from_csv
csv_file = open("cities.csv", "r")
mytable = from_csv(csv_file)
csv_file.close()

table_html = mytable.get_html_string()
# print(table_html)

html_file = open('table.html', 'w')
html_file = html_file.write(table_html)
