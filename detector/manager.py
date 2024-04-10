import os


def check_downloadable():
    pass


def get_available_models():
    result = []
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')
    for file in os.listdir(directory):
        if file.endswith(".pt"):
            result.append(file)
    return result
