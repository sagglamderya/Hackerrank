{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPZ7PhKAf9uJ+k6L4dukI/t"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "id": "oy_P166W1zW6"
      },
      "outputs": [],
      "source": [
        ""
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def is_leap(year):\n",
        "    leap = False\n",
        "    \n",
        "    if year%400==0:\n",
        "      leap= True  \n",
        "    elif  year%4==0:\n",
        "      if year%100!=0:\n",
        "        leap= True \n",
        "    return leap\n",
        "year=int(input())\n",
        "print(is_leap(year))"
      ],
      "metadata": {
        "id": "gbQ8sZdW10AA"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
