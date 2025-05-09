**🥗 Nutrition Tracker**

    A Django-based web application that helps users track their daily food intake with real-time totals and optional data visualization using Chart.js.

**✨ Features**

    🍎 Display of Food Items
    
     Browse a categorized list of food items such as fruits, vegetables, milk products, etc. Each item has a "More Info" button for additional details.

**📊 Tracker with Dropdown & Quantity Input**

    Users can select a food item from a dropdown menu and specify the quantity (e.g., 1, 2, etc.). Upon submitting, the item is added to the daily tracker list.

**➕ Add Multiple Items**

    Continue adding multiple food items with their respective quantities to build a meal log.

**🧮 Calculate Total**

    Click the "Get Total" button to display the total nutritional summary (e.g., calories, protein, carbs, etc.) for the selected food items.

**🔐 User Registration & Authentication**(Optinal)

    Users can register, log in, and manage their personalized food intake records securely.

**📈 Optional Chart.js Integration**

    Visualize daily intake with dynamic charts (bar, pie, or line charts) powered by Chart.js.

**🛠 Tech Stack**

  **Layer**	       **Technology**
   Backend	      Django (Python)
   Frontend	      HTML, CSS, Bootstrap
   Database	      SQLite (default)
  Visualization	  Chart.js (optional)

**🚀 Getting Started**

1. Clone the repository

    -> git clone https://github.com/syashwanths/Nutrition-Tracker.git
    
    -> cd Nutrition-Tracker

2. Set up virtual environment

    -> python -m venv venv
   
    -> source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Run migrations

    -> python manage.py makemigrations
   
    -> python manage.py migrate

4. Start the development server

    -> python manage.py runserver

5. Access the app

   -> Open your browser at: http://127.0.0.1:8000


**✍️ Author**

  Yashwanth S
