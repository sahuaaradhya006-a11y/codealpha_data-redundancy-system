🚀 Data Redundancy Removal System

📌 About the Project

This project is a simple web-based system built using Flask that helps in identifying and removing duplicate data.

The main idea behind this project is to make sure that only unique and valid data gets stored, while redundant (duplicate) data is filtered out. This improves data accuracy and avoids unnecessary storage.

---

🎯 What this project does

- Takes user input from a web interface
- Checks whether the data already exists
- Separates:
  - ✅ Unique data
  - ❌ Duplicate data
- Stores only the unique data in a database file
- Displays results instantly on the screen

---

🛠️ Technologies Used

- Python (Flask)
- HTML & CSS
- File handling ("database.txt") for storage

---

📂 Project Structure

project/
│
├── app.py
├── data_redundancy_system.py
├── database.txt
└── templates/
    └── index.html

---

⚙️ How to run the project

1. Clone the repository

git clone <your-repo-link>

2. Go to the project folder

cd data-redundancy-system

3. Install Flask

python -m pip install flask

4. Run the application

python app.py

5. Open in browser

http://127.0.0.1:5000

---

💡 Example

Input:

data data system system

Output:

- Unique Data → "data system"
- Duplicate Data → "data system"

---

🚀 Future Improvements

- Connect to a real database (MongoDB / Firebase)
- Add file upload feature
- Improve UI with better design
- Add login/authentication system

---

📚 What I learned

- Basics of Flask and backend development
- How to connect frontend with backend
- Handling and validating data
- Preventing duplicate entries in a system

---

👨‍💻 Author

Aaradhya Sahu
B.Tech student

---

⭐ If you found this project useful, feel free to give it a star!
