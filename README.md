# Unifier_TXT_CLI-Mode-v1.0

# Ferramenta de Concatenação de Arquivos (Automação)

## Descrição
Este CLI concatena arquivos de texto em um diretório, ignorando certos tipos de arquivos no diretório onde ele se encontra.

## Funcionalidades
- Ignora arquivos com extensões específicas (`.exe`, `.py`, `.jpg`, `.xlsx`).
- Concatena arquivos de texto em um único arquivo com linhas em branco entre eles.
- Cria uma pasta com o nome do arquivo de saída para armazenar o arquivo concatenado.

## Uso

1. Coloque o Script no diretório onde estão os arquivos de texto que você deseja concatenar.
2. Execute o script usando Python, ou a partir da linha de comando:
    ```bash
    python nome_do_script.pyw
    ```
3. O script criará um arquivo concatenado no diretório selecionado e moverá esse arquivo para uma nova pasta criada no mesmo diretório.

## Requisitos

- Python 3.x

## Bibliotecas Utilizadas

```python
import os
import re
from collections import Counter
