# Roman to Integer
​
The Python class `Solution` contains a method `romanToInt(self, s: str) -> int` that converts a Roman numeral to an integer.
​
## How it Works
​
1. **Setup:** The Roman numeral system uses seven letters: `I`, `V`, `X`, `L`, `C`, `D`, and `M`. These letters stand for one, five, ten, fifty, hundred, five hundred, and one thousand respectively.
​
We first create a dictionary `roman_dict` that maps these Roman numerals to their respective integer values. We initialize `total` to 0, which will hold the final integer value of the Roman numeral. We also initialize `prev_value` to 0, which will hold the value of the previously processed Roman numeral.
​
2. **Processing:** The function enters a loop where it iterates over the input string `s` in reverse order. For each character in the string:
​
- It gets its value `current_value` from `roman_dict`.
- If `prev_value` is greater than `current_value`, it means we have encountered a situation like `IV` (where a smaller number is followed by a larger one), and we should subtract `current_value` from `total`.
- If `prev_value` is less than or equal to `current_value`, we add `current_value` to `total`.
- After processing a character, we set `prev_value` to `current_value`.
​
3. **Result:** Once all characters in the string have been processed, the function returns `total`.
​
## Special Considerations
​
This function correctly handles the subtleties of the Roman numeral system, where a smaller number preceding a larger number indicates subtraction. For example, in 'MCMXCIV' (1994), 'CM' is 900 ('C' is 100, but it comes before 'M' which is 1000, so we do 1000-100 = 900) and 'IV' is 4 ('I' is 1, but it comes before 'V' which is 5, so we do 5-1 = 4).
​