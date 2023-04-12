from sklearn.cluster import KMeans
import numpy as np

# Load data
X = np.loadtxt("data.csv", delimiter=",")

# Try different values of k
k_values = range(2, 11)
bic_scores = []

for k in k_values:
    # Fit KMeans model
    model = KMeans(n_clusters=k).fit(X)
    
    # Calculate SSE
    sse = np.sum(np.min(model.transform(X), axis=1) ** 2)
    
    # Calculate BIC score
    n = X.shape[0]
    k_params = 2 * k
    bic = n * np.log(sse / n) + k_params * np.log(n)
    bic_scores.append(bic)
    
# Print BIC scores for different values of k
for k, bic in zip(k_values, bic_scores):
    print(f"k={k}: BIC={bic}")
