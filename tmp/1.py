
summ = 0
cnt = 0
n = int(input())
while (n != 0 ):
    
    if (n % 8) == 0:
        summ += n
        cnt +=1
    n = int(input())

print(f"Среднее арифметическое {cnt} чисел с суммой {summ} равно {summ/cnt}.")