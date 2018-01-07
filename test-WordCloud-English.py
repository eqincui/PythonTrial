#-*-coding:utf-8-*-  
  
###生成txt文件的词云  
from PIL import Image
import numpy as np
from wordcloud import WordCloud  
import matplotlib.pyplot as plt  


text = open("zeTianji.txt","rb").read()  
 
  
#把分词后的txt写入文本文件  
#fenciTxt  = open("fenciHou.txt","w+")  
#fenciTxt.writelines(wl)  
#fenciTxt.close()  

# 词云形状的来源图片 
phone_mask = np.array(Image.open(r'C:\Python27\temp.jpg')) 
  
  
#设置词云  
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

# 把词云保存下来
#wc.to_file('show_English.png') 
