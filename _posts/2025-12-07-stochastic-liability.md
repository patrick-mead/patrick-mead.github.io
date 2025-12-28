---
layout: post
title: Saving for a house is a duration problem 
date: 2025-12-06 12:00:00
description: 
categories:
---

Most personal-finance advice treats saving for a home deposit as a problem of wealth preservation.
Accordingly, it is commonly recommended that cash is held to minimise volatility and avoid losses prior to the purchase.
This framing and subsequent advice is fundamentally wrong.
A home deposit is an implicit, long-duration liability, and therefore the task of saving for one should be framed as a funding problem.
That is, the economically relevant object of interest should be the volatility of wealth relative to house prices.
Once this perspective is adopted, it becomes immediately obvious that cash is a poor choice because it is duration-mismatched.
It also follows that assets that covary with housing are rational inclusions in a deposit portfolio.


Let,
+ $P$, denote the value of the household's portfolio at the time of purchase
+ $L$, denote the market price of the liability.

Define the funding ratio as,

$$ X := \frac{P}{L}. $$

For the current purposes, we will treat the house price as the present value of a constant flow of real housing services $H > 0$.

$$ L(r) = \int_0^\infty \exp(-rt) H \, dt = \frac{H}{r}. $$

The duration is the semi-elasticity of price with respect to the discount rate,

$$ D := - \frac{\partial \log L}{\partial r}. $$

Applied to our house liability $L$, gives us,

$$ D = \frac{1}{r}. $$

Thus housing is a long-duration asset, and further is more sensitive to rate changes when rates are low.

As cash has zero duration, the duration of the funding ratio is,

$$ \frac{\partial X}{\partial r} = \frac{1}{r}. $$

In this model, interest rates declines cause house prices to increase but do not affect the value of cash holdings.
Therefore, a household holding cash falls behind its target even whilst holding a low volatility asset.


The appropriate framing is of a tracking-error objective from asset-liability management.
For this we rely only on covariance, not causation.
If we can find tradable assets that covary with house prices, we would be able to hedge funding risk.

We propose that housing returns load on two sources of variation:
1. Discount-rate shocks
When rates fall, long-duration assets move upwards.
This risk is spanned by bonds
2. Growth and demand shocks
Housing demand is driven in part by macroeconomic factors such as wages, employment, and credit conditions.
This risk is spanned by equities.

We therefore model housing returns as,

$$ l = \beta_B r_B + \beta_E r_E + \epsilon. $$

Where, 
+ $r_B$ is a bond return,
+ $r_E$ is an equity return,
+ $\epsilon$ is an unhedgable residual risk.

Let $R$ denote the vector of excess returns on tradable assets.
A portfolio is represented by a vector $w$ denoting the weighting applied to each asset.
The return of a portfolio is $r_p = w'R$, and the funding-gap is given by $r_p - l$.
The optimisation problem is then,

$$ \min_w \textrm{Var}(w'R - l). $$

Which can be expanded to give,

$$ \textrm{Var}(w'R - l) = w'\sum_{RR}w - 2w'\sum_{Rl} + \textrm{Var}(l). $$

As a result, as long as there exists at least one tradable asset with non-zero convariance with housing returns, the 100% cash portfolio does not minimise the funding-gap variance.
This also supports maintaining a home-country bias, as domestic equities are likely to covary more strongly with domestic housing than foreign equities.


When considering how to save for a house, it is crucial to recognise that the implicit liability is not constant.
Cash may be "low-risk" from the perspective of volatility in its nominal value, but it in the context of saving for a house it is actually an active short position against duration.
A liability-relative or funding-gap perspective leads naturally to portfolios that hedge both discount-rate and growth risks using a combination of bonds and equities, with a home-country bias being appropriate.
