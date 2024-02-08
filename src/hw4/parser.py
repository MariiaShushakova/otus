import json
from copy import deepcopy
from csv import DictReader

from src.hw4.files.file_path import CSV_FILE, RESULT_JSON_FILE, JSON_FILE


def read_books_csv():
    """read CSV file with books"""

    with open(CSV_FILE, "r") as csv:
        books = DictReader(csv)
        read_csv = []
        for row in books:
            read_csv.append(row)

    return read_csv


def create_book_list(read_csv):
    """creation proper book list"""
    book_list = []
    for i in read_csv:
        book_result = {
            key: value
            for key, value in i.items()
            if key in ("Title", "Author", "Pages", "Genre")
        }
        book_result["title"] = book_result.pop("Title")
        book_result["author"] = book_result.pop("Author")
        book_result["pages"] = book_result.pop("Pages")
        book_result["genre"] = book_result.pop("Genre")
        book_list.append(book_result)

    return book_list


def read_users_json():
    """read JSON file with users"""

    with open(JSON_FILE, "r") as js:
        users = json.loads(js.read())

    return users


def create_users_list(users):
    """creation proper users list"""
    users_list = []
    for user in users:
        users_result = {
            key: value
            for key, value in user.items()
            if key in ("name", "genre", "address", "age")
        }
        users_result["books"] = []
        users_list.append(users_result)

    return users_list


def books_to_users(books_list, users_list):
    """sharing part"""
    result_list = deepcopy(users_list)
    users_numbers = len(users_list)

    for index, book in enumerate(books_list):
        i = index % users_numbers
        user = result_list[i]
        user['books'].append(book)

    return result_list


def add_result_to_json(result_list):
    """write result into JSON file"""
    with open(RESULT_JSON_FILE, "w") as file:
        json.dump(result_list, file, indent=4)
        file.write("\n")


def main():
    read_csv = read_books_csv()
    book_parser = create_book_list(read_csv)
    read_json = read_users_json()
    user_parser = create_users_list(read_json)
    result = books_to_users(book_parser, user_parser)
    add_result_to_json(result)


if __name__ == "__main__":
    main()