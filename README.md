# Second-Largest-number-from-stack
Finding Second Large number without using any sorting algorithms

# Second Largest Element Finder

This repository contains a Python program to find the second largest element in an array of integers. The program avoids using any built-in functions for finding substrings or reversing elements, and it manually traverses the array to determine the largest and second largest numbers.


# Navigate to the project directory:
cd second-largest-element-finder

# Usage
You can run the program directly by executing the second_largest.py file.
      python second_largest.py
You will be prompted to enter the array elements as space-separated integers. The program will output the second largest element.

# Algorithm
Initialize two variables, largest and second_largest, to store the largest and second largest values, respectively.
Traverse the array:
If the current element is greater than largest, update second_largest to the previous value of largest and set largest to the current element.
If the current element is less than largest but greater than second_largest, update second_largest.
After traversing the array, check if second_largest has been updated; if not, it means there was no second largest element.
Return the second largest element.

# Example
Given an input array: 
Enter the array elements separated by spaces: 10 20 5 8 15
The program will output:
output:
The second largest element is: 15
Contributing
Contributions are welcome! If you have suggestions for improvements or additional features, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.
