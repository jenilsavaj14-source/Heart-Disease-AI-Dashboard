# **❤️ Heart Disease Diagnostic Intelligence**

**A high-performance AI-powered dashboard designed to assist medical professionals in predicting heart disease risk. This project combines Machine Learning (Scikit-Learn), Web Deployment (Streamlit), and Advanced Analytics (Power BI).**

### **🚀 Live Demo**
**You can access the live application here:** **[👉 Click to open Heart Disease Dashboard](https://heart-disease-ai-dashboard-pabcn5hmnkx9zyzbvkpuvt.streamlit.app/)**

### **📋 Project Overview**
**This project was developed as a Final Internship Project to bridge the gap between complex machine learning models and end-user clinical tools. It allows users to input 13 key clinical features and receive a real-time risk assessment driven by a Random Forest algorithm.**

### **🌟 Key Features**
* **🧠 AI Prediction:** Utilizes a trained Random Forest model to calculate heart disease probability.
* **🔍 Clinical Reasoning:** Dynamically explains "Why" a patient is at risk based on their unique metrics (e.g., Hypertension, Cholesterol).
* **📄 PDF-Style Reports:** Generates a personalized diagnostic report for each patient, available for immediate download.
* **📊 Power BI Integration:** Includes a downloadable `.pbix` file for deep-dive historical trend analysis.
* **🎨 Responsive UI:** A dark-themed, professional dashboard built for clarity and ease of use.

### **🛠️ Tech Stack**
* **Language:** **Python 3.10+**
* **Framework:** **Streamlit**
* **Machine Learning:** **Scikit-Learn, Pandas, NumPy**
* **Data Visualization:** **Plotly / Streamlit Native**
* **Analytics:** **Microsoft Power BI**
* **Deployment:** **GitHub & Streamlit Cloud**

### **📂 Project Structure**
```text
/
├── app.py                     # Main Streamlit application code
├── requirements.txt           # List of Python dependencies
├── pipe1.pkl                  # Trained Machine Learning Model
├── data.pkl                   # Reference data for model consistency
├── heart.csv                  # Dataset used for historical analysis
├── Heart_Dashboard.pbix       # Professional Power BI Dashboard
└── README.md                  # Project documentation
```

### **⚙️ Installation & Local Testing**

**To run this project on your local machine, follow these steps:**
**1. Clone the Repository**
```bash
git clone https://github.com/jenilsavaj14-source/Heart-Disease-AI-Dashboard.git
```
**2. Install Dependencies**
```bash
pip install -r requirements.txt
```
**3. Run the Application**
```bash
streamlit run app.py
```
To add a dedicated **Testing** section to your README, you should explain both how to test it locally and how you verified the model's accuracy. This shows your internship supervisor that you care about **Quality Assurance (QA)**.

Copy and paste this section into your `README.md`, ideally right after the "Installation" section:

---

### **🧪 Testing & Quality Assurance**

#### **1. Local Functional Testing**
**To verify the application logic locally, perform the following test cases:**
* **Input Validation:** Enter values outside normal ranges (e.g., Cholesterol > 500) to ensure the **Clinical Reasoning** engine triggers the correct warnings.
* **Report Generation:** Run a diagnostic and click **"Download Report"**. Verify that the `.txt` file contains the correct patient name and specific clinical data.
* **Responsive Check:** Resize your browser window to ensure the **Metric Cards** and **Charts** stack correctly for mobile viewing.

#### **2. Model Performance Testing**
**The underlying Random Forest model was tested using a 80/20 train-test split on the Heart Disease dataset:**
* **Accuracy:** The model maintains a high classification accuracy on unseen data.
* **Confusion Matrix:** Verified to minimize **False Negatives** (missing a high-risk patient), which is critical in medical diagnostics.
* **Feature Importance:** Tested to ensure variables like `thalach` (Max Heart Rate) and `cp` (Chest Pain) have the highest weight in the final prediction.

#### **3. Deployment Testing**
**The live environment on Streamlit Cloud is monitored for:**
* **Resource Usage:** Ensuring the `.pkl` models load within the memory limits.
* **Link Integrity:** The Power BI download link is verified to ensure the `.pbix` file is accessible to external users.

### **💡 Pro-Tip**
During your demo, you can actually **demonstrate** testing by:
1.  Opening the **"Manage App"** logs on Streamlit Cloud to show there are no background errors.
2.  Inputting a "Healthy" profile vs. a "High Risk" profile to show the AI reacts differently. 

### **👨‍💻 Details**
**This project was built to demonstrate proficiency in Full-Stack Data Science. It showcases the ability to handle data preprocessing, model deployment, and user-centric design.**

**Note:** *This tool is intended for educational and diagnostic assistance purposes only. Always consult a medical professional for actual health concerns.*
