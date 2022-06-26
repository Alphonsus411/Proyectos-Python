def file_size(file_info):
    name, type, size = file_info
    return("{:.2f}".format(size / 1024))

print(file_size(('Class Assigment', 'docx', 17875))) #should print 17.46
print(file_size(('Notes', 'txt', 496))) #should print 0.48
print(file_size(('Program', 'py', 1239))) #should print 0.12
