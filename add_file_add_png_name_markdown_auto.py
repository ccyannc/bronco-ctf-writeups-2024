import os
import glob

current_dir = os.getcwd()

print(current_dir)

link1 = "https://github.com/ccyannchan/bronco-ctf-writeups-2024/blob/main/"

files_dir = [
    f for f in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, f))
]


for subfolder in files_dir:
    pngs = glob.glob((current_dir + "\\" + str(subfolder)) + "\*.png")
    if len(pngs) != 0:
        png_name = os.path.basename(pngs[0])

        path = current_dir + "\\" + subfolder + "\\" + "README.md"

        file = open(path , "a")
        file.write(link1 + subfolder + "/" + png_name)



    






    




    



