# Design and Analysis of the Backtracking Approach to Generating Parentheses in Python

**By**: Brian Tran and Benjamin Voor​

**Course**: Algorithm Design & Analysis 

**Course ID**: COP 4531

**Instructor**: Sarker Monojit Asish

**Date**: November 15, 2024

## Abstract

We solved an example coding problem from Leetcode.com once in the brute force approach and once in the backtracking approach. We also solved for the time complexity of each approach.

## [Problem Description](https://leetcode.com/problems/generate-parentheses/description/):

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

**Example 1**:

Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]
 
**Example 2**:

Input: n = 1

Output: ["()"]

**Constraints**:

1 <= n <= 8

### Brute force approach
* Permute all opening and closing parantheses as strings of length 2*n, using Python's "permutations" library.
* Check for a valid set of parantheses
* Exclude redundant sets of parantheses.
* Append valid answer to answers.
**Time complexity:** O(n!), because n elements have n! permutations.

### Backtracking approach
* Try all valid possibilites (adding an open or closed parantheses).
* If the parantheses is valid, then continue
  * If not, then backtrack
* Try the next choice until all possibilities have been completed.
**Time complexity:** B(n) best-case, where only the optimal branch of height n is explored to its fullest, and worst-case O(n), where every branch must be explored to their fullest.

## Contact information
Benjamin Voor
* LinkedIn: www.linkedin.com/in/benjamin-voor-31a270204
* GitHub username: [Benjamin-Voor](https://github.com/Benjamin-Voor)
* Handshake: https://app.joinhandshake.com/profiles/n2ct5a

## References
Python "Itertools" library: https://docs.python.org/3/library/itertools.html
