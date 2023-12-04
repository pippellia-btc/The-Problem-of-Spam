# NAIVE ALgorithm

This is a simple implementation of the algorithm.
It computes the powers of the _Belief matrix_ $B , B^2 , \dots B^n$

This requires $n-1$ matrix products.

The default $n$ is set = 5.
Here is how the algorithm performs, compared to the cost of 4 matrix products.

![trust_matrix_algo_NAIVE_plot](https://github.com/pippellia-btc/The-Problem-of-Spam/assets/108896743/2a268bbd-4088-4b5e-a478-894472a1152f)

And here is the asymptotic analysis

![trust_matrix_algo_NAIVE_asyntotic](https://github.com/pippellia-btc/The-Problem-of-Spam/assets/108896743/ef1e4a74-424d-4a59-b00d-7a9850d46ab4)

The ODR polynomial is 
$$\approx 10^{-11} N^3 + 10^{-7} N^2 - 10^{-4} N + 10^{-1}$$

Which means that the cubit term will outweight the quadratic term when $N \geq 10^4$
