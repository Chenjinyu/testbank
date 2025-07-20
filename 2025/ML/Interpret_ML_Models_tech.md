**SHAP values** (Shapley Additive Explanations) and **Partial Dependence Plots (PDPs)** are two different techniques used to interpret machine learning models, especially **black-box models** like XGBoost, Random Forests, or deep learning.


From Youtube: https://www.youtube.com/watch?v=UJeu29wq7d0, 
the Shapley value = expected marginal contribution
                  = weighted average of a player's contributions

![Coalition vaules](./imgs/Coalition%20values.jpg)
![shapley formula](./imgs/shapley%20formula.jpg)

---

## 🔍 Overview Comparison

| Aspect                           | SHAP (Shapley Values)                               | PDP (Partial Dependence Plot)                  |
| -------------------------------- | --------------------------------------------------- | ---------------------------------------------- |
| **Goal**                         | Explain individual predictions                      | Show average model response to a feature       |
| **Granularity**                  | Local (instance-level)                              | Global (feature-level trend)                   |
| **Uses game theory?**            | ✅ Yes (Shapley values from cooperative game theory) | ❌ No                                           |
| **Handles feature interaction?** | ✅ Yes                                               | ❌ No (assumes independence unless ICE is used) |
| **Output**                       | Feature contributions per prediction                | Line or surface plot showing marginal effect   |
| **Best for**                     | Explaining specific model decisions                 | Understanding average feature effect on output |

---

## 🧠 SHAP (Shapley Values)

### 🔸 What it is:

* Based on **cooperative game theory**
* For each prediction, SHAP assigns a **value to each feature** showing **how much that feature contributed** to the prediction.

### 🔸 Key benefits:

* **Consistent**: Sum of SHAP values + base value = model prediction
* **Interpretable**: Great for **why this prediction?**
* **Works well with tree models** (via `TreeSHAP`)

### 🔸 Example:

```python
import shap

explainer = shap.Explainer(model)
shap_values = explainer(X_test)

# Visualize individual prediction
shap.plots.waterfall(shap_values[0])
```

---

## 📈 PDP (Partial Dependence Plot)

### 🔸 What it is:

* Shows how changing a feature affects the model prediction **on average**, keeping all other features fixed (which can be unrealistic!)

### 🔸 Key benefits:

* Easy to interpret visually
* Good for **understanding trends** (e.g., “does higher income increase loan approval probability?”)

### 🔸 Example:

```python
from sklearn.inspection import plot_partial_dependence

plot_partial_dependence(model, X, features=[0])  # feature index or name
```

---

## ✅ When to Use What?

| You want to...                                 | Use This      |
| ---------------------------------------------- | ------------- |
| Explain a **single prediction**                | SHAP          |
| Show how a feature affects predictions overall | PDP           |
| Analyze feature **interactions**               | SHAP (or ICE) |
| Handle **correlated features** safely          | SHAP          |
| Get **quick global insight**                   | PDP           |

---

## 🧠 Bonus: ICE vs PDP

* **PDP** shows average effect
* **ICE (Individual Conditional Expectation)** shows **per-instance lines** — better for spotting heterogeneity
