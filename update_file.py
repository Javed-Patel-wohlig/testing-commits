import os

# Provide the correct file path relative to the script
file_path = "count.txt"

# Read current count from the file
with open(file_path, "r") as file:
    content = file.read()

# Extract numeric part from the content
count = ''.join(filter(str.isdigit, content))

# Convert the count to an integer
count = int(count) + 50

# Update file content
with open(file_path, "w") as file:
    file.write(f"hello i am devops\nmy commit count is: {count}\nthank you")

# Commit and push changes
os.system("git add .")
os.system("git commit -m 'Update commit count'")
os.system(f"git push https://Javed-Patel-wohlig:${{ secrets.TOKEN100 }}@github.com/Javed-Patel-wohlig/test-gitops.git HEAD:main")
