{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPuq5/T43SpX1Zkb+Xdc9Yh"
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
      "execution_count": null,
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
        "def mutate_string(string, position, character):\n",
        "    s_new=s[:int(i)]+str(c)+s[int(i)+1:]\n",
        "    return s_new\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    s = input()\n",
        "    i, c = input().split()\n",
        "    s_new = mutate_string(s, int(i), c)\n",
        "    print(s_new)"
      ],
      "metadata": {
        "id": "gbQ8sZdW10AA"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}