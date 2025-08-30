Awesome—let’s make A/B testing practical and usable.

# What A/B testing is (in one line)

Run **two versions** (A = current, B = change), **randomly assign** users, and use statistics to decide if B improved your **primary metric** (conversion, revenue/user, etc.).

---

# A simple, correct workflow

1. **Define the goal (OEC)**

   * Pick **one primary metric** (e.g., checkout conversion). Add **guardrails(护栏)** (e.g., error rate, latency, refund rate).

2. **Form a hypothesis**

   * “Changing copy to X will increase conversion by **≥ 10% relative**.”

3. **Choose MDE + power**

   * **MDE** (minimum detectable effect) = smallest lift you care about (e.g., +10% relative).
   * Typical settings: **α = 0.05** (5% false positive), **power = 0.8** (80% chance to detect MDE).

4. **Compute sample size**

   * For a **proportion metric** (conversion), per variant:

     $$
     n \approx \frac{2\,(z_{1-\alpha/2}+z_{1-\beta})^2 \; p(1-p)}{d^2}
     $$

     Where $p$ = baseline rate, $d$ = **absolute** MDE (e.g., from 5% to 5.5% → $d=0.005$).
     Rule of thumb for α=0.05, power=0.8: $n \approx \frac{16\,p(1-p)}{d^2}$.

   * **Example**: baseline $p=0.05$, want +10% relative → $d=0.005$.
     $n \approx 16 \times 0.05 \times 0.95 / 0.005^2 \approx 30{,}400$ users **per group**.

5. **Randomize & keep it sticky**

   * Assign by a **stable hash** of user\_id (or cookie for anonymous):

     ```python
     def bucket(user_id: str) -> str:
         import hashlib
         h = int(hashlib.md5(user_id.encode()).hexdigest(), 16)
         return "B" if (h % 100) < 50 else "A"  # 50/50 split
     ```
   * Ensure **stickiness** across sessions/releases; log the assignment.

6. **Run the test (fixed horizon)**

   * Don’t “peek and stop” early; plan duration from step 4.
   * Freeze other big changes; avoid holidays/promos that skew traffic.

7. **Analyze**

   * For **conversion**: two-proportion **z-test**; report **absolute** and **relative** lift with a **95% CI**.
   * For **revenue/user**: two-sample **t-test** (or bootstrap) on user-level means.
   * Check **guardrails** (latency, error rate) and **SRM** (sample ratio mismatch ≠ expected 50/50).

8. **Decide & ship**

   * Ship B if it improves the primary metric and guardrails are clean. Otherwise keep A or iterate.

---

# What to instrument (FastAPI on ECS)

* Emit per-request events with: `user_id`, `variant`, `timestamp`, `endpoint`, and **conversion flag/value** (e.g., purchased? amount).
* Store to your warehouse (Redshift/Snowflake/BigQuery) and build a small daily job:

  ```sql
  -- Conversion example (one row per user)
  WITH last_assign AS (
    SELECT user_id, MAX_BY(variant, ts) AS variant -- or any sticky source
    FROM assignment_events
    GROUP BY 1
  ),
  outcomes AS (
    SELECT user_id, MAX(CASE WHEN purchased THEN 1 ELSE 0 END) AS converted
    FROM events
    WHERE ts BETWEEN :start AND :end
    GROUP BY 1
  )
  SELECT a.variant,
         COUNT(*) AS users,
         SUM(o.converted) AS converters,
         1.0 * SUM(o.converted)/COUNT(*) AS conversion_rate
  FROM last_assign a
  LEFT JOIN outcomes o USING (user_id)
  GROUP BY 1;
  ```
* Keep an **A/A test** occasionally to validate your randomization and analytics (should show no significant difference).

---

# Frequentist vs Bayesian (quick take)

* **Frequentist** (above): fixed sample, p-values, CIs. Simple, industry standard.
* **Bayesian**: posterior probability “B is better”, lets you **monitor continuously** with decision thresholds. Great for product teams, but pick one framework and stick to it.

---

# Common gotchas (avoid these)

* **SRM** (sample ratio mismatch): A\:B ≠ expected 50:50 → fix assignment/logging before trusting results.
* **Peeking**: stopping on a lucky spike increases false positives; use fixed horizon or proper sequential methods.
* **Non-independence**: mixing user-level and session-level metrics without deduping users.
* **Novelty effects**: run long enough to pass the initial excitement dip/spike.
* **Unit mismatch**: assign by **user**, not request; analyze **user-level** outcomes for most business metrics.

---

# Guardrails & kill-switches

* Set **max error-rate** or **p95 latency** thresholds; auto-disable B if exceeded.
* Use **feature flags** (e.g., LaunchDarkly, AWS AppConfig, homegrown) to flip variants safely.

---

# Tiny reference: z-test for conversion (no external libs)

```python
import math

def z_test_conv(success_a, total_a, success_b, total_b):
    p_a = success_a/total_a
    p_b = success_b/total_b
    p_pool = (success_a + success_b) / (total_a + total_b)
    se = math.sqrt(p_pool*(1-p_pool)*(1/total_a + 1/total_b))
    z = (p_b - p_a) / se
    # two-sided p-value from z (approx):
    from math import erf, sqrt
    pval = 2 * (1 - 0.5*(1 + erf(abs(z)/sqrt(2))))
    return {"p_a": p_a, "p_b": p_b, "lift_abs": p_b-p_a, "z": z, "pval": pval}
```

---

## Quick checklist to run your first good test

* [ ] One clear **primary metric** + 2–3 **guardrails**
* [ ] Baseline, **MDE**, α=0.05, power=0.8 → **sample size**
* [ ] **Sticky** randomization by user\_id (hash)
* [ ] Fixed test window (no peeking)
* [ ] Sanity checks: **SRM**, logging completeness
* [ ] Report: effect size, 95% CI, p-value, guardrails

If you share your baseline conversion and desired MDE, I can compute the exact sample size and sketch the run time given your daily traffic.
