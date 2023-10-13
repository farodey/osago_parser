import sys
import openpyxl


def main():
    # Укажите путь к файлу Excel
    file_path = sys.argv[1]

    # Укажите имя листа, на котором вы хотите выполнить поиск
    sheet_name = 'Лист1'

    # Укажите значение, которое вы ищете в 5-ой колонке
    search_value = sys.argv[2]

    # Открываем файл Excel
    workbook = openpyxl.load_workbook(file_path)

    # Получаем лист по его имени
    sheet = workbook[sheet_name]

    # Проходим по каждой строке листа
    for row in sheet.iter_rows(values_only=True):
        # Проверяем, соответствует ли значение в 5-ой колонке искомому значению
        if row[7] == search_value:  # Здесь 4 - индекс 5-ой колонки (0-based индекс)
            # Если соответствует, выводим всю строку
            print(row)

    # Закрываем файл Excel
    workbook.close()


if __name__ == '__main__':
    main()
