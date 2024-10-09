AI Recipe Generator

AI Recipe Generator is a Python-based application that utilizes OpenAI’s ChatGPT API to provide detailed recipes based on user-selected dishes. This project offers an interactive and innovative experience, allowing users to explore various dishes and instantly receive corresponding recipes with ingredients and preparation steps.

Features

	•	Select a dish, and the AI generates the full recipe.
	•	Get a list of ingredients and detailed preparation instructions.
	•	Supports multiple cuisines and dietary preferences.
	•	Leverages OpenAI’s ChatGPT API for natural language understanding and recipe generation.

Technologies Used

	•	Python 3.x: Core programming language.
	•	OpenAI API (ChatGPT): AI model used to generate recipes based on dish selection.
	•	Flask/Django (optional): For web-based interfaces if needed.
	•	Requests: For API calls to the ChatGPT model.

Installation

	1.	Clone the repository:
 git clone https://github.com/your-username/AIRecipeGenerator.git
cd AIRecipeGenerator

	2.	Install required dependencies:
 pip install -r requirements.txt
 
	3.	Set up your OpenAI API key:
 OPENAI_API_KEY=your_openai_api_key
 
 Usage
 
    1.	Run the Python script to start the application:
  python app.py
  
    2.	Select a dish from the list of available options, and the AI will generate a recipe for you.
   	3.	(Optional) If you have a web-based interface, you can access the app in your browser at http://localhost:5000.

  Example
    Enter the dish name: Spaghetti Carbonara

Recipe for Spaghetti Carbonara:
1. Ingredients:
   - Spaghetti
   - Eggs
   - Parmesan cheese
   - Pancetta
   - Black pepper
   - Salt

2. Instructions:
   1. Cook the spaghetti.
   2. Fry the pancetta until crisp.
   3. Whisk the eggs and parmesan together.
   4. Mix the pasta with pancetta, then stir in the egg mixture.
   5. Serve with black pepper and more parmesan.
  
API Reference

    import openai

    def get_recipe(dish_name):
        openai.api_key = "your_openai_api_key"
    
    prompt = f"Give me the recipe for {dish_name}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()


   	
