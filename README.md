# How to Deal With Spam in a Decentralized Way
Decentralised systems, if successful, suffer from spam problems. But what is spam, and more importantly, how to solve it?

## What is Spam?
If you look up the word Spam in a dictionary, what you find is more or less the following
1. _Unsolicited_ e-mail, often of a commercial nature, sent indiscriminately to multiple mailing lists, individuals, or newsgroups;
2. Any _undesired_ electronic content automatically generated.

'_Unsolicited_’, ’_undesired_’, but who judges? Well, obviously the receiver judges it, but he is also the only one who can. What is trash (or spam!) to one is treasure to another.

**Rule 1**. _You cannot judge what spam is for someone else. Not even close
in some cases._

There are online communities that you can consider weird, or excessive, or
transgressive, many would say the same thing about us bitcoiners. In any case,
only the receiver can choose, on a completely personal basis what is spam for
him and what is not.

If someone decided for him _against his will_, that would be called **censorship**.
There are no half-measures here; just as a little theft does not stop being such,
so a little censorship does not stop being censorship.

## How to Censor Gracefully

How to censor gracefully? First, don’t do it; unless it is completely necessary.

In some cases, it is not a question of censorship, but of creating specific rules of interaction (e.g. character limit on Twitter) or rules that incentivise giving more space to the _Signal_ and less to the _Noise_.

Again, who decides what is Signal and what is Noise? Well, you know who, the receiver!


![image](https://github.com/pippellia-btc/The-Problem-of-Spam/assets/108896743/30a21cb3-e083-4146-8841-4fd6e43ba97c)


In a Social Network, the receiver is any user really.

Ideally, the Developer or the Client **should have no power to discard or hide messages**. The Client, however, should be able to _curate_ the experience it offers by applying rules of interactions and filters to all messages, in an _equal manner_. These filters can change the nature of the messages (e.g. length) but cannot choose specifically which one are allowed or not allowed.

**Rule 2:** _Client can only apply filters that are equal for all, otherwise he can choose what messages or opinions are allowed or not allowed._

One of such filters, a tool that was not, but is now present in the toolbox of developers, is money. That is really an equal filter, as the value of money lies in the intersection of each person’s subjective values, coordinated by the market.

Given a message $m$ and a threshold $t$, the Client filters all messages such that 
$$donation(m) < t $$

## Not Just Money

There are other signals to convey trust between the participants in a network,
not only the monetary one. One of the biggest technical mistakes bitcoiners
make is to treat every problem as if it were only an economic one. If you have
a hammer in your hand, everything you see looks like a nail.

An interesting example is the route taken by Nostr.band and their Trust Rank.
By giving a high trust rank to an arbitrarily (but not randomly) chosen set of
users, and seeing with whom they interact, a global trust score can be given
to every participant in the network. https://trust.nostr.band/

Quoting from Nostr.band

> The beauty of Trust Rank/Page Rank is that it’s robust against many types
of abuse. If initial weight is given to a spammer by some accident, they are
most likely loosing it all by the end of the calculation, because almost no one
interacts with their content. If someone builds a bot farm and manages to get
some ’links’ from valid network participants, all the rank passed by these links
is divided by the size of the farm - so sybil attacks are defeated.

However, it would be a mistake to use the score as it is, since it is highly
influenced by the initial choice of users/npubs to be trusted. This score is
used to discard individuals with 0 trust, rather than being used as a general
metric

This is the condition I propose for making a message $m$ from a $usr$ _viewable_, given a Global Trust Score $G(usr)$:

### Content Visibility Condition

The Clients sets the threshold $t$

1. If $G(usr) \approx 0$ AND $donation(m) < t$, sets $m$ to non-viewable
2. Else, $m$ is viewable


In other words, if you are an anonymous person whom nobody knows, then the
burden of proof is on you. Pay some sats and you can get people’s attention.
Also, those who wish to criticise do not run into the problem of having to donate
in the first place. Adam Back could share his criticism of something without having to make a donation, and you would probably want to avoid it being filtered.

However, the fact that a message $m$ is _viewable_ does not mean that it will actually
be seen. Such is only one part of the algorithm I propose.

## Local Trust

Only the receiver/user can judge spam. Furthermore, only him can judge what
is of value to him and what is not. Each user of a social network expresses this
judgement by choosing _to follow_ some people and _not follow_ others. Let us take
this small network as an example.


![image](https://github.com/pippellia-btc/The-Problem-of-Spam/assets/108896743/9135f71b-b64a-4fe9-a52b-20fc89343e06)


We imagine a network as a graph in which the nodes are the people and the
oriented arcs (or arrows) represent that one (the tail) follows another (the tip).
In meatspace, if Satoshi trusts Gigi, and Gigi trusts Pip, Satoshi will also start
to trusts Pip a little. There can be other ways in which trust flows within a
network, but let us focus on this one for now.

A simple algorithm to calculate the ’flow of trust’ is the following:
Let us consider the set of nodes {$n_1, n_2, n_3, n_4$} = {Satoshi, Gigi, Pip, Adam}.

We construct the matrix $B$, in which the element $b_{i,j}$ is 1 if $n_i$ follows $n_j$ , 0
otherwise.

$$ B \doteq \begin{pmatrix} 
    b_{11} & \dots  & b_{1N}\\
    \vdots & \ddots & \vdots\\
    b_{N1} & \dots  & b_{NN} 
    \end{pmatrix} = \begin{pmatrix} 
    0 & 1& 0  & 0 \\
    0 & 0& 1  & 0 \\
    0 & 0& 0  & 1 \\
    0 & 1& 0  & 0 \\
    \end{pmatrix}
$$

We now encode the rule that if $n_i$ trusts $n_j$, which in turn trusts $n_k$, then $n_i$ trusts $n_k$, but this trust is somewhat dampened by a $\gamma \in (0,1)$ factor.

We get the new 'trust arrows' my multiplying the $B$ matrix by itself.

$$ B \cdot B = \begin{pmatrix} 
    0 & 1& 0  & 0 \\
    0 & 0& 1  & 0 \\
    0 & 0& 0  & 1 \\
    0 & 1& 0  & 0 \\
    \end{pmatrix} \cdot \begin{pmatrix} 
    0 & 1& 0  & 0 \\
    0 & 0& 1  & 0 \\
    0 & 0& 0  & 1 \\
    0 & 1& 0  & 0 \\
    \end{pmatrix} = \begin{pmatrix} 
    0 & 0& 1  & 0 \\
    0 & 0& 0  & 1 \\
    0 & 1& 0  & 0 \\
    0 & 0& 1  & 0 \\
    \end{pmatrix}$$

This is the result after one round.


![image](https://github.com/pippellia-btc/The-Problem-of-Spam/assets/108896743/2f5e29b6-5a63-435f-8728-3c9c6253d67d)


If we apply two other rounds of the algorithm, we obtain:

$$ B^3  = \begin{pmatrix} 
    0 & 0& 0  & 1 \\
    0 & 1& 0  & 0 \\
    0 & 0& 1  & 0 \\
    0 & 0& 0  & 1 \\
    \end{pmatrix} \\ $$
    
  $$  B^4  = \begin{pmatrix} 
    0 & 1 & 0  & 0 \\
    0 & 0 & 1  & 0 \\
    0 & 0 & 0  & 1 \\
    0 & 1 & 0  & 0 \\
    \end{pmatrix} = B $$

$B^4$ is the starting matrix $B$, this tells us that trust has gone round and round again. So we stop at $B^3$, which has elements on the diagonal, which means that a node gives itself trust. This is reasonable, but we do not want to count it in our analysis, therefore we set $B^3_*$ to have the same entries like $B^3$ but without the diagonal ones. We define the \textbf{Local Trust Matrix} $T_{\gamma}$ as follows:

$$T_{\gamma}  \doteq  \ \mathbb{I} + B + \gamma B^2 + \gamma^2 B^3_*$$

$$T = \begin{pmatrix} 
    1 & 1 & \gamma  & \gamma^2 \\
    0 & 1 & 1  & \gamma \\
    0 & \gamma& 1  & 1 \\
    0 & 1 & \gamma  & 1 \\
    \end{pmatrix}$$

Choosing $\gamma = \frac{1}{2}$ for example, would result in a matrix $T_{\frac{1}{2}}$

$$ T_{\frac{1}{2}} = \begin{pmatrix} 
    1 & 1 & 0.5  & 0.25 \\
    0 & 1 & 1  & 0.5 \\
    0 & 0.5 & 1  & 1 \\
    0 & 1 & 0.5  & 1 \\
    \end{pmatrix} $$

In all generality, the algorithm for creating the Local Trust Matrix $T_{\gamma}$ is:

### Local Trust Matrix Algorithm
1. Construct $B = (b_{ij})_{ij}$
2. for $j = 1, \dots k$
    1. compute $B^j = B^{j-1} \cdot B$
    2. compute $B^j_*$, which is $B^j$ without all the entries already 'counted' by $\mathbb{I}, B, \dots B^{j-1}$
3. return $T_{\gamma} = \mathbb{I} + \sum_{j=1}^k \gamma^{j-1} B^j_*$

This algorithm is to be considered an initial approach to the problem, since it is still very rudimentary. Moreover, the cost of such an algorithm increases not particularly well, but this I am sure can be improved. The product of two $N \times N$ matrices done naively costs $O(N^3)$. Having to do $k-1$ of such products and then adding everything together, the cost of the algorithm is at least $O(k N^3)$.

How is the Matrix $T_{\gamma}$ used in practice?

### Content Showing Algorithm

The user $n_i$ sets a trust threshold $t_i$

1. If $usr$ is logged-in, $usr = n_i$
2. for every message $m$ from $n_j$ viewable
    1. if $n_i \cdot T_{\gamma} \cdot n_j < t_i$, don't show $m$
3. else, show $m$

The Content Showing Algorithm (horrible name I know) along with the Content Visibility Condition is represented in the following scheme.


![image](https://github.com/pippellia-btc/The-Problem-of-Spam/assets/108896743/e5e7885c-d98d-46e5-a98a-0ae131e799c2)


A great property of this system is that it \textbf{filters out self-donations} that a user might make to make his own profile/post stand out.\\\\
In fact, such a usr would not use his own profile/npub, otherwise he would be immediately caught. He would go on to create secondary identities or make donations anonymously bigger than the threshold $t_{clients}$ with negligible cost.\\\\

In any case, the Local Trust Score would be 0 for every user $n_i$, \textbf{therefore no one will see the fake donations.}

# Conclusions

This paper is to be understood as a first step in the realisation of such a filtering system; the algorithm described suffers from a scalability problem, since each logged-in user of a Client affects the matrix $T_{\gamma}$, which will then have tens of thousands of entries. To avoid a DoS attack against the Client, measures can be implemented that avoid recalculation of $T_{\gamma}$ unless the new user $n_{new}$ has a $G(n_{new})>0$, or by introducing a minimum delay between recalculations (or both).

Furthermore, an interesting direction to explore is to block-decompose the matrix $B$, by doing index rearrangements. An example follows:

$$\left(\begin{array}{@{}ccccc@{}}
     0 & 0 & 1 & 1 & 1 \\
     1 & 1 & 0 & 0 & 1 \\
     0 & 0 & 1 & 1 & 1 \\
     1 & 1 & 0 & 0 & 0 \\
     0 & 0 & 1 & 1 & 1 \\
  \end{array}\right) \sim 
  \left(\begin{array}{@{}cc|ccc@{}}
    1 & 1  & 0 & 0 & 0 \\
    1 & 1  & 0 & 0 & 0 \\\hline
    0 & 0  & 1 & 1 & 1 \\
    0 & 0  & 1 & 1 & 1 \\
    0 & 0  & 1 & 1 & 1 \\
  \end{array}\right)$$
  
In general, if $B$ can be block-decomposed

$$ B \sim \begin{pmatrix} 
    B_1 & 0  & \dots \\
    \vdots & B_2 & \vdots\\
    0 & \dots  & B_K 
    \end{pmatrix} $$

and the dimensions of the blocks $B_i$ are respectively $N_i \times N_i$, then computing $B^2$ doesn't cost $O(N^3) $ anymore, but $O(N_1^3 + N_2^3 + \dots + N_K^3)$. This can be a great improvement!

Consider for instance $N = 10^6$ ,  $N_i = 1000 \ \forall i \leq 1000$.

$$N^3 = 10^{18} \gg 1000 \cdot (1000)^3 = 10^{12}$$

The efficiency gain is a factor of 1 million, or $10^6$.
