def custom_write(file_name, strings):
    strings_positions = {}
    file_name = 'test.txt'
    with open('test.txt', 'w', encoding='utf-8') as file:
        for a, string in enumerate(strings, 1):
            strings_positions[(a, file.tell())] = string
            file.write(string + '\n')
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
