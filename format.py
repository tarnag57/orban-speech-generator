with open('orban-beszedek.txt', 'r') as myfile:
    data = myfile.read().replace('\n', '')

formatted = data.replace('. ', '.\n')

out_file = open("formatted.txt", "w")
out_file.write(formatted)
out_file.close()