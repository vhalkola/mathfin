import numpy as np
import matplotlib.pyplot as plt
import secrets

mu = 1
n = 50
dt = 0.1
x0 = 100
np.random.seed(secrets.randbits(16))

sigma = np.arange(0.8, 2, 0.2)

x = np.exp(
    (mu - sigma ** 2 / 2) * dt
    + sigma * np.random.normal(0, np.sqrt(dt), size=(len(sigma), n)).T
)
x = np.vstack([np.ones(len(sigma)), x])
x = x0 * x.cumprod(axis=0)

plt.plot(x)
plt.legend(np.round(sigma, 2))
plt.xlabel("$t$")
plt.ylabel("$x$")
plt.title(
    "Realisations of Geometric Brownian Motion with different variances\n $\mu=1$"
)
plt.show()
