# Algorithmic Complexity & Big-O Notation

## 📘 What is Algorithmic Complexity?

Algorithmic complexity is the measure of the efficiency of an algorithm in terms of:
- **Time complexity**: how fast it runs (independent of real-world factors like hardware speed)
- **Space complexity**: how much memory it uses

We use **asymptotic notation** to describe how runtime or space grows as input size `n` increases.

---

## 🔢 Big-O Notation (Worst Case)

| Complexity      | Example                              | Notes                            |
|----------------|---------------------------------------|----------------------------------|
| O(1)            | Accessing an array element           | Constant time                    |
| O(log n)        | Binary search                        | Logarithmic                      |
| O(n)            | Linear search                        | Scales with input size           |
| O(n log n)      | Merge sort, heapsort                 | Most efficient comparison sorts  |
| O(n²)           | Bubble sort, insertion sort (nested loops) | Quadratic growth         |
| O(2ⁿ)           | Recursive Fibonacci                  | Exponential                      |
| O(n!)           | Brute-force traveling salesman       | Factorial                        |

---

## ✍️ Common Time Complexities (Visual Aid)

