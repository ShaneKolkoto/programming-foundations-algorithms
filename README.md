# Algorithms

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
6. [Acknowledgements](#acknowledgements)

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

### Inputs and Outputs

> <p name="inputs_outputs">
> What does the algorithm accept, and what are the results?
> </p>

# Classifications

<p name="classifications">
1.  <b>Serial/Parrallel </b><br>
2.  <b>Exact/Approximate</b><br>
3.  <b>Deterministic/Non-deterministic</b> <br>

### Serial / Parrallel

<p name="serial/parrallel">
- <b>Serial</b>: A sequential algorithm or serial algorithm is an algorithm that is executed sequentially – once through, from start to finish,without other processing executing.<br>
    - <b>Parrallel</b>: Is an algorithm which can do multiple operations in a given time.
</p> <br>

### Exact / Approximate

<p name="exact/approximate">
    - <b>Exact</b>: Exact algorithms are algorithms that always find the optimal solution to a given optimization problem.<br>
    - <b>Approximate</b>: This technique does not guarantee the best solution. The goal of the approximation algorithm is to come as close as possible to the optimal solution in polynomial time.
</p><br>

### Deterministic / Non-deterministice

<p name="deterministic/non-deterministic">
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

### Search

<p name="search">
Find specific data in a structure (for example, a substring with a string).
</p>

### Sorting

<p name="sorting">
    Take a dataset and apply a sort order to it.
</p>

### Computatinal

<p name="computatinal">
    Given one set of data, calculate another (is given number prime?).
</p>

### Collection

<p name="collection">
    Work with collection of data (count specific items, navigate among data elements, filter out unwanted data, etc.).
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

<p name="acknowledgements">

# Acknowledgements

- [Joe Marini](https://www.linkedin.com/in/joemarini) (Linkdin Profile)
  - [@Joe Marini](https://github.com/joemarini) (Github Profile)
- [Linkdin Course](https://www.linkedin.com/learning/programming-foundations-algorithms) - programming-foundations-algorithms
</p>
