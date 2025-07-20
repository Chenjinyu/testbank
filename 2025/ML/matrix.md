## Table of Contents
- [Popular Matrix List](#popular-matrix-list)

### Popular Matrix List
Sure! Here are the most **popular metrics** used to **evaluate machine learning models**, grouped by **problem type**:

#### 🧪 1. **Binary Classification Metrics**

| Metric                               | Description                                            |
| ------------------------------------ | ------------------------------------------------------ |
| **Accuracy**                         | Overall % of correct predictions                       |
| **Precision**                        | Of predicted positives, how many are correct           |
| **Recall (Sensitivity)**             | Of actual positives, how many were correctly predicted |
| **F1 Score**                         | Harmonic mean of precision & recall                    |
| **AUC-ROC**                          | Area under ROC curve (trade-off between TPR and FPR)   |
| **Log Loss**                         | Penalizes false confidence in predictions              |
| **Matthews Corr. Coefficient (MCC)** | Balanced metric even for imbalanced datasets           |

#### 🔢 2. **Multiclass Classification Metrics**

| Metric                               | Description                                    |
| ------------------------------------ | ---------------------------------------------- |
| **Accuracy**                         | Overall correct classification rate            |
| **Macro Precision / Recall / F1**    | Average metric across all classes equally      |
| **Weighted Precision / Recall / F1** | Accounts for class imbalance                   |
| **Confusion Matrix**                 | Extension of binary matrix to multiple classes |

#### 📈 3. **Regression Metrics**

| Metric                                      | Description                                           |
| ------------------------------------------- | ----------------------------------------------------- |
| **Mean Absolute Error (MAE)**               | Avg. absolute difference between predicted and actual |
| **Mean Squared Error (MSE)**                | Avg. of squared differences                           |
| **Root Mean Squared Error (RMSE)**          | sqrt(MSE) – same units as target                      |
| **R² Score (Coefficient of Determination)** | % of variance explained by the model                  |
| **Mean Absolute Percentage Error (MAPE)**   | MAE as a percentage of actual values                  |

#### 🎯 4. **Ranking & Recommendation Metrics**

| Metric                                           | Description                                |
| ------------------------------------------------ | ------------------------------------------ |
| **Precision\@k**                                 | Correct items in top-k predictions         |
| **Recall\@k**                                    | % of all relevant items found in top-k     |
| **NDCG (Normalized Discounted Cumulative Gain)** | Measures ranked relevance                  |
| **MAP (Mean Average Precision)**                 | Precision averaged across multiple queries |

#### 📊 5. **Clustering Metrics (Unsupervised Learning)**

| Metric                        | Description                                        |
| ----------------------------- | -------------------------------------------------- |
| **Silhouette Score**          | How well-separated and tight the clusters are      |
| **Adjusted Rand Index (ARI)** | Similarity to ground truth clusters                |
| **Davies-Bouldin Index**      | Lower is better – compact, well-separated clusters |


#### 6. **Correlation Matrix**

![Correlation Matrix](./imgs/Coalition%20values.jpg)

#### 7. **Confusion Matrix**
![confusion Matrix](./imgs/confusion%20matrix.jpg)

##### ✅ TL;DR Summary Table

| Task Type       | Top Metrics                              |
| --------------- | ---------------------------------------- |
| Classification  | Accuracy, F1, ROC-AUC, Precision, Recall |
| Regression      | MAE, RMSE, R²                            |
| Ranking/Recomm. | Precision\@k, Recall\@k, NDCG            |
| Clustering      | Silhouette, ARI, Davies-Bouldin          |

---

## 