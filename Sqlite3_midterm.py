from bs4 import BeautifulSoup
import requests
import csv
import sqlite3


con = sqlite3.connect('midterm.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS professors (
                name text PRIMARY KEY, expertise text)''')
con.commit()


page_to_scarpe = requests.get("https://csie.asia.edu.tw/zh_tw/TeacherIntroduction/Full_time_faculty")
soup = BeautifulSoup(page_to_scarpe.text, "html.parser")


professors = soup.findAll("span", attrs={"class": "i-member-value member-data-value-name"})
expertises = soup.findAll("span", attrs={"class": "i-member-value member-data-value-7"})


file = open("professor_Expertise.csv", "w", encoding='utf-8-sig', newline='')
writer = csv.writer(file)
writer.writerow(["Professor", "Expertises"])


for professor, expertise in zip(professors, expertises):
    professor_name = professor.text.strip()
    professor_expertise = expertise.text.strip()
    print(f"{professor_name} - {professor_expertise}")
    writer.writerow([professor_name, professor_expertise])
    cur.execute("INSERT OR REPLACE INTO professors (name, expertise) VALUES (?, ?)", (professor_name, professor_expertise))


con.commit()
con.close()
file.close()

print("saved into professor_Expertise.csv and midterm.db")