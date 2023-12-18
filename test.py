import tkinter
import tkinter.font
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

window = tkinter.Tk()
window_width = 1280
window_height = 720
window.geometry(f'{window_width}x{window_height}')
window.resizable(False, False)

disease_1 = "감기"
disease_2 = "인플루엔자"
disease_3 = "독감"

#각종 함수 선언
def result_window():
    title_frame.pack_forget()
    result_frame.pack()

#타이틀 화면
title_frame = tkinter.Frame(window, width=1280, height=720)

title_label = tkinter.Label(title_frame, text="질병 자가진단", font=tkinter.font.Font(family="빙그레체Ⅱ", size=48, weight='bold'))
title_label.place(x=83, y=315)
symptom_entry = tkinter.Entry(title_frame, font=tkinter.font.Font(family="빙그레체Ⅱ", size=23, weight='bold'))
symptom_entry.place(x=595, y=320, width=600, height=80)
explain_label  = tkinter.Label(title_frame, text="현재 자신의 증상을 알려주세요", font=tkinter.font.Font(family="빙그레체Ⅱ", size=23, weight='bold'))
explain_label.place(x=595, y=265)
search_button = tkinter.Button(title_frame, text="진단 시작", command=result_window, font=tkinter.font.Font(family="빙그레체Ⅱ", size=23, weight='bold'))
search_button.place(x=823, y=413, width=140, height=60)

#결과 화면
result_frame = tkinter.Frame(window, width=1280, height=720)

disease_first_title = tkinter.Label(result_frame, text=disease_1, font=tkinter.font.Font(family="빙그레체Ⅱ", size=48, weight='bold'))
first_percent = tkinter.Label(result_frame, text="87%", font=tkinter.font.Font(family="빙그레체Ⅱ", size=26, weight='bold'))
disease_first_title.place(x=56, y=2)
first_percent.place(x=206, y=34)
disease_second_title = tkinter.Label(result_frame, text=disease_2, font=tkinter.font.Font(family="빙그레체Ⅱ", size=40, weight='bold'))
second_percent = tkinter.Label(result_frame, text="64%", font=tkinter.font.Font(family="빙그레체Ⅱ", size=26, weight='bold'))
disease_second_title.place(x=341, y=12)
second_percent.place(x=465, y=34)
disease_thrid_title = tkinter.Label(result_frame, text=disease_3, font=tkinter.font.Font(family="빙그레체Ⅱ", size=34, weight='bold'))
thrid_percent = tkinter.Label(result_frame, text="53%", font=tkinter.font.Font(family="빙그레체Ⅱ", size=26, weight='bold'))
disease_thrid_title.place(x=590, y=21)
thrid_percent.place(x=698, y=34)

disease_label1 = tkinter.Label(result_frame, text=disease_1, font=tkinter.font.Font(family="빙그레체Ⅱ", size=44, weight='bold'))
disease_label1.place(x=67, y=157)
disease_label2 = tkinter.Label(result_frame, text=disease_2, font=tkinter.font.Font(family="빙그레체Ⅱ", size=44, weight='bold'))
disease_label2.place(x=67, y=367)
disease_label3 = tkinter.Label(result_frame, text=disease_3, font=tkinter.font.Font(family="빙그레체Ⅱ", size=44, weight='bold'))
disease_label3.place(x=67, y=577)

figure = plt.Figure()
chart_1 = FigureCanvasTkAgg(figure, result_frame)
chart_1.get_tk_widget().place(x=225, y=92, width=651, height=187)
chart_2 = FigureCanvasTkAgg(figure, result_frame)
chart_2.get_tk_widget().place(x=225, y=304, width=651, height=187)
chart_3 = FigureCanvasTkAgg(figure, result_frame)
chart_3.get_tk_widget().place(x=225, y=516, width=651, height=187)

select_label = tkinter.Label(result_frame, text="사용자에게 나타난 증상", font=tkinter.font.Font(family="빙그레체Ⅱ", size=23, weight='bold'))
select_label.place(x=910, y=51)
content_1 = tkinter.Label(result_frame, background='#F78D75')
content_1.place(x=916, y=92, width=304, height=187)
content_2 = tkinter.Label(result_frame, background='#F78D75')
content_2.place(x=916, y=304, width=304, height=187)
content_3 = tkinter.Label(result_frame, background='#F78D75')
content_3.place(x=916, y=516, width=304, height=187)

title_frame.pack()

window.mainloop()