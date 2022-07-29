import os
import sys


def main():
    # Get path from arguments (assumes that there is only one file path in the arguments, meaning the argument separators are interpreted as spaces)
    filepath = ' '.join(sys.argv[1:])
    
    # Get last folder in the path
    dir_name = os.path.basename(os.path.normpath(filepath))
    
    # Get path + files in path (if next(...) raises a StopIteration, no root directory was found and thus the file the path is not valid)
    try:
        root, _, files = next(os.walk(filepath))
    except StopIteration:
        print('Invalid project directory path!')
        return
    
    # Paths for the verilog files that are not the main file (%dir_name%.v)
    verilog_files = ['"' + root + '\\' + _file + '"' for _file in files if not _file.startswith(dir_name + '.') and _file.endswith('.v')]
    
    # Runs pitanga.py with the appropriate arguments
    print('> python pitanga.py -v "' + root + '\\' + dir_name + '.v" ' + ' '.join(verilog_files) + ' -p "' + root + '\\' + dir_name + '.pinout"')
    print()
    os.system('python pitanga.py -v "' + root + '\\' + dir_name + '.v" ' + ' '.join(verilog_files) + ' -p "' + root + '\\' + dir_name + '.pinout"')


if __name__ == '__main__':
    main()
