# działania z plikami
# context managerów
# with - context manager w pythonie

# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('test.log', "w", encoding="utf-8") as f:  # filehandler
    f.write("Powitanie\n")
    f.write("Kolejne\n")
    f.write("Jeszcze jedno\n")

# FileExistsError: [Errno 17] File exists: 'test.log'
# x - tworzy nowy plik
# # jesli istnieje będzie błąd: FileExistsError
# with open('test.log', 'x', encoding="utf-8") as file:
#     file.write("Jestem X")

# w - nadpisze plik jeśli juz istnieje
with open('test.log', "w", encoding="utf-8") as f:
    f.write("Nowe dane\n")

with open('test.log', "a", encoding="utf-8") as f:
    f.write("Dopisane\n")
    f.write("Kolejne\n")
    f.write("Jeszcze jedno\n")
    f.write("Dośąćźpisane\n")

with open('test.log', "r", encoding="utf-8") as fh:
    lines = fh.read()

print(lines)
# Nowe dane
# Dopisane
# Kolejne
# Jeszcze jedno
# Dopisane
