In Python, integers are one of the most fundamental data types, and there are various operations that can be performed on them. Here is a comprehensive list of basic and advanced operations you can apply to integers in Python:

### Basic Integer Operations

1. **Arithmetic Operations**
   - **Addition (`+`)**
     ```python
     a = 5
     b = 3
     result = a + b
     # Output: 8
     ```
   - **Subtraction (`-`)**
     ```python
     result = a - b
     # Output: 2
     ```
   - **Multiplication (`*`)**
     ```python
     result = a * b
     # Output: 15
     ```
   - **Division (`/`)**
     ```python
     result = a / b
     # Output: 1.6666666666666667
     ```
   - **Floor Division (`//`)**
     ```python
     result = a // b
     # Output: 1
     ```
   - **Modulus (`%`)**
     ```python
     result = a % b
     # Output: 2
     ```
   - **Exponentiation (`**`)**
     ```python
     result = a ** b
     # Output: 125
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
   a = 5
   ```

2. **Add and Assign (`+=`)**
   ```python
   a += 3
   # Equivalent to: a = a + 3
   # Output: 8
   ```

3. **Subtract and Assign (`-=`)**
   ```python
   a -= 2
   # Equivalent to: a = a - 2
   # Output: 6
   ```

4. **Multiply and Assign (`*=`)**
   ```python
   a *= 2
   # Equivalent to: a = a * 2
   # Output: 12
   ```

5. **Divide and Assign (`/=`)**
   ```python
   a /= 4
   # Equivalent to: a = a / 4
   # Output: 3.0
   ```

6. **Floor Divide and Assign (`//=`)**
   ```python
   a //= 3
   # Equivalent to: a = a // 3
   # Output: 1
   ```

7. **Modulus and Assign (`%=`)**
   ```python
   a %= 2
   # Equivalent to: a = a % 2
   # Output: 1
   ```

8. **Exponentiate and Assign (`**=`)**
   ```python
   a **= 3
   # Equivalent to: a = a ** 3
   # Output: 1
   ```

### Bitwise Operations

1. **AND (`&`)**
   ```python
   result = a & b
   # Output: result of bitwise AND
   ```

2. **OR (`|`)**
   ```python
   result = a | b
   # Output: result of bitwise OR
   ```

3. **XOR (`^`)**
   ```python
   result = a ^ b
   # Output: result of bitwise XOR
   ```

4. **NOT (`~`)**
   ```python
   result = ~a
   # Output: result of bitwise NOT
   ```

5. **Left Shift (`<<`)**
   ```python
   result = a << 1
   # Output: a shifted left by 1 bit
   ```

6. **Right Shift (`>>`)**
   ```python
   result = a >> 1
   # Output: a shifted right by 1 bit
   ```

### Type Conversion

1. **Convert to Float**
   ```python
   a = 5
   result = float(a)
   # Output: 5.0
   ```

2. **Convert to String**
   ```python
   result = str(a)
   # Output: "5"
   ```

3. **Convert to Binary**
   ```python
   result = bin(a)
   # Output: "0b101"
   ```

4. **Convert to Hexadecimal**
   ```python
   result = hex(a)
   # Output: "0x5"
   ```

5. **Convert to Octal**
   ```python
   result = oct(a)
   # Output: "0o5"
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
   result = math.factorial(a)
   # Output: factorial of a
   ```

4. **Power**
   ```python
   result = math.pow(a, b)
   # Output: a raised to the power of b
   ```

By understanding and utilizing these operations, you can effectively work with integers in Python to perform a wide range of computational tasks.
