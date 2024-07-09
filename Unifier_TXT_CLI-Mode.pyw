import os
import re
from collections import Counter


def get_most_common_prefix(files):
    prefixes = []
    for file in files:
        if file.endswith('.txt'):
            prefix = re.sub(r'\d+', '', file).strip().rsplit('.', 1)[0]
            prefixes.append(prefix)

    if prefixes:
        most_common_prefix, _ = Counter(prefixes).most_common(1)[0]
        return most_common_prefix
    return "AGRP"


def add_final_newline(filename):
    with open(filename, 'r+') as f:
        try:
            f.seek(-1, os.SEEK_END)
            last_char = f.read(1)
            if last_char != '\n':
                f.write('\n')
        except IOError:
            f.write('\n')


def concatenate_files(directory):
    # Excluir arquivos .exe, .py, .pyw, imagens e Excel
    exclude_extensions = ['.exe', '.py', '.pyw', '.jpg', '.jpeg', '.png', '.xls', '.xlsx']
    files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))
             and not any(file.endswith(ext) for ext in exclude_extensions)]

    most_common_prefix = get_most_common_prefix(files)
    output_filename = f"{most_common_prefix}_ARQUIVOS_AGRUPADOS.txt"
    output_filepath = os.path.join(directory, output_filename)

    linha_em_branco = "\n"  # Apenas uma linha em branco para separar os arquivos

    with open(output_filepath, 'w') as outfile:
        for i, file in enumerate(files):
            with open(os.path.join(directory, file), 'r') as infile:
                for line in infile:
                    if line.strip():
                        outfile.write(line)
            if i < len(files) - 1:
                outfile.write(linha_em_branco)

    add_final_newline(output_filepath)

    folder_name = output_filename.replace('.txt', '')
    output_folder_path = os.path.join(directory, folder_name)
    os.makedirs(output_folder_path, exist_ok=True)
    os.replace(output_filepath, os.path.join(output_folder_path, output_filename))

    print(f"Arquivos concatenados e pasta '{folder_name}' criada com sucesso em '{output_folder_path}'!")


concatenate_files(os.path.dirname(os.path.abspath(__file__)))
