import os
import sys
import numpy as np
from skimage.io import imread, imsave
from skimage.transform import resize
import itertools

src_image_folder = sys.argv[1]
dst_phase_folder = sys.argv[2]
phase_name = 'val'

image_names = []
person_names = set([])
for image_name in os.listdir(src_image_folder):
  image_names.append(image_name)
  person_names.add(image_name.split('-')[0])

# Step 2:
postfix_map = {0 : '-1-4x', 1: '-3-4x', 2: '-p-4x', 3: '-5-4x'}
from_to_pattern = [t for t in itertools.product(range(0, 4), range(0, 4)) if t[0] != t[1]]
print(from_to_pattern)
pattern_pairs = []
ext_name = 'jpg'
for person_name in person_names:
  for pattern in from_to_pattern:
    name1 = '{}{}.{}'.format(person_name, postfix_map[pattern[0]], ext_name)
    name2 = '{}{}.{}'.format(person_name, postfix_map[pattern[1]], ext_name)
    print(name1, name2)
    if not (name1 in image_names and name2 in image_names):
      continue
    pattern_pairs.append([name1, name2])
with open(os.path.join(dst_phase_folder, 'fashion-pairs-{}.csv'.format(phase_name)), 'w') as fp:
  fp.write(',from,to\n')
  for index, pattern_pair in enumerate(pattern_pairs):
    fp.write('{},{},{}\n'.format(index, pattern_pair[0], pattern_pair[1]))

