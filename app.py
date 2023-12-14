import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

def generate_recipe_ideas(meal_category, preferences):
    try:
        prompt = f"Imagine you are a seasoned chef preparing a {meal_category.lower()} dish for a special occasion. Your goal is to create a unique and unforgettable recipe that combines {preferences} flavors. Consider using unconventional ingredients or cooking techniques to surprise and delight the diners. Provide a step-by-step guide with detailed instructions and a list of ingredients for this exceptional {meal_category.lower()} experience."

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1500,  # Adjust max_tokens as needed
            temperature=0.7,
        )
        
        # Returning the complete response text without processing
        return response.choices[0].text
    except Exception as e:
        return str(e)
    
# if want to process
def process_recipe_response(text):
    # You need to implement this function to parse the GPT response
    # and structure it into a format suitable for display.
    pass


# Set the layout to a wide format
st.set_page_config(layout="wide")

# List of meal categories
meal_categories = ["Breakfast", "Lunch", "Dinner"]

# Left section
left_col = st.sidebar
left_col.title("Recipe Idea Generator:")

# Box for meal category selection
selected_category = left_col.selectbox("Select Meal Category", meal_categories)

# Box for any specific preferences or details
recipe_preferences = left_col.text_area("Any specific preferences or details?", height=100, max_chars=500)

# Button to generate recipe ideas
generate_button_clicked = left_col.button(label="Generate Recipes", key="generate_button", help="Click to generate recipe ideas")

# Variables for controlling the display speed
delay_between_sentences = 0.2

# Right section
right_col = st
right_col.title("Generated Recipes")

# Generate recipe ideas using GPT API when the button is pressed
if generate_button_clicked and selected_category:

    generated_recipes = generate_recipe_ideas(selected_category, recipe_preferences)

    if generated_recipes:
        st.text_area("Recipes:", generated_recipes, height=400)

