# Draxen.exe - Premium Developer Portfolio

A high-performance, futuristic portfolio landing page designed for the modern web developer. This project combines a fully responsive, app-like frontend with a lightweight, easily extensible Python Flask backend.

## 🌟 Features

*   **Premium Cyberpunk Aesthetic**: Immersive dark mode with vibrant neon cyan and purple gradients.
*   **Dynamic Backgrounds**: CSS-based blurred background meshes and custom HTML5 canvas particle engines.
*   **Mobile-First App UI**: Completely optimized for mobile devices with horizontal swipeable cards (snap scrolling) and an elegant hamburger menu.
*   **Glassmorphism Panels**: Semi-transparent, blurred cards that create depth and visual richness.
*   **REST API Integration**: Includes a Python Flask backend to securely handle form transmissions.
*   **Analytics**: Built-in simple visitor tracking via local file storage.
*   **Zero-Dependency Icons**: Uses robust, high-quality inline SVGs to guarantee icon rendering on any network.

## 🛠️ Tech Stack

### Frontend
*   HTML5 (Semantic structuring)
*   CSS3 (Variables, Flexbox/Grid, Animations, Glassmorphism)
*   Vanilla JavaScript ES6+ (Intersection Observers, Canvas API, Fetch API)

### Backend
*   Python 3.x
*   Flask (Web framework)
*   Werkzeug (Routing)

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/draxen-exe/landing-page
   cd landing-page
   ```

2. **Install Python Dependencies:**
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is missing, simply run `pip install flask werkzeug`)*

3. **Start the Backend Server:**
   ```bash
   python app.py
   ```

4. **View the Site:**
   Open your browser and navigate to `http://127.0.0.1:5000`

## 📁 Project Structure

```
draxen-portfolio/
│
├── app.py                  # Main Flask application and API routes
├── analytics.json          # Local storage for visitor count
├── messages.json           # Local storage for contact form submissions
├── requirements.txt        # Python dependencies
│
├── templates/
│   └── index.html          # Main HTML structure
│
└── static/
    ├── style.css           # Core styling and mobile media queries
    ├── script.js           # Frontend logic, animations, and API calls
    └── draxen_logo.png     # Brand logo
```

## 📱 Mobile Experience

The mobile layout is specifically engineered to mimic native applications:
- Stacked elements collapse into horizontal, swipeable carousels.
- Excessive vertical scrolling is eliminated.
- High-intensity background animations are paused to save battery life.
- Touch targets (buttons, links) are resized for ergonomic thumb interaction.
