import os
import sys
from PIL import Image
from pathlib import Path

current_path = os.getcwd()
source = os.path.join(current_path, sys.argv[1])
destination = os.path.join(current_path, sys.argv[2])

print('Current path is: {}'.format(current_path))
print('Source path is: {}'.format(source))
print('Destination path is: {}'.format(destination))

def minimize_image(filename, source, dest):
  print('Process image file.')
  try:
    image = Image.open(os.path.join(source, filename))
    image.save(os.path.join(dest, filename), quality=50)
  except IOError:
    print('Error, is not file.')

def process_images(source, destination):
  if not os.path.exists(destination):
    os.mkdir(destination)
    print('Directory is created by path {}'.format(destination))

  directory_context = os.listdir(source)

  for path in directory_context:
    full_path = os.path.join(source, path)

    if os.path.isfile(full_path):
      minimize_image(path, source, destination)

    if os.path.isdir(full_path):
      os.chdir(full_path)
      print('Changed directory to {}'.format(full_path))
      process_images(os.getcwd(), os.path.join(os.getcwd(), destination, path))

def main():
  process_images(source, destination)

if __name__ == "__main__":
  main()