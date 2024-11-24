import os
import shutil

def copy_static_to_public():
    public_items = os.listdir("public")
    for item in public_items:
        ull_path = os.path.join("public", item)
        if os.path.isfile(ull_path) or os.path.islink(ull_path):
            os.remove(ull_path)
        elif os.path.isdir(ull_path):
            shutil.rmtree(ull_path)
    
    static_items = os.listdir("static")
    for item in static_items:
        ull_path = os.path.join("static", item)
        destination_path = os.path.join("public", item)
        if os.path.isfile(ull_path) or os.path.islink(ull_path):
            shutil.copy(ull_path, destination_path)
        elif os.path.isdir(ull_path):
            shutil.copytree(ull_path, destination_path)

    