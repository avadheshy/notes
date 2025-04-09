"""
There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.

The rules of the game are as follows:

Start at the 1st friend.
Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some friends more than once.
The last friend you counted leaves the circle and loses the game.
If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat.
Else, the last friend in the circle wins the game.
Given the number of friends, n, and an integer k, return the winner of the game.
"""
class Solution:
    def solve(self, arr, index, k):
        if len(arr) == 1:
            return arr[0]
        n = len(arr)
        next = (index + k - 1) % n
        arr.pop(next)
        return self.solve(arr, next, k)

    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i + 1 for i in range(n)]
        return self.solve(arr, 0, k)
""""
The recurrence relation is:

🧠 f(1, k) = 0 ← Base case: Only one person, they are the winner (0-indexed)
🔁 f(n, k) = (f(n - 1, k) + k) % n

This means:

If you know the winner’s position in a circle of n-1 people, you can compute the winner's position in a circle of n people by shifting by k, and wrapping around using % n.
"""
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0  
        for i in range(2, n + 1):
            winner = (winner + k) % i
        return winner + 1  
