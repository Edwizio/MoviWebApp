# 🎬 MoviWebApp

**MoviWebApp** is a Flask-based web application that allows users to create and manage personal movie lists.  
Each user can add, view, and organize their favorite movies — with automatic data fetching from the **OMDb API** and robust error handling.

---

## 🚀 Features

✅ **User Management**  
- Add and view users dynamically.  
- Flash notifications for success or error events.  

✅ **Movie Management**  
- Add movies manually or automatically using the OMDb API.  
- Auto-fetch movie title, director, year, and poster.  
- Optional “year” field – users can provide it or let OMDb fill it in.  
- Displays a **custom fallback image** when the poster is missing or broken.  

✅ **Responsive UI**  
- Built with HTML5, CSS3, and Jinja2 templates.  
- Hover effects on buttons for interactive feedback.  
- Flash messages fade out automatically after 10 seconds.  
- Clean, mobile-friendly design.  

✅ **Error Handling**  
- OMDb errors handled gracefully with clear messages.  
- Database integrity errors prevented with default fallback data.  

---

## 🧠 Tech Stack

| Category | Technology |
|-----------|-------------|
| **Backend** | Python, Flask, SQLAlchemy |
| **Database** | SQLite |
| **Frontend** | HTML5, CSS3, Jinja2 |
| **API** | [OMDb API](https://www.omdbapi.com/) |
| **Version Control** | Git & GitHub |

## ⚙️ Installation & Setup

### 1. Clone the repository
    ```bash
    git clone https://github.com/Edwizio/MoviWebApp.git
    cd MoviWebApp

### 2. Create and activate a virtual environment 
    ```bash
    python -m venv venv
    # Activate on Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate

### 3. Install dependencies
    ```bash
    pip install -r requirements.txt

### 4. Add your OMDb API key
    OMDB_API_KEY=your_api_key_here

### 5. Run the application
    ```bash
    python app.py

Access the app in your browser:
👉 http://127.0.0.1:5000/
    
📂 Project Structure

MoviWebApp/
│
├── app.py                 # Main Flask app
├── data_manager.py        # Handles CRUD operations
├── models.py              # SQLAlchemy models
│
├── templates/             # HTML templates (Jinja2)
│   ├── base.html
│   ├── users.html
│   └── movies.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── images/
│   │   ├── placeholder.png
│   │   └── userlogo.jpg
│   └── favicon.ico
│
├── requirements.txt
└── README.md

🧩 Key Highlights

Auto-fetches missing movie data from OMDb.

Protects database integrity with default values.

Clean UI with hover animations and feedback.

Flash messages disappear automatically after 10 seconds.

🧪 Example Screens

(You can add screenshots here later, for example:)

🧍 User List Page – Displays all users with buttons to view their movies.

🎥 Movies Page – Shows each movie as a card with title, director, and poster.

👨‍💻 Author

Zahra Rauf
📍 Developed with ❤️ using Flask & OMDb API
🔗 GitHub Profile

🪪 License

This project is licensed under the MIT License – you’re free to use and modify it.
    

