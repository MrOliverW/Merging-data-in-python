# Merging-data-in-python
Merging two sorted customer datasets in-place.

My task is to merge two sorted customer datasets in-place. To do this efficiently, I'm utilizing customerData1’s trailing space. The most efficient way to solve this is by working backwards.
Think of it like organizing two stacks of files into a single drawer: If you start from the front, you have to keep shifting the files you already have to make room. If you start from the back, you can drop the largest files into the empty space without moving anything else. We compare the largest elements of both arrays and place them at the end, avoiding overwriting any data we still need."


In a "bad" version of this code (like inserting from the front), you might have to shift every single file every time you add a new one. That would be $O(m \times n)$, which is like moving 100 files 100 times.

My approach runs in Linear Time ($O(m+n)$) because we only touch each record once, and it uses Constant Space ($O(1)$) because we perform the merge entirely within the existing memory of the first array."
