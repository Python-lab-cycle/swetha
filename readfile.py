#Write a program to read a file line by line & store it into a list
fn = open('text1.txt', 'r')
# read the content of the file line by line
list = fn.readlines()
print("content of file\n\n",list)
fn.close()
