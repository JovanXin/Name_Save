import os
names = [] 
PATH = "programData\\name" #setting the path 


try:
  os.makedirs(PATH, exist_ok=True) #if path exists, do not error, else make path
except OSError:
    print ("Creation of the directory %s failed" % PATH) #if error occurs, print a error message
else:
    print ("Successfully created the directory %s" % PATH)
    os.chdir(PATH) #navigate to path


with open("names.txt", "r") as file_1:
  for line in file_1:
    names.append(line.strip()) #adds names from file to list


if len(names)==0: #if there are no names in list
  names = input("please type names, seperated by a comma:").split(",")

# try:
#   len(names)
# except Exception:
#   names = input("please type names, seperated by a comma").split(",")

while True: #add extra names
  print(names)
  choice = input("would you like to add more names? y/n:")
  if choice == ("y"):
    extra_names = input("please type names, seperated by a comma:").split(",")
    for name in extra_names:
      names.append(name)
    print(f'These are your names currently:{",".join(names)}')
    break

  elif choice == ("n"):
    print("okay, exiting") 
    break

  else:
    print("not a valid input, try again")

with open("names.txt", "w") as file_1:
  for name in names:
    file_1.write(f"{name}\n") #writes names back into file
