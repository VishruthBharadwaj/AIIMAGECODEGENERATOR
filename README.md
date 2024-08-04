# AIIMAGECODEGENERATOR
Shape Drawing Automation


This project automates the process of generating and drawing shapes with specified colors using Python and Matplotlib, with the assistance of OpenAI's GPT-4 model. The main steps include generating a prompt, receiving Python code from the AI model, executing the code to create an image, and verifying the output.

Installation
Clone the repository

pip install openai matplotlib numpy


Configuration
Set your OpenAI API key in the script:

openai.api_key = 'your-api-key-here'


Run the script:

python shape_drawing.py




Steps
Shape Selection:

The AI model randomly selects a 2D or 3D shape from a predefined list.
Color Assignment:

The model chooses a random color or set of colors for the shape and specifies the areas to be colored.
Code Generation:

The AI model generates Python code to create the specified shapes and apply the colors using Matplotlib.
File Creation and Dependency Installation:

The Python application receives the generated code, creates necessary script files, and ensures all dependencies are installed.
Code Execution:

The app executes the generated Python code to draw the shapes and generate an image.
Image Production:

The image is created based on the executed code and saved to the specified output path.
Image Verification:

The generated image is sent back to the AI model for verification to ensure it matches the initial plan. It checks that all shapes are present and correctly rendered.
Feedback and Regeneration (if needed):

If the image verification fails, feedback is provided to the AI model, and the image is regenerated as necessary.
Example Output
The script will generate images with random shapes and colors, save them to the working directory, and print verification results for each image.



Notes
Ensure that your OpenAI API key is kept secure and not shared publicly.
The current image verification process is a placeholder and always returns True for demonstration purposes. It should be replaced with actual image verification logic based on specific requirements.


