# Write a function that takes in a Binary Search Tree (BST) and a target integer
# value and returns the closest value to that target value contained in the BST.
# </p>
# <p>You can assume that there will only be one closest value.</p>
# <p>
#   Each <span>BST</span> node has an integer <span>value</span>, a
#   <span>left</span> child node, and a <span>right</span> child node. A node is
#   said to be a valid <span>BST</span> node if and only if it satisfies the BST
#   property: its <span>value</span> is strictly greater than the values of every
#   node to its left; its <span>value</span> is less than or equal to the values
#   of every node to its right; and its children nodes are either valid
#   <span>BST</span> nodes themselves or <span>None</span> / <span>null</span>.
# </p>
# <h3>Sample Input</h3>
# <pre><span class="CodeEditor-promptParameter">tree</span> =   10
#        /     \
#       5      15
#     /   \   /   \
#    2     5 13   22
#  /           \
# 1            14
# <span class="CodeEditor-promptParameter">target</span> = 12
# </pre>
# <h3>Sample Output</h3>
# <pre>13</pre>

# O(log(n)) time | O(log(n)) space
# O(n) time | O(n) space
def findClosestValueInBst(tree, target):
    # Write your code here.
    return findClosestValue(tree, target, tree.value)

def findClosestValue(tree, target, closestValue):
	if tree is None:
		return closestValue
	if abs(target - closestValue) > abs(target - tree.value):
		closestValue = tree.value
	if target < tree.value:
		return findClosestValue(tree.left, target, closestValue)
	elif target > tree.value:
		return findClosestValue(tree.right, target, closestValue)
	else:
		return closestValue


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None