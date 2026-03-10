import kagglehub
import shutil

#Download latest version of mnist dataset

path = kagglehub.dataset_download("hojjatk/mnist-dataset")

print("downloaded to ", path)

dest = "./dataset"

shutil.move(path, dest)

print("check", dest)