#!/usr/bin/env python
import sys
import warnings
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\user_d\tesseract\tesseract.exe'

from datetime import datetime

from diet_recommender.crew import DietRecommender

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def extract_text_from_image(image_path):
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)

root = tk.Tk()
root.title("Health Document Uploader")
root.geometry("600x400")

def run():
    file_path = filedialog.askopenfilename(
        filetypes=[("Documents", "*.png *.jpg *.jpeg *.pdf")]
    )
    if file_path:
        if file_path.endswith(('.png', '.jpg', '.jpeg')):
            extracted = extract_text_from_image(file_path)
            root.destroy()
        else:
            messagebox.showerror("Error", "Unsupported file format.")
            return

        print("Extracted text ready to send to CrewAI:", extracted[:300])  # return string
    
    inputs = {
        'extracted_text': extracted,
    }
    
    try:
        DietRecommender().crew().kickoff(inputs=inputs)
        messagebox.showinfo("Success", "Diet generated successfully.")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        DietRecommender().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        DietRecommender().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        DietRecommender().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

upload_btn = tk.Button(root, text="Upload Health Document", command=run)
upload_btn.pack(pady=20)

text_box = tk.Text(root, wrap="word", height=20)
text_box.pack(padx=10, pady=10, fill="both", expand=True)
