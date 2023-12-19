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
        datas = getDiseaseData()[:30]
        diseases = getPercentage(datas, res)
        numList = pickThree(diseases)
        print(numList)
        diseases = [diseases[numList[0]], diseases[numList[1]], diseases[numList[2]]]
        self.diseases = diseases
        print(self.diseases[0].name)
        print(self.diseases[1].name)
        print(self.diseases[2].name)
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
search_button = tkinter.Button(title_frame, text="진단 시작", command=lambda: a.result_window(diseases), font=tkinter.font.Font(family="빙그레체Ⅱ", size=23, weight='bold'))
search_button.place(x=823, y=413, width=140, height=60)

#결과 화면
result_frame = tkinter.Frame(window, width=1280, height=720)

def make_result_frame():
    disease_title = []
    percentage = []
    disease_label = []
    chart = []
    content = []
    symptoms = []
    details = []

    sizeList = [48, 40, 34]

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
        symptomInfo = ""
        if (a.diseases[i].symptom != None):
            for symptom in a.diseases[i].symptom:
                symptomInfo += symptom + ' '
        treatInfo = ""
        if (a.diseases[i].treat != None):
            for treat in a.diseases[i].treat:
                treatInfo += treat + ' '
        preventInfo = ""
        if (a.diseases[i].prevent != None):
            for prevent in a.diseases[i].prevent:
                preventInfo += prevent + ' '
        


        chart.append(FigureCanvasTkAgg(figure, result_frame))
        details.append(tkinter.Text(result_frame, 
                                      width=651,
                                      height=187,
                                      wrap="word",
                                      font=tkinter.font.Font(family="빙그레체Ⅱ", size=20, weight='normal')))
        details[i].tag_configure("custom_tag1", selectforeground="#000000")
        details[i].insert(tkinter.END, a.diseases[i].info + '\n\n', "custom_tag1")
        details[i].insert(tkinter.END, "증상 : " + symptomInfo + '\n\n', "custom_tag1")
        details[i].insert(tkinter.END, "치료 : " + treatInfo + '\n\n', "custom_tag1")
        details[i].insert(tkinter.END, "예방 : " + preventInfo + '\n\n', "custom_tag1")
        


        details[i].config(state=tkinter.DISABLED)        
        details[i].place(x=xPos, y=yPos, width=651, height=187)

        chart[i].get_tk_widget().place(x=xPos, y=yPos, width=651, height=187)
        yPos += 212

    xPos = 916
    yPos = 92

    select_label = tkinter.Label(result_frame, text="사용자에게 나타난 증상", font=tkinter.font.Font(family="빙그레체Ⅱ", size=23, weight='bold'))
    select_label.place(x=910, y=51)
    for i in range(3):
        content.append(tkinter.Label(result_frame, background='#F78D75'))
        content[i].place(x=xPos, y=yPos, width=304, height=187)

        chosenSymptom = ""
        unchosenSymptom = ""
        for j in range(len(a.diseases[i].symptom)):
            if (a.diseases[i].symptomMatch[j] != 0):
                chosenSymptom += a.diseases[i].symptom[j] + ' '
                chosenSymptom += str(int(a.diseases[i].symptomMatch[j])) + '%' + ' '

            else:
                unchosenSymptom += a.diseases[i].symptom[j] + ' '
                unchosenSymptom += str(int(a.diseases[i].symptomMatch[j])) + '%' + ' '

        symptoms.append(tkinter.Text(result_frame, 
                                      width=304,
                                      height=187,
                                      wrap="word",
                                      bg="#F78D75",
                                      font=tkinter.font.Font(family="빙그레체Ⅱ", size=20, weight='normal')))
        symptoms[i].tag_configure("custom_tag1", selectforeground="#000000")
        symptoms[i].insert(tkinter.END, chosenSymptom, "custom_tag1")
        #symptoms[i].tag_configure("custom_tag2", selectforeground="#AAAAAA")
        #symptoms[i].insert(tkinter.END, unchosenSymptom, "custom_tag2")
        symptoms[i].config(state=tkinter.DISABLED)
        
        symptoms[i].place(x=xPos, y=yPos, width=304, height=187)
        yPos += 212

    xPos = 56
    yPos = 250

    percentage.append(tkinter.Label(result_frame, text=(str(int(a.diseases[0].symptomAve)) + '%'), font=tkinter.font.Font(family="빙그레체Ⅱ", size=20, weight='bold')))
    percentage[0].place(x=85, y=240)
    percentage.append(tkinter.Label(result_frame, text=(str(int(a.diseases[1].symptomAve)) + '%'), font=tkinter.font.Font(family="빙그레체Ⅱ", size=20, weight='bold')))
    percentage[1].place(x=85, y=452)
    percentage.append(tkinter.Label(result_frame, text=(str(int(a.diseases[2].symptomAve)) + '%'), font=tkinter.font.Font(family="빙그레체Ⅱ", size=20, weight='bold')))
    percentage[2].place(x=85, y=664)


    def exit_window():
        window.destroy()
    exit_button = tkinter.Button(result_frame, text="X", font=tkinter.font.Font(family="빙그레체Ⅱ", size=20, weight='bold'), command=exit_window)
    exit_button.place(x=1222, y=4, width=40, height=40)

title_frame.pack()

window.mainloop()