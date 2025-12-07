---
layout: post
title: On Funding A Stochastic Liability
date: 2025-12-06 12:00:00
description: We consider various correlations between domestic equities, global (ex domestic) equities, and domestic property prices.
categories: sample-posts
---

Planning to purchase a house can be a difficult task.
I have heard the common advice that if an expense is less than three years away, you should maintain a more defensive portfolio.
Often the advice is to taper your exposure to volatility starting from around five years to prevent the supposedly devastating consequences of not having sufficient assets to meet the looming liability.
I have never been convinced that this is the optimal strategy for, at least, the following two reasons:

1. It does not model the expense as a choice. Or at least, it does not allow the decision maker to deviate from their initial choice.
2. It does not consider correlations between equities and property.

There is no apparent reason to me that extending or contracting the date of purchase is unreasonable.
From the user cost of housing perspective, owning and renting (the natural alternative) should be economically equivalent.
This is obviously contrary to much popular personal finance advice, which states unequivocally that owning is superior to renting.
Sometimes even going as far as to say that "renting is paying someone else's mortgage" (humorous when you consider that rental yields are currelty lower than the cost of borrowing).
Analysis that supports this view commonly overstates the expected return on equity by using an unrealistic growth rate or neglecting to consider material costs of ownership (or misunderstanding how leverage affects return on equity).

To resolve both 1. and 2., we will examine a model with a risk-free rate (denoted $r$) and two risky assets:

1. Domestic equities (denoted $S_d(t)$)
2. Global (ex-domestic) equities (denoted $S_g(t)$)

And one risky liability representing domestic property (denoted $L(t)$).

We model the processes using geometric Brownian motion with parameters $\mu_i$ and $\sigma_i$ for $i\in \{d,g,L\}$.
For example,

$$ \frac{dS_d}{S_d} = \mu_d dt + \sigma_d dZ_d. $$


Part of the motivation to consider the setup was the implications for the optimal home-country bias when you had a future liability which was correlated moreso with domestic equities than "rest-of-world" equities.
The correlation between two GBMs is given by,

$$ dZ_i dZ_j = \rho_{ij} dt \quad \text{for } i,j \in \{ d,g,L \}.  $$

Let $w_d$ and $w_g$ be the portfolio weights in domestic and global (ex-domestic) equities respectively.
Then the weight given to the risk-free rate is $1 - w_d - w_g$.

The dynamics of the portfolio wealth $W_t$,

$$ \frac{dW}{W} = [w_d(\mu_d - r) + w_g(\mu_g - r) + r] dt + w_d \sigma_d dZ_d + w_g \sigma_g dZ_g. $$

Our primary concern is the ratio of wealth to liability, 

$$ F_t = \frac{W_t}{L_t}. $$

We will be able to fund the liability when $F_t \geq 1$. To solve for the dynamics of $F_t$, we apply Ito's quotient rule,

$$ \frac{dF/F} = \left(\frac{dW}{W} - \frac{dL}{L}\right) - \left( \frac{dW}{W} \cdot \frac{dL}{L} \right) + \left( /frac{dL}{L} \right)^2. $$

...insert working here...

$$ \frac{dF}{F} = \frac{dW}{W} - \frac{dL}{L} + \sigma^2_L dt - \sigma_W\sigma_L \rho_{WL} dt. $$

...insert working here...

$$ \sigma^2_F = w_d^2\sigma_d^2 + w_g^2\sigma_g^2 + 2w_d w_g\sigma_d\sigma_g\rho{dg}+\sigma^2_L - 2(w_d\sigma_d\sigma_L\rho_{dL} + w_g\sigma_g\sigma_L\rho_{gL}. $$

...insert working here...

$$ \begin{align*} \mu_F &= \mu_W - \mu_L + \sigma^2_L - \sigma_W\sigma_L\rho_{WL} \\ &= ...  \end{align*} $$








