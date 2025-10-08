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
OUTPUT:
---
<img width="1436" height="335" alt="image" src="https://github.com/user-attachments/assets/d6558ccf-b07f-4182-9792-497ce4ca2909" />
<img width="1798" height="377" alt="image" src="https://github.com/user-attachments/assets/fb97e4b3-890f-44a6-bdfc-1cc29122adb1" />
<img width="1824" height="546" alt="image" src="https://github.com/user-attachments/assets/0004fa81-9566-44ad-a6be-b90a01a1a2ff" />
<img width="1820" height="707" alt="image" src="https://github.com/user-attachments/assets/3d417a0d-c5cd-43f1-81fc-1bd3b6067997" />
<img width="1812" height="494" alt="image" src="https://github.com/user-attachments/assets/33250de1-213a-42a3-81fa-f9da690d39b1" />
<img width="1808" height="686" alt="image" src="https://github.com/user-attachments/assets/e667e608-2dfa-4ece-990f-335a1cd521ad" />
<img width="1803" height="874" alt="image" src="https://github.com/user-attachments/assets/d1cb4071-a5f1-416f-9727-c011b4281499" />
<img width="1824" height="685" alt="image" src="https://github.com/user-attachments/assets/1074a511-8f2a-486c-aa2f-558360bbf0dc" />







## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/hotel-booking-analysis.git
cd hotel-booking-analysis
