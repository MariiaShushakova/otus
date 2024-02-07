import os


def get_path(file_name):
    work_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(work_folder, file_name)



JSON_FILE_LIST_DOGS = get_path('list_dogs.json')

