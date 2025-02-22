import os, shutil

def main():
    generate_public_folder()

def generate_public_folder():
    if os.path.exists("./public"):
        print("Found existing ./public folder, deleting...")
        shutil.rmtree("./public")
    print("Creating new ./public folder...")
    os.mkdir("public")
    if not os.path.exists("./static"):
        raise Exception("static directory not found, aborting.")
    copy_folder_to_public()

def copy_folder_to_public(current_path=""):
    static_path = os.path.join("./static", current_path)
    public_path = os.path.join("./public", current_path)
    folder_contents = os.listdir(static_path)
    for item in folder_contents:
        if os.path.isdir(static_path + item):
            print(f"Creating new directory: {public_path + item}")
            os.mkdir(public_path + item)
            copy_folder_to_public(current_path + item + "/")
        else:
            print(f"Copying file {static_path + item} to location {public_path}")
            shutil.copy(static_path + item, public_path + item)
main()