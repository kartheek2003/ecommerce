
# 🛒 E-Commerce Customer Segmentation

This project performs **customer segmentation** on e-commerce data using **RFM analysis** (Recency, Frequency, Monetary) and **K-Means clustering**. The goal is to identify distinct customer groups and provide actionable insights for targeted marketing strategies.

---

## 📊 Project Overview
- **Data Source:** E-commerce transactions dataset
- **Techniques:** RFM Analysis, K-Means Clustering, Data Preprocessing, Feature Scaling
- **Objective:** Classify customers into meaningful segments for business decision-making
- **Deployment:** Azure App Service (Flask API)
- **Local Setup:** Run easily on any system with Python

---

## 🔑 Features
- RFM (Recency, Frequency, Monetary) calculation
- K-Means clustering for customer segmentation
- Customer segment mapping with descriptive labels
- Flask-based API for predictions
- Azure cloud deployment
- Easy-to-run locally

---

## 🧩 Tech Stack
| Component        | Technology                |
|------------------|-------------------------|
| **Language**     | Python 3                |
| **Libraries**    | Pandas, NumPy, Scikit-learn, Flask, Matplotlib, Seaborn |
| **Model**        | K-Means Clustering      |
| **Deployment**   | Microsoft Azure App Service |
| **Version Control** | Git & GitHub          |

---


---

## 🧠 Customer Segments

| Cluster | Segment Name                  | Recency (days) | Frequency | Monetary (₹) |
|---------|------------------------------|---------------|-----------|-------------|
| 0       | Churned / At-Risk Customers  | 229.5         | 1.8       | 406.0       |
| 1       | High-Value Loyal Customers   | 34.0          | 6.8       | 1741.3      |
| 2       | Potential Loyalists          | 49.0          | 2.2       | 553.1       |

**Segment Mapping:**
segment_map = {
    0: "Churned / At-Risk Customers",
    1: "High-Value Loyal Customers",
    2: "Potential Loyalists"
}

---
## 🧪 Test Data Points (Sample)

| Customer ID | Recency (days) | Frequency | Monetary ($) | Expected Segment |
|------------|---------------|-----------|--------------|-----------------|
| CUST001    | 5             | 20        | 1200         | **High-Value**  |
| CUST002    | 60            | 8         | 350          | **At-Risk**     |
| CUST003    | 180           | 2         | 80           | **Low-Value**   |

🔹 **How to test:**  
Input these values into the app’s prediction form or API endpoint to see if it correctly identifies the segment.

---
###  Project Demo
| Interface | Prediction High Value | Prediction At Risk | Prediction loyal |
|-----------|-------------------|-----------------------|--------------------|
| ![Homepage](webimages/homepage_cc.png) | ![Prediction](webimages/prediction_hv.png) | ![Prediction](webimages/prediction_ar.png) | ![Prediction](webimages/prediction_pl.png) |

---
###  How to Run Locally
```bash
# Clone the repository
git clone https://github.com/kartheek2003/ecommerce.git
cd ecommerce

# Create virtual environment
python -m venv venv

# Activate environment
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```
---

> The app will be available at:
🔗 http://127.0.0.1:8000/

## ☁️ Deployment

The application is deployed on **Azure App Service** for production-ready access.  
**Steps included:**
- Building and testing locally  
- Creating Azure App Service  
- Deploying via GitHub Actions  

---

## 📈 Results & Insights

- Identified **3 major customer segments** to improve targeted marketing campaigns  
- **High-value customers** contribute significantly to revenue  
- **At-risk customers** need retention strategies  
- Model is **scalable** and ready for real-world datasets  

---

## 📝 Author

👤 **Kartheek Akkabathula**
[GitHub](https://github.com/kartheek2003)  
