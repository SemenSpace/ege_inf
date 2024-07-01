"""Текстовый файл 24-J3.txt состоит не более чем из 10 в 6 степени символов I, K, O, T.
Сколько раз встречаются комбинации «TIK» и «TOK»."""

f = open('6.txt')
f = f.readline()

f = f.replace('TIK', 'TOK')
f = f.replace('TOK', 'G')

print(f.count('G'))
