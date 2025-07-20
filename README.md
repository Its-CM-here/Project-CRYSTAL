# Project CRYSTAL  
### **Complex Reprocessing of Yearly Statistics Targeted at Achieving Linearity**

![Python](https://img.shields.io/badge/Python-3.x-blue) ![MySQL](https://img.shields.io/badge/Database-MySQL-orange) ![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Overview
**CRYSTAL** is a data-driven analytical tool designed to provide actionable insights for managing global pandemics.  
It processes health-related data from **MySQL databases** and **CSV files**, performs **42 types of statistical analyses**, and visualizes results using interactive **charts & graphs**.  

The program aims to demonstrate the power of **data science** in understanding pandemic trends and assisting decision-making.  

---

## ✨ Features
- **Comprehensive Analysis** – 42 different data analyses using Python data visualization libraries.  
- **Hybrid Data Handling** – Uses **MySQL** for user data & authentication, and **CSV** for case statistics.  
- **Secure User Management** – Login/Signup system with admin-controlled user records.  
- **Pandemic-focused Insights** – Highlights trends & patterns useful in pandemic management.  
- **Visual Reports** – Clear graphical representations for better understanding.  

---

## 🛠️ Tech Stack
- **Language:** Python (3.10)  
- **Libraries:** Matplotlib, Numpy (data visualization & processing)  
- **Database:** MySQL (user management & security)  
- **File Handling:** CSV (case data input & processing)  

---

## 📂 Project Structure
```
CRYSTAL/
│
├── main.py                         # Entry point of the program
├── database/                       # MySQL database scripts & admin controls
│   ├── pms_admin_login.sql         # Admin table
│   ├── pms_admin_blocked.sql       # Blocked Admin Credentials
│   ├── pms_people_login.sql        # User table
│   └── pms_people_blocked.sql      # Blocked User Credentials
├── data/                           # CSV files (case details)
├── analysis/                       # Data processing & visualization modules
├── requirements.txt                # Required libraries
├── Project Log.txt                 # Project Development Timeline
└── README.md                       # Project documentation
```

---

## ⚡ Installation & Setup
1. **Clone the repository**  
   ```bash
   git clone https://github.com/<your-username>/CRYSTAL.git
   cd CRYSTAL
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup MySQL database (IMPORTANT)**  
   - Create a database (e.g., `crystal_db`).  
   - Sequentially import all SQL files in the `/database` folder:  
     ```sql
     SOURCE database/pms_admin_login.sql;
     SOURCE database/pms_admin_blocked.sql;
     SOURCE database/pms_people_login.sql;
     SOURCE database/pms_people_blocked.sql;
     ```
   - Ensure you update your MySQL credentials (username, password, database name) in `main.py` or the config file.  

4. **Run the program**  
   ```bash
   python main.py
   ```

---

## 📊 Usage
- **Login / Signup:** Secure authentication for users and admins.  
- **Upload Case Data:** Place the CSV files in `/data`.  
- **Run Analysis:** Choose from 42 statistical visualizations.  
- **View Results:** Graphs & charts are displayed for interpretation.  

---

## 🧠 Concepts Demonstrated
- Data Science applications in healthcare  
- Statistical modeling & visualization  
- Secure database integration with Python  
- File handling & hybrid data processing  

---

## 🤝 Contributing
Pull requests are welcome! If you’d like to suggest features or fix bugs, feel free to fork the repo and submit a PR.  

---

## 📜 License
This project is licensed under the **MIT License** – free to use & modify with attribution.

---

## 👤 Author
**Chandramouli M**  
🔗 [LinkedIn](https://www.linkedin.com/in/itschandramouli) | [GitHub](https://github.com/its-CM-here)
