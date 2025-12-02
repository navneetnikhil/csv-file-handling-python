import csv

header = ["name", "roll", "section"]
rows = [
    ["Navneet", 230520000, 35],
    ["Rohan",   230520001, 40],
    ["Rahul",   230520002, 45]
]

with open("output.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)
