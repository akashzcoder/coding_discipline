## Sorting a list with 3 unique numbers

Standard way is that you can just sort it using quick sort, merge sort, etc. Quick sort was the worst case scenario in thsi case
which is O(n^2) times if you chose the pivot poorly.

You can easily do it using a hashmap containing the counts of each number but that also implies linear use of the storage space.

So, this question is interesting when we want to solve this problem in linear time but constant space.