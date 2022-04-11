#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/usr/bin/env python
# coding: utf-8

# In[3]:


import re
import os
import os.path
import matplotlib.pyplot as plt
import numpy as np
import glob
import pandas as pd


# In[10]:


def open_file1(file) :
    info = pd.read_excel('C:/Users/PC/표/sleep_file/새 폴더/'+file+'_1.xlsx',engine='openpyxl')
    info = info[['Epoch','Stage']]
    info = info.dropna(axis=0)
    epoch_1 = info['Epoch'].values
    stage = info['Stage'].values
    epoch = []
    for i in epoch_1 :
        epoch.append(int(i))
        
    return stage, epoch

def open_file2(file) :
    myFile = open(file+'-P.txt','r')
    lines = myFile.readlines()
    n=len(lines)

    text=[]
    date=[] #날짜
    hour=[] #시간
    mi=[]   #분
    sec=[]  #초
    eeg=[]
    eog=[]
    check = 0
    for line in lines :
        if check == 0 :
            text =line.split()
            date.append(text[0]) 
            hour.append(text[1])
            mi.append(text[2])
            sec.append(text[3])
            eeg.append(text[4])
            eog.append(text[5])
            check = check+1
        else :
            text =line.split()
            date.append(text[0]) 
            hour.append(text[1])
            mi.append(text[2])
            sec.append(text[3])
            eeg.append(float(text[4])*10)
            eog.append(float(text[5])*10)

    myFile.close()

    del date[0]
    del hour[0]
    del mi[0]
    del sec[0]
    del eeg[0]
    del eog[0]

    eeg_max = float(max(eeg))
    eeg_min = float(min(eeg))
    eog_max = float(max(eog))
    eog_min = float(min(eog))

    eeg_max = int(eeg_max)
    eeg_min = int(eeg_min)
    eog_max = int(eog_max)
    eog_min = int(eog_min)
    return date,hour,mi,sec,eeg,eog,eeg_max,eeg_min,eog_max,eog_min

def select(file) :
    stage,epoch = open_file1(file)
    date,hour,mi,sec,eeg,eog,eeg_max,eeg_min,eog_max,eog_min=open_file2(file)
    for i in range(len(eeg)) :
        eeg[i] = str(eeg[i])
        eog[i] = str(eog[i])
        
    count=len(stage)
    start=0
    end=6000
    data=[]
    count_w=1
    count_o=1
    count_t=1
    count_tr=1
    count_f=1
    count_r=1
    a=1
    eeg_max = str(eeg_max)
    eeg_min = str(eeg_min)
    eog_max = str(eog_max)
    eog_min = str(eog_min)

    if not os.path.exists('File_Data'):  #파일 존재여부 판단
            os.makedirs('File_Data')     #파일 생성

    f=open('File_Data/1_data.txt','w')
    f.write(eeg_max+'\n')
    f.write(eeg_min+'\n')
    f.write(eog_max+'\n')
    f.write(eog_min+'\n')
    f.close()

    for i in range(0,count):#총 횟수
        n=epoch[i]
    #     for j in range(0,n):#한 스테이지당 횟수(30초단위)
        for k in range(start,end):
             data.append(date[k]+"    "+hour[k]+"    "+mi[k]+"    "+sec[k]+"    "+eeg[k]+"    "+eog[k])   

        if stage[i] == 'W' :
                if not os.path.exists('W'):
                    os.makedirs('W')
                if not os.path.exists('W/W_data'):
                    os.makedirs('W/W_data')
                copy=open('W/W_data/'+file+'_%d.txt'%count_w,'w')
                copy.writelines('\n'.join(data))
                copy.close()
                start+=6000
                end+=6000
                count_w+=1 
                data=[]
                print("%d개 생성완료 " % a)
                a+=1
        if stage[i] == 'N1' :
                if not os.path.exists('1'):
                    os.makedirs('1')
                if not os.path.exists('1/1_data'):
                    os.makedirs('1/1_data')
                copy=open('1/1_data/'+file+'_%d.txt'%count_o,'w')
                copy.writelines('\n'.join(data))
                copy.close()
                start+=6000
                end+=6000
                count_o+=1 
                data=[]
                print("%d개 생성완료 " % a)
                a+=1
        if stage[i] == 'N2' :
                if not os.path.exists('2'):
                    os.makedirs('2')
                if not os.path.exists('2/2_data'):
                    os.makedirs('2/2_data')
                copy=open('2/2_data/'+file+'_%d.txt'%count_t,'w')
                copy.writelines('\n'.join(data))
                copy.close()
                start+=6000
                end+=6000
                count_t+=1 
                data=[]
                print("%d개 생성완료 " % a)
                a+=1
        if stage[i] == 'N3' :
                if not os.path.exists('3'):
                    os.makedirs('3')
                if not os.path.exists('3/3_data'):
                    os.makedirs('3/3_data')
                copy=open('3/3_data/'+file+'_%d.txt'%count_tr,'w')
                copy.writelines('\n'.join(data))
                copy.close()
                start+=6000
                end+=6000
                count_tr+=1 
                data=[]
                print("%d개 생성완료 " % a)
                a+=1
        if stage[i] == 'R' :
                if not os.path.exists('R'):
                    os.makedirs('R')
                if not os.path.exists('R/R_data'):
                    os.makedirs('R/R_data')
                copy=open('R/R_data/'+file+'_%d.txt'%count_r,'w')
                copy.writelines('\n'.join(data))
                copy.close()
                start+=6000
                end+=6000
                count_r+=1 
                data=[]
                print("%d개 생성완료 " % a)
                a+=1


def open_file3(file) :
    myFile = open(file,'r')
    lines = myFile.readlines()
    n=len(lines)

    text=[]
    date=[] 
    hour=[] 
    mi=[]   
    sec=[]
    eeg=[]
    eog=[]


    for line in lines :
        text =line.split()
        date.append(text[0]) 
        hour.append(text[1])
        mi.append(text[2])
        sec.append(text[3])
        eeg.append(text[4])
        eog.append(text[5])
        



def draw_time(file,file_name,thick,c,a):
    date,hour,mi,sec,eeg,eog=open_file3(file)
    x=[]
    y=[]
    z=[]
     
    for i in range(0,6000):
        x.append(i)
        y.append(eeg[i])
        z.append(eog[i])
       
    y_a=[float(num) for num in y]
    

    plt.plot(x,y_a,c,linewidth=thick)
    plt.axis('off'), plt.xticks([]), plt.yticks([])
    plt.tight_layout()
    plt.ylim(-200,200)
    plt.subplots_adjust(left = 0, bottom = 0, right = 1, top = 1, hspace = 0, wspace = 0)
    
    if file[0] == 'W' :
                    if not os.path.exists('W'):
                        os.makedirs('W')
                    if not os.path.exists('W/W_eeg'):
                        os.makedirs('W/W_eeg')
                    plt.savefig('W/W_eeg/'+file_name+'.png',format='png')
                    plt.clf()
                    print("%d개 생성완료 " % a)
                    
    if file[0] == '1' :
                    if not os.path.exists('1'):
                        os.makedirs('1')
                    if not os.path.exists('1/1_eeg'):
                        os.makedirs('1/1_eeg')
                    plt.savefig('1/1_eeg/'+file_name+'.png',format='png')
                    plt.clf()
                    print("%d개 생성완료 " % a)
                    
    if file[0] == '2' :
                   
                    if not os.path.exists('2/2_eeg'):
                        os.makedirs('2/2_eeg')
                    plt.savefig('2/2_eeg/'+file_name+'.png',format='png')
                    plt.clf()
                    print("%d개 생성완료 " % a)
                    
    if file[0] == '3' :
                    
                    if not os.path.exists('3/3_eeg'):
                        os.makedirs('3/3_eeg')
                    plt.savefig('3/3_eeg/'+file_name+'.png',format='png')
                    plt.clf() 
                    print("%d개 생성완료 " % a)
                                        
    if file[0] == 'R' :
                   
                    if not os.path.exists('R/R_eeg'):
                        os.makedirs('R/R_eeg')
                    plt.savefig('R/R_eeg/'+file_name+'.png',format='png')
                    plt.clf()
                    print("%d개 생성완료 " % a)
                    
                    
def draw_time_eog(file,file_name,thick,c,a):
    date,hour,mi,sec,eeg,eog=open_file3(file)
    x=[]
    y=[]
    z=[]
     
    for i in range(0,6000):
        x.append(i)
        y.append(eog[i])
        
       
    y_a=[float(num) for num in y]
    

    plt.plot(x,y_a,c,linewidth=thick)
    plt.axis('off'), plt.xticks([]), plt.yticks([])
    plt.tight_layout()
    plt.ylim(-550,550)
    plt.subplots_adjust(left = 0, bottom = 0, right = 1, top = 1, hspace = 0, wspace = 0)
    
    if file[0] == 'W' :
                    if not os.path.exists('W'):
                        os.makedirs('W')
                    if not os.path.exists('W/W_eog'):
                        os.makedirs('W/W_eog')
                    plt.savefig('W/W_eog/'+file_name+'.png',format='png')
                    plt.clf()
                    print("%d개 생성완료 " % a)
                    
    if file[0] == '1' :
                    if not os.path.exists('1'):
                        os.makedirs('1')
                    if not os.path.exists('1/1_eog'):
                        os.makedirs('1/1_eog')
                    plt.savefig('1/1_eog/'+file_name+'.png',format='png')
                    plt.clf()
                    print("%d개 생성완료 " % a)
                    
    if file[0] == '2' :
                   
                    if not os.path.exists('2/2_eog'):
                        os.makedirs('2/2_eog')
                    plt.savefig('2/2_eog/'+file_name+'.png',format='png')
                    plt.clf()
                    print("%d개 생성완료 " % a)
                    
    if file[0] == '3' :
                    
                    if not os.path.exists('3/3_eog'):
                        os.makedirs('3/3_eog')
                    plt.savefig('3/3_eog/'+file_name+'.png',format='png')
                    plt.clf() 
                    print("%d개 생성완료 " % a)                    
                    
    if file[0] == 'R' :
                   
                    if not os.path.exists('R/R_eog'):
                        os.makedirs('R/R_eog')
                    plt.savefig('R/R_eog/'+file_name+'.png',format='png')
                    plt.clf()
                    print("%d개 생성완료 " % a)
                    
                    
def draw_fft(file,file_name,c,a):
    date,hour,mi,sec,eeg,eog=open_file3(file)
    x=[]
    y=[]
    z=[]
    fmax = 200      # 주파수 샘플링
    dt = 1/fmax     # dt
    N  = 6000    # 신호 길이
    
    for i in range(0,6000):
        x.append(i)
        y.append(eeg[i])
        z.append(eog[i])
       
    y_a=[float(num) for num in y]
    
    df = fmax/N
    f = np.arange(0,N)*df
    xf = np.fft.fft(y_a)*dt
    plt.plot(f[0:int(N/2+1)],np.abs(xf[0:int(N/2+1)]),c)
    plt.axis('off'), plt.xticks([]), plt.yticks([])
    plt.grid()
    plt.tight_layout()
    

    if file[0] == 'W' :
                    
                    if not os.path.exists('W/W_eeg_fft'):
                        os.makedirs('W/W_eeg_fft')
                    plt.savefig('W/W_eeg_fft/'+file_name+'.png',format='png')
                    plt.clf()
                    print("%d개 생성완료 " % a)
                    
    if file[0] == '1' :
                    
                    if not os.path.exists('1/1_eeg_fft'):
                        os.makedirs('1/1_eeg_fft')
                    plt.savefig('1/1_eeg_fft/'+file_name+'.png',format='png')
                    plt.clf()
                    print("%d개 생성완료 " % a)
                    
    if file[0] == '2' :
                   
                    if not os.path.exists('2/2_eeg_fft'):
                        os.makedirs('2/2_eeg_fft')
                    plt.savefig('2/2_eeg_fft/'+file_name+'.png',format='png')
                    plt.clf()
                    print("%d개 생성완료 " % a)
                    
    if file[0] == '3' :
                    
                    if not os.path.exists('3/3_eeg_fft'):
                        os.makedirs('3/3_eeg_fft')
                    plt.savefig('3/3_eeg_fft/'+file_name+'.png',format='png')
                    plt.clf() 
                    print("%d개 생성완료 " % a)
                                       
    if file[0] == 'R' :
                   
                    if not os.path.exists('R/R_eeg_fft'):
                        os.makedirs('R/R_eeg_fft')
                    plt.savefig('R/R_eeg_fft/'+file_name+'.png',format='png')
                    plt.clf()
                    print("%d개 생성완료 " % a)
                    
                    
def draw_eog_fft(file,file_name,c,a):
    date,hour,mi,sec,eeg,eog=open_file3(file)
    x=[]
    y=[]
    z=[]
    fmax = 200      # 주파수 샘플링
    dt = 1/fmax     # dt
    N  = 6000    # 신호 길이
    
    for i in range(0,6000):
        x.append(i)
        y.append(eeg[i])
        z.append(eog[i])
       
    z_a=[float(num) for num in z]
    
    df = fmax/N
    f = np.arange(0,N)*df
    xf = np.fft.fft(z_a)*dt
    plt.plot(f[0:int(N/2+1)],np.abs(xf[0:int(N/2+1)]),c)
    plt.axis('off'), plt.xticks([]), plt.yticks([])
    plt.grid()
    plt.tight_layout()
    

    if file[0] == 'W' :
                    
                    if not os.path.exists('W/W_eog_fft'):
                        os.makedirs('W/W_eog_fft')
                    plt.savefig('W/W_eog_fft/'+file_name+'.png',format='png')
                    plt.clf()
                    print("%d개 생성완료 " % a)
                    
    if file[0] == '1' :
                    
                    if not os.path.exists('1/1_eog_fft'):
                        os.makedirs('1/1_eog_fft')
                    plt.savefig('1/1_eog_fft/'+file_name+'.png',format='png')
                    plt.clf()
                    print("%d개 생성완료 " % a)
                    
    if file[0] == '2' :
                   
                    if not os.path.exists('2/2_eog_fft'):
                        os.makedirs('2/2_eog_fft')
                    plt.savefig('2/2_eog_fft/'+file_name+'.png',format='png')
                    plt.clf()
                    print("%d개 생성완료 " % a)
                    
    if file[0] == '3' :
                    
                    if not os.path.exists('3/3_eog_fft'):
                        os.makedirs('3/3_eog_fft')
                    plt.savefig('3/3_eog_fft/'+file_name+'.png',format='png')
                    plt.clf() 
                    print("%d개 생성완료 " % a)
                    
    if file[0] == 'R' :
                   
                    if not os.path.exists('R/R_eog_fft'):
                        os.makedirs('R/R_eog_fft')
                    plt.savefig('R/R_eog_fft/'+file_name+'.png',format='png')
                    plt.clf()
                    print("%d개 생성완료 " % a)
                    
                    
def draw_data_fft(input_data,dir_name):

     x=[]
     y=[]
     count=0
     for i in glob.glob(dir_name+input_data+'_*'):
          x.append(i)
     a=len(x)    
     for i in range (0,a):
         x[i]=x[i].replace("\\","/")
    
     
     k='k'   # 색 수정
     path = dir_name
     file_list = os.listdir(path)
     n=len(file_list)
     
     z=len(input_data)
     for i in range(0,n):
          
          file_name=file_list[i]
          b=len(file_name)
          file_name=(file_name[0:b-4])
          if z == 1:
              if file_name[:2]==(input_data+'_'):
                   y.append(file_name)
          if z == 2:
              if file_name[:3]==(input_data+'_'):
                   y.append(file_name)
                   
     for i in range(0,a):
            count+=1
            draw_fft(x[i],y[i],k,count)         
                 
     return count 


def draw_data_eog_fft(input_data,dir_name):

     x=[]
     y=[]
     count=0
     for i in glob.glob(dir_name+input_data+'_*'):
          x.append(i)
     a=len(x)    
     for i in range (0,a):
         x[i]=x[i].replace("\\","/")
    
     
     k='k'   # 색 수정
     path = dir_name
     file_list = os.listdir(path)
     n=len(file_list)
     
     z=len(input_data)
     for i in range(0,n):
          
          file_name=file_list[i]
          b=len(file_name)
          file_name=(file_name[0:b-4])
          if z == 1:
              if file_name[:2]==(input_data+'_'):
                   y.append(file_name)
          if z == 2:
              if file_name[:3]==(input_data+'_'):
                   y.append(file_name)
               
               
     for i in range(0,a):
            count+=1
            draw_eog_fft(x[i],y[i],k,count)         
                 
     return count 

def draw_data_time(input_data,dir_name):

     x=[]
     y=[]
     count=0
     for i in glob.glob(dir_name+input_data+'_*'):
          x.append(i)
     a=len(x)    
     for i in range (0,a):
         x[i]=x[i].replace("\\","/")
    
     thick=1 #선 굵기 변경
     k='k'   #선 색 변경
     path = dir_name
     file_list = os.listdir(path)
     n=len(file_list)
     z=len(input_data)
     for i in range(0,n):
          
          file_name=file_list[i]
          b=len(file_name)
          file_name=(file_name[0:b-4])
          if z == 1:
              if file_name[:2]==(input_data+'_'):
                   y.append(file_name)
          if z == 2:
              if file_name[:3]==(input_data+'_'):
                   y.append(file_name)
               
     for i in range(0,a):
          count+=1
          draw_time(x[i],y[i],thick,k,count)
                 
     return count


def draw_data_eog(input_data,dir_name):

     x=[]
     y=[]
     count=0
     for i in glob.glob(dir_name+input_data+'_*'):
          x.append(i)
     a=len(x)    
     for i in range (0,a):
         x[i]=x[i].replace("\\","/")
    
     thick=1 #선 굵기 변경
     k='k'   #선 색 변경
     path = dir_name
     file_list = os.listdir(path)
     n=len(file_list)
     z=len(input_data)
     for i in range(0,n):
          
          file_name=file_list[i]
          b=len(file_name)
          file_name=(file_name[0:b-4])
          if z == 1:
              if file_name[:2]==(input_data+'_'):
                   y.append(file_name)
          if z == 2:
              if file_name[:3]==(input_data+'_'):
                   y.append(file_name)
               
     for i in range(0,a):
          count+=1
          draw_time_eog(x[i],y[i],thick,k,count)
                 
     return count




def menu():
    print("■■■■■■■■■■■■■")
    print("■  1.시           작   ■")
    print("■                      ■")
    print("■  2.프 로 그 램 종료  ■")
    print("■■■■■■■■■■■■■")

def draw_menu():
    print("■■■■■■■■■■■■■■■■")
    print("■  1. E E G 시간영역 데이터  ■")
    print("■                            ■")
    print("■  2. E O G 시간영역 데이터  ■")
    print("■                            ■")
    print("■  3. E E G 주파수영역데이터 ■")
    print("■                            ■")
    print("■  4. E O G 주파수영역데이터 ■")
    print("■                            ■")
    print("■  7.프 로 그 램 종료        ■")
    print("■■■■■■■■■■■■■■■■")


# In[ ]:





# In[ ]:





# In[ ]:




