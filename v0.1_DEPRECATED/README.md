# Trust Matrix Algorithm v0.1

_This should be considered deprecated_

This is a simple implementation of the algorithm, in which the entries of B are float.
It computes the powers of the _Belief matrix_ $B , B^2 , \dots B^n$, removes the indices already counted and then computes the Local Trust Matrix $T$.

This requires $n-1$ matrix products.

The default $n$ is set = 5.
Here is how the algorithm performs, compared to the cost of 4 matrix products.

![trust_matrix_algo_NAIVE_plot](https://github.com/pippellia-btc/The-Problem-of-Spam/assets/108896743/2a268bbd-4088-4b5e-a478-894472a1152f)

And here is the asymptotic analysis

![trust_matrix_algo_NAIVE_asyntotic](https://github.com/pippellia-btc/The-Problem-of-Spam/assets/108896743/ef1e4a74-424d-4a59-b00d-7a9850d46ab4)

The ODR polynomial is 

$$\approx 10^{-11} N^3 + 10^{-7} N^2 - 10^{-4} N + 10^{-1}$$

Which implies that the cubit term will outweight the quadratic term when $N \geq 10^4$

## Creating the Trust Matrix for all Nostr users

According to [Nostr.band](https://stats.nostr.band/), there are 103555 _trusted pubkeys_ on Nostr.
The time cost of computing the Trust Matrix for all of these users, on my CPU (Intel i5-4690k) is

$$\approx 44330 s \approx 12.3 h$$

Operations were not parallelised, so only one core was used at a time. In any case, this algorithm does not scale well.

As mentioned in the introductory README, an interesting way to go is to decompose the matrix $B$ into blocks on the diagonal by doing index rearrangements. This way, the complexity of the algorithm can be greatly reduced.

This is an interesting avenue also in practice because it makes use of the fact that the web is not a giant community, on the contrary, _it is populated by thousands of sub-communities that are internally well connected and loosely connected to each other._
