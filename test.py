import os
import glob

from main import read_data, PATH, create_images
TEST_JSON = 'test_data.json'


def test_read_data():
    message = read_data(f'{PATH}/{TEST_JSON}')
    assert message == "Температура: 70.4\nCO2: 1971"


def test_images():
    dir_name = f'{PATH}'
    test = os.listdir(dir_name)
    for item in test:
        if item.endswith(".png"):
            os.remove(os.path.join(dir_name, item))
    create_images()
    assert (len(glob.glob1(dir_name, "*.png")) == 5)