from os import walk
dir_path = r'C:\Users\EV-02\Documents\GitHub\bronco-ctf-writeups-2024'
temp1 = "https://raw.githubusercontent.com/ccyannchan/bronco-ctf-writeups-2024/main/"

res = []

for (dir_path, dir_names, file_names) in walk(dir_path):
    res.extend(file_names)
print(res)



#temp2 = path
#print(f"{temp1+temp2+'/'}")

#print(f"{res}")

#first part
#https://raw.githubusercontent.com/ccyannchan/bronco-ctf-writeups-2024/main/
#second part
#blue_boy_storage
#third part
#/
#fourth part
#blue_boy_storage_prompt.PNG

#c:\Users\EV-02\Documents\GitHub\bronco-ctf-writeups-2024\blue_boy_storage



#filename = temp1 + temp2 + temp3
#print(f"{filename}")

