#!/usr/bin/env python3
#Author ID: rakbar8


def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r')
    stringx = f.read()
    f.close()
    return(stringx)
    
    
def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open(file_name, 'r')
    listx = f.read().strip().split('\n')
    f.close()
    return(listx)
    
    
    

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
   f = open(file_name, 'a')
   string_append =  f.write(string_of_lines)
   f.close()
   
   

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    f = open(file_name, 'w')
    for listn in list_of_lines:
        f.write(str(listn) + '\n')
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    f = open(file_name_read, 'r')
    list2 = f.read().strip().split('\n')
    f.close()
    
    f = open(file_name_write, 'w')
    line_no = 1
    for line in list2:
        f.write(str(line_no) + ':' + str(line) + '\n')
        line_no += 1
    
    




if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))