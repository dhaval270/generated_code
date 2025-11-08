**Implementation Plan**

| Step | What to do | Why |
|------|------------|-----|
| **1. Data structures** | • `cleaned: str` – the input string with all spaces removed.<br>• `groups: List[str]` – the result list.<br>• `depth: int` – current nesting level.<br>• `start: int` – index where the current group starts. | These are the minimal structures needed to walk through the string once and collect balanced groups. |
| **2. Algorithm** | 1. **Pre‑process** – build `cleaned` by filtering out spaces (`''.join(ch for ch in paren_string if ch != ' ')`).<br>2. **Edge case** – if `cleaned` is empty, return `[]` immediately.<br>3. **Scan** – iterate over `cleaned` with an index `i` and character `ch`.<br>   * If `ch == '('`: <br>        * If `depth == 0`, this is the start of a new group → set `start = i`. <br>        * Increment `depth`.<br>   * If `ch == ')'`: <br>        * Decrement `depth`. <br>        * If `depth