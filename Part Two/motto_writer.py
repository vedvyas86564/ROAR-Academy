# Step 1: Create a file named motto.txt and write the first line
with open('motto.txt', 'w') as file:
    file.write('Fiat Lux!\n')

# Step 2: Properly close the file, then reopen it to print out its content
with open('motto.txt', 'r') as file:
    content = file.read()
    print('Content of motto.txt after first write:')
    print(content)

# Step 3: Append the file with the second line
with open('motto.txt', 'a') as file:
    file.write('Let there be light!\n')

# Reopen the file to print out its updated content
with open('motto.txt', 'r') as file:
    updated_content = file.read()
    print('Content of motto.txt after appending:')
    print(updated_content)