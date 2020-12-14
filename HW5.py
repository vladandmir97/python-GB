#!/usr/bin/env python
# coding: utf-8

# In[197]:


#1
with open('dz5_1.txt','w') as file:
    while True:
        text = input('Введите текст для окончания введите пустую строку: ')
        if text!='':
            file.write(text+'\n')
        else:
            break


# In[199]:


#2
with open('lists.txt','r') as file:
    for i,line in enumerate(file):
        n_words = len(line.split(' '))
        print(f'Строка {i+1} число слов: {n_words}')
    print(f'Всего строк {i+1}')


# In[219]:


#3
with open('wages.txt','r',encoding='utf-8') as file:
    lines = file.readlines()
    names = [i.split(' ')[0] for i in lines]
    wages = [float(i.split(' ')[1].replace('\n','')) for i in lines]
max_w = max(wages)
max_salary_person = names[wages.index(max_w)]
print(f'Персона с максимальной ЗП - {max_salary_person} с окладом {max_w}$')


# In[222]:


#4
rus = {
    'One':'Один',
    'Two':'Два',
    'Three':'Три',
    'Four':'Четыре'
}
with open('numbers.txt','r',encoding='utf-8') as file:
    with open('numbers_rus.txt','w') as file_ru:
        lines = file.readlines()
        nums_text = [i.split(' ')[0] for i in lines]
        nums = [i.split(' ')[-1].replace('\n','') for i in lines]
        [file_ru.write(rus[w]+' - '+ c +'\n') for w,c in zip(nums_text, nums)]


# In[227]:


#5
with open('summa.txt','w') as file:
    while True:
        text = input('Введите числа для окончания введите пустую строку: ')
        if text!='':
            file.write(text+' ')
        else:
            break
with open('summa.txt','r') as file:
    numbers = file.read()
summa = sum([float(i) for i in numbers.split(' ')[:-1]])
print('Сумма чисел в файле:',summa)


# In[253]:


#6
import re
with open('class.txt','r',encoding='utf-8') as file:
    lessons_time = {re.findall('(\w+):',a)[0]:sum([int(i) for i in re.findall('(\d+)',a)]) for a in file}

lessons_time


# In[261]:


#7
with open('firms.txt','r',encoding='utf-8') as file:
    mean_prof = []
    for i in file:
        f = i.split(' ')
        name = f[0]
        form = f[1]
        inc = float(f[2])
        cost = float(f[3])
        prof = inc-cost
        if prof>=0:
            mean_prof = mean_prof+[prof]
        print(f'Фирма {name} имеет прибыль {prof}')
    mean_prof = sum(mean_prof)/len(mean_prof)
print('Средняя прибыль среди прибыльных компаний',round(mean_prof,2))


# In[ ]:




