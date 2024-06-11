Dictionaries in Python are unordered collections of items. Each item is a key-value pair. Below is a comprehensive list of operations and methods you can use with dictionaries in Python:

### Basic Dictionary Operations

1. **Creating Dictionaries**
   ```python
   my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
   empty_dict = {}
   ```

2. **Accessing Elements**
   ```python
   name = my_dict['name']
   # Output: 'Alice'
   age = my_dict.get('age')
   # Output: 25
   ```

3. **Modifying Elements**
   ```python
   my_dict['age'] = 26
   # my_dict is now {'name': 'Alice', 'age': 26, 'city': 'New York'}
   ```

4. **Adding Elements**
   ```python
   my_dict['email'] = 'alice@example.com'
   # my_dict is now {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}
   ```

5. **Removing Elements**
   - **Using `del`**
     ```python
     del my_dict['city']
     # my_dict is now {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}
     ```
   - **Using `pop`**
     ```python
     email = my_dict.pop('email')
     # Output: 'alice@example.com'
     # my_dict is now {'name': 'Alice', 'age': 26}
     ```
   - **Using `popitem` (removes the last inserted key-value pair)**
     ```python
     last_item = my_dict.popitem()
     # Output: ('age', 26)
     # my_dict is now {'name': 'Alice'}
     ```

### Dictionary Methods

1. **Keys, Values, and Items**
   - **Keys**
     ```python
     keys = my_dict.keys()
     # Output: dict_keys(['name', 'age'])
     ```
   - **Values**
     ```python
     values = my_dict.values()
     # Output: dict_values(['Alice', 25])
     ```
   - **Items**
     ```python
     items = my_dict.items()
     # Output: dict_items([('name', 'Alice'), ('age', 25)])
     ```

2. **Checking Existence of Keys**
   ```python
   is_name_in_dict = 'name' in my_dict
   # Output: True
   is_city_in_dict = 'city' in my_dict
   # Output: False
   ```

3. **Copying**
   - **Shallow Copy**
     ```python
     copied_dict = my_dict.copy()
     # copied_dict is {'name': 'Alice', 'age': 25}
     ```
   - **Deep Copy**
     ```python
     import copy
     deep_copied_dict = copy.deepcopy(my_dict)
     ```

4. **Merging Dictionaries**
   - **Using `update`**
     ```python
     my_dict.update({'city': 'New York', 'email': 'alice@example.com'})
     # my_dict is now {'name': 'Alice', 'age': 25, 'city': 'New York', 'email': 'alice@example.com'}
     ```
   - **Using dictionary unpacking (Python 3.5+)**
     ```python
     dict1 = {'name': 'Alice', 'age': 25}
     dict2 = {'city': 'New York', 'email': 'alice@example.com'}
     merged_dict = {**dict1, **dict2}
     # merged_dict is {'name': 'Alice', 'age': 25, 'city': 'New York', 'email': 'alice@example.com'}
     ```

5. **Setting Default Values**
   ```python
   age = my_dict.setdefault('age', 30)
   # Output: 25 (age already exists, so the value remains unchanged)
   country = my_dict.setdefault('country', 'USA')
   # Output: 'USA' (country didn't exist, so it is added with the default value)
   ```

### Dictionary Comprehensions

1. **Creating a Dictionary with Comprehensions**
   ```python
   squares = {x: x ** 2 for x in range(6)}
   # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
   ```

### Iterating Through Dictionaries

1. **Iterating Over Keys**
   ```python
   for key in my_dict:
       print(key)
   # Output: 'name', 'age', 'city', 'email', 'country'
   ```

2. **Iterating Over Values**
   ```python
   for value in my_dict.values():
       print(value)
   # Output: 'Alice', 25, 'New York', 'alice@example.com', 'USA'
   ```

3. **Iterating Over Key-Value Pairs**
   ```python
   for key, value in my_dict.items():
       print(f"{key}: {value}")
   # Output:
   # name: Alice
   # age: 25
   # city: New York
   # email: alice@example.com
   # country: USA
   ```

### Advanced Dictionary Operations

1. **Dictionary from Keys**
   ```python
   keys = ['name', 'age', 'city']
   default_value = None
   new_dict = dict.fromkeys(keys, default_value)
   # Output: {'name': None, 'age': None, 'city': None}
   ```

2. **Counting with Dictionaries**
   ```python
   text = "hello world"
   count_dict = {}
   for char in text:
       count_dict[char] = count_dict.get(char, 0) + 1
   # Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
   ```

By mastering these operations and methods, you can effectively manipulate and interact with dictionaries in Python to perform a wide range of tasks.