# <div class="_2cjRhfXbSATpeY6gWYgvJE"><p>
#   Write a function that takes in an array of integers and returns a sorted
#   version of that array. Use the Selection Sort algorithm to sort the array.
# </p>
# <p>
#   If you're unfamiliar with Selection Sort, we recommend watching the Conceptual
#   Overview section of this question's video explanation before starting to code.
# </p>
# <h3>Sample Input</h3>
# <pre><span class="CodeEditor-promptParameter">array</span> = [8, 5, 2, 9, 5, 6, 3]
# </pre>
# <h3>Sample Output</h3>
# <pre>[2, 3, 5, 5, 6, 8, 9]
# </pre></div>

def selectionSort(array):
  currentIdx = 0
  while currentIdx < len(array) - 1:
    smallestIdx = currentIdx
    for i in range(currentIdx + 1, len(array)):
      if array[smallestIdx] > array[i]:
        smallestIdx = i
    swap(currentIdx, smallestIdx, array)
    currentIdx += 1
  return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]