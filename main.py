namelist = []

def printlist():
  print()
  for name in namelist:
    print(name)
  print()
while True:
  firstname = input("First Name: ").strip().capitalize()
  lastname = input("Last Name: ").strip().capitalize()
  name = f"{firstname} {lastname}"
  if name not in namelist:
    namelist.append(name)
  else:
    print("ERROR: Duplicate name")
  printlist()
