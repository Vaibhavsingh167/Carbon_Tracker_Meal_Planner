from flask import Flask, render_template, request, redirect, url_for, flash
import google.generativeai as genai
import re

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Ensure you have a secret key for sessions

# Initialize Google Generative AI
genai.configure(api_key="AIzaSyA_CXDGqn0nmoLeKd60yUg8l7F9uL3PSgk")  # Ensure your API key is set in the environment
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# List of common non-vegetarian items
non_veg_items = ['chicken', 'beef', 'pork', 'fish', 'shrimp', 'bacon', 'turkey', 'lamb']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_meal_suggestions', methods=['POST'])
def get_meal_suggestions():
    if request.method == 'POST':
        items = request.form.get('items', '').split(',')
        items = [item.strip().lower() for item in items if item.strip()]
        
        if not items:
            flash('Please enter at least one item.')
            return redirect(url_for('index'))

        # Check for non-vegetarian items
        entered_non_veg_items = [item for item in items if item in non_veg_items]

        if entered_non_veg_items:
            # Redirect to the non-veg explanations page if any non-veg items are found
            return redirect(url_for('non_veg_explanation', items=','.join(entered_non_veg_items)))

        # Call the Google Gen AI service to fetch vegetarian meal suggestions
        vegetarian_meal_suggestions = fetch_meal_suggestions(items)

        return render_template('results.html', items=items, meal_suggestions=vegetarian_meal_suggestions)

@app.route('/non_veg_explanation')
def non_veg_explanation():
    items = request.args.get('items', '').split(',')
    non_veg_explanations = {item: fetch_non_veg_explanation(item) for item in items}

    return render_template('non_veg_explanation.html', non_veg_explanations=non_veg_explanations)

def fetch_meal_suggestions(items):
    item_list = ', '.join(items)
    try:
        response = model.generate_content(f"Suggest 3-5 vegetarian meals with these ingredients: {item_list}. If all items are non-veg, respond that no vegetarian meals can be formed.")
        suggestions = response.text.strip()

        # Clean up the text by removing numbering, asterisks, and unnecessary symbols
        cleaned_suggestions = re.sub(r'\d+\.\s*|\d+\)\s*|\*\*?', '', suggestions)
        suggestions_list = [s.strip() for s in cleaned_suggestions.split('\n') if s.strip()]

        return suggestions_list or ['No vegetarian meal suggestions available.']
    except Exception as e:
        print("Error fetching vegetarian meal suggestions:", e)
        return ['Error occurred while fetching suggestions.']

def fetch_non_veg_explanation(item):
    try:
        response = model.generate_content(f"Explain briefly in 2-3 sentences why eating {item} can be harmful to nature.")
        explanation = response.text.strip()
        return explanation or 'No explanation available.'
    except Exception as e:
        print(f"Error fetching explanation for {item}:", e)
        return 'Error occurred while fetching explanation.'

if __name__ == '__main__':
    app.run(debug=True)
