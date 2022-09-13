from typing import List

def insertionSort(array) -> List[int]:
  # Write your code here
  for i in range(1, len(data)):
    temp = data[i]
    j = i-1
    while j>=0 and temp<data[j]:
      data[j+1] = data[j]
      j = j-1
    data[j] = temp

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
