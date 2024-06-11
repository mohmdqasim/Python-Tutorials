In Python, floating-point numbers (floats) are used to represent decimal numbers. Similar to integers, there are various operations and methods you can apply to floats. Here's a comprehensive list of basic and advanced operations you can use with floats in Python:

### Basic Float Operations

1. **Arithmetic Operations**
   - **Addition (`+`)**
     ```python
     a = 5.5
     b = 3.2
     result = a + b
     # Output: 8.7
     ```
   - **Subtraction (`-`)**
     ```python
     result = a - b
     # Output: 2.3
     ```
   - **Multiplication (`*`)**
     ```python
     result = a * b
     # Output: 17.6
     ```
   - **Division (`/`)**
     ```python
     result = a / b
     # Output: 1.71875
     ```
   - **Floor Division (`//`)**
     ```python
     result = a // b
     # Output: 1.0
     ```
   - **Modulus (`%`)**
     ```python
     result = a % b
     # Output: 2.2999999999999994
     ```
   - **Exponentiation (`**`)**
     ```python
     result = a ** b
     # Output: 312.61870534473767
     ```

### Comparison Operations

1. **Equal (`==`)**
   ```python
   result = a == b
   # Output: False
   ```
2. **Not Equal (`!=`)**
   ```python
   result = a != b
   # Output: True
   ```
3. **Greater Than (`>`)**
   ```python
   result = a > b
   # Output: True
   ```
4. **Less Than (`<`)**
   ```python
   result = a < b
   # Output: False
   ```
5. **Greater Than or Equal To (`>=`)**
   ```python
   result = a >= b
   # Output: True
   ```
6. **Less Than or Equal To (`<=`)**
   ```python
   result = a <= b
   # Output: False
   ```

### Assignment Operations

1. **Assign (`=`)**
   ```python
   a = 5.5
   ```

2. **Add and Assign (`+=`)**
   ```python
   a += 3.2
   # Equivalent to: a = a + 3.2
   # Output: 8.7
   ```

3. **Subtract and Assign (`-=`)**
   ```python
   a -= 2.1
   # Equivalent to: a = a - 2.1
   # Output: 6.6
   ```

4. **Multiply and Assign (`*=`)**
   ```python
   a *= 2
   # Equivalent to: a = a * 2
   # Output: 13.2
   ```

5. **Divide and Assign (`/=`)**
   ```python
   a /= 4
   # Equivalent to: a = a / 4
   # Output: 3.3
   ```

6. **Floor Divide and Assign (`//=`)**
   ```python
   a //= 1.5
   # Equivalent to: a = a // 1.5
   # Output: 2.0
   ```

7. **Modulus and Assign (`%=`)**
   ```python
   a %= 2
   # Equivalent to: a = a % 2
   # Output: 1.5
   ```

8. **Exponentiate and Assign (`**=`)**
   ```python
   a **= 3
   # Equivalent to: a = a ** 3
   # Output: 3.375
   ```

### Mathematical Functions from `math` Module

1. **Absolute Value**
   ```python
   import math
   result = math.fabs(a)
   # Output: absolute value of a
   ```

2. **Square Root**
   ```python
   result = math.sqrt(a)
   # Output: square root of a
   ```

3. **Factorial**
   ```python
   # Note: math.factorial() only works with integers.
   result = math.factorial(int(a))
   # Output: factorial of a
   ```

4. **Power**
   ```python
   result = math.pow(a, b)
   # Output: a raised to the power of b
   ```

5. **Exponential**
   ```python
   result = math.exp(a)
   # Output: exponential of a
   ```

6. **Logarithm**
   ```python
   result = math.log(a)
   # Output: natural logarithm of a
   result_base10 = math.log10(a)
   # Output: base-10 logarithm of a
   ```

7. **Trigonometric Functions**
   - **Sine**
     ```python
     result = math.sin(a)
     # Output: sine of a
     ```
   - **Cosine**
     ```python
     result = math.cos(a)
     # Output: cosine of a
     ```
   - **Tangent**
     ```python
     result = math.tan(a)
     # Output: tangent of a
     ```

8. **Rounding Functions**
   - **Round to nearest integer**
     ```python
     result = round(a)
     # Output: a rounded to nearest integer
     ```
   - **Round down**
     ```python
     result = math.floor(a)
     # Output: a rounded down
     ```
   - **Round up**
     ```python
     result = math.ceil(a)
     # Output: a rounded up
     ```

### Type Conversion

1. **Convert to Integer**
   ```python
   a = 5.5
   result = int(a)
   # Output: 5
   ```

2. **Convert to String**
   ```python
   result = str(a)
   # Output: "5.5"
   ```

### Random Numbers (from `random` Module)

1. **Generate a Random Float**
   ```python
   import random
   result = random.uniform(1.0, 10.0)
   # Output: random float between 1.0 and 10.0
   ```

2. **Generate a Random Float Between 0 and 1**
   ```python
   result = random.random()
   # Output: random float between 0 and 1
   ```

By mastering these operations and methods, you can effectively manipulate and interact with floating-point numbers in Python to perform a wide range of tasks.
