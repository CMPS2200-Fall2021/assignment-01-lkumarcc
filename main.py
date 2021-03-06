"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        (ra, rb) = (foo(x-1), foo(x-2))
    return ra+rb
    #it does the fibonnaci sequence




def longest_run(mylist, key):
    #make a list with the indices of the places where the key takes place
    newlist = list(enumerate(mylist))
    indices = []
    for x, y in newlist:
        if y == key:
            indices.append(x)
    #add the number of times there are consecutive numbers to the list
    count = [1]
    for x, y in zip(indices, indices[1::]):
        if x == y-1:
            count[-1] = count[-1] + 1
        else:
            count.append(1)
    #return the max number in the list
    return max(count)


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def longest_run_recursive(mylist, key, newlist, prev):
    #base case - if there is nothing in the list
    #consider case [1, 12, 12, 12, 5, 6, 7, 12 1]
    if len(mylist > 1):
        half = len(mylist)//2
        return longest_run_recursive(:half) + longest_run_recursive(half:)
    else:
        if prev:
            if mylist[0] == key:
                count += 1
            else:
                newlist.append(count)
        else:
            if mylist[0] == key:s
                count += 1
            else:
                count = 0 
        highestval = max(newlist)
        return highestval        


## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3

test_longest_run()
