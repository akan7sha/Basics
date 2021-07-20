{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "07724098",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "140708070909296\n",
      "140708108913840\n",
      "140708108913840\n",
      "kS\n"
     ]
    }
   ],
   "source": [
    "def occ_freq(input_string, index1,index2):\n",
    "     \n",
    "    a = input_string[index1]\n",
    "    print(id(a))\n",
    "    b = input_string[index2]\n",
    "    c = b.upper()\n",
    "    return a+c\n",
    "      \n",
    "a = occ_freq(\"Akansha\",1,4)\n",
    "z = a\n",
    "print(id(z))\n",
    "print(id(a))\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6441999e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "a1fc7bb6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "WILL YOU MARRY ME, OFFCOURSE I WILL, FOR THE NEXT SEVEN LIVES\n"
     ]
    }
   ],
   "source": [
    "sid = \"will you marry me, offcourse i will, for the next seven lives\"\n",
    "ak = sid.upper()\n",
    "print(ak)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "9aaea29e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n"
     ]
    }
   ],
   "source": [
    "sid = \"w\"\n",
    "a = sid.upper()\n",
    "print(type(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "6f3f80e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "aisa lgta h khatarnaak teacher\n"
     ]
    }
   ],
   "source": [
    "print(\"aisa lgta h khatarnaak teacher\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "f7692605",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'haa'"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"haa\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "1259799a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['helllo']\n"
     ]
    }
   ],
   "source": [
    "li = \"helllo\"\n",
    "c = li.split(',')\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c28d8737",
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
