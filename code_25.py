Below is a concise, type‑annotated implementation that follows the specification exactly.  
I’ll walk through the reasoning first, then show the final code.

---

## Step‑by‑step reasoning

1. **What is required?**  
   * Input: a *positive* floating‑point number.  
   * Output: the fractional (decimal) part of that number, i.e.  
     `number - floor(number)`.

2. **Edge cases**  
   * If the input is an integer (e.g. `3.0`), the fractional part is `0.0`.  
   * For very large numbers the subtraction can lose precision, but that is inherent to binary floating‑point arithmetic and is acceptable for the problem’s scope.  
   * The docstring explicitly says “positive”, so we don’t need to handle negatives, but the implementation can be extended trivially if desired.

3. **Choosing the right tool**  
   * `math.floor` gives the largest integer ≤ `number`.  
   * `math.modf` returns a tuple `(fractional, integer)`; the fractional part is exactly what we need.  
   * Using `math.modf` is slightly cleaner because it does the subtraction internally and guarantees the sign of the fractional part