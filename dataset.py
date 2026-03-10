import kagglehub
#Download latest version of mnist dataset

path = kagglehub.dataset_download("hojjatk/mnist-dataset")

print("downloaded to ", path)