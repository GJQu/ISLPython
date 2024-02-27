import numpy as np

# Original dataset
data = np.array([160, 165, 170, 175, 180, 185, 165, 170, 175, 180])

# Number of bootstrap samples
n_bootstrap_samples = 1000

# Bootstrap process
bootstrap_means = []
for _ in range(n_bootstrap_samples):
    # Create a bootstrap sample with replacement
    sample = np.random.choice(data, size=len(data), replace=True)
    # Calculate the mean of the sample
    sample_mean = np.mean(sample)
    bootstrap_means.append(sample_mean)

# Calculating the 95% confidence interval
lower_bound = np.percentile(bootstrap_means, 2.5)
upper_bound = np.percentile(bootstrap_means, 97.5)

##print (lower_bound, upper_bound)

print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

