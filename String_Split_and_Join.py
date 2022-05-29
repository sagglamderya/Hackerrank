{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPJmJlkVmcYKSIoTQYFDhCe"
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
        "def split_and_join(line):\n",
        "    line=\"-\".join(line.split(\" \"))\n",
        "    return line\n",
        "if __name__ == '__main__':\n",
        "    line = input()\n",
        "    result = split_and_join(line)\n",
        "    print(result)"
      ],
      "metadata": {
        "id": "gbQ8sZdW10AA"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}