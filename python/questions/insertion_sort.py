# <div class="N2R35Mw6IkWkfVyEP6Ysv"><p>
#   Write a function that takes in an array of integers and returns a sorted
#   version of that array. Use the Insertion Sort algorithm to sort the array.
# </p>
# <p>
#   If you're unfamiliar with Insertion Sort, we recommend watching the Conceptual
#   Overview section of this question's video explanation before starting to code.
# </p>
# <h3>Sample Input</h3>
# <pre><span class="CodeEditor-promptParameter">array</span> = [8, 5, 2, 9, 5, 6, 3]
# </pre>
# <h3>Sample Output</h3>
# <pre>[2, 3, 5, 5, 6, 8, 9]
# </pre></div>


# O(n^2) time || O(1) Space
def insertionSort(array):
  for i in range(1, len(array)):
    j = i
    while j > 0 and array[j] < array[j - 1]:
      swap(j, j - 1, array)
      j -= 1
  return array


def swap(i, j, array):
  array[i], array[j]  = array[j], array[i]
