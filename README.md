
# 🏥 Medical Insurance Cost Prediction

This project uses **Linear Regression** to predict the **medical insurance charges** an individual might incur based on personal attributes like age, sex, BMI, number of children, smoking status, and region.

---

## 📊 Project Overview

Medical costs can vary significantly based on lifestyle and demographics. Using a dataset of insured individuals, this project:
- Performs **exploratory data analysis (EDA)**
- Encodes categorical variables
- Trains a **linear regression model**
- Evaluates model performance using **R² score**
- Builds a predictive system for real-world use

---

## 🛠️ Technologies & Libraries

- Python
- Pandas
- NumPy
- Matplotlib & Seaborn (for data visualization)
- Scikit-learn (for modeling)

---

## 📁 Dataset

The dataset used is [`insurance.csv`](https://www.kaggle.com/datasets/mirichoi0218/insurance), containing:

| Feature | Description |
|---------|-------------|
| age     | Age of the primary beneficiary |
| sex     | Gender (male/female) |
| bmi     | Body mass index |
| children | Number of children covered by insurance |
| smoker  | Smoking status (yes/no) |
| region  | Residential area in the US |
| charges | Individual medical costs billed by health insurance |

---

## 🔍 Key Steps

1. **Data Exploration**: 
   - Checked for missing values
   - Visualized distributions (age, BMI, charges, etc.)
2. **Data Preprocessing**:
   - Encoded categorical features (sex, smoker, region)
3. **Model Building**:
   - Trained using **LinearRegression** from `sklearn`
4. **Model Evaluation**:
   - R² score on training data: `~0.74`
   - R² score on test data: `~0.78`
5. **Prediction System**:
   - Built a simple input-based system to predict new charges

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/medical-insurance-cost-prediction.git

# Install required packages
pip install pandas numpy matplotlib seaborn scikit-learn

# Run the Python script
python medical_insurance_cost_prediction.py
```

---

## 📌 Sample Prediction

Input:  
`(31, female, 25.74 BMI, 0 children, non-smoker, southeast)`

Output:  
`The insurance cost is USD 3760.61`

---

## 📈 Future Improvements

- Use more advanced models (e.g., XGBoost, RandomForest)
- Hyperparameter tuning
- Deploy as a Flask API or Streamlit web app

---

## 🤝 Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
