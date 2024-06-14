def copy_file(source_file, destination_file):
   
    try:
        with open(source_file, 'r') as src:
            contents = src.read()
        
        with open(destination_file, 'w') as dst:
            dst.write(contents)
            
        print(f"Contents of '{source_file}' have been copied to '{destination_file}'.")
    except FileNotFoundError:
        print(f"The file '{source_file}' does not exist.")
    except IOError as e:
        print(f"An error occurred while copying the file: {e}")


source_file = 'source.txt'
destination_file = 'destination.txt'


copy_file(source_file, destination_file)
