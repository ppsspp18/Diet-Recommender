# Diet Recommender using CrewAI

## Overview

Diet Recommender is an AI-powered healthcare assistant that analyzes health reports and generates personalized diet recommendations using a multi-agent workflow built with CrewAI.

The system allows users to upload medical documents through a graphical user interface (GUI). The uploaded document is processed using OCR technology to extract text, which is then analyzed by a team of AI agents that collaboratively generate diet plan.

The primary objective of this project is to demonstrate the implementation of Agentic AI workflows using CrewAI while solving a practical healthcare-related problem.

---

## Features

* Upload scanned health reports and prescriptions
* OCR-based text extraction using Tesseract
* Image preprocessing using Pillow
* Multi-agent workflow using CrewAI
* Automatic correction of OCR-generated text
* Extraction of health parameters and medications
* Identification of health conditions mentioned in reports
* Personalized vegetarian diet recommendations
* Personalized non-vegetarian diet recommendations
* YAML-based agent and task configuration
* Secure API key management using .env

---

## System Architecture

User Uploads Health Report

↓

Image Preprocessing (Pillow)

↓

OCR Extraction (Tesseract OCR)

↓

Text Corrector Agent

↓

Health Parameter Extraction Agent

↓

Diet Planner Agent

↓

Vegetarian & Non-Vegetarian Diet Plans

---

## Technologies Used

### Programming Language

* Python

### GUI

* Tkinter

### OCR

* Tesseract OCR Engine
* pytesseract

### Image Processing

* Pillow (PIL) : height and width resize to double, convert it to black and white, increase contrast to make text darker, 
  

### Agent Framework

* CrewAI

### Configuration

* YAML

### Environment Management

* python-dotenv

---

## Agent Design

### 1. Text Corrector Agent

#### Role

Text Corrector

#### Goal

Correct spelling, grammatical, and formatting errors present in OCR-generated text.

#### Backstory

An experienced editor specializing in identifying and correcting OCR-related mistakes.

#### Responsibilities

* Correct spelling errors
* Improve grammar
* Enhance readability
* Preserve medical information

---

### 2. Health Parameter Extraction Agent

#### Role

Health Parameter Extractor

#### Goal

Extract important medical information from the corrected health report.

#### Backstory

An expert medical information extraction assistant capable of identifying health parameters, medications, and health conditions from unstructured medical documents.

#### Responsibilities

* Extract laboratory values
* Identify medications
* Extract medical conditions
* Organize information into structured output

---

### 3. Diet Planner Agent

#### Role

Diet Planner

#### Goal

Generate personalized diet recommendations based on extracted health information.

#### Backstory

A professional nutrition planner capable of creating customized dietary recommendations based on patient health data.

#### Responsibilities

* Analyze extracted health information
* Create vegetarian diet plans
* Create non-vegetarian diet plans
* Provide practical dietary recommendations

---

## Tasks

### Text Correction Task

Input:
OCR Extracted Text

Output:
Cleaned and grammatically corrected text

---

### Health Parameter Extraction Task

Input:
Corrected Health Report

Output:
Structured health parameters, medications, and medical conditions

---

### Diet Planning Task

Input:
Extracted health information

Output:
Customized diet plan

---

## CrewAI Workflow

The project uses a Sequential Process workflow.

Each task depends on the output of the previous task.

Step 1:
OCR extracts text from the uploaded document.

Step 2:
Text Corrector Agent cleans the extracted text.

Step 3:
Health Parameter Extraction Agent extracts important medical information.

Step 4:
Diet Planner Agent generates personalized diet plans.

This sequential architecture ensures that every stage receives improved and structured information from the previous stage.

---

## Configuration

Agents and tasks are defined using YAML configuration files.

### Agent Configuration

Each agent contains:

* Role
* Goal
* Backstory

### Task Configuration

Each task contains:

* Description
* Expected Output
* Input
* Assigned Agent

---

## Security

Sensitive credentials such as API keys are stored securely using environment variables.

Example:

.env

OPENAI_API_KEY=your_api_key

---

## Learning Outcomes

This project helped in understanding:

* Agentic AI architecture
* CrewAI framework
* Multi-agent collaboration
* Sequential workflow orchestration
* Prompt engineering
* OCR pipelines
* AI-powered document processing
* Healthcare data extraction
* End-to-end AI application development

---

## Limitations

* OCR accuracy depends on document quality.
* The generated diet plans are AI-generated recommendations and should not replace professional medical advice.
* The system does not perform certified medical diagnosis.
* Results depend on the quality of extracted text and LLM responses.

---

## Future Improvements

* Integration with medical knowledge bases
* Validation using clinical guidelines
* Advanced OCR models
* PDF support
* Multi-language health report processing
* Retrieval-Augmented Generation (RAG)
* Human-in-the-loop verification
* Deployment as a web application

---

## Project Goal

The primary purpose of this project was to learn and implement Agentic AI workflows using CrewAI by designing a practical multi-agent system capable of processing medical reports and generating personalized diet recommendations.
