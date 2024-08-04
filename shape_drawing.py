import openai
import os
import random
from datetime import datetime
import time
import matplotlib.pyplot as plt
import numpy as np

# Set your OpenAI API key here
openai.api_key = 'your-api-key-here'

class OpenAIClient:
    def __init__(self):
        self.client = openai

    def generate_prompt(self):
        shapes = ['circle', 'square', 'triangle', 'cube', 'sphere', 'pyramid']
        colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
        shape = random.choice(shapes)
        num_colors = random.randint(1, 3)
        color_list = random.sample(colors, num_colors)
        
        prompt = (
        f"Generate Python code to draw a {shape} with colors "
        f"{', '.join(color_list)} using matplotlib. Ensure that the code is valid, "
        f"and for shapes that require vertices, ensure the vertices are defined with the correct 2D shape (M, 2) "
        f"or 3D shape (M, 3) as needed. Only include the code, without any explanations or comments."
    )
        return prompt

def generate_code(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.7
    )
    response_text = response.choices[0]['message']['content'].strip()
    code_start = response_text.find('```') + 3
    code_end = response_text.rfind('```')
    code = response_text[code_start:code_end].strip()

    # Remove any leading or trailing non-code lines
    code_lines = code.split('\n')
    code_lines = [line for line in code_lines if not any(keyword in line.lower() for keyword in ['python', 'here', 'code:', 'example'])]

    # Fix common issues with generated code
    for i, line in enumerate(code_lines):
        if line.startswith('port'):
            code_lines[i] = 'import' + line[4:]
        if 'plt.show(' in line:
            code_lines[i] = 'plt.show()'
    
    # Ensure import statements are present
    if not any('import matplotlib' in line for line in code_lines):
        code_lines.insert(0, 'import matplotlib.pyplot as plt')
    if not any('import numpy' in line for line in code_lines):
        code_lines.insert(1, 'import numpy as np')

    code = '\n'.join(code_lines)

    return code

def save_and_execute_code(code, output_path, script_path):
    # Insert plt.savefig() before plt.show()
    if 'plt.show()' in code:
        code = code.replace('plt.show()', f'plt.savefig("{output_path}")\nplt.show()')
    else:
        code += f'\nplt.savefig("{output_path}")'
    
    code += '\nplt.close()'  # Ensure plt.close() is called at the end
    
    with open(script_path, "w") as code_file:
        code_file.write(code)
    
    time.sleep(2)  # Wait for file system operations to complete
    exec(open(script_path).read())
    time.sleep(2)  # Ensure that the image file has been written

def verify_image(image_path, prompt):
    # Placeholder for an image verification process.
    # This function currently just returns True for demonstration purposes.
    print(f"Verifying image '{image_path}' with prompt: {prompt}")
    return True  # Assume verification passed for this example

def main():
    client = OpenAIClient()
    
    # Generate and save images
    for i in range(10):
        prompt = client.generate_prompt()
        print(f"Generated Prompt: {prompt}")
        
        # Generate code from the AI model
        code = generate_code(prompt)
        print("Generated Code:\n", code)
        
        # Generate a unique filename using timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = f"image_{timestamp}_{i}.png"
        script_path = f"generated_code_{timestamp}_{i}.py"
        
        # Save and execute the generated code to create the image
        save_and_execute_code(code, output_path, script_path)
        
        # Verify the image
        if verify_image(output_path, prompt):
            print(f"Image verification passed: {output_path}")
        else:
            print("Image verification failed. Regenerating image...")
            code = generate_code(prompt)
            save_and_execute_code(code, output_path, script_path)
        
        # No need to delete the image
        # os.remove(output_path)

if __name__ == "__main__":
    main()
