

---

## 🧠 1. **Epoch**

> An **epoch** is **one complete pass** through the **entire training dataset** by the learning algorithm.

* If you have 10,000 samples and train for 5 epochs:

  * Your model will see **all 10,000 samples** 5 times
* Training for multiple epochs helps the model learn better

---

## 📦 2. **Batch** and **Batch Size**

> A **batch** is a small **subset of the training data** used to compute the gradient and update the model during training.

* Instead of feeding all data at once (which is slow and memory-heavy), we split the data into **smaller chunks**
* The **batch size** is the **number of samples per batch**

### Example:

* Dataset: 10,000 samples
* Batch size: 100
* → Each epoch = 10,000 ÷ 100 = **100 batches**

---

## 🔁 3. **Iteration**

> An **iteration** is **one update step** (forward + backward pass) using **one batch**.

So:

```
Iterations per Epoch = Total Samples / Batch Size
```

### Using the same example:

* Batch size = 100
* Dataset size = 10,000
* → **100 iterations per epoch**

If you train for 5 epochs:

* → 5 × 100 = **500 iterations total**

---

## 🔁 Visualizing the Relationship

```
Epoch = 1 full cycle through dataset
Batch Size = how many samples you process at a time
Iteration = 1 batch → forward + backward pass + weights updated
```

### Diagram:

```
Epoch 1
  ├─ Iteration 1 → batch 1 (100 samples)
  ├─ Iteration 2 → batch 2 (100 samples)
  ├─ ...
  └─ Iteration 100 → batch 100

Epoch 2
  ├─ Iteration 101 → batch 1 again (shuffled)
  └─ ...
```

---

## 🎯 TL;DR

| Term           | Definition                                       |
| -------------- | ------------------------------------------------ |
| **Epoch**      | One full pass over the training dataset          |
| **Batch**      | Subset of data processed at once                 |
| **Batch Size** | Number of samples per batch                      |
| **Iteration**  | One update step per batch (per forward+backward) |

---

