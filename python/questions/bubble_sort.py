#   Write a function that takes in an array of integers and returns a sorted
#   version of that array. Use the Bubble Sort algorithm to sort the array.
# </p>
# <p>
#   If you're unfamiliar with Bubble Sort, we recommend watching the Conceptual
#   Overview section of this question's video explanation before starting to code.
# </p>
# <h3>Sample Input</h3>
# <pre><span class="CodeEditor-promptParameter">array</span> = [8, 5, 2, 9, 5, 6, 3]
# </pre>
# <h3>Sample Output</h3>
# <pre>[2, 3, 5, 5, 6, 8, 9]
# </pre></div>


# O(n^2) time | O(1) space
def bubbleSort(array):
    # Write your code here.
    isSorted = False
    counter = 0
    # Counter is just a minor optimization to prevent it from including the largest number in subsequent sort, since it's already sorted
    while not isSorted:
      isSorted = True
      for i in range(len(array) - 1 - counter):
        if array[i] > array[i + 1]:
          swap(i, i + 1, array)
          isSorted = False
      counter += 1
    return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]


