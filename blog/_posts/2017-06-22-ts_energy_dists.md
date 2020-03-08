---
layout: posts
author: Colin Kinz-Thompson
title: Distributions of Transition State Energies
date: 2017-06-22
---

## Gamma
Let's say that you're analyzing the survival probability (*i.e.*, $$1-CDF$$) of the lifetime, $$t$$, of a molecule in a particular state with rate constant, $$k$$. If the system is Markovian, then this probability is

$$S(t\vert k) = e^{-k*t}$$

but, what if there is a distribution of rate constants? What does this look like? Following *Austin ... Frauenfelder, Biochemistry 1975*, they note that they see power-law decays for the probably of ligand rebinding to myoglobin, and that this is probably because of a distribution of activation energies for the barrier crossings. They give an expression that looks quite a bit like the gamma distribution, so let's start there. What if you have rate constants distributed according to the gamma distribution,

$$G(k\vert \alpha , \beta) = \frac{\beta^\alpha k^{\alpha-1} e^{-\beta k}}{\Gamma (\alpha )}$$.

We can then marginalize $$k$$ out of the survival probability expression as follows

$$\begin{aligned}
S(t \vert \alpha, \beta) &= \int_0^\infty dk \cdot S(t \vert k) \cdot G(k \vert \alpha, \beta) \\
&= \frac{\beta^\alpha}{\Gamma (\alpha )} \int_0^\infty dk \cdot k^{\alpha - 1}e^{-k(t + \beta)} \\
&= \frac{\beta^\alpha}{\Gamma (\alpha )} \int_0^\infty \frac{dz}{t + \beta} \cdot \left(\frac{z}{t + \beta}\right)^{\alpha - 1}e^{-z},\text{ where } z \equiv (t+\beta)k \\
&= \frac{\beta^\alpha}{\Gamma (\alpha )} (t+\beta )^{-\alpha} \int_0^\infty dz \cdot z^{\alpha-1}\cdot e^{-z} \\
&= \frac{\beta^\alpha}{\Gamma (\alpha )} (t+\beta )^{-\alpha} \cdot \Gamma (\alpha) \\
&= \left( \frac{\beta}{t + \beta}\right)^\alpha
\end{aligned}$$

This is pretty interesting, because the form is actually a power-law decay, just like Austin *et al* said. Anyway, going with the gamma distribution interpretation of these parameters, you find the $$\beta$$ is the (constant) time of each sub-step (*i.e.*, elementary reactions) involved in the decay step out of the molecular state. Additionally, $$\alpha$$ is the number of sub-steps made be decay step (*i.e.*, this is an Erlang distribution interpretation). Austin *et al* give an expression for this distribution,

$$g(k) = \frac{(kt)^n e^{-kt}}{RT \Gamma (n)}.$$

To make sure that this distribution is normalized(!!), we can match the parameters given here with the parameters of the gamma distribution. If we find that $$\alpha \sim n$$, $$\beta \sim t$$, and $$k \sim k$$. Thus, those parameters have the same interpretation. To ensure that $$g(k)$$ is normalized, we find that $$\alpha = RT$$. This is an interesting thought. For instance, is this a result of the equipartition of energy? I guess it means that the transition involves more sub-steps with increasing temperature (linearly). That is kind of a strange thought; $$\beta$$ should also have some temperature dependence (i.e. it should decrease with increasing temperature).

## Normal

A less exact case is if the rate constants are distributed according to a normal distribution, $$\mathcal{N}(k \vert \mu, \sigma)$$. This is a bit of a stretch, because rate constants aren't negative, but the support of the normal distribution is from $$-\infty$$ to $$+\infty$$. However, as long as the normal distribution is very small when $$k < 0$$, then this is fairly reasonable. Here, we'll ignore the bounds of the integral for that reason. An additional note is that the gamma distribution should begin to approximate the normal distribution when $$\alpha$$ becomes quite large. Anyway, if we marginalize out $$k$$, as above, we find that

$$\begin{aligned}
S(k \vert \mu, \sigma) &= \int dk \cdot \mathcal{N} (k \vert \mu, \sigma)\cdot e^{-kt} \\
&= \frac{1}{\sqrt{2 \pi \sigma^2}} \int dk \cdot e^{\frac{-1}{2\sigma^2} (k-\mu)^2 - kt}\\
&= \frac{1}{\sqrt{2 \pi \sigma^2}} \int dk \cdot e^{\frac{-1}{2\sigma^2} \left(k^2 - 2\mu k + \mu^2 - 2\sigma^2 kt \right)}\\
&= \frac{1}{\sqrt{2 \pi \sigma^2}} \int dk \cdot e^{\frac{-1}{2\sigma^2} \left( (k-(\mu-\sigma^2t))^2 + 2\mu \sigma^2 t - \sigma^4 t^2 \right)}\\
&= \frac{1}{\sqrt{2 \pi \sigma^2}} \int dk \cdot e^{\frac{-1}{2\sigma^2} \cdot (k-(\mu-\sigma^2t))^2}e^{\frac{-1}{2\sigma^2} ( 2\mu \sigma^2 t - \sigma^4 t^2 )}\\
&= e^{\frac{-1}{2\sigma^2} ( 2\mu \sigma^2 t - \sigma^4 t^2 )}\cdot \frac{1}{\sqrt{2 \pi \sigma^2}} \int dk \cdot e^{\frac{-1}{2\sigma^2} \cdot (k-(\mu-\sigma^2t))^2}\\
&= e^{\frac{-1}{2\sigma^2} ( 2\mu \sigma^2 t - \sigma^4 t^2 )}\cdot \int dk \cdot \mathcal{N} ( k\vert \mu-\sigma^2 t, \sigma^2 )\\
&= e^{\frac{-1}{2\sigma^2} ( 2\mu \sigma^2 t - \sigma^4 t^2 )} \\
&= e^{-\mu t + \frac{1}{2} \sigma^2 t^2}.
\end{aligned}$$


This expression is exact if there is not a significant contribution from the $$k < 0$$ region (*i.e.*, very slow rates, where the decay times are very long). If there are those effects, you will find that at small $$t$$, the form is exact, and then at long $$t$$, you see a curved deviation away from the exact solution towards increasing survival probability. That's obviously wrong, but it's the effects of the $$k < 0$$ region.
