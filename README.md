<div align="center">
<h1>FlavorForge - Your AI-Powered Recipe Generator</h1>

![FlavorForge Logo](flavorforge_logo.png)
</div>

FlavorForge is an AI-powered web app that generates creative and delicious recipe ideas for breakfast, lunch, and dinner. It leverages the power of ChatGPT to provide users with unique recipes based on meal category preferences and additional details.

## Features

- **Meal Category Selection:** Choose from breakfast, lunch, or dinner to generate recipes tailored to your preferences.
- **Custom Preferences:** Add specific preferences or details to further personalize your recipe suggestions.
- **Interactive Display:** View generated recipes with ingredients and instructions in an interactive format.

<!-- ## Demo

![FlavorForge Demo](screenshot.png) -->

## Getting Started

To run FlavorForge locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/nabinbhatt/flavorforge.git
   ```

2. Install dependencies:

   ```bash
   cd flavorforge
   pip install -r requirements.txt
   ```

3. On the file `app.py` Enter your [OpenAI API key](https://platform.openai.com/api-keys) 

    ```python
    openai.api_key = "YOUR_API_KEY"
    ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

5. Access the app in your browser at `http://localhost:8501`.

## Usage

1. Select the meal category (breakfast, lunch, or dinner).
2. Add any specific preferences or details.
3. Click the "Generate Recipes" button.
4. Explore the AI-generated recipes presented.


<center>
<br>

<br>
</center>

Thanks to [OpenAI](https://openai.com) and Streamlit. This project is licensed under the [MIT License](LICENSE). <br>
For questions or feedback, you can contact me on Twitter ([@thenabinbhatt](http://x.com/thenabinbhatt))