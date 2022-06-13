import numpy as np
import random
from utils import add_class

output_el = Element('output').element
console.log(output_el)

arr = np.array([2, 13, 7, 64, 17, 23, 31])
pyscript.write('output', f"{arr}")

def shuffle_array(*args):
  shuffled = sorted(arr, key=lambda k: random.random())
  output_el.innerHTML = f"{shuffled}"
  # change color
  add_class(output_el, 'text-blue-500')

def sort_array(*args):
  sort = sorted(arr)
  output_el.innerHTML = f"{sort}"
  
  add_class(output_el, 'text-pink-500')