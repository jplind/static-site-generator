import os, shutil

def generate_public():
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public")
    recursive_copy("static", "public")

def recursive_copy(src, dest):
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        else:
            os.mkdir(dest_path)
            recursive_copy(src_path, dest_path)