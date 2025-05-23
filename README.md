# 🎫 Sydney Event Scraper Web App

A minimalistic full-stack web application that scrapes and displays upcoming events in **Sydney, Australia**. Users can view event details and book tickets via a “GET TICKETS” button, which prompts for their email and redirects to the original event page.

---

## 🚀 Features

- Automatically scrapes Sydney events from [Eventbrite](https://www.eventbrite.com.au/)
- Displays event titles, dates, and images in a clean UI
- “GET TICKETS” button asks for email input and redirects users to the event site
- Backend auto-updates every hour using a scheduled job

---

## 🛠 Tech Stack

| Layer     | Technology               |
|-----------|---------------------------|
| Frontend  | HTML, TailwindCSS, JavaScript |
| Backend   | Python, Flask, Flask-CORS |
| Scraping  | Selenium, BeautifulSoup   |
| Scheduler | APScheduler               |

---

## 📁 Folder Structure

louderworld-task/
├── backend/
│ ├── app.py # Flask backend
│ ├── scraper.py # Scraper using Selenium
│ ├── requirements.txt # Backend dependencies
├── frontend/
│ ├── index.html # Minimal event UI
│ └── assets/ # (Optional) static images
├── venv/ # Python virtual environment
└── README.md # Project documentation


---

## 🧪 Getting Started

### 1. Clone the Repository


git clone https://github.com/yourusername/sydney-events-app.git
cd louderworld-task


### 2. Set Up Virtual Environment (Windows PowerShell)

python -m venv venv
.\venv\Scripts\Activate
cd backend
pip install -r requirements.txt

### 3. Run Flask API

python app.py
API runs at: http://127.0.0.1:5000/api/events

### 4. Run Frontend
Open frontend/index.html directly in your browser or serve with Live Server.

