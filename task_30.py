i = {'a': ['у', 'е', 'ё', 'а', 'о', 'э', 'я', 'и', 'ю', 'ы'],
           'b': ['й', 'ц', 'к', 'н', 'г', 'ш', 'щ', 'з', 'х',
                          'ф', 'в', 'п', 'р', 'л', 'д', 'ж', 'ч', 'с', 'м', 'т', 'б']}

string = str(input())
a_sum, b_sum = 0, 0

for letter in string:
  if letter in i['a']:
    a_sum += 1

  elif letter in i['b']:
    b_sum += 1

print(f'Количество гласных - {a_sum}, количество согласных - {b_sum}')