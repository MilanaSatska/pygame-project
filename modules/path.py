import os
def find_path(path_name):
    try:
        path = os.path.abspath(__file__+"/../..")
        path = os.path.join(path, f"assets/{path_name}")
        return path
    except Exception as error:
        print(f"ошибка при поиске пути, {error}")