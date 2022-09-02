'''
*Programming Assignment 8
*Ean Vandergraaf & Laura Pareja
*11/1/2019
*Algorithms
*Tree Traverals and Leaf Count
*
*V1
'''

##method traverse the tree using the traversal method using recursion.
##@param tree: the root of the tree.
##@return arr the array of letters in the inorder traversal.
inOrder = []
def inorder(tree):
  ##base case if the node does not exist
  if (len(tree) == 0):
    return []
  else:
      ##traverse the left side
      arr = inorder(tree[1])
      ##add the root to the array
      arr = arr + [tree[0]]
      ##traverse the right side
      return arr + inorder(tree[2])

##method traverse the tree using the preorder traversal method using recursion.
##@param tree: the root of the tree.
##@return arr the array of letters in the preorder traversal.
preOrder = []
def preorder(tree):
  ##base case if the node does not exist
  if (len(tree) == 0):
    return []
  else:
      ##add the root to the array
      arr = [tree[0]]
      ##traverse the left side
      arr = arr + preorder(tree[1])
      ##traverse the right side
      arr = arr + preorder(tree[2])
      return arr

##method traverse the tree using the postorder traversal method using recursion.
##@param tree: the root of the tree.
##@return arr the array of letters in the postorder traversal.
postOrder = []
def postorder(tree):
  ##base case if the node does not exist
  if (len(tree) == 0):
    return []
  else:
      ##traverse the left side
      arr = postorder(tree[1])
      ##traverse the right side
      arr = arr + postorder(tree[2])
      ##add the root to the array
      arr = arr + [tree[0]]
      return arr

##method counts the number of leaves that the tree contains using recursion.
##@param tree: the root of the tree.
##@return arr the number 
def leafCount(tree):
  ##base case 1: if the node is empty
  if(len(tree) == 0):
    return 0
  ##base case 2: if the node is actually a leaf
  if(len(tree[1]) == 0 and len(tree[2]) == 0):
    return 1
  else:
    ##gets the amount of leaves on the left and the right
    return leafCount(tree[1]) + leafCount(tree[2])

def testCase(testNumber,function,tree,expectedAnswer):
  if expectedAnswer==function(tree):
    print ("Test",testNumber,"passed.")
  else:
    print ("Test",testNumber,"failed.")
    
def test1():
  f=["f",[],[]]
  c=["c",f,[]]
  e=["e",[],[]]
  g=["g",[],[]]
  d=["d",[],g]
  b=["b",d,e]
  root=["a",b,c]
  testCase(1,inorder,root,['d', 'g', 'b', 'e', 'a', 'f', 'c'])
  testCase(2,preorder,root,['a', 'b', 'd', 'g', 'e', 'c', 'f'])
  testCase(3,postorder,root,['g', 'd', 'e', 'b', 'f', 'c', 'a'])
  testCase(4,inorder,c,['f','c'])
  testCase(5,preorder,e,['e'])
  testCase(6,leafCount,root,3)
  testCase(7,leafCount,e,1)

def test2():
  b=["b",[],[]]
  a=["a",[],b]
  e=["e",[],[]]
  f=["f",e,[]]
  d=["d",[],f]
  i=["i",[],[]]
  h=["h",d,i]
  root=["c",a,h]
  testCase(8,inorder,root,['a','b','c','d','e','f','h','i'])
  testCase(9, preorder, root, ['c','a','b','h','d','f','e','i'])
  testCase(10,postorder,root,['b','a','e','f','d','i','h','c'])
  testCase(11, leafCount,root,3)
  testCase(12, leafCount, h, 2)

test1()
test2()