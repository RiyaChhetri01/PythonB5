{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ccc9f5b0-f886-4ce4-9b07-b4d763b3c36f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Example: Creating a list of squares of even numbers from 0 to 9\n",
    "\n",
    "squares = []\n",
    "for i in range(10):\n",
    "    if i % 2 == 0:\n",
    "        squares.append(i ** 2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3f94f4d5-72de-4cf1-9be9-851c011a3e00",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 4, 16, 36, 64]\n"
     ]
    }
   ],
   "source": [
    "print(squares)  # Output: [0, 4, 16, 36, 64]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8641561f-e459-4e91-9eb5-23a3d43bf117",
   "metadata": {},
   "outputs": [],
   "source": [
    "# The same functionality using list comprehension\n",
    "\n",
    "squares = [i ** 2 for i in range(10) if i % 2 == 0]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "856066ca-9dd7-424b-bb5e-e3dc2bdf8692",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 4, 16, 36, 64]\n"
     ]
    }
   ],
   "source": [
    "print(squares)  # Output: [0, 4, 16, 36, 64]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d8bb825f-38b5-4cd6-bf69-e4712c59b69c",
   "metadata": {},
   "source": [
    "# map(), filter(), and reduce() Functions in Python"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c986528c-3b9f-47f1-a035-48d0e1711f31",
   "metadata": {},
   "source": [
    "# with map()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "379c169a-eb3c-4632-b119-468b41271c10",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Example: Converting a list of strings to uppercase\n",
    "\n",
    "def to_upper(word):\n",
    "    return word.upper()\n",
    "words = ['hello', 'world', 'python']\n",
    "upper_words = []\n",
    "for word in words:\n",
    "    upper_words.append(to_upper(word))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "14a4546f-280a-4725-9c8b-c4ee232092b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Using map to achieve the same result\n",
    "\n",
    "upper_words = list(map(to_upper, words))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "a11d1e0b-a8d5-4ff5-b70d-26f2f1ecacf5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['HELLO', 'WORLD', 'PYTHON']\n"
     ]
    }
   ],
   "source": [
    "print(upper_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "613f16c8-049a-4f1c-8ea4-0c44f9c17bd5",
   "metadata": {},
   "source": [
    "# Without map():"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "e67ac8d6-5621-499b-ad24-0d21ba1ee426",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Example: Converting a list of strings to uppercase\n",
    "\n",
    "def to_upper(word):\n",
    "    return word.upper()\n",
    "words = ['hello', 'world', 'python']\n",
    "upper_words = []\n",
    "for word in words:\n",
    "    upper_words.append(to_upper(word))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "bcbb887a-27ee-4416-b528-3d3a2b018934",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['HELLO', 'WORLD', 'PYTHON']\n"
     ]
    }
   ],
   "source": [
    "print(upper_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e472ce8c-7cc1-4db6-a972-8e689374d02f",
   "metadata": {},
   "source": [
    "# Without filter() Function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "b6f8f411-4995-456a-b8e7-a735f1f7b12e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Example: Filter even numbers from a list\n",
    "\n",
    "def is_even(num):\n",
    "    return num % 2 == 0\n",
    "numbers = [1, 2, 3, 4, 5, 6]\n",
    "even_numbers = []\n",
    "for num in numbers:\n",
    "    if is_even(num):\n",
    "        even_numbers.append(num)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "709c5cd7-1946-4b0b-acf8-9ceaed81ea03",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6]\n"
     ]
    }
   ],
   "source": [
    "print(even_numbers)  # Output: [2, 4, 6]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d082e87f-8c92-4520-88fb-d3274c174195",
   "metadata": {},
   "source": [
    "# with filter():"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "f2c8b6ef-b976-40c9-9f81-9220ac38de7e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Example: Filter even numbers from a list\n",
    "\n",
    "def is_even(num):\n",
    "    return num % 2 == 0\n",
    "numbers = [1, 2, 3, 4, 5, 6]\n",
    "even_numbers = []\n",
    "for num in numbers:\n",
    "    if is_even(num):\n",
    "        even_numbers.append(num)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "4a1b3d83-6a48-4308-9da8-1de55149c589",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Using filter to achieve the same result\n",
    "\n",
    "even_numbers = list(filter(is_even, numbers))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "27cb6dee-604b-4d1a-8c66-0f8555a16ad3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6]\n"
     ]
    }
   ],
   "source": [
    "print(even_numbers)  # Output: [2, 4, 6]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "75bb2fba-0118-4ba7-81b4-da92227bb33d",
   "metadata": {},
   "source": [
    "# without reduce()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "63905c1c-a9c4-47b5-9d3a-67cd2364b879",
   "metadata": {},
   "outputs": [],
   "source": [
    "from functools import reduce\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "def multiply(x, y):\n",
    "    return x * y\n",
    "numbers = [1, 2, 3, 4]\n",
    "product = 1\n",
    "for num in numbers:\n",
    "    product = multiply(product, num)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "2c1fe88a-2aaa-4ea4-bfd7-6898f135006f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "24\n"
     ]
    }
   ],
   "source": [
    "print(product)  # Output: 24\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "53005c42-6bca-4525-97b4-8a3e02daad4d",
   "metadata": {},
   "source": [
    "# with reduce()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "32149573-f57e-44e7-ae11-646603a1285a",
   "metadata": {},
   "outputs": [],
   "source": [
    "from functools import reduce\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "def multiply(x, y):\n",
    "    return x * y\n",
    "numbers = [1, 2, 3, 4]\n",
    "product = 1\n",
    "for num in numbers:\n",
    "    product = multiply(product, num)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "a6d62c7b-eb5c-4c26-9202-6b219b625b3e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Using reduce to achieve the same result\n",
    "\n",
    "product = reduce(multiply, numbers)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "5ae77ef5-a467-4c02-9d02-0f1c02fe9cd4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "24\n"
     ]
    }
   ],
   "source": [
    "print(product)  # Output: 24\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c78db6ac-beb1-454e-b74d-780e9607b1c8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
