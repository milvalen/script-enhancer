import os
import openai

openai.api_key = ''
GENERATED_FOLDER = 'generated'
SCRIPTS_FOLDER = 'scripts'


def load_scripts_from_folder(folder_path):
    scripts = {}

    for filename in os.listdir(folder_path):
        if filename.endswith('.py'):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                scripts[filename] = file.read()

    return scripts


def generate_prompt(script_content):
    return f'Change the style of the following code and return only the code:\n\n{script_content}\n\n'


def get_completion(prompt):
    return openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    ).choices[0].text.strip()


def save_generated_script(filename, content, output_folder):
    with open(os.path.join(output_folder, filename), 'w', encoding='utf-8') as file:
        file.write(content)


if __name__ == '__main__':
    if not os.path.exists(GENERATED_FOLDER):
        os.makedirs(GENERATED_FOLDER)

    for filename, script_content in load_scripts_from_folder(SCRIPTS_FOLDER).items():
        new_script_content = get_completion(generate_prompt(script_content))
        save_generated_script(filename, new_script_content, GENERATED_FOLDER)
        print(f'The {filename} script has been updated and saved in {GENERATED_FOLDER}.')
