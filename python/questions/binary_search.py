# <div class="_1-ioPm4Fvc_wJB9qPf6w6C"><div class="_1AQYwWTRrR5D5yePhtRblW"><div class="_3ofsZbOFbxIeQT0YuvxUEl"><span class="_3geoVgjjBkfAvmsu_0iEYJ">Difficulty: </span><span class="
#   _3n3-4r4kri345NtLxT7KNV
#   _3RwgBjc4KfsZjzETFt4GPN" data-tip="Easy" currentitem="false"></span></div><div class="_3ofsZbOFbxIeQT0YuvxUEl"><span class="_3geoVgjjBkfAvmsu_0iEYJ">Category: </span><span class="_1Z67dTlk5y-7QrRzsORbUu" data-tip="Hidden" currentitem="false">Hidden</span></div><div class="_3ofsZbOFbxIeQT0YuvxUEl"><span class="_3geoVgjjBkfAvmsu_0iEYJ">Successful Submissions: </span><span class="">23129+</span></div></div><h2 class="_7c9Xd7SD532Lez9esJhVX">Binary Search<div class="_26jR6AW2XmDGUjI6SzzyT4 undefined" data-tip="Question Not Submitted" currentitem="false"></div><svg viewBox="0 0 16 16" fill="currentColor" xmlns="http://www.w3.org/2000/svg" class="_2bMwrm15W_TE6DAFGbeTJ-"><path d="M12.821 16a.5.5 0 01-.203-.043L8 13.901l-4.618 2.056a.501.501 0 01-.694-.556L3.707 10.3.147 6.732a.502.502 0 01.255-.845l5.103-1.023L7.543.272c.16-.362.753-.362.914 0l2.037 4.592 5.104 1.023a.5.5 0 01.255.845l-3.56 3.567L13.31 15.4a.5.5 0 01-.49.6zM8 12.852c.069 0 .138.015.203.043l3.938 1.754-.882-4.417a.502.502 0 01.137-.452l3.09-3.094-4.441-.89a.5.5 0 01-.36-.288L8 1.708l-1.686 3.8a.5.5 0 01-.36.288l-4.44.89 3.09 3.094c.117.118.169.288.136.452l-.882 4.417 3.939-1.754A.497.497 0 018 12.852z"></path></svg></h2><div class="_2Z1QnqTcQRifY9j8GvbCr8"><p>
#   Write a function that takes in a sorted array of integers as well as a target
#   integer. The function should use the Binary Search algorithm to determine if
#   the target integer is contained in the array and should return its index if it
#   is, otherwise <span>-1</span>.
# </p>
# <p>
#   If you're unfamiliar with Binary Search, we recommend watching the Conceptual
#   Overview section of this question's video explanation before starting to code.
# </p>
# <h3>Sample Input</h3>
# <pre><span class="CodeEditor-promptParameter">array</span> = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
# <span class="CodeEditor-promptParameter">target</span> = 33
# </pre>
# <h3>Sample Output</h3>
# <pre>3
# </pre></div><div class="i_9zIMYnPpU3Ytkl8T2R7"><h3 class="klUO7Mz36GoQpV7OLZXXl">Hints</h3><div class="_3MGOzh6CTxV-pXim21iR66"><div class="
#       EGA5hB1SfCvXrmbRa0dVL
#       _3ueNrNUkUEYmQdId1IdK4Y
      
#       " tabindex="0"><div class="
#       _2VETeTVuVEIZz8hft8XmYx
#       _10QkcGvpB2df5C5bxWnmct
#       "><div class="_1NVSPYP3hBJSyQIQThJcVr">Hint 1</div><svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 292.362 292.362" class="ziG9cplWruSO34u3rlTHj "><path d="M286.935 69.377c-3.614-3.617-7.898-5.424-12.848-5.424H18.274c-4.952 0-9.233 1.807-12.85 5.424C1.807 72.998 0 77.279 0 82.228c0 4.948 1.807 9.229 5.424 12.847l127.907 127.907c3.621 3.617 7.902 5.428 12.85 5.428s9.233-1.811 12.847-5.428L286.935 95.074c3.613-3.617 5.427-7.898 5.427-12.847 0-4.948-1.814-9.229-5.427-12.85z"></path></svg></div><div class="_3eVBLPRkiVIcsNJFJ-3urG"><div class="_2uaA-tUdCiVqJRNjXDpITG"><p class="_3pAwmWjFEZ914S4ilA1cDQ">The Binary Search algorithm works by finding the number in the middle of the input array and comparing it to the target number. Given that the array is sorted, if this middle number is smaller than the target number, then the entire left part of the array is no longer worth exploring since the target number can no longer be in it; similarly, if the middle number is greater than the target number, then the entire right part of the array is no longer worth exploring. Applying this logic recursively eliminates half of the array until the number is found or until the array runs out of numbers.</p></div></div></div></div><div class="_3MGOzh6CTxV-pXim21iR66"><div class="
#       EGA5hB1SfCvXrmbRa0dVL
#       _3ueNrNUkUEYmQdId1IdK4Y
      
#       " tabindex="0"><div class="
#       _2VETeTVuVEIZz8hft8XmYx
#       _10QkcGvpB2df5C5bxWnmct
#       "><div class="_1NVSPYP3hBJSyQIQThJcVr">Hint 2</div><svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 292.362 292.362" class="ziG9cplWruSO34u3rlTHj "><path d="M286.935 69.377c-3.614-3.617-7.898-5.424-12.848-5.424H18.274c-4.952 0-9.233 1.807-12.85 5.424C1.807 72.998 0 77.279 0 82.228c0 4.948 1.807 9.229 5.424 12.847l127.907 127.907c3.621 3.617 7.902 5.428 12.85 5.428s9.233-1.811 12.847-5.428L286.935 95.074c3.613-3.617 5.427-7.898 5.427-12.847 0-4.948-1.814-9.229-5.427-12.85z"></path></svg></div><div class="_3eVBLPRkiVIcsNJFJ-3urG"><div class="_2uaA-tUdCiVqJRNjXDpITG"><p class="_3pAwmWjFEZ914S4ilA1cDQ">Write a helper function that takes in two additional arguments: a left pointer and a right pointer representing the indices at the extremities of the array (or subarray) that you are applying Binary Search on. The first time this helper function is called, the left pointer should be zero and the right pointer should be the final index of the input array. To find the index of the middle number mentioned in Hint #1, simply round down the number obtained from: (left + right) / 2. Apply this logic recursively until you find the target number or until the left pointer becomes greater than the right pointer.</p></div></div></div></div><div class="_3MGOzh6CTxV-pXim21iR66"><div class="
#       EGA5hB1SfCvXrmbRa0dVL
#       _3ueNrNUkUEYmQdId1IdK4Y
      
#       " tabindex="0"><div class="
#       _2VETeTVuVEIZz8hft8XmYx
#       _10QkcGvpB2df5C5bxWnmct
#       "><div class="_1NVSPYP3hBJSyQIQThJcVr">Hint 3</div><svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 292.362 292.362" class="ziG9cplWruSO34u3rlTHj "><path d="M286.935 69.377c-3.614-3.617-7.898-5.424-12.848-5.424H18.274c-4.952 0-9.233 1.807-12.85 5.424C1.807 72.998 0 77.279 0 82.228c0 4.948 1.807 9.229 5.424 12.847l127.907 127.907c3.621 3.617 7.902 5.428 12.85 5.428s9.233-1.811 12.847-5.428L286.935 95.074c3.613-3.617 5.427-7.898 5.427-12.847 0-4.948-1.814-9.229-5.427-12.85z"></path></svg></div><div class="_3eVBLPRkiVIcsNJFJ-3urG"><div class="_2uaA-tUdCiVqJRNjXDpITG"><p class="_3pAwmWjFEZ914S4ilA1cDQ">Can you implement this algorithm iteratively? Are there any advantages to doing so?</p></div></div></div></div><div class="_3MGOzh6CTxV-pXim21iR66"><div class="
#       EGA5hB1SfCvXrmbRa0dVL
#       _3ueNrNUkUEYmQdId1IdK4Y
      
#       " tabindex="0"><div class="
#       _2VETeTVuVEIZz8hft8XmYx
#       _10QkcGvpB2df5C5bxWnmct
#       "><div class="_1NVSPYP3hBJSyQIQThJcVr">Optimal Space &amp; Time Complexity</div><svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 292.362 292.362" class="ziG9cplWruSO34u3rlTHj "><path d="M286.935 69.377c-3.614-3.617-7.898-5.424-12.848-5.424H18.274c-4.952 0-9.233 1.807-12.85 5.424C1.807 72.998 0 77.279 0 82.228c0 4.948 1.807 9.229 5.424 12.847l127.907 127.907c3.621 3.617 7.902 5.428 12.85 5.428s9.233-1.811 12.847-5.428L286.935 95.074c3.613-3.617 5.427-7.898 5.427-12.847 0-4.948-1.814-9.229-5.427-12.85z"></path></svg></div><div class="_3eVBLPRkiVIcsNJFJ-3urG"><div class="_2uaA-tUdCiVqJRNjXDpITG"><p class="_3pAwmWjFEZ914S4ilA1cDQ">O(log(n)) time | O(1) space - where n is the length of the input array</p></div></div></div></div></div></div>

def binarySearch(array, target):
    # Write your code here.
    return binarySearcher(array, target, 0, len(array) - 1)

def binarySearcher(array, target, left, right):
	if left > right:
		return -1
	middle = (left + right) // 2
	potentialMatch = array[middle]
	if target == potentialMatch:
		return middle
	elif target < potentialMatch:
		return binarySearcher(array, target, left, middle -1)
	else:
		return binarySearcher(array, target, middle + 1, right)



# def binarySearch(array, target):
#     # Write your code here.
#     return binarySearcher(array, target, 0, len(array) - 1)

# def binarySearcher(array, target, left, right):
# 	while left <= right:
# 		middle = (left + right) // 2
# 		potentialMatch = array[middle]
# 		if target == potentialMatch:
# 			return middle
# 		elif target < potentialMatch:
# 			right =  middle - 1
# 		else:
# 			left = middle + 1
#   return -1    