"""
==================================
Sliced Average Variance Estimation
==================================

An example plot of :class:`sdr.SlicedAverageVarianceEstimation`
"""
import numpy as np
import sdr
import matplotlib.pyplot as plt

from sdr import datasets


X, y = datasets.make_quadratic(random_state=123)

save = sdr.SlicedAverageVarianceEstimation()
X_save = save.fit_transform(X, y)

# estimate of the first direction
beta1_hat = save.components_[:, 0]

plt.scatter(X_save[:, 0], y, c=y, cmap='viridis', linewidth=0.5)
plt.xlabel("$X\hat{\\beta_1}$")
plt.ylabel("y")

# annotation showing the direction found
beta_text = "$\\beta_1$ = " + "{0}".format([0.707, 0.707])
plt.annotate(beta_text, xy=(-1, 2))
beta1_hat_text = "$\hat{\\beta_1}$ = " + "{0}".format(
    np.round(beta1_hat, 3).tolist()[:2])
plt.annotate(beta1_hat_text, xy=(-1, 1.75))

plt.show()