import csv

data = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"],
        ["Training Day", "Man on Fire", "Flight"]]

with open('data.csv', "w") as file:
    r = csv.writer(file, delimiter=',')
    for line in data:
        r.writerow(line)
