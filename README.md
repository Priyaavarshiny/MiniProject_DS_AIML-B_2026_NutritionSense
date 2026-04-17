# NutritionSense: Data-Driven Analysis of Dietary Patterns and Health Risks

## 1. Introduction
Lifestyle diseases such as obesity and diabetes are increasing due to poor dietary habits and lack of physical activity. Understanding how diet and lifestyle influence health is important for improving overall well-being.

This project focuses on analyzing dietary patterns and predicting health risks using data analytics and machine learning techniques.

---

## 2. Problem Statement
Poor dietary habits contribute significantly to lifestyle diseases such as obesity and diabetes. This project analyzes nutritional and lifestyle data to identify unhealthy patterns and predict associated health risks.

---

## 3. Objectives
- To analyze dietary and lifestyle data
- To identify patterns influencing health risks
- To visualize relationships between different features
- To build a machine learning model to predict obesity levels

---

## 4. Dataset Description
The dataset contains information related to dietary habits, physical activity, and lifestyle factors.

### Features include:
- Age
- Height and Weight
- Eating habits
- Physical activity frequency (FAF)
- Water consumption (CH2O)
- Screen time (TUE)

### Target Variable:
- NObeyesdad (Obesity Level)

The target variable represents different health risk categories such as normal, overweight, and obesity.

---

## 5. Methodology

### 5.1 Data Preprocessing
- Removed missing values
- Eliminated duplicate records
- Converted categorical variables into numerical format using encoding
- Stored cleaned dataset in processed_data folder

### 5.2 Data Visualization
- Created graphs to analyze patterns in the data
- Used count plots and box plots for better understanding
- Simplified obesity categories for clarity

### 5.3 Model Building
- Used Random Forest Classifier
- Split data into training and testing sets
- Trained model on training data
- Evaluated performance using accuracy

---

## 6. Results
- The model achieved an accuracy of approximately 96%
- Predictions closely matched actual values
- Visualization revealed strong relationships between lifestyle factors and obesity

---

## 7. Key Insights
- Lower physical activity is associated with higher obesity risk
- Dietary habits significantly influence health outcomes
- Water intake and lifestyle factors impact overall health
- Age varies across different obesity categories

---

## 8. Conclusion
The project demonstrates that dietary patterns and lifestyle choices play a significant role in determining health risks. Machine learning models can effectively predict obesity levels and support data-driven health awareness.
The project follows a structured data science workflow, including data preprocessing, exploratory data analysis, visualization, and model development. Each stage is implemented systematically to ensure data quality, accurate analysis, and reliable prediction of health risks. The results demonstrate the effectiveness of machine learning in identifying patterns related to obesity and lifestyle factors.

---

## 9. Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 10. Project Structure
dataset/
├── raw_data/
├── processed_data/

notebooks/
├── data_understanding.ipynb
├── preprocessing.ipynb
├── visualization.ipynb
├── model_building.ipynb

report/
README.md
requirements.txt

This project analyzes dietary patterns and predicts health risks using machine learning techniques. The implementation follows a structured data science workflow including preprocessing, visualization, and model development.