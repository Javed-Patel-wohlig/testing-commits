import os

file_path = "test-gitops/count.txt"

# Read current count from the file
with open(file_path, "r") as file:
    count = int(file.read().split(":")[1].strip())

# Update count
count += 50

# Update file content
with open(file_path, "w") as file:
    file.write(f"hello i am devops\nmy commit count is: {count}\nthank you")

# Commit and push changes
os.system("git add .")
os.system("git commit -m 'Update commit count'")
os.system(f"git push https://Javed-Patel-wohlig:${{ secrets.TOKEN100 }}@github.com/Javed-Patel-wohlig/test-gitops.git HEAD:main")
