from multiprocessing import Pool
import os.path

def process_file(name):
   windows_line_ending = '\r\n';
   linux_line_ending = '\n'
   
   with open(name,'rb') as f:
      content = f.read();
      content = content.replace(windows_line_ending, linux_line_ending)

   with open(name, 'wb') as f:
      f.write(content)

def process_files_parallel(directory):
   pool = Pool()
   files = []
   for item in os.listdir(directory):
      entry = os.path.join(directory, item)
      if os.path.isfile(entry):
         files.append(entry)
   pool.map(process_file, files)



if __name__ == '__main__':
   directory_path = raw_input("Enter Directory: ");
   process_files_parallel(directory_path)