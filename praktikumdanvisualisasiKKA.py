{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/reganpr/KKA/blob/main/praktikumdanvisualisasiKKA.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install -q kaggle\n",
        "from google.colab import files\n",
        "files.upload()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 90
        },
        "id": "mOl0TgPiyqco",
        "outputId": "22a1e4ef-eb7f-4702-e640-db1b4fc08a26"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-9bfccbc7-370f-43d4-99a5-21155071afcf\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-9bfccbc7-370f-43d4-99a5-21155071afcf\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving kaggle.json to kaggle.json\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'kaggle.json': b'{\"username\":\"regans57\",\"key\":\"6836682f2a0596ad5c52e11bc3940b85\"}'}"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!mkdir -p ~/.kaggle"
      ],
      "metadata": {
        "id": "Yj6SYl6MzQUl"
      },
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!cp kaggle.json ~/.kaggle/"
      ],
      "metadata": {
        "id": "WJJN7GS5zQN4"
      },
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!chmod 600 ~/.kaggle/kaggle.json"
      ],
      "metadata": {
        "id": "zybwfkPxzQHx"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns"
      ],
      "metadata": {
        "id": "2itx0udlzbUH"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv('data_praktikum_analisis_data.csv')\n",
        "print(df.head())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jYdhqMspzgFI",
        "outputId": "58b38fa0-fa35-4142-8442-123673805269"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   Order_ID  CustomerID  Order_Date Product_Category  Quantity  \\\n",
            "0      1001        5039  2023-08-19            Books         4   \n",
            "1      1002        5029  2023-08-29          Fashion         5   \n",
            "2      1003        5015  2023-02-21          Fashion         4   \n",
            "3      1004        5043  2023-04-06          Fashion         2   \n",
            "4      1005        5008  2023-08-10       Home Decor         2   \n",
            "\n",
            "   Price_Per_Unit  Ad_Budget  Total_Sales  \n",
            "0       1184000.0   982000.0    4736000.0  \n",
            "1       1733000.0  3513000.0    8665000.0  \n",
            "2       1767000.0  2117000.0    7068000.0  \n",
            "3        512000.0  4384000.0    1024000.0  \n",
            "4       1820000.0  2625000.0    3640000.0  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RSWQmSo7zyt0",
        "outputId": "550bbd81-342c-4dbe-c3e3-4e1126ff1149"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 150 entries, 0 to 149\n",
            "Data columns (total 8 columns):\n",
            " #   Column            Non-Null Count  Dtype  \n",
            "---  ------            --------------  -----  \n",
            " 0   Order_ID          150 non-null    int64  \n",
            " 1   CustomerID        150 non-null    int64  \n",
            " 2   Order_Date        150 non-null    object \n",
            " 3   Product_Category  150 non-null    object \n",
            " 4   Quantity          150 non-null    int64  \n",
            " 5   Price_Per_Unit    150 non-null    float64\n",
            " 6   Ad_Budget         150 non-null    float64\n",
            " 7   Total_Sales       143 non-null    float64\n",
            "dtypes: float64(3), int64(3), object(2)\n",
            "memory usage: 9.5+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 335
        },
        "id": "71HFcnREz1GG",
        "outputId": "6f051a62-f8a1-47e2-a1ea-bf11c07849d9"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Order_ID            0\n",
              "CustomerID          0\n",
              "Order_Date          0\n",
              "Product_Category    0\n",
              "Quantity            0\n",
              "Price_Per_Unit      0\n",
              "Ad_Budget           0\n",
              "Total_Sales         7\n",
              "dtype: int64"
            ],
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>0</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>Order_ID</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>CustomerID</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Order_Date</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Product_Category</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Quantity</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Price_Per_Unit</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Ad_Budget</th>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Total_Sales</th>\n",
              "      <td>7</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div><br><label><b>dtype:</b> int64</label>"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['Order_Date'] = pd.to_datetime(df['Order_Date'])"
      ],
      "metadata": {
        "id": "sifyHbu4z-ij"
      },
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df['Month'] = df['Order_Date'].dt.to_period('M').astype(str)"
      ],
      "metadata": {
        "id": "NrR8czDDz-e4"
      },
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "monthly_sales = df.groupby('Month')['Total_Sales'].sum()"
      ],
      "metadata": {
        "id": "RhIeVAOmz-bt"
      },
      "execution_count": 20,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(10,5))\n",
        "plt.plot(monthly_sales.index, monthly_sales.values, marker='o', color='b')\n",
        "plt.title('Tren Penjualan Bulanan')\n",
        "plt.xticks(rotation=45)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 504
        },
        "id": "8x8yeyJMz-Y-",
        "outputId": "3d2bb9b6-4b41-47c9-d2c5-0efce25a74bd"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x500 with 1 Axes>"
            ],
            "image/png": "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woULMWXKlAz73759G9999x3efvttHeESkYd58cUX8cMPP6Bv377YsGEDHn74YZjNZvz333/44YcfsHr1ajRo0MApsXh5eWHBggVo164datSogZdffhllypRBZGQkNmzYgMDAwNQT8bxo06YNypUrhz59+uDNN9+Et7c3vvjiCxQrVgxnz55N3a9JkyYIDg5Gr169MGjQIJhMJnzzzTc5Go7UoUMHzJw5E48//ji6deuGy5cvY968eahcuTL279+f5zbcac+ePfj2228ByIQB69atw7Jly9CkSRO0adMmdb9XXnkFffv2xTPPPIPWrVtj3759WL16NYoWLZrt769WrRoqVaqE4cOHIzIyEoGBgVi2bFme6kmcfYyIiIzCkEnLgQMHYDabUbVq1Qz3JyYmZjqv/IoVKxAbG5ttISoRkb14eXnhp59+wgcffICvv/4aK1asQIECBXDfffdh8ODBd713OVrz5s3xzz//YOLEiZg7dy5u3bqFkiVLonHjxnjttdfs8hy+vr5YsWIF+vfvjzFjxqBkyZIYMmQIgoODM8yuFhISgl9//RVvvPEG3nnnHQQHB6NHjx5o1aoV2rZtm+1ztGzZEp9//jmmTp2KIUOGoGLFipg2bRpOnz7tkBPyxYsXY/HixQAAHx8flCtXDm+++SbGjh0LL6+0gQj/+9//EBERgc8//xx//PEHmjZtijVr1qBVq1bZ/n5fX1/88ssvGDRoEMLDw+Hv74+nn34aAwcOzNCTYwtnHyMiIqMwKQNU45lMpgyzh33//ffo3r07Dh06dFcRYaFChVCyZMkM97Vq1QqBgYFYsWKFs0ImInJroaGhaNu2LRYsWKA7FCIiImP2tNSrVw9msxmXL1++Z41KREQENmzYgJUrVzopOiIi95acnIxr167dc/gTERGRs2hLWm7duoUTJ06kfh8REYG9e/eiSJEiqFq1Krp3746ePXvi/fffR7169XDlyhWsW7cOtWvXRocOHVIf98UXX6BUqVLZzkRGREQ5s3r1aixZsgQJCQn3HP5ERETkLNqGh23cuBEtWrS46/5evXrhyy+/RHJyMiZNmoSvv/4akZGRKFq0KB588EFMmDAhde58i8WC8uXLo2fPnpg8ebKzm0BE5HZatGiBEydOoF+/fhg1apTucIiIiAAYpKaFiIiIiIgoK4Zdp4WIiIiIiAhg0kJE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dYfkdIcPH8b//vc/TJs2DY888ojucJzu33//xVNPPYWFCxeidOnSusNxuv379+PJJ5/EE088gQkTJqBIkSK6Q3KqAwcOoGHDhkhKSkKTJk3QuHFj3SE51dGjR/Hhhx/i5MmTePjhh/H666971N/A6dOnsWbNGiQkJKBKlSpo166d7pCc6uTJk1i6dCliYmJQp04ddOjQAQULFtQdltMppWAymXSH4XTnzp3D+vXrcePGDdSuXRstW7Z0bgCKcuzQoUMqKChITZ48OfU+s9msMSLn2r9/v6pUqZJq0KCBKleunCpXrpz69ddfdYflNPv27VNly5ZVLVu2VE2aNFEmk0n9/PPPusNyupdfflmZTCZVqVIl9ffff+sOx6n27t2rChYsqAYPHqw7FC2OHz+uihUrpoYPH65u376tOxyn27t3r/L391c9e/ZUzZs3V++8845SynM+Bw4cOKCKFi2qnn32WdW/f3/l6+urwsPDdYflNPv371fFixdXLVq0UM2bN1deXl7qxRdfVNu3b9cdmlMcOHBAFS5cWDVr1kw98sgjytvbW3Xt2lX9+eefukNzmmvXrqVuWywWjZE43/79+1X58uVVkyZNVFhYmPL19VXfffedU2Ng0pJD586dU/Xq1VNVq1ZVRYoUyfBG7QkfWCdOnFBlypRRI0aMUDdu3FD79+9Xffv2Vc8884y6deuW2//zHj16VJUtW1aNHDlSJSYmquvXr6v27durefPm6Q7N6b744gs1YsQI1adPHxUSEqI2b96sOySnOHjwoAoICFBvv/22UkqplJQU9e+//6q//vpLHTx4UHN0zvHBBx+obt26KaWUSk5OVvPnz1cjRoxQH330kTp69Kjm6Bxrz549KiAgQI0ePVoppdSbb76pihUrpm7evKmUcv8TmBs3bqgHH3xQjRw5MvW+sWPHqmHDhqnk5GSNkTnH1atXVZ06dVJff6WU+v3335WXl5fq2LGjWr9+vcboHC8+Pl61b99eDRw4MPW+7du3q/r166vWrVurn376SWN0znHo0CHl4+OT4aKVu//fW506dUqVL19ejRgxQiUkJKjLly+rsWPHqgceeEBdvHjRacfBs8Y25ZLFYsGyZctQsWJFfPzxx3jrrbcQHh6OqVOnAkDqUDF3lZSUhHnz5qFJkyaYOHEiChcujFq1aqFhw4b4559/YLFY3Lqb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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "correlation = df[['Total_Sales', 'Ad_Budget']].corr()\n",
        "sns.heatmap(correlation, annot=True, cmap='coolwarm')\n",
        "plt.title('Peta Korelasi Antar Variabel')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 452
        },
        "id": "QLnZEStmz-V-",
        "outputId": "2b53ecb0-b655-41d2-eb49-99b6d353400b"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 2 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAgMAAAGzCAYAAACy+RS/AAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAASARJREFUeJzt3XdYFFfbBvB7QViQJkQBRRRFRFEiRpQgtijGKKIm9ljQRPw0mqioURJ7w1jxtccajRq70WiwYDe2YG9gwVgiKALSpO2e74+87ptdVt3VhQXn/l3XXBdz5szMM6zIw2kjE0IIEBERkWSZGDsAIiIiMi4mA0RERBLHZICIiEjimAwQERFJHJMBIiIiiWMyQEREJHFMBoiIiCSOyQAREZHEMRkgIiKSOCYDRBrc3NzQp0+fQrn26tWrIZPJcPfu3UK5vtQ1a9YMzZo10/u8u3fvQiaTYdasWQaL5fDhw5DJZDh8+LDBrklUWJgMvKNe/NJ5sVlYWKB69eoYPHgwEhMT9b7e+vXrERkZafA4mzVrhtq1axcoj46ORunSpfHBBx8gOTnZ4PctSb799lvIZDJ07dr1ra9VWJ+jNufOnYNMJsOYMWNeWufmzZuQyWQICwsrkpiISDsmA++4SZMmYe3atViwYAEaNmyIxYsXw9/fH1lZWXpdpyh/iRw8eBDBwcHw9PTEgQMH4ODgUCT3LQq9evXC8+fPUblyZZ3qCyGwYcMGuLm5YdeuXUhPT3+r+xfl5/jBBx+gRo0a2LBhwyvjAYCePXsa5J779u3Dvn37DHItIilhMvCOa926NXr27Il+/fph9erVGDp0KOLj4/Hrr78aOzStjhw5guDgYFSvXt1giYC+iU9hMjU1hYWFBWQymU71Dx8+jAcPHmDlypXIz8/Htm3bCjlC/eXn5yM3N1frsR49euDOnTs4deqU1uMbNmxAjRo18MEHH7xVDC8+Y3Nzc5ibm7/VtYikiMmAxDRv3hwAEB8fryr7+eefUa9ePVhaWsLBwQHdunXD/fv3VcebNWuG3bt346+//lJ1O7i5uQEAcnNzMW7cONSrVw92dnawsrJC48aNcejQIb1jO3bsGIKCglCtWjUcOHAA7733ntrxRYsWoVatWpDL5ahQoQIGDRqE1NRUtTovuh1iYmLQpEkTlC5dGt999x0AICcnB+PHj0e1atUgl8vh6uqKb7/9Fjk5Oa+MKzk5GSNGjIC3tzesra1ha2uL1q1b4+LFiwXqzp8/H7Vq1ULp0qVhb28PX19f1V+/gP5jBtatWwcvLy989NFHCAwMxLp16wrUedE3vWnTJkydOhUVK1aEhYUFWrRogVu3bql9b972c/x333pkZCTc3d0hl8tx7do1rfH36NEDANS+By/ExMQgNjZWVefXX39FUFAQKlSoALlcDnd3d0yePBkKhULtvFd9xppjBt7k3+fcuXNRuXJlWFpaomnTprhy5UqBOjdu3ECnTp3g4OAACwsL+Pr6YufOnS+9JlFxV8rYAVDRun37NgCoftFOnToVY8eORZcuXdCvXz88efIE8+fPR5MmTXD+/HmUKVMG33//PZ49e4YHDx5g7ty5AABra2sAQFpaGpYvX47u3bsjNDQU6enpWLFiBVq1aoUzZ87Ax8dHp7hOnDiBNm3aoEqVKoiOjkbZsmXVjk+YMAETJ05EYGAgBg4ciNjYWCxevBhnz57FiRMnYGZmpqr79OlTtG7dGt26dUPPnj3h5OQEpVKJdu3a4fjx4+jfvz9q1qyJy5cvY+7cuYiLi8OOHTteGtudO3ewY8cOdO7cGVWqVEFiYiKWLl2Kpk2b4tq1a6hQoQIAYNmyZfjmm2/QqVMnDBkyBNnZ2bh06RJOnz6Nzz//XKfvw7/l5ORg69atGD58OACge/fu6Nu3LxISEuDs7Fyg/vTp02FiYoIRI0bg2bNnmDFjBnr06IHTp08DgEE/x1WrViE7Oxv9+/eHXC5/aQtOlSpV0LBhQ2zatAlz586Fqamp6tiLBOHF92b16tWwtrZGWFgYrK2tcfDgQYwbNw5paWmYOXOm2nW1fcba6Ptca9asQXp6OgYNGoTs7GzMmzcPzZs3x+XLl1X3uHr1KgICAuDi4oLRo0fDysoKmzZtQocOHbB161Z8+umnWmMhKtYEvZNWrVolAIgDBw6IJ0+eiPv374tffvlFvPfee8LS0lI8ePBA3L17V5iamoqpU6eqnXv58mVRqlQptfKgoCBRuXLlAvfJz88XOTk5amUpKSnCyclJfPHFF6+Ns2nTpsLBwUHY2NiIWrVqicePHxeo8/jxY2Fubi4+/vhjoVAoVOULFiwQAMTKlSvVrgdALFmyRO0aa9euFSYmJuLYsWNq5UuWLBEAxIkTJ1RllStXFiEhIar97OxstfsKIUR8fLyQy+Vi0qRJqrL27duLWrVqvfJ5X3wu8fHxr6wnhBBbtmwRAMTNmzeFEEKkpaUJCwsLMXfuXLV6hw4dEgBEzZo11T6LefPmCQDi8uXLqrK3/Rzj4+MFAGFra6v1s9Jm4cKFAoDYu3evqkyhUAgXFxfh7++vKsvKyipw7v/93/+J0qVLi+zsbFXZyz7jF8eaNm36xs/14mfjhdOnTwsAYtiwYaqyFi1aCG9vb7WYlEqlaNiwofDw8FCVvfhcDh069LJvDVGxwW6Cd1xgYCDKlSsHV1dXdOvWDdbW1ti+fTtcXFywbds2KJVKdOnSBUlJSarN2dkZHh4eOjX1m5qaqvpolUolkpOTkZ+fD19fX5w7d06nGDMzM5Geng4nJyfY2toWOH7gwAHk5uZi6NChMDH53z/Z0NBQ2NraYvfu3Wr15XI5+vbtq1a2efNm1KxZEzVq1FB71hfdJq96VrlcrrqvQqHA06dPYW1tDU9PT7VnLFOmDB48eICzZ8/q9Nyvs27dOvj6+qJatWoAABsbGwQFBWntKgCAvn37qvWXN27cGMA/LRuvo+/n2LFjR5QrV06n5+jatSvMzMzUugqOHDmChw8fqroIAMDS0lL1dXp6OpKSktC4cWNkZWXhxo0batfU9hkb4rk6dOgAFxcX1X6DBg3g5+eHPXv2APiny+jgwYPo0qWLKsakpCQ8ffoUrVq1ws2bN/Hw4UOdvi9ExQm7Cd5xCxcuRPXq1VGqVCk4OTnB09NT9Yvt5s2bEELAw8ND67n/bnp/lZ9++gmzZ8/GjRs3kJeXpyqvUqWKTudXq1YNvXv3xqhRo9C9e3ds3rxZrTn5r7/+AgB4enqqnWdubo6qVauqjr/g4uJSYBDZzZs3cf369Zf+Anv8+PFL41MqlZg3bx4WLVqE+Ph4tT7sf49rGDVqFA4cOIAGDRqgWrVq+Pjjj/H5558jICDgNd+BglJTU7Fnzx4MHjxYrd8/ICAAW7duRVxcHKpXr652TqVKldT27e3tAQApKSk63VOfz1HXzxb453vUqlUrbN++HUuWLIGFhQXWr1+PUqVKoUuXLqp6V69exZgxY3Dw4EGkpaWpXePZs2dq+9o+Y0M8l7afherVq2PTpk0AgFu3bkEIgbFjx2Ls2LFa7/f48WO1hIKoJGAy8I5r0KABfH19tR5TKpWQyWT4/fff1X75vvCiP/lVfv75Z/Tp0wcdOnTAyJEj4ejoCFNTU0RERKjGJ+ji22+/xdOnTzFjxgyEhoZixYoVOo+41/TvvzBfUCqV8Pb2xpw5c7Se4+rq+tLrTZs2DWPHjsUXX3yByZMnw8HBASYmJhg6dCiUSqWqXs2aNREbG4vffvsNUVFR2Lp1KxYtWoRx48Zh4sSJej3D5s2bkZOTg9mzZ2P27NkFjq9bt67ANbV9hsA/0xNfR9/PUdv3+FV69uyJ3377Db/99hvatWuHrVu34uOPP1YlZ6mpqWjatClsbW0xadIkuLu7w8LCAufOncOoUaPUvs/63N9Q/z5feBHHiBEj0KpVK611XrTkEJUkTAYkzN3dHUIIVKlSpcBfmZpe9ot5y5YtqFq1KrZt26ZWZ/z48XrH88MPPyA5ORnLly+Hvb296pfgizn5sbGxqFq1qqp+bm4u4uPjERgY+Npru7u74+LFi2jRooXeScaWLVvw0UcfYcWKFWrlqampBQY6WllZoWvXrujatStyc3Px2WefYerUqQgPD4eFhYXO91y3bh1q166t9fu4dOlSrF+/Xu8EAyiaz1Gbdu3awcbGBuvXr4eZmRlSUlLUuggOHz6Mp0+fYtu2bWjSpImq/N+zXt6Evs918+bNAmVxcXGqWRcv/v2ZmZnp9O+OqKTgmAEJ++yzz2BqaoqJEycW+OtRCIGnT5+q9q2srAo01QL/+2v03+efPn0aJ0+efKOYli5dik6dOmHOnDmYMmUKgH/GPZibm+M///mP2n1WrFiBZ8+eISgo6LXX7dKlCx4+fIhly5YVOPb8+XNkZma+9FxTU9MC35/NmzcX6Bv+9/cL+Kcbw8vLC0IItebp17l//z6OHj2KLl26oFOnTgW2vn374tatW6pZAvooqs9Rk6WlJT799FPs2bMHixcvhpWVFdq3b//K++fm5mLRokVvdV99n2vHjh1qn+uZM2dw+vRptG7dGgDg6OiIZs2aYenSpXj06FGB8588efJW8RIZC1sGJMzd3R1TpkxBeHg47t69iw4dOsDGxgbx8fHYvn07+vfvjxEjRgAA6tWrh40bNyIsLAz169eHtbU1goOD0bZtW2zbtg2ffvopgoKCEB8fjyVLlsDLywsZGRl6x2RiYoJ169bh2bNnGDt2LBwcHPDVV18hPDwcEydOxCeffIJ27dohNjYWixYtQv369XVava5Xr17YtGkTBgwYgEOHDiEgIAAKhQI3btzApk2bsHfv3pd2p7Rt2xaTJk1C37590bBhQ1y+fBnr1q1Ta6UAgI8//hjOzs4ICAiAk5MTrl+/jgULFiAoKAg2NjY6fw/Wr18PIQTatWun9XibNm1QqlQprFu3Dn5+fjpfFyi6z1Gbnj17Ys2aNdi7dy969OgBKysr1bGGDRvC3t4eISEh+OabbyCTybB27VqdujheRd/nqlatGho1aoSBAwciJycHkZGReO+99/Dtt9+q6ixcuBCNGjWCt7c3QkNDUbVqVSQmJuLkyZN48OCB1vUniIo9I8xgoCLwYgrb2bNnX1t369atolGjRsLKykpYWVmJGjVqiEGDBonY2FhVnYyMDPH555+LMmXKCACq6WlKpVJMmzZNVK5cWcjlclG3bl3x22+/iZCQEK1T2DQ1bdpU63S8jIwM8eGHHwoTExOxbt06IcQ/Uwlr1KghzMzMhJOTkxg4cKBISUnR6XpCCJGbmyt++OEHUatWLSGXy4W9vb2oV6+emDhxonj27JmqnraphcOHDxfly5cXlpaWIiAgQJw8ebLANLalS5eKJk2aiPfee0/I5XLh7u4uRo4cqXZtXaYWent7i0qVKr3iuyZEs2bNhKOjo8jLy1NNYdu8ebNanRfT5VatWqUqe9vP8cU1Z86c+cr4tMnPzxfly5cXAMSePXsKHD9x4oT48MMPhaWlpahQoYL49ttvxd69ewtMz3vVZ6z5mbzJc82ePVu4uroKuVwuGjduLC5evFjgPrdv3xa9e/cWzs7OwszMTLi4uIi2bduKLVu2qOpwaiGVJDIh3jL1JiIiohKNYwaIiIgkjskAERGRxDEZICIikjgmA0RERMXE0aNHERwcjAoVKkAmk73yJWovHD58GB988AHkcjmqVauG1atX631fJgNERETFRGZmJurUqYOFCxfqVD8+Ph5BQUH46KOPcOHCBQwdOhT9+vXD3r179bovZxMQEREVQzKZDNu3b0eHDh1eWmfUqFHYvXs3rly5oirr1q0bUlNTERUVpfO92DJARERUiHJycpCWlqa25eTkGOTaJ0+eLLA0dqtWrfRePbTYrEC428zz9ZWIJCbikx+NHQJRsXR8V9NCvb4hfyed/b57gXeJjB8/HhMmTHjrayckJMDJyUmtzMnJCWlpaXj+/LnOL/UqNskAERFRcSEze7O3pmoTHh6OsLAwtTK5XG6w6xsCkwEiIiINJqUMlwzI5fJC++Xv7OyMxMREtbLExETY2trq9apxjhkgIiIqofz9/REdHa1Wtn//fvj7++t1HbYMEBERaZCZGedv5YyMDNy6dUu1Hx8fjwsXLsDBwQGVKlVCeHg4Hj58iDVr1gAABgwYgAULFuDbb7/FF198gYMHD2LTpk3YvXu3XvdlMkBERKTBkN0E+vjzzz/x0UcfqfZfjDUICQnB6tWr8ejRI9y7d091vEqVKti9ezeGDRuGefPmoWLFili+fDlatWql132ZDBARERUTzZo1w6uW/9G2umCzZs1w/vz5t7ovkwEiIiINhpxNUBIwGSAiItJgrG4CY+FsAiIiIoljywAREZEGdhMQERFJHLsJiIiISFLYMkBERKRBZiqtlgEmA0RERBpMmAwQERFJm8xEWskAxwwQERFJHFsGiIiINMhMpfW3MpMBIiIiDVIbMyCt1IeIiIgKYMsAERGRBqkNIGQyQEREpIHdBERERCQpbBkgIiLSwBUIiYiIJE5mIq2Gc2k9LRERERXAlgEiIiINnE1AREQkcVKbTcBkgIiISIPUWgY4ZoCIiEji2DJARESkQWqzCZgMEBERaWA3AREREUkKWwaIiIg0cDYBERGRxLGbgIiIiCSFLQNEREQaOJuAiIhI4thNQERERJLClgEiIiINUmsZYDJARESkgckAERGRxEltAKG0npaIiIgKYMsAERGRBq5ASEREJHFSGzPAbgIiIiKJY8sAERGRBqkNIGQyQEREpIHdBERERCQpbBkgIiLSILWWASYDREREGqQ2ZkBaT0tEREQFsGWAiIhIA7sJiIiIJE5q3QRMBoiIiDTJpNUyIK3Uh4iIiArQOxmIiorC8ePHVfsLFy6Ej48PPv/8c6SkpBg0OCIiImOQmcgMtpUEeicDI0eORFpaGgDg8uXLGD58ONq0aYP4+HiEhYUZPEAiIqKiJjMxMdhWEug9ZiA+Ph5eXl4AgK1bt6Jt27aYNm0azp07hzZt2hg8QCIiIipceqcs5ubmyMrKAgAcOHAAH3/8MQDAwcFB1WJARERUkkmtm0DvloFGjRohLCwMAQEBOHPmDDZu3AgAiIuLQ8WKFQ0eIBERUVErKc37hqL30y5YsAClSpXCli1bsHjxYri4uAAAfv/9d3zyyScGD5CIiIgKl94tA5UqVcJvv/1WoHzu3LkGCYiIiMjYSkrzvqG8UTvI7du3MWbMGHTv3h2PHz8G8E/LwNWrVw0aHBERkTFIbcyA3snAkSNH4O3tjdOnT2Pbtm3IyMgAAFy8eBHjx483eIBERERUuPROBkaPHo0pU6Zg//79MDc3V5U3b94cp06dMmhwRERERmFiYritBNB7zMDly5exfv36AuWOjo5ISkoySFBERETGJOO7CV6tTJkyePToUYHy8+fPq2YWEBERlWRSW4FQ7yi7deuGUaNGISEhATKZDEqlEidOnMCIESPQu3fvwoiRiIiICpHeycC0adNQo0YNuLq6IiMjA15eXmjSpAkaNmyIMWPGFEaMRERERUpqswn0HjNgbm6OZcuWYezYsbhy5QoyMjJQt25deHh4FEZ8RERERa+ENO8bit7JwAuVKlVCpUqVDBkLERERGYFOyYA+ryaeM2fOGwdDRERUHJSU5n1D0SkZOH/+vE4Xk9pUDCIiejfJZOwmKODQoUOFHQcRERH918KFCzFz5kwkJCSgTp06mD9/Pho0aPDS+pGRkVi8eDHu3buHsmXLolOnToiIiICFhYVO93vjMQNERETvLCN2E2zcuBFhYWFYsmQJ/Pz8EBkZiVatWiE2NhaOjo4F6q9fvx6jR4/GypUr0bBhQ8TFxaFPnz6QyWQ6d92/UTLw559/YtOmTbh37x5yc3PVjm3btu1NLklERFRsGHOxoDlz5iA0NBR9+/YFACxZsgS7d+/GypUrMXr06AL1//jjDwQEBODzzz8HALi5uaF79+44ffq0zvfU+2l/+eUXNGzYENevX8f27duRl5eHq1ev4uDBg7Czs9P3ckRERMWOIdcZyMnJQVpamtqWk5Oj9b65ubmIiYlBYGCgqszExASBgYE4efKk1nMaNmyImJgYnDlzBgBw584d7NmzB23atNH5ed9o0aG5c+di165dMDc3x7x583Djxg106dKFUw2JiIg0REREwM7OTm2LiIjQWjcpKQkKhQJOTk5q5U5OTkhISNB6zueff45JkyahUaNGMDMzg7u7O5o1a4bvvvtO5xj1TgZu376NoKAgAP8sQJSZmQmZTIZhw4bhxx9/1PdyRERExY/MxGBbeHg4nj17praFh4cbLNTDhw9j2rRpWLRoEc6dO4dt27Zh9+7dmDx5ss7X0HvMgL29PdLT0wEALi4uuHLlCry9vZGamoqsrCx9L0dERFTsGHKdAblcDrlcrlPdsmXLwtTUFImJiWrliYmJcHZ21nrO2LFj0atXL/Tr1w8A4O3tjczMTPTv3x/ff/89THQY/6B3y0CTJk2wf/9+AEDnzp0xZMgQhIaGonv37mjRooW+lyMiIqL/Mjc3R7169RAdHa0qUyqViI6Ohr+/v9ZzsrKyCvzCNzU1BQAIIXS6r94tAwsWLEB2djYA4Pvvv4eZmRn++OMPdOzYkS8qIiKid4MRZxOEhYUhJCQEvr6+aNCgASIjI5GZmamaXdC7d2+4uLioxh0EBwdjzpw5qFu3Lvz8/HDr1i2MHTsWwcHBqqTgdfROBhwcHFRfm5iYaJ3mQEREVJIZc0Xdrl274smTJxg3bhwSEhLg4+ODqKgo1aDCe/fuqbUEjBkzBjKZDGPGjMHDhw9Rrlw5BAcHY+rUqTrfUyZ0bEPIz8+HQqFQ6/dITEzEkiVLkJmZiXbt2qFRo0Y631jTbjPPNz6X6F0V8QkH5RJpc3xX00K9fvq84Qa7ls2Q2Qa7VmHRuWUgNDQU5ubmWLp0KQAgPT0d9evXR3Z2NsqXL4+5c+fi119/1WteIxERUbEksVcY6/y0J06cQMeOHVX7a9asgUKhwM2bN3Hx4kWEhYVh5syZhRIkERFRUTLkokMlgc4tAw8fPoSHh4dqPzo6Gh07dlStOhgSEoJVq1YZPkIqEg6NfFF1+Jew+6A2LCo44s+OXyFxZ/TrTyQqIT5rUwHdP3OFg705bsdnYO7SW7h+M/2l9T8KKIt+PavA2dECD/7OwuLV8TgVk6w6/t1QT7RpoT7V63RMMoZPuKza37zcD+Wd1F8Us+SnO/h5y30DPRWRYeicDFhYWOD58+eq/VOnTqm1BFhYWCAjI8Ow0VGRMbUqjbRLsbi/eit8tyw0djhEBtW8UTkM7ueOWQvjcC0uHV3auWDOJG90H3AWqc/yCtSvXcMW40d6YelPd/DH2WS0bOqIiO9r4YuhMYi/97/1VE7FJGNa5A3Vfl5ewSFYy36Ox669j1T7Wc8VBn46KhQSe4Wxzk/r4+ODtWvXAgCOHTuGxMRENG/eXHX89u3bqFChguEjpCLxZO9RxI2PROKvB4wdCpHBdetQEbv2PsKe6ETcvZ+FmYtuIjtHibYttS/i0rmdC06fS8aG7Q/w14MsLF93F3G3M9CxrYtavdw8JZJT81RbemZ+gWtlPVeo1cnOURbKM5KBmcgMt5UAOrcMjBs3Dq1bt8amTZvw6NEj9OnTB+XLl1cd3759OwICAgolSCKiN1WqlAzVq9lg7ZZ7qjIhgD8vpKCWp63Wc2rXsMUvOx6olZ0+n4wmH5ZVK6tbuwx2rfVHekY+Yi6lYtnP8UhLV08IenaqhD5dKyPxSTb2H3mMTb8+gIL5QLEnk1jLgM7JQNOmTRETE4N9+/bB2dkZnTt3Vjvu4+ODBg0a6HStnJycAm9syhNKmEnsm09Ehc/O1gylTGVITlHvDkhOzUPliqW1nuNQxhwpqeqvZ09JzYNDGXPV/umYZBz5IwmPErPhUt4C/XtVwawJ3hgw8jyU//1lv2XXQ8TdTkdaRj5q17DFgJAqeM9BjgUrbhv2IYnekl6LDtWsWRM1a9bUeqx///5q+0FBQVi+fLla68ELERERmDhxolpZd5kDepiWLVCXiKg4ij72RPX1nb8ycTs+E5uW+6Fu7TKIuZQKANj46/9aF27fzUR+vsDIQR5Y+tMd5OXrtkwsGUkJad43lEL7U/zo0aNqAw7/TdsbnLqYOGitS0T0Np6l5SFfIeBgb6ZW7lDGDE9TcrWek5yaC/t/tQIAgH0ZMySnaq8PAH8nZiPlWS4qVrB8aZ1rcWkoVcoEzhozDKj4kZmYGGwrCYwSpVwuh62trdrGLgIiKgz5+QJxt9JR7317VZlMBtSrY4+rsWlaz7lyIw2+dezVyur72OPKDe31AaDce+awszFDUvLLE4ZqVayhUAikphacwUBkTHq/m4DeTaZWpWFVrZJqv3SVirCtUwO5yc+Qff/RK84kKv5+2fEA3w+rgRu30nE9Lh1d2rvA0sIEuw8kAADGDPPEk6e5WLomHgCweedDLIiog24dKuKPP58isLEjalSzwYwFcQAASwsT9O3uhiN/PMHTlFy4OFviq75V8fDRc5w5989aBLU8beHlaYPzl1KR9VyBWjVs8U0/d+w7nKh11gEVM0Z8N4ExMBkgAIBdvdrwj16r2vea9R0A4P6abbj0ZbixwiIyiIPHn6CMnRn69XCDg705bt3JwPDxl5Hy37/QncpZQPmvLvwrN9IwcdZ1hPasgv69q+DB388RPvWqao0BhRJwd7NC6+ZOsLYqhaTkXJw9n4xl6+6qxgLk5SsR2NgRX3R3g7mZDH8nZmPjrw+wUWOWAhVTJaR531B0flGRvmxsbHDx4kVUrVpVp/p8URFRQXxREZF2hf2ioqzVE19fSUel+4w32LUKC1sGiIiINLGbwDC+++47ODhwhgAREZU8JWUWgKHolAzs3LlT5wu2a9cOwD/TB4mIiKj40ykZ6NChg04Xk8lkUCj4Eg4iIirhJDbdXadkQKnkQtpERCQhEluBkAMIiYiINPBFRTrIzMzEkSNHcO/ePeTmqq+29c033xgkMCIiIioaeicD58+fR5s2bZCVlYXMzEw4ODggKSkJpUuXhqOjI5MBIiIq+STWTaB3O8iwYcMQHByMlJQUWFpa4tSpU/jrr79Qr149zJo1qzBiJCIiKloyE8NtJYDeUV64cAHDhw+HiYkJTE1NkZOTA1dXV8yYMQPfffddYcRIREREhUjvZMDMzAwm/12MwdHREffu3QMA2NnZ4f79+4aNjoiIyBhkMsNtJYDeYwbq1q2Ls2fPwsPDA02bNsW4ceOQlJSEtWvXonbt2oURIxERUdGS2AqEej/ttGnTUL58eQDA1KlTYW9vj4EDB+LJkydYunSpwQMkIiKiwqV3y4Cvr6/qa0dHR0RFRRk0ICIiIqMrIQP/DEXvp23evDlSU1MLlKelpaF58+aGiImIiMi4TGSG20oAvZOBw4cPF1hoCACys7Nx7NgxgwRFRERERUfnboJLly6pvr527RoSEhJU+wqFAlFRUXBxcTFsdERERMYgsW4CnZMBHx8fyGQyyGQyrd0BlpaWmD9/vkGDIyIiMooSMiXQUHROBuLj4yGEQNWqVXHmzBmUK1dOdczc3ByOjo4wNTUtlCCJiIiKlMSmFuqcDFSuXBkAX2dMRET0rnmjtxbevn0bkZGRuH79OgDAy8sLQ4YMgbu7u0GDIyIiMgqJdRPo3Q6yd+9eeHl54cyZM3j//ffx/vvv4/Tp06hVqxb2799fGDESEREVLYm9qEjvloHRo0dj2LBhmD59eoHyUaNGoWXLlgYLjoiIiAqf3inL9evX8eWXXxYo/+KLL3Dt2jWDBEVERGRUJiaG20oAvaMsV64cLly4UKD8woULcHR0NERMRERExsW3Fmo3adIkjBgxAqGhoejfvz/u3LmDhg0bAgBOnDiBH374AWFhYYUWKBERERUOnZOBiRMnYsCAARg7dixsbGwwe/ZshIeHAwAqVKiACRMm4Jtvvim0QImIiIpMCRn4Zyg6JwNCCACATCbDsGHDMGzYMKSnpwMAbGxsCic6IiIiYyghzfuGotdsApnGN4dJABERUcmnVzJQvXr1AgmBpuTk5LcKiIiIyOhKyCwAQ9ErGZg4cSLs7OwKKxYiIqJiQbCb4OW6devG6YNERPTuk9gAQp2f9nXdA0RERFQy6T2bgIiI6J0nsZYBnZMBvrqYiIikQmpjBqSV+hAREVEBer+1kIiI6J3HbgIiIiKJYzcBERERSQlbBoiIiDRxBUIiIiJp42wCIiIikhS2DBAREWnibAIiIiJpE0wGiIiIJI5jBoiIiEhK2DJARESkgd0EREREUsduAiIiIpIStgwQERFpYjcBERGRtHEFQiIiIpIUtgwQERFpYjcBERGRtAmwm4CIiIiMaOHChXBzc4OFhQX8/Pxw5syZV9ZPTU3FoEGDUL58ecjlclSvXh179uzR+X5sGSAiItJgzEWHNm7ciLCwMCxZsgR+fn6IjIxEq1atEBsbC0dHxwL1c3Nz0bJlSzg6OmLLli1wcXHBX3/9hTJlyuh8TyYDREREmoyYDMyZMwehoaHo27cvAGDJkiXYvXs3Vq5cidGjRxeov3LlSiQnJ+OPP/6AmZkZAMDNzU2ve7KbgIiISIOQyQy25eTkIC0tTW3LycnRet/c3FzExMQgMDBQVWZiYoLAwECcPHlS6zk7d+6Ev78/Bg0aBCcnJ9SuXRvTpk2DQqHQ+XmZDBARERWiiIgI2NnZqW0RERFa6yYlJUGhUMDJyUmt3MnJCQkJCVrPuXPnDrZs2QKFQoE9e/Zg7NixmD17NqZMmaJzjOwmICIi0mDIMQPh4eEICwtTK5PL5Qa7vlKphKOjI3788UeYmpqiXr16ePjwIWbOnInx48frdA0mA0RERJoMuAKhXC7X+Zd/2bJlYWpqisTERLXyxMREODs7az2nfPnyMDMzg6mpqaqsZs2aSEhIQG5uLszNzV97X3YTEBERFRPm5uaoV68eoqOjVWVKpRLR0dHw9/fXek5AQABu3boFpVKpKouLi0P58uV1SgQAJgNEREQFCJmJwTZ9hYWFYdmyZfjpp59w/fp1DBw4EJmZmarZBb1790Z4eLiq/sCBA5GcnIwhQ4YgLi4Ou3fvxrRp0zBo0CCd78luAiIiIg3GXIGwa9euePLkCcaNG4eEhAT4+PggKipKNajw3r17MDH5X5Lh6uqKvXv3YtiwYXj//ffh4uKCIUOGYNSoUTrfUyaEEAZ/kjew28zT2CEQFTsRn/xo7BCIiqXju5oW6vWTrmifxvcmytbW3rxfnLBlgIiISIMxVyA0BiYDREREmgw4m6AkkFbqQ0RERAWwZYCIiEiDkNjfykwGiIiINAiJdRMwGSAiItIgtQGE0npaIiIiKoAtA0RERBqMueiQMTAZICIi0sBuAiIiIpIUtgwQERFp4GwCIiIiiZPamAF2ExAREUkcWwaIiIg0SG0AIZMBIiIiDewmICIiIklhywAREZEGdhMQERFJnNS6CZgMEBERaZBay4C0npaIiIgKYMsAERGRBnYTGEnEJz8aOwSiYic8qr+xQyAqpmIL9epSW46Y3QREREQSV2xaBoiIiIoLIaTVMsBkgIiISIOQWMO5tJ6WiIiICmDLABERkQbOJiAiIpI4qSUD7CYgIiKSOLYMEBERaZBaywCTASIiIg1MBoiIiCROausMcMwAERGRxLFlgIiISAO7CYiIiCROaskAuwmIiIgkji0DREREGqTWMsBkgIiISANnExAREZGksGWAiIhIg5LdBERERNImtTED7CYgIiKSOLYMEBERaZDaAEImA0RERBqk1k3AZICIiEiD1FoGOGaAiIhI4tgyQEREpIHdBERERBLHbgIiIiKSFLYMEBERaVAaO4AixmSAiIhIA7sJiIiISFLYMkBERKSBswmIiIgkjt0EREREJClsGSAiItLAbgIiIiKJUwpjR1C0mAwQERFpkFrLAMcMEBERSRxbBoiIiDRIbTYBkwEiIiINQmJjBthNQEREJHFsGSAiItKglNgAQiYDREREGqQ2ZoDdBERERBLHlgEiIiINUhtAyGSAiIhIAxcdIiIiIqNauHAh3NzcYGFhAT8/P5w5c0an83755RfIZDJ06NBBr/sxGSAiItKgFIbb9LVx40aEhYVh/PjxOHfuHOrUqYNWrVrh8ePHrzzv7t27GDFiBBo3bqz3PZkMEBERaRBCZrBNX3PmzEFoaCj69u0LLy8vLFmyBKVLl8bKlStfeo5CoUCPHj0wceJEVK1aVe97MhkgIiLSIIThtpycHKSlpaltOTk5Wu+bm5uLmJgYBAYGqspMTEwQGBiIkydPvjTeSZMmwdHREV9++eUbPS+TASIiokIUEREBOzs7tS0iIkJr3aSkJCgUCjg5OamVOzk5ISEhQes5x48fx4oVK7Bs2bI3jpGzCYiIiDQYcgXC8PBwhIWFqZXJ5XKDXDs9PR29evXCsmXLULZs2Te+DpMBIiIiDYZcZ0Aul+v8y79s2bIwNTVFYmKiWnliYiKcnZ0L1L99+zbu3r2L4OBgVZlSqQQAlCpVCrGxsXB3d3/tfdlNQEREVEyYm5ujXr16iI6OVpUplUpER0fD39+/QP0aNWrg8uXLuHDhgmpr164dPvroI1y4cAGurq463ZctA0RERBqM+W6CsLAwhISEwNfXFw0aNEBkZCQyMzPRt29fAEDv3r3h4uKCiIgIWFhYoHbt2mrnlylTBgAKlL8KkwEiIiINb7I+gKF07doVT548wbhx45CQkAAfHx9ERUWpBhXeu3cPJiaGbdiXCVE8VmBuFHzE2CEQFTvhUf2NHQJRsRSUF1uo199xVmGwa3Wob2qwaxUWtgwQERFpKB5/JhcdvdsZqlatiqdPnxYoT01NfaNVj4iIiIobAZnBtpJA72Tg7t27UCgKNp/k5OTg4cOHBgmKiIiIio7O3QQ7d+5Ufb13717Y2dmp9hUKBaKjo+Hm5mbQ4IiIiIzBmAMIjUHnZODF6xBlMhlCQkLUjpmZmcHNzQ2zZ882aHBERETGILUxAzonAy9WNKpSpQrOnj37VsseEhERFWdMBl4jPj5e9XV2djYsLCwMGhAREREVLb0HECqVSkyePBkuLi6wtrbGnTt3AABjx47FihUrDB4gERFRUVMKmcG2kkDvZGDKlClYvXo1ZsyYAXNzc1V57dq1sXz5coMGR0REZAxCGG4rCfROBtasWYMff/wRPXr0gKnp/1ZVqlOnDm7cuGHQ4IiIiKjw6T1m4OHDh6hWrVqBcqVSiby8PIMERUREZEwl5S96Q9G7ZcDLywvHjh0rUL5lyxbUrVvXIEEREREZk1IYbisJ9G4ZGDduHEJCQvDw4UMolUps27YNsbGxWLNmDX777bfCiJGIiIgKkd4tA+3bt8euXbtw4MABWFlZYdy4cbh+/Tp27dqFli1bFkaMRERERUoImcG2kuCN3lrYuHFj7N+/39CxEBERFQscM0BERESSonfLgL29PWSygs0eMpkMFhYWqFatGvr06YO+ffsaJEAiIqKiVlIG/hnKGw0gnDp1Klq3bo0GDRoAAM6cOYOoqCgMGjQI8fHxGDhwIPLz8xEaGmrwgImIiAqb1LoJ9E4Gjh8/jilTpmDAgAFq5UuXLsW+ffuwdetWvP/++/jPf/7DZICIiEokqSUDeo8Z2Lt3LwIDAwuUt2jRAnv37gUAtGnTRvXOAiIiIire9E4GHBwcsGvXrgLlu3btgoODAwAgMzMTNjY2bx8dERGREXDRodcYO3YsBg4ciEOHDqnGDJw9exZ79uzBkiVLAAD79+9H06ZNDRspERFREZFaN4HeyUBoaCi8vLywYMECbNu2DQDg6emJI0eOoGHDhgCA4cOHGzZKIiIiKjRvtOhQQEAAAgICDB0LERFRsaBUGjuCoqVTMpCWlqbzBW1tbd84GCIiouKA3QRalClTRutCQ9ooFIq3CoiIiIiKlk7JwKFDh1Rf3717F6NHj0afPn3g7+8PADh58iR++uknREREFE6URERERYgtA1r8e2bApEmTMGfOHHTv3l1V1q5dO3h7e+PHH39ESEiI4aMkIiIqQiVlSqCh6L3OwMmTJ+Hr61ug3NfXF2fOnDFIUERERFR09E4GXF1dsWzZsgLly5cvh6urq0GCIiIiMiYhhMG2kkDvqYVz585Fx44d8fvvv8PPzw/APy8qunnzJrZu3WrwAImIiIpaCfkdbjB6JwNt2rRBXFwcFi9ejBs3bgAAgoODMWDAALYMFAOftamA7p+5wsHeHLfjMzB36S1cv5n+0vofBZRFv55V4OxogQd/Z2Hx6niciklWHf9uqCfatHBWO+d0TDKGT7is2t+83A/lnSzU6iz56Q5+3nLfQE9FZDwOjXxRdfiXsPugNiwqOOLPjl8hcWe0scOiQsZ1BnTg6uqKadOmGToWekvNG5XD4H7umLUwDtfi0tGlnQvmTPJG9wFnkfosr0D92jVsMX6kF5b+dAd/nE1Gy6aOiPi+Fr4YGoP4e1mqeqdikjEt8oZqPy+vYMq87Od47Nr7SLWf9ZxTTOndYGpVGmmXYnF/9Vb4bllo7HCICoXeycDRo0dfebxJkyZvHAy9nW4dKmLX3kfYE50IAJi56Cb867+Hti2dtf6V3rmdC06fS8aG7Q8AAMvX3UV9H3t0bOuCWYtuqurl5imRnFowmfi3rOeK19YhKome7D2KJ3tf/f8evXvYTfAazZo1K1D27wWJuOiQcZQqJUP1ajZYu+WeqkwI4M8LKajlqX1VyNo1bPHLjgdqZafPJ6PJh2XVyurWLoNda/2RnpGPmEupWPZzPNLS89Xq9OxUCX26Vkbik2zsP/IYm359AIXEmtmI6N0htamFeicDKSkpavt5eXk4f/48xo4di6lTp+p0jZycHOTk5KiVKRW5MDE11zcc+i87WzOUMpUhOUX9r/Pk1DxUrlha6zkOZcyRkpqrVpaSmgeHMv/7HE7HJOPIH0l4lJgNl/IW6N+rCmZN8MaAkedVfWpbdj1E3O10pGXko3YNWwwIqYL3HORYsOK2YR+SiIgKhd7JgJ2dXYGyli1bwtzcHGFhYYiJiXntNSIiIjBx4kS1MlePEFTy7KtvOFTIoo89UX19569M3I7PxKblfqhbuwxiLqUCADb++r/Whdt3M5GfLzBykAeW/nQHefkSS6+J6J0gtW4CvdcZeBknJyfExsbqVDc8PBzPnj1T2ypW62GoUCTpWVoe8hUCDvZmauUOZczwNCVX6znJqbmwL6PeGmNfxgzJqdrrA8DfidlIeZaLihUsX1rnWlwaSpUygbPGDAMiopJCKIXBtpJA75aBS5cuqe0LIfDo0SNMnz4dPj4+Ol1DLpdDLperlbGL4O3k5wvE3UpHvfftcezUUwCATAbUq2OPbbsfaj3nyo00+Naxx+ad/zte38ceV268/C2V5d4zh52NGZKSX54wVKtiDYVCIJUDComISgS9kwEfHx/IZLICqyp9+OGHWLlypcECI/39suMBvh9WAzdupeN6XDq6tHeBpYUJdh9IAACMGeaJJ09zsXRNPABg886HWBBRB906VMQffz5FYGNH1KhmgxkL4gAAlhYm6NvdDUf+eIKnKblwcbbEV32r4uGj5zhz7p+1CGp52sLL0wbnL6Ui67kCtWrY4pt+7th3OBHpmfnaAyUqQUytSsOqWiXVfukqFWFbpwZyk58h+/6jV5xJJVkJ+YPeYPROBuLj49X2TUxMUK5cOVhYsEnY2A4ef4Iydmbo18MNDvbmuHUnA8PHX0bKf/9CdypnofYP/MqNNEycdR2hPaugf+8qePD3c4RPvapaY0ChBNzdrNC6uROsrUohKTkXZ88nY9m6u6qxAHn5SgQ2dsQX3d1gbibD34nZ2PjrA2zUmKVAVFLZ1asN/+i1qn2vWd8BAO6v2YZLX4YbKywqZFIbMyATxWTh5EbBR4wdAlGxEx7V39ghEBVLQXm6jVF7Uz9sMdzc6FGdDDY8r9DoFWF6ejpiYmKQkZEBADh37hx69+6Nzp07Y926dYUSIBERUVFTKoXBtpJA526Co0ePom3btsjIyIC9vT02bNiATp06wcXFBaampti2bRuysrIQGhpamPESEREVuuLRZl50dG4ZGDNmDDp37oz79+9j6NCh6Nq1KwYPHozr16/jypUrmDhxIhYu5LrdRERU8glhuK0k0DkZuHTpEkaOHAkXFxeMGjUKaWlp6Nq1q+p4t27dcPs2V5wjIiIqaXTuJkhLS4ODgwMAwNzcHKVLl4aNjY3quI2NDbKysl52OhERUYmhLCl/0huIzsmATCZTeyGR5j4REdG7QkjsRWs6JwNCCLRo0QKlSv1zSlZWFoKDg2Fu/s/Kgfn5XGCGiIioJNI5GRg/frzafvv27QvU6dix49tHREREZGTFZAmeIvPGycDrnDhxAr6+vgXeQUBERFTcKSXWTVBoyyK1bt0aDx9qf0EOERERFR96v5tAV1JrYiEioneH1H6HFVoyQEREVFKVkFWEDab4vz2BiIiIChVbBoiIiDQIiTUNFFoywAWJiIiopJLYkAEOICQiItJUUl49bCiFlgykp6cX1qWJiIjIgHRKBurWratzs/+5c+feKiAiIiJjk1rrtk7JQIcOHVRfZ2dnY9GiRfDy8oK/vz8A4NSpU7h69Sq++uqrQgmSiIioKPFFRVr8eynifv364ZtvvsHkyZML1Ll//75hoyMiIqJCp/c6A5s3b0bv3r0LlPfs2RNbt241SFBERETGpBTCYFtJoHcyYGlpiRMnThQoP3HiBCwsLAwSFBERkTEJIQy2lQR6zyYYOnQoBg4ciHPnzqFBgwYAgNOnT2PFihUYN26cwQMkIiKiwqV3MjB69GhUrVoV8+bNw88//wwA8PLywk8//YSaNWsaPEAiIqKixnUGdNClSxd06dIFAJCWloYNGzZg5syZiImJgUKhMGiARERERa2EtO4bzBu/qOjo0aMICQlBhQoVMHv2bDRv3hynTp0yZGxERERGIZTCYFtJoFcykJCQgOnTp8PDwwOdO3eGra0tcnJysGPHDkyfPh3169cvrDiJiIgkY+HChXBzc4OFhQX8/Pxw5syZl9ZdtmwZGjduDHt7e9jb2yMwMPCV9bXRORkIDg6Gp6cnLl26hMjISPz999+YP3++XjcjIiIqCYw5tXDjxo0ICwvD+PHjce7cOdSpUwetWrXC48ePtdY/fPgwunfvjkOHDuHkyZNwdXXFxx9/jIcPH+p8T5nQcd5DqVKl8M0332DgwIHw8PBQlZuZmeHixYvw8vLS+abaNAo+8lbnE72LwqP6GzsEomIpKC+2UK8/eM4zg11r9iAL5OTkqJXJ5XLI5XKt9f38/FC/fn0sWLAAAKBUKuHq6oqvv/4ao0ePfu39FAoF7O3tsWDBAq3rAmmjc8vA8ePHkZ6ejnr16sHPzw8LFixAUlKSrqcTERFJUkREBOzs7NS2iIgIrXVzc3MRExODwMBAVZmJiQkCAwNx8uRJne6XlZWFvLw8ODg46ByjzsnAhx9+iGXLluHRo0f4v//7P/zyyy+oUKEClEol9u/fz7cUEhHRO8OQAwjDw8Px7NkztS08PFzrfZOSkqBQKODk5KRW7uTkhISEBJ1iHzVqFCpUqKCWULyO3rMJrKys8MUXX+D48eO4fPkyhg8fjunTp8PR0RHt2rXT93JERETFjlIYbpPL5bC1tVXbXtZF8LamT5+OX375Bdu3b9drVeA3nloIAJ6enpgxYwYePHiADRs2vM2liIiIJK9s2bIwNTVFYmKiWnliYiKcnZ1fee6sWbMwffp07Nu3D++//75e932rZOAFU1NTdOjQATt37jTE5YiIiIzKWOsMmJubo169eoiOjlaVKZVKREdHw9/f/6XnzZgxA5MnT0ZUVBR8fX31ft43WoGQiIjoXWbMFwyFhYUhJCQEvr6+aNCgASIjI5GZmYm+ffsCAHr37g0XFxfVIMQffvgB48aNw/r16+Hm5qYaW2BtbQ1ra2ud7slkgIiIqBjp2rUrnjx5gnHjxiEhIQE+Pj6IiopSDSq8d+8eTEz+17C/ePFi5ObmolOnTmrXGT9+PCZMmKDTPZkMEBERaTD2i4oGDx6MwYMHaz12+PBhtf27d+++9f2YDBAREWkwZjeBMTAZICIi0lBSXjBkKAaZTUBEREQlF1sGiIiINEitZYDJABERkYY3edtgScZuAiIiIoljywAREZEGdhMQERFJnNSmFrKbgIiISOLYMkBERKTB2CsQFjUmA0RERBqkNmaA3QREREQSx5YBIiIiDVIbQMhkgIiISINQKo0dQpFiMkBERKRBagMIOWaAiIhI4tgyQEREpIFjBoiIiCSOUwuJiIhIUtgyQEREpEFqLQNMBoiIiDQohbSmFrKbgIiISOLYMkBERKSB3QREREQSJ7VkgN0EREREEseWASIiIg1cdIiIiEjilHxRERERkbRxzAARERFJClsGiIiINAiJLTrEZICIiEgDuwmIiIhIUtgyQEREpEFqLQNMBoiIiDTwRUVEREQkKWwZICIi0sBuAiIiIokTEluBkN0EREREEseWASIiIg3sJiAiIpI4rkBIREQkcUqJtQxwzAAREZHEsWWAiIhIg9RmEzAZICIi0iC1AYTsJiAiIpI4tgwQERFp4GwCIiIiiWM3AREREUkKWwaIiIg0SG02gUwIIa22EHqlnJwcREREIDw8HHK53NjhEBUL/Lmgdx2TAVKTlpYGOzs7PHv2DLa2tsYOh6hY4M8Fves4ZoCIiEjimAwQERFJHJMBIiIiiWMyQGrkcjnGjx/PQVJE/8KfC3rXcQAhERGRxLFlgIiISOKYDBAREUkckwEiIiKJYzJAREQkcUwGJEgmk2HHjh1Fdr9mzZph6NChRXY/kq4JEybAx8fH2GHg8OHDkMlkSE1NNXYoRDphMmBEMpnslduECRNeeu7du3chk8lw4cKFQo3xyJEjaN68ORwcHFC6dGl4eHggJCQEubm5hXpfohdOnjwJU1NTBAUFGfS6EyZMUPt5s7OzQ+PGjXHkyBGD3seQijqRJ+lgMmBEjx49Um2RkZGwtbVVKxsxYoRR47t27Ro++eQT+Pr64ujRo7h8+TLmz58Pc3NzKBQKo8ZG0rFixQp8/fXXOHr0KP7++2+DXrtWrVqqn7eTJ0/Cw8MDbdu2xbNnzwx6H6LijsmAETk7O6s2Ozs7yGQy1b6joyPmzJmDihUrQi6Xw8fHB1FRUapzq1SpAgCoW7cuZDIZmjVrBgA4e/YsWrZsibJly8LOzg5NmzbFuXPn3ii+ffv2wdnZGTNmzEDt2rXh7u6OTz75BMuWLYOlpSUA4OnTp+jevTtcXFxQunRpeHt7Y8OGDa+8bk5ODkaMGAEXFxdYWVnBz88Phw8fVh3/66+/EBwcDHt7e1hZWaFWrVrYs2fPGz0DlWwZGRnYuHEjBg4ciKCgIKxevVrt+PTp0+Hk5AQbGxt8+eWXyM7O1uv6pUqVUv3MeXl5YdKkScjIyEBcXBwA7S1wqampkMlkav9m9+zZg+rVq8PS0hIfffQR7t69W+Bey5Ytg6urK0qXLo1PP/0Uc+bMQZkyZdTq/Prrr/jggw9gYWGBqlWrYuLEicjPzwcAuLm5AQA+/fRTyGQy1T6RITAZKKbmzZuH2bNnY9asWbh06RJatWqFdu3a4ebNmwCAM2fOAAAOHDiAR48eYdu2bQCA9PR0hISE4Pjx4zh16hQ8PDzQpk0bpKen6x2Ds7MzHj16hKNHj760TnZ2NurVq4fdu3fjypUr6N+/P3r16qWKT5vBgwfj5MmT+OWXX3Dp0iV07twZn3zyierZBg0ahJycHFVrxA8//ABra2u946eSb9OmTahRowY8PT3Rs2dPrFy5Ei/WSdu0aRMmTJiAadOm4c8//0T58uWxaNGiN75XTk4OVq1ahTJlysDT01Pn8+7fv4/PPvsMwcHBuHDhAvr164fRo0er1Tlx4gQGDBiAIUOG4MKFC2jZsiWmTp2qVufYsWPo3bs3hgwZgmvXrmHp0qVYvXq1qt7Zs2cBAKtWrcKjR49U+0QGIahYWLVqlbCzs1PtV6hQQUydOlWtTv369cVXX30lhBAiPj5eABDnz59/5XUVCoWwsbERu3btUpUBENu3b39tTPn5+aJPnz4CgHB2dhYdOnQQ8+fPF8+ePXvleUFBQWL48OGq/aZNm4ohQ4YIIYT466+/hKmpqXj48KHaOS1atBDh4eFCCCG8vb3FhAkTXhsfvfsaNmwoIiMjhRBC5OXlibJly4pDhw4JIYTw9/dX/Ty84OfnJ+rUqaPTtcePHy9MTEyElZWVsLKyEjKZTNja2orff/9dVUfbz1lKSooAoIojPDxceHl5qV171KhRAoBISUkRQgjRtWtXERQUpFanR48eaj/zLVq0ENOmTVOrs3btWlG+fHnVvq4/u0T6YstAMZSWloa///4bAQEBauUBAQG4fv36K89NTExEaGgoPDw8YGdnB1tbW2RkZODevXt6x2FqaopVq1bhwYMHmDFjBlxcXDBt2jRVPysAKBQKTJ48Gd7e3nBwcIC1tTX27t370vtdvnwZCoUC1atXh7W1tWo7cuQIbt++DQD45ptvMGXKFAQEBGD8+PG4dOmS3rFTyRcbG4szZ86ge/fuAP5p0u/atStWrFgBALh+/Tr8/PzUzvH399frHp6enrhw4QIuXLiAmJgYDBw4EJ07d8aff/6p8zV0iSM2NhYNGjRQK9Pcv3jxIiZNmqT2cxEaGopHjx4hKytLr+ci0lcpYwdAhhUSEoKnT59i3rx5qFy5MuRyOfz9/d9q9L+Liwt69eqFXr16YfLkyahevTqWLFmCiRMnYubMmZg3bx4iIyPh7e0NKysrDB069KX3y8jIgKmpKWJiYmBqaqp27EVXQL9+/dCqVSvs3r0b+/btQ0REBGbPno2vv/76jZ+BSp4VK1YgPz8fFSpUUJUJISCXy7FgwQKD3MPc3BzVqlVT7detWxc7duxAZGQkfv75Z5iYmKju+0JeXp5B7q0pIyMDEydOxGeffVbgmIWFRaHck+gFJgPFkK2tLSpUqIATJ06gadOmqvITJ06o/powNzcHgAKj+k+cOIFFixahTZs2AP7pz0xKSjJYbPb29ihfvjwyMzNV92vfvj169uwJAFAqlYiLi4OXl5fW8+vWrQuFQoHHjx+jcePGL72Pq6srBgwYgAEDBiA8PBzLli1jMiAh+fn5WLNmDWbPno2PP/5Y7ViHDh2wYcMG1KxZE6dPn0bv3r1Vx06dOvXW9zY1NcXz588BAOXKlQPwz8yfunXrAkCB6bw1a9bEzp071co04/D09CzQx6+5/8EHHyA2NlYtOdFkZmbGmTxUKJgMFFMjR47E+PHj4e7uDh8fH6xatQoXLlzAunXrAACOjo6wtLREVFQUKlasCAsLC9jZ2cHDwwNr166Fr68v0tLSMHLkSNXIf30tXboUFy5cwKeffgp3d3dkZ2djzZo1uHr1KubPnw8A8PDwwJYtW/DHH3/A3t4ec+bMQWJi4kuTgerVq6NHjx7o3bs3Zs+ejbp16+LJkyeIjo7G+++/j6CgIAwdOhStW7dG9erVkZKSgkOHDqFmzZpv9o2kEum3335DSkoKvvzyS9jZ2akd69ixI1asWIERI0agT58+8PX1RUBAANatW4erV6+iatWqOt8nPz8fCQkJAP4ZfLtx40Zcu3YNo0aNAgBYWlriww8/xPTp01GlShU8fvwYY8aMUbvGgAEDMHv2bIwcORL9+vVDTExMgVkPX3/9NZo0aYI5c+YgODgYBw8exO+//w6ZTKaqM27cOLRt2xaVKlVCp06dYGJigosXL+LKlSuYMmUKgH9mFERHRyMgIAByuRz29vY6PyvRKxl70AL9Q3MAoUKhEBMmTBAuLi7CzMxM1KlTR21gkxBCLFu2TLi6ugoTExPRtGlTIYQQ586dE76+vsLCwkJ4eHiIzZs3i8qVK4u5c+eqzoOOg5DOnTsnevbsKapUqSLkcrl47733RJMmTcTOnTtVdZ4+fSrat28vrK2thaOjoxgzZozo3bu3aN++varOvwcQCiFEbm6uGDdunHBzcxNmZmaifPny4tNPPxWXLl0SQggxePBg4e7uLuRyuShXrpzo1auXSEpK0vl7SSVf27ZtRZs2bbQeO336tAAgLl68KKZOnSrKli0rrK2tRUhIiPj222/1GkAIQLWVLl1aeHt7i8WLF6vVu3btmvD39xeWlpbCx8dH7Nu3T20AoRBC7Nq1S1SrVk3I5XLRuHFjsXLlSrUBhEII8eOPPwoXFxdhaWkpOnToIKZMmSKcnZ3V7hUVFSUaNmwoLC0tha2trWjQoIH48ccfVcd37twpqlWrJkqVKiUqV66s03MS6UImxL86w4iIqEiEhobixo0bOHbsmLFDIWI3ARFRUZg1axZatmwJKysr/P777/jpp5/eal0EIkPi1EIJmzZtmto0pn9vrVu3NnZ4RG/lZf+2ra2tjfLX+JkzZ9CyZUt4e3tjyZIl+M9//oN+/foVeRxE2rCbQMKSk5ORnJys9ZilpSVcXFyKOCIiw7l169ZLj7m4uLzxwFqidxGTASIiIoljNwEREZHEMRkgIiKSOCYDREREEsdkgIiISOKYDBAREUkckwEiIiKJYzJAREQkcf8PZT//UhP6kcIAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import datetime as dt\n",
        "\n",
        "snapshot_date = df['Order_Date'].max() + dt.timedelta(days=1)\n",
        "rfm = df.groupby('CustomerID').agg({\n",
        "'Order_Date': lambda x: (snapshot_date - x.max()).days, # Recency\n",
        "'Order_ID': 'count', # Frequency\n",
        "'Total_Sales': 'sum' # Monetary\n",
        "})\n",
        "# Rename kolom agar mudah dibaca\n",
        "rfm.columns = ['Recency', 'Frequency', 'Monetary']\n",
        "# Memberikan skor 1-5 (Semakin tinggi semakin baik)\n",
        "\n",
        "rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1])\n",
        "rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])\n",
        "rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5])\n",
        "# Gabungkan skor menjadi satu segmen\n",
        "rfm['RFM_Group'] = rfm.R_Score.astype(str) + rfm.F_Score.astype(str) + rfm.M_Score.astype(str)"
      ],
      "metadata": {
        "id": "nThblCwMz-QD"
      },
      "execution_count": 23,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.linear_model import LinearRegression\n",
        "\n",
        "# Drop rows where 'Total_Sales' is NaN\n",
        "df_cleaned = df.dropna(subset=['Total_Sales'])\n",
        "\n",
        "X = df_cleaned[['Ad_Budget']] # Fitur\n",
        "y = df_cleaned['Total_Sales'] # Target\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
        "model = LinearRegression()\n",
        "model.fit(X_train, y_train)\n",
        "print(f\"Koefisien Iklan: {model.coef_[0]}\")\n",
        "print(f\"Akurasi Model (R2 Score): {model.score(X_test, y_test)}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XKNVNsp-4AYA",
        "outputId": "53250d30-d391-4ff3-b508-d4f1b2a2d91e"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Koefisien Iklan: 0.1841982749623798\n",
            "Akurasi Model (R2 Score): -0.1956467472142791\n"
          ]
        }
      ]
    }
  ]
}