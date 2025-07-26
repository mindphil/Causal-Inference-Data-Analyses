Analyzing the SIPP 1991 dataset to understand how 401(k) programs affect household financial assets. The analysis follows the pattern established in the [LDW job](ldw) training example but focuses on [retirement savings policy](401k).
### WIP
## 1\. Data Context and Background

**Research Question:** Do 401(k) programs increase household savings, or do they just shift savings from other accounts?

**The Challenge:** People who participate in 401(k)s might already be good savers. Simply comparing participants vs. non-participants would give biased results.

**The Solution:** Using employer offering (`e401`) as an instrument for participation (`p401`) to get causal estimates.

**Key Variables:**

* **Outcome:** `net_tfa` (Net total financial assets) - what we want to explain
* **Treatment:** `p401` (401k participation) - the policy intervention of interest
* **Instrument:** `e401` (employer offers 401k) - affects participation but not directly savings
* **Controls:** Demographics and other savings-related factors

**Setting up your virtual enviroment:**
```conda create --name <env name> python=3.8```
```conda activate <env name>```
```conda install --file requirements.txt```