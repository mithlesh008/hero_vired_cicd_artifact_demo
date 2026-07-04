from datetime import datetime
print("Python Artifact Demo")

with open("results.txt","w")  as file:
  file.write("Hello from Github\n")
  file.write("Created by Git\n")
  file.write(f"Generated Time: {datetime.now()}\n")

print("results.txt file is created successfully")
