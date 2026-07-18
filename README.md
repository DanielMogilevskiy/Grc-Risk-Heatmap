# 🔥 GRC Risk Heatmap Generator

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

---

## 📌 What is this?

A lightweight Python tool that transforms a CSV file with risk scores into a **5×5 risk heatmap** – a colour‑coded matrix that instantly shows which combinations of **likelihood** and **impact** are most frequent.

---

## 🎯 Why was it made?

In Governance, Risk, and Compliance (GRC), risk registers are often huge tables of numbers.  
This tool **visualises** that data, enabling:

- Quick identification of **high‑priority risk clusters**
- Clear communication to **non‑technical stakeholders**
- Faster **decision‑making** on risk mitigation budgets

---

## 🔥 What GRC problem does it solve?

- **Before**: dozens of rows with likelihood/impact scores – hard to interpret.
- **After**: a single heatmap where **red = urgent attention**, **yellow = monitor**, **green = low priority**.

It helps answer:

> *"Where are we most exposed?"*  
> *"Which risks need immediate action?"*

---

## 🚀 How to run it

### 1️⃣ Clone the repository

```bash
git clone https://github.com/DanielMogilevskiy/grc-risk-heatmap.git
cd grc-risk-heatmap
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Prepare your data

Example (sample_risks.csv is provided):

```csv
risk_name,likelihood,impact
Data breach,5,5
Phishing attack,4,4
...
```

### 4️⃣ Run the script

```bash
python src/generate_heatmap.py
```
You can also pass custom paths:
```bash
python src/generate_heatmap.py data/my_risks.csv outputs/my_heatmap.png
```

### 5️⃣ View the result
The heatmap will be saved as outputs/risk_heatmap.png (or your custom path).

## 📷 Screenshot
![Example Heatmap](screenshots/heatmap_example.png)

## 🛠 Customisation
- Change the colour palette by modifying the `cmap` parameter (e.g., `'Blues'`, `'Greens'`).
- The script counts occurrences; you can modify it to average scores or use weighted values.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

Maintained by [Daniel Mogilevskiy](https://www.linkedin.com/in/daniel-mogilevskiy/)