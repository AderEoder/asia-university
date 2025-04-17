from bs4 import BeautifulSoup
import  requests
import csv


page_to_scarpe = requests.get("https://csie.asia.edu.tw/zh_tw/TeacherIntroduction/Full_time_faculty")
soup = BeautifulSoup(page_to_scarpe.text, "html.parser")

professor = soup.findAll("span", attrs={"class" : "i-member-value member-data-value-name"})
Expertise = soup.findAll("span", attrs={"class" : "i-member-value member-data-value-7"})

file = open("professor_Expertise.csv", "w", encoding='utf-8-sig')
writer = csv.writer(file)

writer.writerow(["Professor", "Expertises"])

for professors, Expertises in zip(professor, Expertise):
    print(professors.text + " - " + Expertises.text)
    writer.writerow([professors.text, Expertises.text])
file.close()