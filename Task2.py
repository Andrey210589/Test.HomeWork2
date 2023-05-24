# Задача 12: 
# Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

s = int(input("Input sum of numbers "))
p = int(input("Input the product of numbers "))
d = s**2-4*p
x=(s + (s**2-4*p)**0.5)/2
y=(s - (s**2-4*p)**0.5)/2
if d == 0:
    print(f"Root is {x} ")
elif d > 0:
    print(f"Roots of the equation is {x} and {y}")
else:
    print("Input another numbers")

