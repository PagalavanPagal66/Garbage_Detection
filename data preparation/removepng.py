import glob
import pathlib

for file in glob.glob('Garbage blob dataset/*.png'):
  path = pathlib.Path(file)
  path.unlink()