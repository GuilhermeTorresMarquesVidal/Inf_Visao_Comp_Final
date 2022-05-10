from os import listdir
from skimage import transform
from os.path import isfile, join
import matplotlib.image as mpimg

def read_Base(path):

    files = [f for f in listdir(path) if isfile(join(path,f))]

    images_db = []

    print("Carregando arquivos")

    for file in files:
        images_db.append(mpimg.imread(join(path,file)))

    print("Arquivos carregados")

    return images_db

def images_resize(images_db, height, width, n_channels):

    images_db_resize = []

    count = 1

    print("Começando o resize das imagens")

    for image in images_db:
        print(count)
        images_db_resize.append(transform.resize(image,(height,width,n_channels),anti_aliasing = True))
        count += 1

    return images_db_resize

def save_new_Base(path, images_db):

    count = 0

    print("Salvando arquivos")

    for image in images_db:
        mpimg.imsave(path + str(count) + '.png',image)
        count += 1

    print("Done")

path = 'DataBase/'

height = 150
width = 225
n_channels = 3

new_path = 'DataBaseResize/'

images_db = read_Base('DataBase/')

images_db_resize = images_resize(images_db, height, width, n_channels)

save_new_Base(new_path, images_db_resize)