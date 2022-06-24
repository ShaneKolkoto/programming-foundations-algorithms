# Algorithms

## Tools required

<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />

# Table of contents

1. [What is an Algorithm? ](#introduction)
2. [Algorithm Characteristics](#Characteristics)

   - [Complexity](#complexity)
   - [Inputs and Outputs](#inputs_outputs)
   - [Classifications](#classifications)
     - [Serial/Parrallel](#serial_parrallel)
     - [Exact/Approximate](#exact_approximate)
     - [Deterministic/Non-deterministic](#deterministic_non-deterministicl)

3. [Comman Algorithms](#comman)

   - [Search](#search)
   - [Sorting](#sorting)
   - [Computatinal](#computatinal)
   - [Collection](#collection)

4. [Exercise](#exercise1)
5. [Understanding Algorithm Performance](#understanding)
6. [Data Structure](#structure)
7. [Recursion](#recursion)
8. [Acknowledgements](#acknowledgements)

<p name="introduction">

# What is an Algorithm

> A process or set of rules to be followed in calculations or other problem-solving operations, especially by a computer.
> "a basic algorithm for division"</p>

<p name="characteristics">

# Characteristics

### Complexity

> <p name="complexity">
>    - <b>Space Complexity</b>: How much memory does it require? <br>
>    - <b>Time complexity</b>: How much time does it take to complete?
> </p>

<p name="inputs_outputs">

### Inputs and Outputs

> What does the algorithm accept, and what are the results?

</p>

<p name="classifications">

# Classifications

1.  <b>Serial/Parrallel </b><br>
2.  <b>Exact/Approximate</b><br>
3.  <b>Deterministic/Non-deterministic</b> <br>

<p name="serial_parrallel">

### Serial / Parrallel

- <b>Serial</b>: A sequential algorithm or serial algorithm is an algorithm that is executed sequentially – once through, from start to finish,without other processing executing.<br> - <b>Parrallel</b>: Is an algorithm which can do multiple operations in a given time.
</p> <br>

<p name="exact_approximate">

### Exact / Approximate

- <b>Exact</b>: Exact algorithms are algorithms that always find the optimal solution to a given optimization problem.<br>
- <b>Approximate</b>: This technique does not guarantee the best solution. The goal of the approximation algorithm is to come as close as possible to the optimal solution in polynomial time.

</p><br>

<p name="deterministic_non-deterministic">

### Deterministic / Non-deterministice

- <b>Deterministic</b>: eterministic algorithm is an algorithm that, given a particular input, will always produce the same output, with the underlying machine always passing through the same sequence of states.<br>
- <b>Non-deterministic</b>: ondeterministic algorithm is an algorithm that, even for the same input, can exhibit different behaviors on different runs.

</p>
</p>

<p name="comman">

# Comman Algorithms

1.  <b>Search</b><br>
2.  <b>Sorting</b><br>
3.  <b>Computatinal</b><br>
4.  <b>Collection</b><br>

<p name="search">

### Search

> Find specific data in a structure (for example, a substring with a string).

</p>

<p name="sorting">

### Sorting

> Take a dataset and apply a sort order to it.

</p>

<p name="computatinal">

### Computatinal

> Given one set of data, calculate another (is given number prime?).

</p>

<p name="collection">

### Collection

> Work with collection of data (count specific items, navigate among data elements, filter out unwanted data, etc.).

</p>
</p>

<p name="exercise1">

# Exercise

> Find the greatest common denominator (GCD) of two integers, Using the Euclid's Algorithm, <b>Try to not look at the gcd_start.py file</b>.

_Example_

GCD of 20 and 8 is 4
(because 8 / 4 is 2; and 20 / 4 is 5, <b>with no remainder</b>).

1.  For two integers <b>num1</b> and <b>num2</b>, where <b>num1</b> > <b>num2</b>, divide <b>num1</b> by <b>num2</b>
2.  If the remainder, <b>R</b>, is 0, then stop: GCD is <b>num2</b>.
3.  Otherwise, set <b>num1</b> to <b>num2</b>, <b>num2</b> to <b>R</b>, and repeat at step 1 until <b>R</b> is 0
</p>

<p name="understanding">

# Understanding Algorithm Performance

> Measure how an algorithm responds to datset size

- <b>Big-O notation</b>
  - Classifies performance as the input size grows
  - "O" indicates the order of operation: time scale to perfome an opertation
- <b>Many algorithms and data structure have more than one O, inserting data, searching for data, deleting of data.</b>

### Common Big-O Terms

| Notation                                                       | Description   | Example                                                                            |
| -------------------------------------------------------------- | ------------- | ---------------------------------------------------------------------------------- |
| 0(1)                                                           | Constant time | Looking up a single element in an array                                            |
| 0(log n)                                                       | Logarithmic   | Finding an item in a sorted array with a binary search.                            |
| 0(n)                                                           | Linear time   | Searching an unsorted array for a specfic value                                    |
| 0(n log n)                                                     | Log-linear    | Complex sorting algorithms like heap sort and merge sort.                          |
| 0(n<span style="vertical-align:super;font-size:50%;">2</span>) | Quadratic     | Simple sorting algorithms, such as bubble sort, selection sort, and insertion sort |

</p>

<p name="structure">

# Data Structure

> Used to organize data so it can be processed

## Common Data Structures

1. [Arrays](#arrays)
2. [Linked lists](#linked) - **exercise in linklist_start.py**
3. [Stacks and queues](#stack) - **exercise in stack_start.py and queue_start.py**
4. [Tress](#tress)
5. [Hash tables](#hash) - **exercise in hashtable_start.py**

<p name="arrays">

## Arrays

<hr>

> - Collection of elements identified by index or key
> - Arrays starts at <b>0</b> for its <b>first element</b>

## Linar form array

| Elements | Function                                     | Output                               |
| -------- | -------------------------------------------- | ------------------------------------ |
| (elem 1) | even_ele = array[2n] (Get all even elements) | `n` is the number you want to access |
| (elem 2) |                                              |                                      |
| (elem 3) |                                              | will show cause its element 2        |
| (elem 4) |                                              |                                      |
| (elem 5) |                                              | will show cause its element 4        |

</p>

## Two-dimensinal Arrays

- Needs two indexs

**Example** <br>

> Lets get the third element we will need the 2nd element cause element 1 is 0 index, 1 indicates which cloumn to access.

| Elements |     | Indexs |
| -------- | --- | ------ |
| (elem 1) |     |        |
| (elem 2) |     |        |
| (elem 3) |     | (2, 1) |
| (elem 4) |     |        |
| (elem 5) |     |        |

</p>
<hr>

## Array Operations

1. Calculate item index: 0(1)
2. Insert or delete item at beginning: 0(n),
3. Insert or delete item in middle: 0(n),
4. Insert or delete item at end: 0(1)
</p>
<hr>

<p name="linked">

## Linked Lists

- Collection of data elements, called nodes.
- Contains refernece to the nex node in the list.
- Hold whatever data the application needs.

</p>

<p name="stack">

## Stacks and Queues

### Stacks

> - Collection of elements that supports push and pop operations.
> - The last item pushed is the first one popped.
> - Expression processing
> - Backtracking: browser back stack, for example (back button on browser)

### Queues

> - Collection that supports adding and removing
> - First item added is the first item
> - Order processing
> - Messaging

</p>

<p name="tress">

## Tress

> The way you construct your folders or even files

**Example**

```
Main Folder
    └── sub-folder1
            └── file.txt
            └── file.py
    └── sub-folder2
            └── file.html
            └── file.css
            └── file.js
```

</p>

<p name="hash">

## Hash Tables

> - Key-to-calue mappings are unique.
> - Hash tables are typically very fast.
> - For small datasets, arrays are usally more efficient
> - Hash tables dont order entries in a predicatable table

</p>

<p name="recursion">

# Recursion

> - Recursion is when a fuction calls itself.

**Example**
Lets say your program had to find a pirtucluar file that is nestle somewhere in a set of directories, and your program doesnt know how many directories there are.

```
Main Folder 1
    └── sub-folder1
            └── file.txt
            └── file.py
    └── sub-folder2
            └── file.html
            └── file.css
            └── file.js
Main Folder 2
```

**Question?**
So What algothrim would you use to search for a file?

**Secnorio**

> **_Repat this until you find the file._**

```
Make a list of directory items
        |
While the list is not empty
        |
Get an item
        |
    File or dir? ── Done
        |
        |   if Dir
        |
        |
Add contents to the list

<!-- Next step -->

Examine every directory item
|       |
|  Dir  | File
|       |
|____ Dir ____ Done


```

## Import things to remember about recursion

> - Recursive fuction need to have a breaking condition.
> - This prevents infinite loops and eventual crashes.
> - Each time the fuction is called, the old arguments are saced.

- This is called the "call stack" (This is used by a stack data structure).

_**Example Breaking Condition function**_

> Function to print a countdown of numbers starting with initial number, the function checks to see if the argument <b>x</b> is equal to 0. Otherwise it prints the number and then calls itself with the current number minus 1.

```ruby
function countdown(x){
        if (x == 0)
        print("done!")
        return
        else
        print(x, "...")
        countdown(x-1)
}
countdown(4)
```

## Exercise

1. Use the recursion to implement a countdown counter (project can be found in countdown_start.py)
2. Using recursion to implement power and factorial functions (project can be found in recursion_start.py)

</p>

<p name="sorting">

# Sorting

> To help make sense of the data and can be sorted in variity of ways.

_Example_

> A real estate agency needs sort the data so the app can work on the informatioin sufficiently.

| Elements  |     | Prices   |
| --------- | --- | -------- |
| (house 2) |     | R365,000 |
| (house 3) |     | R369,000 |
| (house 4) |     | R371,000 |

- The user might not want it to be sorted by price level, but if the do want it sorted by max-price it will sort the data
- The app needs to sort the data internal, to limit the amount of additinal information.

### Big O charactritic of the Sorting

> Most modern languages have sorting built in

## Sorting algorthims

- Bubble sort (Basic algorthim used as a teaching tool)
- Merge sort (uses of recursion)
- Quicksort (also uses recursion)

## Bubble Sort

_Example_
Suppose you have an array of numbers as below

| 23         | 8          | 15     | 17     | 4      | 40     | 11     | 31     |
| ---------- | ---------- | ------ | ------ | ------ | ------ | ------ | ------ |
| **elem 1** | **elem 2** | elem 3 | elem 4 | elem 5 | elem 6 | elem 7 | elem 8 |

> The Bubble sort starts off by comparing the first two elements to see which of the two is larger, if the first element is larger than the second it will swip the two

| 8          | 23         | 15     | 17     | 4      | 40     | 11     | 31     |
| ---------- | ---------- | ------ | ------ | ------ | ------ | ------ | ------ |
| **elem 1** | **elem 2** | elem 3 | elem 4 | elem 5 | elem 6 | elem 7 | elem 8 |

> The proccess continues until it examains all the numbers in the array and sorts them all

# Charactaristics

- Very simple to understand and implement
- Performance: O(n<span style="vertical-align:super;font-size:50%;">2</span>)
  - For loops inside of for loops are usally n<span style="vertical-align:super;font-size:50%;">2</span>.
- Other sorting algorithms are generally much better
- Not considered to be a practical solution.

**Exercise**

> With a given list of items use the bubble sort methond to sort the list. _Can be found in bubble_start.py_

| 6   | 20  | 8   | 19  | 56  | 23  | 87  | 41  | 49  | 53  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

</p>

<p name="merge">

# Merge Sort

> - The merge sort is known as a divide and conquer algorithm.
> - Breaks a dataset into individual pieces and merges them.
> - Uses recursion to operate on datasets.
> - Performs well on large sets of data.
> - In general has a performance of O(n log n) time complexity. (Log Linear)

## How it works

> The key is how to merge two sorted arrays together

**Example**

> Lets say you got two arrays. and you need to merge them into one and keep them sorted.

| Array 1      |     | Array 2 |
| ------------ | --- | ------- |
| [12, 19, 31] |     | [4, 23] |

> - We start with the first elements from the two arrays. in the case the 4 is smaller than the 12 so 4 gets inserted into the array.
> - it checks the second element of array 2, and compares it to the first element of array 1, in this case 12 is smaller than 23. so 12 gets inserted into array.
> - It checks the next element in array one to find and compare elements until all elment are compared and the lists are sorted.

**Exercise**

> Given the array below, use the merge sort algorthim.

| 6   | 20  | 8   | 19  | 56  | 23  | 87  | 41  | 49  | 53  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

</p>

<p name="quick">

# QuickSort

> - The quicksort is conquer algorithm, like the merge sort.
> - Also uses recursion to perform sorting.
> - Generally performs better than merge sort, O(n log n).
> - Operates in place on the data. (Dont need extra memory to do its work)
> - Worst case is O(n<span style="vertical-align:super;font-size:50%;">2</span>) when data is mostly sorted already.

## Pivot Point

> One of the main fetures on quicksort.

**Example**
Lets say you have an array as below

| 20  | 6   | 8   | 19  | 56  | 23  | 87  | 41  | 49  | 53  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- Lets take the **first element** (20) this becomes the pivot value
- We start the process of partitioning the list.

  > Main purpose of partitioning process is to move items that are on the wrong side of the pivot value and figure out the point at which to split the array, so we can recursivly do this again.

- We have two indexs the lower index(6) and upper index(87).

  > So you start with the lower index as long as it is less than the upper index, until we find a value latger than the pivot value.

- If point point is larger than index we stop,
- On the right side we decrement this index until we find a value that is less than the pivot and upper index is greater than lower index.
- We the indexs cross each other thats known as the split point, where we going to split the array.
- At split point we will excahnge the pivot value with the upper index.

**Exercise**
With given array, use the quicksort method and find the crossing point using the first element as your pivot point

| 20  | 6   | 8   | 53  | 56  | 23  | 87  | 41  | 49  | 53  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

> Task can be found in quick_start.py

</p>

<p 
name="acknowledgements">

# Acknowledgements

- [Joe Marini](https://www.linkedin.com/in/joemarini) (Linkdin Profile)
  - [@Joe Marini](https://github.com/joemarini) (Github Profile)
- [Linkdin Course](https://www.linkedin.com/learning/programming-foundations-algorithms) - programming-foundations-algorithms
</p>
