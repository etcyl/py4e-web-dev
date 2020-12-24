# Uses regular expressions to add the sum of all numbers found in the text document.

import re

#sample_text_filename = "sample_text.txt"
actual_text_filename = "actual_text.txt"

#sample_file = open(sample_text_filename, 'r') 
actual_file = open(actual_text_filename, 'r') 
#sample_lines = sample_file.readlines() 
actual_lines = actual_file.readlines()

total_sum = 0

#for line in sample_lines:
    #nums = re.findall('[0-9]+', line)
    #for i in range(len(nums)):
        #num = int(nums[i])
        #total_sum += num
    
#print(sample_text_filename, "value is: ", total_sum)

total_sum = 0

for line in actual_lines:
    nums = re.findall('[0-9]+', line)
    for i in range(len(nums)):
        num = int(nums[i])
        total_sum += num
    
print(actual_text_filename, "value is: ", total_sum)
