import os
import subprocess

def createDoc(doc_name, content):
    """
    Creates a LaTeX document, compiles it to a PDF, and cleans up auxiliary files.
    """
    
    document_path = f"{doc_name}.tex"
    write_content_to_file(document_path, content)
    if compile_latex(document_path):
        print("PDF created successfully.")
    else:
        print("PDF creation failed.")
    clean_auxiliary_files(doc_name)

def write_content_to_file(file_path, content):
    """
    Writes the provided content to a specified file.
    """
    with open(file_path, "w") as file:
        file.write(content)

def compile_latex(file_path):
    """
    Compiles the specified LaTeX file to PDF using pdflatex.
    Returns True if successful, False otherwise.
    """
    try:
        subprocess.run(["pdflatex", file_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError as error:
        print(f"Error during PDF compilation: {error}")
        return False

def clean_auxiliary_files(doc_name):
    """
    Removes LaTeX auxiliary files generated during compilation.
    """
    extensions = [".aux", ".log", ".out", ".tex"]
    for ext in extensions:
        file_path = f"{doc_name}{ext}"
        try:
            os.remove(file_path)
        except FileNotFoundError:
            continue
