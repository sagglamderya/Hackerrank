{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOa3LV0z/SOoU0fhDECNpQW"
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
        "n = int(input())\n",
        "list=[]\n",
        "for i in range(n):\n",
        "  list.append(i)\n",
        "list.append(n)\n",
        "list.remove(0)\n",
        "a=\"\"\n",
        "for i in list:\n",
        "  a=a+str(i)\n",
        "print(a)\n"
      ],
      "metadata": {
        "id": "gbQ8sZdW10AA"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}