{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "2235d172-a762-4e12-b0dd-113ed77b502f",
   "metadata": {},
   "source": [
    "# WAP that display current time and pause  for 2 sec and display current time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a8cfbd6d-d9ac-4814-9e2e-f2c5933f2b2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import time\n",
    "from datetime import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "df49691d-c0bc-426d-b6df-26e9355b2e4b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Current Time:10:55:12\n"
     ]
    }
   ],
   "source": [
    "def display_time():\n",
    "    current_time = datetime.now().strftime(\"%H:%M:%S\")\n",
    "    print(f\"Current Time:{current_time}\")\n",
    "    \n",
    "display_time()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "01d14cd5-ce46-4228-8b8c-627dc11a8b42",
   "metadata": {},
   "outputs": [],
   "source": [
    "time.sleep(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "1e253b76-1763-4f6f-a8ed-290a2d7f09f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Current Time:10:55:15\n"
     ]
    }
   ],
   "source": [
    "display_time()"
   ]
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
