from src.lab4.io_txt_csv import read_text, write_csv
txt = read_text("src/data/lab4/input.txt") 
print(txt) # должен вернуть строку
write_csv([("word","count"),("test",3)], "src/data/lab4/check.csv")  # создаст CSV
