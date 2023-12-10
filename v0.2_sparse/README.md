# Trust Matrix Algorithm v0.2 (Boolean, Sparse Matrices)

This is a simple implementation of the algorithm, in which the entries of $B$ are _boolean_.
It computes the powers of the _Belief matrix_ $B^2 , B^3 , \dots B^n$, removes the indices already counted and then computes the Local Trust Matrix $T$.

This requires $n-1$ matrix products. The default $n$ is set = 5.

The [v0.2 trust matrix algorithm for dense matrices](https://github.com/pippellia-btc/The-Problem-of-Spam/tree/main/v0.2_dense) works great when the density $p$ of 1s in the matrix is high.
If $p \approx \frac{1}{2}$, then that algorithm has average time complexity of $O(N^2)$. When $p \approx 0$, instead it has $O(N^3)$. 
In practice, it performs rather poorly, even worse than the v0.1.

For $p < 0.05$, this algorithm should be used, which will improve both time complexity and space complexity. This situation will be the most relevant in practice.

For a social media like Twitter, it is not unreasonable to assume that one person follows an average of 1k people.
Thus, if $N$ is the number of total users, the density of 1s in the matrix $B$ is:

$$p \doteq \frac{1000 \cdot N}{N^2} = \frac{1000}{N}$$

If $N = 10^9$, then $p = 10^{-6}$

It is interesting to discuss how these (relatively) few 1s will be distributed within the matrix $B$.
The history of the Web teaches us that people will rarely be part of a single, gigantic community. What we see in practice is the emergence of communities linked by a topic of discussion or shared values among the members.
A community is here defined as a collection of people well connected to each other and poorly connected to other individuals or external communities.

The **v0.2 trust matrix algorithm for dense matrices** works well for calculating the Local Trust Matrix within communities, but it is inadequate for calculating the Local Trust Matrix for all users.
