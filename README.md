# Meal Suggestions Web App

This Flask-based web application provides meal suggestions based on user input. The app checks if the entered ingredients contain non-vegetarian items and gives explanations for them. If all items are vegetarian, the app provides vegetarian meal suggestions using Google Generative AI's API.

## Features
- Accepts a list of ingredients and suggests vegetarian meals using Google Generative AI.
- If non-vegetarian ingredients are entered, the app provides explanations for their environmental impact.
- The app handles both vegetarian and non-vegetarian items separately.

## Setup and Installation

### Prerequisites
- Python 3.x
- Flask
- Google Generative AI API key

### Installation Steps

1. **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. **Install required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your Google Generative AI API Key:**
   - You need a valid API key from Google.
   - Replace the following line with your API key:

    ```python
    genai.configure(api_key="your_google_api_key")
    ```

4. **Run the Flask application:**

    ```bash
    python app.py
    ```

5. **Open the app in your browser:**

    The app will be available at `http://127.0.0.1:5000/`.

## Usage

### Home Page (`/`)

- The home page provides a form where users can input a list of ingredients.
- Submit the form to get vegetarian meal suggestions or non-vegetarian explanations.

### Meal Suggestions (`/get_meal_suggestions`)

- After the user submits the ingredients, the app checks if any non-vegetarian items are present.
- If non-vegetarian items are detected, it redirects to the non-vegetarian explanation page.
- Otherwise, the app will provide a list of vegetarian meal suggestions.

### Non-Veg Explanations (`/non_veg_explanation`)

- If non-vegetarian items are detected, the app provides an explanation of why consuming these items can be harmful to nature.

## Example

### Vegetarian Meal Suggestions

- **Input Ingredients:** spinach, tomatoes, potatoes
- **Generated Suggestions:** 
    - "Spinach and tomato curry with potatoes."
    - "Vegetarian stir-fry with spinach, tomatoes, and potatoes."

### Non-Veg Explanations

- **Input Ingredient:** Chicken
- **Explanation:** "Eating chicken is harmful to nature because it contributes to deforestation, water wastage, and greenhouse gas emissions."


