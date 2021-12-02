from os import getcwd, listdir

def get_files():
    cwd = getcwd()
    li = listdir(cwd+"/output/oversized_images")
    l = len(li)
    return l

if __name__ == "__main__":
    print(get_files())