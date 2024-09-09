{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "62bbe1c8-25c1-424f-8962-dbb09e8eced2",
   "metadata": {},
   "outputs": [],
   "source": [
    " def modify_mutable(lst):\n",
    "      lst.append(4)\n",
    "      print(f\"Inside function: {lst}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8a283201-1647-439b-8829-b9a1bf2d7fc8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Inside function: [1, 2, 3, 4]\n",
      "Outside function: [1, 2, 3, 4]\n"
     ]
    }
   ],
   "source": [
    "  my_list = [1, 2, 3]\n",
    "  modify_mutable(my_list)\n",
    "  print(f\"Outside function: {my_list}\")  # Output: [1, 2, 3, 4] (modified)\n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "304a83fb-5d0e-43e6-bb3d-0c3867f06778",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "def square(x):\n",
    "\n",
    "    return x \n",
    "\n",
    "\n",
    "f = square\n",
    "print(f(5))  # Output: 25Passing a function as an argument\n",
    "\n",
    "\n",
    "def apply_function(func, value):\n",
    "    return func(value)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "77120902-c858-4fb6-acd4-149ff6d7c3be",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "result = apply_function(square, 4)\n",
    "print(result)  # Output: 16\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f24ae8a-a3e6-4f5c-a6d2-25a3cd56e300",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "83abc0ef-db50-4555-9ca3-1a6cf5a628d0",
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
