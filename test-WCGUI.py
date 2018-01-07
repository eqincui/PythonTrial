#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter as tk
import tkFileDialog

from PIL import Image
import numpy as np
from wordcloud import WordCloud  
import matplotlib.pyplot as plt 
import jieba

global filenameWCFile,filenameWCMask

def btnWCFileClicked():
    global filenameWCFile
    filenameWCFile = tkFileDialog.askopenfilename(initialdir = 'C:\Python27')
    labelWCFile.config(text = filenameWCFile)

def btnWCMaskClicked():
    global filenameWCMask
    filenameWCMask = tkFileDialog.askopenfilename(initialdir = 'C:\Python27')
    labelWCMask.config(text = filenameWCMask)

def btnGenerateClicked():
    text = open(filenameWCFile,"rb").read() 
    phone_mask = np.array(Image.open(filenameWCMask))

    if radioBtnLanguage.get()==2:
         wc = WordCloud(background_color = "pink", #设置背景颜色 
                        max_words = 2000, #设置最大显示的字数  
         			    mask=phone_mask,
                        #stopwords = "", #设置停用词  
         			   #设置中文字体，使得词云可以显示（词云默认字体是“DroidSansMono.ttf字体库”，不支持中文）
                        font_path = "C:\Python27\simfang.ttf",
                        max_font_size = 50,  #设置字体最大值  
                        random_state = 30, #设置有多少种随机生成状态，即有多少种配色方案  
         			   width=800, 
         			   height=400
             )	
         wordlist = jieba.cut(text,cut_all=True)
         wl = " ".join(wordlist) 
         myword = wc.generate(wl)#生成词云
    else:
         wc = WordCloud(background_color = "pink", #设置背景颜色  
                        mask=phone_mask,  #设置背景图片  
                        max_words = 2000, #设置最大显示的字数  
                        #stopwords = "", #设置停用词  
                        max_font_size = 80,  #设置字体最大值  
                        random_state = 30, #设置有多少种随机生成状态，即有多少种配色方案 
                        width=1000, 
         			   height=400			   
             ) 	
         myword = wc.generate(text)#生成词云  
      
    #展示词云图  
    plt.imshow(myword)  
    plt.axis("off")  
    plt.show()	
	
	
	
top = tk.Tk()
top.title("WordCloud Generator")
 
labelWCFile = tk.Label(top, text = "Pls choose WordCloud file...", height = 5, width = 50, fg = "blue")
labelWCFile.pack()
 
btnWCFile = tk.Button(top, text = "Choose", command = btnWCFileClicked)
btnWCFile.pack()

radioBtnLanguage = tk.IntVar()
radioBtnLanguage.set(1)

tk.Radiobutton(top, 
              text="English",
              padx = 20, 
              variable=radioBtnLanguage, 
              value=1).pack(anchor=tk.W)
tk.Radiobutton(top, 
              text="Chinese",
              padx = 20, 
              variable=radioBtnLanguage, 
              value=2).pack(anchor=tk.W)
			  
			  

labelWCMask = tk.Label(top, text = "Pls choose WordCloud mask file...", height = 5, width = 50, fg = "blue")
labelWCMask.pack()
 
btnWCMask = tk.Button(top, text = "Choose", command = btnWCMaskClicked)
btnWCMask.pack()

btnGenerate = tk.Button(top, text = "Generate!", width = 15, fg = "red", bg = "green", command = btnGenerateClicked)
btnGenerate.pack()

 
top.mainloop()
