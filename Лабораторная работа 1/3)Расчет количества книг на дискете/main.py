# TODO Найдите количество книг, которое можно разместить на дискете

# Параметры книги
pages = 100
lines_per_page = 50
symbols_per_line = 25
bytes_per_symbol = 4

# Размер дискеты
disk_size_mb = 1.44
kb_in_mb = 1024
bytes_in_kb = 1024

# Расчеты
total_symbols_in_book = pages * lines_per_page * symbols_per_line
book_size_bytes = total_symbols_in_book * bytes_per_symbol
disk_size_bytes = disk_size_mb * kb_in_mb * bytes_in_kb
books_on_disk = disk_size_bytes // book_size_bytes

# Вывод результата
print("Количество книг, помещающихся на дискету:", books_on_disk)

