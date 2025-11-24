# Ancestry-ai
# Ancestry-ai
AncestryAI: Intelligent Lineage Advisor

Student Name: Pratiksha Jain

Course: Fundamentals of AI & ML

Project Type: Rule-Based Expert System

1. Project Overview

AncestryAI is an expert system designed to track family lineages and deduce complex relationships dynamically. Unlike static family trees, this system uses a Prolog Inference Engine to calculate relationships (like cousins, ancestors, and in-laws) based on logical rules rather than hard-coded database entries.

2. Features

Inference Engine: Automatically deduces implicit relationships.

Recursive Logic: Implements recursive depth searches for finding all ancestors.

Dynamic Learning: Allows users to add new family members at runtime.

Hybrid Architecture: Combines Python (Interface) with Prolog (Logic).

3. Prerequisites

To run this project, you need:

Python 3.x installed.

SWI-Prolog installed and added to your system PATH.

Download: https://www.swi-prolog.org/download/stable

Important: Select "Add swipl to system PATH" during installation.

4. Installation

Clone this repository.

Install dependencies:

pip install -r requirements.txt


Ensure your folder structure is:

/AncestryAI
   /logic
      family_rules.pl
   /src
      app.py
      ancestry_engine.py


5. Usage

Navigate to the src folder and run the application:

cd src
python app.py
