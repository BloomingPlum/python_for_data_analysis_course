#!/usr/bin/env python
# coding: utf-8

# В цьому наборі завдань попрацюємо з фукнціями, класами та list comprehensions.
# Нагадую синтаксис list comprehension 
# - з умовою if:
# ```
# newlist = [expression for item in iterable if condition == True]
# ```
# 
# - з умовою if...else:
# ```
# newlist = [expression if condition == True else second_expression for item in iterable ]
# ```

# 1.Задана функція `strange_func`. 
# Запустіть цю функцію на обчислення всіх елементів зі списку `input_list`. Результат обчислень запишіть у `output_list` та виведіть `output_list` на екран.
# 
# Реалізуйте прохід всіх елементів списку `input_list` через цикл та через `list comprehension` - двома способами окремо.

# In[19]:


def strange_func(number: int) -> str:
    if number < 0:
        return "слон"
    else:
        return "жираф"


# In[20]:


input_list = [14, -48, 26, 33, 50, 36, 47, -3, 32, -6, -39, -1, 14, -35, 31, -28, 32, 4, 33, 11, -7, 43, -5, 17, -33, -37, 45, -27, -29, 14]


# In[21]:


# через цикл
output_list = []
for i in input_list:
        output_list.append(strange_func (i))
print (output_list)    


# In[22]:


# через list comprehension 
output_list2 = [strange_func(i) for i in input_list]
print (output_list2)  


# Очікуваний результат: ```['жираф', 'слон', 'жираф', 'жираф', 'жираф', 'жираф', 'жираф', 'слон', 'жираф', 'слон', 'слон', 'слон', 'жираф', 'слон', 'жираф', 'слон', 'жираф', 'жираф', 'жираф', 'жираф', 'слон', 'жираф', 'слон', 'жираф', 'слон', 'слон', 'жираф', 'слон', 'слон', 'жираф']```

# 2.Напишіть функцію `custom_func`, яка приймає на вхід число, перевіряє, чи воно є цілочислельного типу, і якщо так, то перевіряє число на парність: 
# - якщо парне - вертає це число в степені 3, 
# - а якщо непарне - це число мінус 10.  
# 
# Якщо ж число на вході не цілочисельного типу, функція вертає 0.  
# 
# Запустіть цю функцію на обчислення всіх чисел зі списку `input_list`. Результат обчислень запишіть у `output_list` та виведіть `output_list` на екран. 
# 
# Реалізуйте прохід всіх чисел списку `input_list` через цикл та через `list comprehension` - двома способами окремо.

# In[23]:


input_list = [36, 11.1, 91, 93, 26, 12.3213, 69, 50, 58, 22, 77, 18, 24, 55, 11, 76, 10.111, 39, 49, 94, 34, 40, 13, 111.111, 26, 44, 11, 34, 30, 39, 84, 37, 16, 1]


# In[24]:


# function
def custom_func(number: int):
    if type(number) is int:
        if number % 2 == 0:
            number **= 3
        else:
            number -= 10 
    else:
        number = 0
    return number


# In[25]:


# через цикл
output_list = []
for i in input_list:
    output_list.append (custom_func(i))

print (output_list)   
    


# In[26]:


# через list comprehension 
output_list2 = [custom_func(i) for i in input_list]
print (output_list2)  


# Очікуваний результат:
# ```[46656, 0, 81, 83, 17576, 0, 59, 125000, 195112, 10648, 67, 5832, 13824, 45, 1, 438976, 0, 29, 39, 830584, 39304, 64000, 3, 0, 17576, 85184, 1, 39304, 27000, 29, 592704, 27, 4096, -9]```

# Аби програмно порівняти ваш результат за очікуваним - використайте код нижче:

# In[27]:


output_list == [46656, 0, 81, 83, 17576, 0, 59, 125000, 195112, 10648, 67, 5832, 13824, 45, 1, 438976, 0, 29, 39, 830584, 39304, 64000, 3, 0, 17576, 85184, 1, 39304, 27000, 29, 592704, 27, 4096, -9]


# In[28]:


if output_list == output_list2:
    print ("Ви впорались з завданням!")
else:
    print ("Завдання виконано невірно :( ")


# 3.Напишіть функцію, яка отримує список чисел і повертає інший список із квадратами чисел, які діляться на 2 із вихідного списку. Наприклад, якщо на вході список [1,2,3,4], то на виході буде список [4,8].
# 
# Запустіть функцію на вхідних списках `numbers_1`, `numbers_2`, `numbers_3` та виведіть результат роботи фукнції на екран.

# In[29]:


numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [-18, 35, 50, 2, -39, 8, -39, -15, 14, -42]
numbers_3 = [-3.1, 1.11, 3.48, 4.48, 4.68, -1.59, -1.8, 1.76, 4.7, 2.0]


# In[30]:


# через цикл
numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [-18, 35, 50, 2, -39, 8, -39, -15, 14, -42]
numbers_3 = [-3.1, 1.11, 3.48, 4.48, 4.68, -1.59, -1.8, 1.76, 4.7, 2.0]

def square_func(numbers):
    result = []
    for i in numbers:
        if i % 2 == 0:
            result.append(i**2)
    return result

all_numbers = [numbers_1, numbers_2, numbers_3]

for figures in all_numbers:
    print(square_func(figures))


# In[31]:


# через list comprehension 
numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [-18, 35, 50, 2, -39, 8, -39, -15, 14, -42]
numbers_3 = [-3.1, 1.11, 3.48, 4.48, 4.68, -1.59, -1.8, 1.76, 4.7, 2.0]

def square_func(numbers):
    return [i**2 for i in numbers if i % 2 == 0]

all_numbers = [numbers_1, numbers_2, numbers_3]

for figures in all_numbers:
    print(square_func(figures))


# Очікуваний результат:
# 
# ```
#     [4, 16, 36, 64, 100]
#     [324, 2500, 4, 64, 196, 1764]
#     [4.0]
# ```

# 4. Наданий список фруктів. Запишіть у новий список лише ті фрукти, які містять у своїй назві літеру `a`. Виведіть фінальний список на екран.
# 
# Виконайте завдання із використанням циклу, та через `list comprehension` - двома способами окремо.  
# Увага! В цьому завданні логіку перевірки чи містить рядок літеру можна винести у функцію. Але якщо не виносити, то реалізація з `list comprehension` буде цікавішою :)

# In[32]:


fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "indian prune", "jackfruit", "kiwi", "lemon", "mango", "nectarine", "orange", "pineapple", "quince", "raspberry", "strawberry", "tangerine", "ugli fruit", "victoria plum", "watermelon", "xigua", "yellow passionfruit", "zucchini"]


# In[33]:


words_with_a = []
for word in fruits:
    for letter in word:
        if letter == "a":
            words_with_a.append (word)
            break
        
print (words_with_a)


# In[34]:


words_with_a = [word for word in fruits if "a" in word]
print (words_with_a)


# 5.Заданий список чисел. Створіть новий список на основі заданоо за наступною логікою
# - якщо число більше або дорівнює 45, то в новий список додаємо це число + 5. Наприклад, для числа 50 вихідного списку, в новий ми додамо число 55
# - інакше - це число - 4. Наприклад, для числа 30 вихідного списку, в новий ми додамо число 26  
# 
# Виведіть отриманий список на екран.
# 
# Реалізуйте логіку через цикл та через `list comprehension` - двома способами окремо.

# In[35]:


input_list = [22, 13, 45, 50, 98, 69, 43, 44, 1]


# In[36]:


output_list = []
for number in input_list:
    if number >= 45:
        output_list.append (number+5) 
    else:
        output_list.append (number-4) 
print (output_list)


# In[37]:


#newlist = [expression if condition == True else second_expression for item in iterable ]
output_list2 = [number + 5 if number >= 45 else number-4 for number in input_list]
print (output_list2)


# 6.Заданий список `input_list` з пропущеними значеннями. Напишіть логіку, за якою ми будемо створювати новий список такий, що якщо значення None, то ми замість нього вставляємо 0, інакше - елемент вихідного спику.
# Тобто зі списку [1, None, 2] за цією логікою ми отримаємо [1, 0, 2] у новому списку.
# 
# Виведіть отриманий список на екран.
# 
# Реалізуйте логіку через цикл та через list comprehension - двома способами окремо.

# In[38]:


input_list = [22, None, 13, None, None, 45, 50, 98, None, 69, 43, 44, 1, None]


# In[39]:


output_list = []
for number in input_list:
    if number == None:
        output_list.append(0)
    else:
        output_list.append(number)

print (output_list)


# In[40]:


output_list2 = [0 if number == None else number for number in input_list]
print (output_list2)


# 7.Заданий клас, який описує коло та вміє рахувати площу кола по заданому радіусу. Створіть два кола з радіусами 5 і 11. Обчислість з допомогою функціоналу класу площі цих двох кіл і виведіть результати на екран.

# In[41]:


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return round(math.pi * self.radius ** 2, 2)


# In[42]:


circle1 = Circle (5)
circle2 = Circle (11)

print(circle1.calculate_area())
print(circle2.calculate_area())


# 8.Додайте в клас `Circle`, визначений в попередньому завданні, метод для обчислення периметра `calculate_perimeter` з округленням до двох цифр після коми. Периметр кола рахується за формулою `C = 2 · π · r`, де π - це значення числа Пі, яке ми можемо отримати з math.pi, а r - радіус кола. Спопіюйте визначення класу і додайте в нього новий метод. Після цього створіть нові кола з радіусами 5 і 11 та обчисліть їх периметри.   
# Увага: нам треба додати новий метод, але ми нічого не видаляємо :)

# In[43]:


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return round(math.pi * self.radius ** 2, 2)
    
    def calculate_perimeter(self):
        return round(2 * math.pi * self.radius, 2)

circle3 = Circle (5)
circle4 = Circle (11)

print(circle3.calculate_perimeter())
print(circle4.calculate_perimeter())


# 9.Створіть клас під назвою `Student`, який має два атрибути: `name` (ім'я) та `grade` (оцінка). Оцінкою може були літера - з набору  ["F", "D", "C", "B", "A"], де "А" - найвища оцінка, "F" - найнижча.  Клас повинен мати наступні функціональні можливості:
# 
# 1. Метод `__init__`, який ініціалізує `name` та `grade`.
# 2. Метод `display_student()`, який відображає ім'я та оцінку студента з допомогою `print`. Форматування - на Ваш розсуд.
# 3. Метод `upgrade_grade()`, який підвищує оцінку на 1 рівень (наприклад, з "B" на "A"), якщо вона вже не "A". Якщо вже "А", то необхідно вивести повідомлення про те, що оцінка не може бути підвищена, оскільки вона вже і так найвища.
# 
# Після створення класу, створіть 2 екземпляри `Student` з вигаданими імʼями та оцінками, і перевірте роботу методів `display_student()` та `upgrade_grade()`. Виведіть результат перевірки на екран.

# In[44]:


class Student:
    GRADES = ["F", "D", "C", "B", "A"] 
    
    def __init__(self, name, grade):
        if grade not in self.GRADES:
            raise ValueError(f"Недійсна оцінка - '{grade}'. Має бути она за ціх оцінок - {self.GRADES}.")
        self.name = name
        self.grade = grade
    
    def display_student(self):
        print(f"Ім'я студента - {self.name}, оцінка студента - {self.grade}")
        return self  # Return self для використання ланцюгового методу 
    
    def upgrade_grade(self):
        if self.grade != "A":
            self.grade = self.GRADES[self.GRADES.index(self.grade) + 1]
        else:
            print (f"Оцінка {self.name} не може бути підвищена, оскільки вона і так найвища.")
        return self  # Return self для використання ланцюгового методу 
            
            

# Create two instances of Student
student1 = Student("Alex", "C")
student2 = Student("Maria", "D")
student3 = Student("Petro", "A")

student1.upgrade_grade().display_student()
student2.upgrade_grade().display_student()
student3.upgrade_grade().display_student()


# 10.Створіть клас з назвою `GraduateStudent`, який є нащадком класу `Student` з попереднього завдання.
# Клас `GraduateStudent` повинен мати додатковий атрибут `thesis_title` (назва дисертації - тип str). Тобто цей атрибут має зʼявитись при ініціації екземпляру класу.  
# Він також повинен мати метод `display_thesis()`, який виводить назву дисертації.
# 
# Після створення класу, створіть екземпляр `GraduateStudent` і перевірте роботу методів `display_student()`, `upgrade_grade()`, та `display_thesis()`. Виведіть результат перевірки на екран.
# 
# 

# In[45]:


class GraduateStudent(Student):
    
    def __init__(self, name, grade, thesis_title):
        super().__init__(name, grade)
        self.thesis_title = thesis_title
        
    def display_thesis(self):
        print (f"Назва дисертації студента {self.name} - {self.thesis_title}")
        return self
    

student4 = GraduateStudent("Ivan", "B", "Data analysis")
student4.upgrade_grade().display_student().display_thesis()

