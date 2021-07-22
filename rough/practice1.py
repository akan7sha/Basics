{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "57fd4210",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "['A', 3]\n",
      "3\n",
      "4\n",
      "5\n",
      "['A', 3, 'B', 3]\n",
      "6\n",
      "7\n",
      "['A', 3, 'B', 3, 'A', 2]\n",
      "8\n",
      "9\n",
      "['A', 3, 'B', 3, 'A', 2, 'C', 2]\n",
      "10\n",
      "11\n",
      " i am in 1st if\n",
      "['A', 3, 'B', 3, 'A', 2, 'C', 2, 'D', 2]\n"
     ]
    }
   ],
   "source": [
    "def character_occurence(input_string):\n",
    "    count = 1\n",
    "    out_list = []\n",
    "    for i in range(0, len(input_string)):\n",
    "        print(i)\n",
    "        \n",
    "        if i == len(input_string)-1:\n",
    "            print(\" i am in 1st if\")\n",
    "            out_list.append(input_string[i])\n",
    "            out_list.append(count)\n",
    "            print(out_list)\n",
    "            break\n",
    "        elif input_string[i] != input_string[i+1]:\n",
    "            out_list.append(input_string[i])\n",
    "            out_list.append(count)\n",
    "            print(out_list)\n",
    "            count = 1\n",
    "        else:\n",
    "            count += 1\n",
    "\n",
    "character_occurence(\"AAABBBAACCDD\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "55bd8963",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "AAABBBAACCDD\n"
     ]
    }
   ],
   "source": [
    "s = \"AAABBBAACCDD\"\n",
    "print(s)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "a0ddcb07",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "for i in range (0, len(s)-1):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "980e0620",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
