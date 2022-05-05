import os
import sys
import scipy.io.wavfile as wavfile


def sort_wavs(source):
    # Create destination folders
    directories = ['0s-10s', '10s-30s', '30s-60s', '60s+']
    for directory in directories:
        if not os.path.isdir(directory):
            os.mkdir(directory)

    # Navigate through file tree at source path
    for root, folderNames, fileNames in os.walk(source[1]):
        print('root: ' + str(root))
        print('folders: ' + str(folderNames))
        print('files:  ' + str(fileNames) + '\n')

        # Loop through each file
        # Move them to corresponding folder according to duration
        for file in fileNames:
            # Get absolute path of file
            file_path = os.path.join(root, file)
            print('Reading ' + file + ' from ' + file_path)

            fs, aud = wavfile.read(file_path)
            print(str(aud.shape) + '\n')

            # Select left channel only
            if len(aud.shape) > 1:
                aud = aud[:, 0]

            # Calculate duration
            duration = aud.shape[0] / fs

            # Move files based on duration
            if duration < 10:
                move_file(file, file_path, directories[0])
            elif duration < 30:
                move_file(file, file_path, directories[1])
            elif duration < 60:
                move_file(file, file_path, directories[2])
            else:
                move_file(file, file_path, directories[3])


def move_file(file, file_path, destination):
    path_to_folder = os.path.join(os.getcwd(), destination)
    new_path = os.path.join(path_to_folder, file)
    if os.path.exists(new_path):
        new_path = new_path + '(1)'
    print('Moving ' + file)
    print('From ' + file_path + ' to ' + new_path + '\n')
    os.rename(file_path, new_path)


if __name__ == '__main__':
    sort_wavs(sys.argv)
