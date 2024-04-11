import os

def list_files_and_save(directory_path, output_file):
    # Get the list of files in the specified directory
    files = os.listdir(directory_path)
    files.sort()
    # Create or open the output file in write mode
    with open(output_file, 'w') as file:
        # Write each file name to the file
        for file_name in files:
            file.write('/home1/chengen175/yolov5n_ori/yolov5/dataset_val0304/val/images/'+file_name + '\n')

# Specify the directory path and the output file name
directory_path = "/home1/chengen175/dataset/test_images_20220304/"
output_file = '/home1/chengen175/yolov5n_ori/yolov5/20220304.txt'

# Call the function to list files and save to the text file
list_files_and_save(directory_path, output_file)
