# Trust Matrix Algorithm v0.2 (Boolean, Dense Matrices)

This is a simple implementation of the algorithm, in which the entries of B are _boolean_.
It computes the powers of the _Belief matrix_ $B , B^2 , \dots B^n$, removes the indices already counted and then computes the Local Trust Matrix $T$.

This requires $n-1$ matrix products. The default $n$ is set = 5.

Here is how v0.2 performs against v0.1 and the cost of 4 boolean matrix products (the density of 1s is 0.5).

![trust_matrix_algo_v02_plot](https://github.com/pippellia-btc/The-Problem-of-Spam/assets/108896743/0ac5083c-afd5-47e5-b45e-8e7ec62aeee3)

The v0.2 is still 50% more costly than the matrix multiplications, but the improvement over the previous version is massive.

From this [great paper](https://www.sciencedirect.com/science/article/pii/S0019995873902283?via%3Dihub) we know that, on average it takes $O(N^2)$ to do the matrix product of two boolean matrixes of dimention $N$. The worst case scenario is O(N^3).

Here is the asymptotic analysis for v0.2, using a polynomial of degree 2 as the theory suggest.

![trust_matrix_algo_v0 2_asyntotic](https://github.com/pippellia-btc/The-Problem-of-Spam/assets/108896743/e9b87fc8-aa7e-4ed7-a10e-465617df62f1)

with polynomial

$$\approx f(N) = 4.6 \cdot 10^{-8} N^2 - 1.2 \cdot 10^{-5} N - 0.009$$

According to [Nostr.band](https://stats.nostr.band/), there are 103555 _trusted pubkeys_ on Nostr.
Using the previous asymptotic analysis, the time cost of computing the Trust Matrix for all of these users, on my CPU (Intel i5-4690k) is

$$\approx f(103555) \approx 497 s$$

Operations were not parallelised, so only one core was used at a time. This is a very promising result!
