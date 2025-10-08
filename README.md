# Hotel-Booking-Conflict-Resolution-Analysis
# 🏨 Hotel Booking Conflict Resolution Analysis

A data-driven **Streamlit web application** designed to help hotel management teams identify booking conflicts, analyze early/late checkouts, manage room upgrades, handle no-shows with deposit implications, and maintain high data quality.  

This system provides **interactive visual analysis, financial impact calculations**, and downloadable reports (Excel and PDF) for decision-making efficiency.

---

## 📘 Project Overview

**Hotel Booking Conflict Resolution Analysis** automates the detection and reporting of key operational challenges in hotel booking systems.  

The dashboard offers a centralized view of:

- 🔁 **Double Booking Conflicts** with prioritized resolution actions  
- ⏰ **Early & Late Checkouts** with estimated revenue loss or late fees  
- 🏷️ **Room Upgrade Tracking** and recommendations  
- 💳 **No-Show Management** with deposit reconciliation ($0 vs paid)  
- 📅 **Daily Occupancy Calendar** highlighting conflicts and gaps  
- ⚠️ **Data Quality Issues** (missing names, timestamps, invalid entries)

---

## 🧮 Built-In Assumptions (Configurable)

| Parameter | Value | Description |
|------------|--------|-------------|
| Default Check-in | 15:00 | Used when missing actual check-in time |
| Default Checkout | 11:00 | Used when missing actual checkout time |
| **Room Rates** | Standard ₹3,000 / Deluxe ₹4,500 / Suite ₹8,000 | Used for financial calculations |
| **Late Checkout Policy** | 0–1 hr → 0%, 1–2 hrs → 25%, 2–4 hrs → 25%, 4–6 hrs → 50%, >6 hrs → 100% | Applied to financial impact analysis |

> 💡 Replace these with your property’s actual rates and policies to get exact results.

---

## 🧰 Tech Stack

| Category | Technology |
|-----------|-------------|
| **Frontend / UI** | Streamlit |
| **Backend / Logic** | Python (Pandas, NumPy) |
| **Data Input** | CSV Dataset (Hotel Bookings) |
| **Reports** | Excel (OpenPyXL), PDF (FPDF) |
| **Visualization** | Streamlit DataFrames, Tables, and Interactive Tabs |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/hotel-booking-analysis.git
cd hotel-booking-analysis
