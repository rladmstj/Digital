import difflib

def show_file_diff(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        diff = difflib.unified_diff(
            f1.readlines(), f2.readlines(),
            fromfile=file1, tofile=file2,
            lineterm=''
        )
        print('\n'.join(diff))
 
show_file_diff("/Users/kim-eunseo/Desktop/Digital/hw2/sample.txt.out", "/Users/kim-eunseo/Desktop/Digital/hw2/sample.txt.out2")