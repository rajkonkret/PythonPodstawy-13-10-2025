import chardet

# pip - manager pakietów
print(chardet)
# <module 'chardet' from 'C:\\Users\\Szkolenie\\PycharmProjects\\PythonPodstawy-13-10-2025\\
# .venv\\Lib\\site-packages\\chardet\\__init__.py'>

file_path = 'test.log'

# biblioteka wymaga odczytu jako bajty
# rb - odczyt bajtowy
with open(file_path, "rb") as file:
    raw_data = file.read()

print(raw_data)
# b'Nowe dane\r\nDopisane\r\nKolejne\r\nJeszcze jedno\r\nDo\xc5\x9bpisane\r\n'

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'MacRoman', 'confidence': 0.621044776119403, 'language': ''}
#  po zwiekszeniu próbki otrzymujemy wyższa zgodność
# {'encoding': 'utf-8', 'confidence': 0.938125, 'language': ''}
encoding = result['encoding']
confidence = result['confidence']
print("Kodowanie zanków:", encoding)  # Kodowanie zanków: utf-8
print("Trafnośc:", confidence)  # Trafnośc: 0.938125

print(raw_data.decode(encoding=encoding))
# Nowe dane
# Dopisane
# Kolejne
# Jeszcze jedno
# Dośąćźpisane
