## Table Contents
- [What Are Hyperparameters](#-what-are-hyperparameters)
- [What Is Fine-Tuning](#-what-is-fine-tuning)
- [What Models Can Be Fine-Tuned](#what-models-can-be-fine-tuned)
- [WWhat Is Provisioned Throughput in Amazon Bedrock](#-what-is-provisioned-throughput-in-amazon-bedrock)


### 🧠 What Are **Hyperparameters**?

**Hyperparameters** are the **configuration settings** used to **control the training process** of a machine learning model.
They are **not learned** from the data — instead, you set them **before** training starts.

#### 🔧 Examples of Common Hyperparameters

| Category                | Hyperparameter                  | Description                                                             |
| ----------------------- | ------------------------------- | ----------------------------------------------------------------------- |
| **Optimization**        | `learning_rate`                 | How much the model adjusts weights each step                            |
|                         | `batch_size`                    | Number of samples used per training step                                |
|                         | `epochs`                        | How many times the model sees the full dataset                          |
| **Regularization**      | `dropout_rate`                  | Prevents overfitting by randomly dropping units                         |
|                         | `weight_decay`                  | Penalizes large weights                                                 |
| **Model Architecture**  | `num_layers`, `hidden_size`     | Structure of the model (e.g., for neural nets)                          |
| **Tokenizer/LLMs**      | `max_seq_length`, `vocab_size`  | Input limits and vocabulary size                                        |
| **Sampling/Generation** | `temperature`, `top_k`, `top_p` | (for LLMs) control randomness of output during generation, not training |

#### 🕒 When to Use / Tune Hyperparameters?

| When                           | Why It Matters                                                                       |
| ------------------------------ | ------------------------------------------------------------------------------------ |
| **Before Training**            | You must **set** them to define how the model learns                                 |
| **During Model Optimization**  | You **tune** them to improve accuracy, speed, or generalization                      |
| **When Using Pretrained LLMs** | You adjust generation hyperparameters like `temperature`, `top_p` for better outputs |

### ⚖️ Hyperparameters vs Parameters

| Feature                  | Parameters                  | Hyperparameters                    |
| ------------------------ | --------------------------- | ---------------------------------- |
| Learned during training? | ✅ Yes (e.g., model weights) | ❌ No (you define them manually)    |
| Examples                 | Weights, biases             | Learning rate, batch size, dropout |
| Set by                   | Model training              | You (or auto-tuner)                |

#### 🧪 How to Tune Hyperparameters?

* **Manual Search** – Try different combinations
* **Grid Search / Random Search** – Systematically test multiple values
* **Bayesian Optimization / AutoML** – Smart tuning based on performance
* **Libraries**: Optuna, Ray Tune, Scikit-learn GridSearchCV

#### ✅ Summary

| Term             | Hyperparameters                                             |
| ---------------- | ----------------------------------------------------------- |
| What             | Configurations set **before training**                      |
| Why use          | Control training process, improve model performance         |
| Tune When?       | Always, especially during model development                 |
| Typical Examples | `learning_rate`, `batch_size`, `dropout_rate`, `num_layers` |

---

### 🧠 What Is **Fine-Tuning**?

**Fine-tuning** is the process of taking a **pre-trained model** (like a foundation model or LLM) and **training it further** on your **specific dataset** to specialize it for a particular task or domain.

Instead of training from scratch, you **start from a strong base** and adapt it to your needs.

#### 🏗️ How It Works

| Stage           | What Happens                                                             |
| --------------- | ------------------------------------------------------------------------ |
| **Pretraining** | Train on huge, general-purpose data (e.g., all of Wikipedia, books, web) |
| **Fine-tuning** | Train further on your task-specific or domain-specific data              |

#### 🔧 When Do You Need Fine-Tuning?

| Situation                                                                   | Fine-Tuning Needed? | Why?                                             |
| --------------------------------------------------------------------------- | ------------------- | ------------------------------------------------ |
| You want better performance in a **specific domain** (e.g., medical, legal) | ✅ Yes               | General models may lack domain expertise         |
| You need **custom behavior** (e.g., a chatbot with your company tone)       | ✅ Yes               | Prompts alone aren't enough                      |
| You need to solve a **specific task** (e.g., classify customer feedback)    | ✅ Yes               | Model needs task-specific training               |
| You only need **general reasoning or generation**                           | ❌ No                | Use prompting or few-shot instead                |
| You’re doing **real-time querying over documents**                          | ❌ No                | Use RAG (Retrieval-Augmented Generation) instead |

#### 📦 Example Use Cases

| Use Case                        | Fine-Tuning? | Notes                           |
| ------------------------------- | ------------ | ------------------------------- |
| Legal Q\&A system for lawyers   | ✅ Yes        | Train on legal documents        |
| Customer support chatbot        | ✅ Yes        | Train on your support tickets   |
| Summarize generic news          | ❌ No         | Prompting is enough             |
| Translate between rare dialects | ✅ Yes        | Base model may not know dialect |

#### ⚙️ Types of Fine-Tuning

| Type                                                  | Description                                                                   |
| ----------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Full Fine-Tuning**                                  | All model weights are updated — more accurate but needs more compute          |
| **Parameter-Efficient Fine-Tuning (PEFT)**            | Use techniques like **LoRA**, adapters, QLoRA — efficient and memory-friendly |
| **Instruction Tuning**                                | Fine-tune model to follow instructions better                                 |
| **RLHF (Reinforcement Learning with Human Feedback)** | Align model with human preferences (used in GPT-4 training)                   |

#### ✅ Summary

| Feature     | Fine-Tuning                                               |
| ----------- | --------------------------------------------------------- |
| What        | Adapt a pre-trained model to your task/data               |
| When Needed | When prompts are not enough or domain is highly specific  |
| Input       | Your labeled data or task-specific examples               |
| Output      | A custom version of the model optimized for your use case |


---

### 🧠 What Models Can Be Fine-Tuned?
You can fine-tune **any pre-trained model**, but **some are better suited** (or explicitly designed) for fine-tuning.

##### ✅ **Fine-tuning Friendly Models**

| Model Family                  | Type                | Good for Fine-Tuning? | Notes                                                                     |
| ----------------------------- | ------------------- | --------------------- | ------------------------------------------------------------------------- |
| **Open-source LLMs**          | Text                | ✅ Yes                 | Designed to be extended: LLaMA, Mistral, Falcon, GPT-J, BLOOM             |
| **Hugging Face Transformers** | NLP, vision, audio  | ✅ Yes                 | Most models on Hugging Face support fine-tuning (BERT, T5, RoBERTa, etc.) |
| **Whisper**                   | Audio → Text        | ✅ Yes                 | OpenAI’s ASR model, trainable on custom audio                             |
| **DINOv2 / CLIP**             | Vision              | ✅ Yes                 | Image/text embedding or classification                                    |
| **SAM (Segment Anything)**    | Vision segmentation | ✅ Yes                 | Can be fine-tuned with additional images and masks                        |
| **LoRA-compatible models**    | NLP, code, etc.     | ✅ Yes                 | Support efficient parameter tuning (e.g., QLoRA on LLaMA)                 |

#### 🚫 Models **Not Easily Fine-Tuned**

| Type                                                     | Reason                                                     |
| -------------------------------------------------------- | ---------------------------------------------------------- |
| **Closed-source models** (e.g., ChatGPT, Claude, Gemini) | ❌ Cannot access weights                                    |
| **Models without weights released**                      | ❌ Not trainable                                            |
| **Heavily quantized models (e.g., GGUF at 4-bit)**       | ⚠️ Fine-tuning limited or impossible due to low precision  |
| **Embedding-only models** (e.g., sentence-transformers)  | ⚠️ Can be tuned but limited to vector representation tasks |

#### 🔍 How to Know If a Model Is Good for Fine-Tuning?

##### ✅ Check These:

1. **Weights Available?**

   * Check if `.bin`, `.pt`, or `.safetensors` files are provided.
   * Hugging Face models usually offer "Download model" and "Config" buttons.

2. **Tokenizer + Config Provided?**

   * Fine-tuning needs tokenizer and architecture info (`config.json`, `tokenizer.json`, etc.)

3. **Fine-tuning Examples or Docs Available?**

   * If the model page or GitHub repo provides sample fine-tuning code, it's a good sign.

4. **Community Adoption**

   * Models with popular LoRA adapters, PEFT support, or Hugging Face integration are safer to start with.

#### 🔧 Tools to Help You Decide

| Tool / Resource               | Use                                                     |
| ----------------------------- | ------------------------------------------------------- |
| **Hugging Face Hub**          | Model cards often state “intended for fine-tuning”      |
| **Papers with Code**          | Shows benchmarks, training recipes                      |
| **AdapterHub.ml**             | Shows models compatible with adapter tuning             |
| **llmware.ai**, **ollama.ai** | Show popular models suitable for lightweight finetuning |

#### 🧩 Summary Table

| Criteria                        | Good for Fine-Tuning | Not Good |
| ------------------------------- | -------------------- | -------- |
| Open-source weights             | ✅                    | ❌        |
| Has training config + tokenizer | ✅                    | ❌        |
| Supported by PEFT/LoRA          | ✅                    | ⚠️ Maybe |
| Quantized for inference only    | ⚠️ Sometimes         | ❌        |
| Closed model (e.g., OpenAI API) | ❌                    | ❌        |


If you're using **Amazon Bedrock** for model **fine-tuning** (especially **custom model fine-tuning** using **foundation models** like those from Anthropic, Meta, Cohere, or Amazon Titan), then **yes**, you may **need to use provisioned throughput** — depending on the provider and the type of tuning.

Here’s a breakdown:

---

### 🧠 What Is **Provisioned Throughput** in Amazon Bedrock?

**Provisioned throughput** means you **reserve dedicated capacity (TPS and tokens/sec)** to ensure consistent and fast performance for:

* Inference (real-time generation)
* **Fine-tuning** or model customization jobs

It’s often **required** for workloads that involve:

* **High-volume traffic**
* **Custom model training or fine-tuning**
* **Large prompt/response size**
* **SLA guarantees**

#### 🔍 When Is Provisioned Throughput **Required**?

| Use Case                                               | Provisioned Throughput Needed?             | Why?                                               |
| ------------------------------------------------------ | ------------------------------------------ | -------------------------------------------------- |
| **General prompt-based usage** (few-shot, no training) | ❌ No                                       | Can use on-demand                                  |
| **RAG or embedding lookups**                           | ❌ No (if using Titan Embeddings on-demand) | Standard usage                                     |
| **Fine-tuning (Custom models)**                        | ✅ **Yes**                                  | Needed to run training jobs and test them reliably |
| **Batch inference or real-time SLA workloads**         | ✅ Yes (optional)                           | For speed and consistency                          |

#### 🏗️ Fine-Tuning on Amazon Bedrock

Currently, Amazon Bedrock supports **fine-tuning (aka customization)** for specific models:

| Model Provider         | Fine-Tuning Support                      | Requires Provisioned Throughput |
| ---------------------- | ---------------------------------------- | ------------------------------- |
| **Amazon Titan**       | ✅ Yes                                    | ✅ Yes                           |
| **Meta (LLaMA)**       | ❌ No (inference only)                    | —                               |
| **Anthropic (Claude)** | ❌ No (prompt-only)                       | —                               |
| **Cohere**             | ✅ Yes (text-classification + generation) | ✅ Yes                           |
| **Mistral**            | ❌ No                                     | —                               |

#### 💰 Cost Consideration

* **Provisioned throughput is more expensive** than on-demand.
* You pay for reserved capacity whether you use it fully or not.
* Required for **training**, but not for simple prompt usage.

#### ✅ Summary

| Question                                                            | Answer                                                                                 |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Do I need provisioned throughput for **prompting only** on Bedrock? | ❌ No                                                                                   |
| Do I need it for **fine-tuning or customization**?                  | ✅ **Yes**                                                                              |
| Why is it needed?                                                   | Dedicated capacity for training jobs, reliable performance, and higher resource demand |

---
