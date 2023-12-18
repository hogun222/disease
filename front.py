import tkinter
import tkinter.font
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

from diseaseAranger import getDiseaseData
from diseaseAranger import DiseaseData
from diseaseMatch import getPercentage
from diseaseMatch import pickThree

window = tkinter.Tk()
window_width = 1280
window_height = 720
window.geometry(f'{window_width}x{window_height}')
window.resizable(False, False)

diseases = getDiseaseData()[0:3]

#각종 함수 선언
class A:
    diseases = getDiseaseData()[0:3]
    def result_window(self, diseases):
        res = symptom_entry.get()
        
        datas = getDiseaseData()[:20]
        diseases = getPercentage(datas, res)
        numList = pickThree(diseases)
        diseases = [diseases[numList[0]], diseases[numList[1]], diseases[numList[2]]]
        self.diseases = diseases
        print("\n\n-------------------------")
        print(numList)
        for disease in self.diseases:
            print(disease.symptomAve)

        title_frame.pack_forget()
        make_result_frame()
        result_frame.pack()
a = A()

#타이틀 화면
title_frame = tkinter.Frame(window, width=1280, height=720)

title_label = tkinter.Label(title_frame, text="질병 자가진단", font=tkinter.font.Font(family="빙그레체Ⅱ", size=48, weight='bold'))
title_label.place(x=83, y=315)
symptom_entry = tkinter.Entry(title_frame, font=tkinter.font.Font(family="빙그레체Ⅱ", size=23, weight='bold'))
symptom_entry.place(x=595, y=320, width=600, height=80)
explain_label  = tkinter.Label(title_frame, text="현재 자신의 증상을 알려주세요", font=tkinter.font.Font(family="빙그레체Ⅱ", size=23, weight='bold'))
explain_label.place(x=595, y=265)
search_button = tkinter.Button(title_frame, text="진단 시작", command=lambda: a.result_window(a.diseases), font=tkinter.font.Font(family="빙그레체Ⅱ", size=23, weight='bold'))
search_button.place(x=823, y=413, width=140, height=60)

#결과 화면
result_frame = tkinter.Frame(window, width=1280, height=720)

def make_result_frame():
    disease_title = []
    percentage = []
    disease_label = []
    chart = []
    content = []

    sizeList = [48, 40, 34]
    xPos = 56
    yPos = 2

    for i in range(3):
        disease_title.append(tkinter.Label(result_frame, text=a.diseases[i].name, font=tkinter.font.Font(family="빙그레체Ⅱ", size=sizeList[i], weight='bold')))
        percentage.append(tkinter.Label(result_frame, text=(str(int(a.diseases[i].symptomAve)) + '%'), font=tkinter.font.Font(family="빙그레체Ⅱ", size=26, weight='bold')))
        disease_title[i].place(x=xPos, y=yPos)
        xPos += sizeList[i] * len(a.diseases[i].name) * 1.3
        yPos += 10
        percentage[i].place(x=xPos, y=34)
        xPos += 26 * len(str(int(a.diseases[i].symptomAve)) + '%') * 1.5

    xPos = 67
    yPos = 157

    for i in range(3):
        disease_label.append(tkinter.Label(result_frame, text=a.diseases[i].name, font=tkinter.font.Font(family="빙그레체Ⅱ", size=int(90/len(a.diseases[i].name)), weight='bold')))
        disease_label[i].place(x = xPos, y = yPos)
        yPos += 210

    xPos = 225
    yPos = 94

    figure = plt.Figure()
    for i in range(3):
        chart.append(FigureCanvasTkAgg(figure, result_frame))
        chart[i].get_tk_widget().place(x=xPos, y=yPos, width=651, height=187)
        yPos += 212

    xPos = 916
    yPos = 92

    select_label = tkinter.Label(result_frame, text="사용자에게 나타난 증상", font=tkinter.font.Font(family="빙그레체Ⅱ", size=23, weight='bold'))
    select_label.place(x=910, y=51)
    for i in range(3):
        content.append(tkinter.Label(result_frame, background='#F78D75'))
        content[i].place(x=xPos, y=yPos, width=304, height=187)
        yPos += 212


title_frame.pack()

window.mainloop()