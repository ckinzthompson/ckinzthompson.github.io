---
title: Autocorrelation Function Precision
description: A Bayesian take on estimating ACFs
author: Colin Kinz-Thompson
date: 2017-06-23
format:
  html:
    toc: true
    code-fold: true
---


## The Autocorrelation Function

### Definition
Following Berne and Pecora's *Dynamic Light Scattering with Applications to Chemistry, Biology, and Physics*, the autocorrelation function of a time-dependent signal, $A(t)$, is defined by

$$\begin{aligned}
\langle A(0)A(\tau) \rangle &= \lim_{T \to \infty} \frac{1}{T} \int_0^T dt\, A(t)A(t+\tau) \\
&\cong \lim_{N \to \infty} \frac{1}{N} \sum_{j=1}^N A_j A_{j+n},
\end{aligned}$$

where the bottom line is for a signal sampled at discrete intervals $\Delta t$ such that $t = j\Delta t$, and $\tau = N\Delta t$.



### Notes
At each point, the autocorrelation function is an average. The average is of the product of the signal and the signal after a given delay, $\tau$. Therefore, what we're really interested in is the average value of a set of these products. Given a finite-length vector, you will only have a limited number of these products at each $\tau$. In particular, at large values of $\tau$, you have very few products contributing to the average. In fact, at the maximum $\tau$ you only have one product contributing to the average. Therefore the precision with which you can define that actually value of the autocorrelation function given only a few of these products is limited. But, we can leverage Bayesian inference to help us out and quantify that precision.

## Bayesian Inference
We will assume that the products at a particular value of $\tau$ mentioned above are distributed according to a normal distribution with a mean, $\mu$, and a precision, $\lambda = 1/\sigma^2$, that are unknown. Given a set of these samples at the particular value of $\tau$, we can use Bayesian inference to infer the value of $\mu$, which corresponds to the value of the autocorrelation function at that $\tau$.

### Prior
We can do this inference easily with a normal-gamma distribution conjugate prior, *i.e.*,

$$\begin{aligned}p(\mu,\lambda \vert D) &= NG(\mu,\lambda \vert \mu_0, \kappa_0,\alpha_0,\beta_0) \\
&= \frac{1}{Z_0} \lambda^{\alpha_0-0.5} \cdot e^{-\frac{\lambda}{2}\left(\kappa_0(\mu-\mu_0)^2+2\beta \right)}
\end{aligned}$$

where

$$Z_0 =  \frac{\Gamma(\alpha)}{\beta^\alpha}\left(\frac{2\pi}{\kappa_0}\right)^{0.5},$$

and where $\Gamma(x)$ is the gamma function.

### Posterior
Following Kevin Murphy's nice paper, *Conjugate Bayesian analysis of the Gaussian distribution*, we can easily evaluate the posterior probability distribution of a normal likelihood, and a normal-gamma conjugate prior. The posterior probability distribution is also a normal-gamma distribution with

$$\begin{aligned}
\kappa_n &= \kappa_0 + n \\
\alpha_n &= \alpha_0 + n/2 \\
\mu_n &= \mu_0 \frac{\kappa_0\mu_0+n\bar{x}}{\kappa_n}\\
\beta_n &= \beta_0 + \frac{1}{2}\sum_{i=1}^n (x_i - \bar{x})^2 + \frac{\kappa_0 n (\bar{x} - \mu_0)^2}{2\kappa_n},
\end{aligned}$$

where $n$ is the number of datapoints in the set of products at the particular $\tau$ being evaluated, and $\bar{x}$ is the mean of those products in that set.

### Posterior Marginals
Actually, if we're just interested in the autocorrelation function, we dont' really care about $\lambda$, so we can marginalize it out of the posterior distribution given above. The posterior marginal for $\mu$ alone given the data, $\{A(t_i)A(t_i+\tau)\}$, is a Student's T distribution

$$p(\mu \vert \mu_n, \kappa_n, \alpha_n, \beta_n, \{A(t_i)A(t_i+\tau)\}) = T_{2 \alpha_n} \left( \mu \vert \mu_n, \frac{\beta_n}{\alpha_n\kappa_n}\right),$$

where the second argument is the variance parameter ($\sigma^2$). Note that the cumulative distribution function (CDF) of the Student's T distribution can be used to calculate the credible intervals on $\mu$ given this marginalized posterior probability distribution.

## Precision of the Autocorrelation function
We can calculate the autocorrelation function as shown above, but this does not give any notion of the precision of the autocorrelation function (particularly at large $\tau$). Instead, we will use Bayesian inference to infer the posterior probability distribution describing the autocorrelation function at every delay. This will provide us with the mean value, and a credible interval - the latter of which provides an idea of the precision with with the autocorrelation function is defined at any given $\tau$. The credible interval (95%) blows up at large $\tau$ (*i.e.*, n), showing us to be wary about using the mean value. Note, that the autocorrelation function is normalized to the first datapoint, $\tau=0$.
