import os
import openai

openai.api_key = ''


def load_scripts_from_folder(folder_path):
    scripts = {}

    for filename in os.listdir(folder_path):
        if filename.endswith('.py'):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                scripts[filename] = file.read()

    return scripts


def generate_prompt(script_content):
    return f'Поменяй стиль следующего кода и верни только код:\n\n{script_content}\n\n'


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

# TODO: save only code
def main(scripts_folder, generated_folder):
    if not os.path.exists(scripts_folder):
        os.makedirs(scripts_folder)

    if not os.path.exists(generated_folder):
        os.makedirs(generated_folder)

    for filename, script_content in load_scripts_from_folder(scripts_folder).items():
        new_script_content = get_completion(generate_prompt(script_content))
        save_generated_script(filename, new_script_content, generated_folder)
        print(f"Скрипт {filename} дополнен и сохранен в {generated_folder}.")


if __name__ == '__main__':
    main('scripts', 'generated')
