{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "32e0e3f2-53df-4917-bc7d-52e359c16050",
   "metadata": {},
   "source": [
    "WAP to take sap id as a input from user and printing their email"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "393af342-4735-471c-bbfb-c2cf9701ed79",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter no of element : 7\n",
      "enter SAP ID : 789\n",
      "enter SAP ID : 789\n",
      "enter SAP ID : 9999\n",
      "enter SAP ID : 90987\n",
      "enter SAP ID : 9979\n",
      "enter SAP ID : 979\n",
      "enter SAP ID : 9876\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['789@stu.upes.ac.in', '789@stu.upes.ac.in', '9999@stu.upes.ac.in', '90987@stu.upes.ac.in', '9979@stu.upes.ac.in', '979@stu.upes.ac.in', '9876@stu.upes.ac.in']\n"
     ]
    }
   ],
   "source": [
    "def generate_emails_addresses(sap_ids):\n",
    "    emails = []\n",
    "    for sap_id in sap_ids:\n",
    "    \n",
    "        email = sap_id + \"@stu.upes.ac.in\"\n",
    "        emails.append(email)\n",
    "    return emails\n",
    "\n",
    "\n",
    "Sap=[]\n",
    "n=int(input(\"enter no of element :\"))\n",
    "for i in range(n):\n",
    "    id=input(\"enter SAP ID :\")\n",
    "    Sap.append(id)\n",
    "\n",
    "print(generate_emails_addresses(Sap))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e8811b59-896d-4751-99a6-86f5323dd656",
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
