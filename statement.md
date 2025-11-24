Project Statement: AncestryAI

1. Problem Statement

Tracing complex family lineages and determining legal or biological relationships manually is error-prone and time-consuming for large families. Traditional static databases cannot easily infer relationships (like "cousin" or "ancestor") without explicit entries for every connection. There is a need for an intelligent system that can store basic facts and logically deduce complex relationships automatically.

2. Scope of the Project

AncestryAI is a desktop-based Expert System designed to:

Store family genealogy data (Facts) in a logic-based format.

Apply logical rules to infer relationships (Rules) using a Prolog engine.

Visualize lineage and provide answers to natural language-style queries.

Allow dynamic expansion of the family tree by end-users without modifying source code.

3. Target Users

Genealogists & Historians: For digitizing and analyzing historical family trees.

Legal Advisors: For determining legal heirs and succession planning based on lineage rules.

General Users: For maintaining personal family records and exploring ancestry.

4. High-Level Features

Inference Engine: Automatically calculates implied relationships (Grandparents, Cousins, In-laws) using logical deduction.

Recursive Search: Identifies all ancestors or descendants of a specific individual regardless of tree depth (e.g., Great-Great-Grandparents).

Dynamic Updates: Users can add new family members via the Python interface, which updates the Prolog Knowledge Base in real-time.

Truth Validation: Verifies if a claimed relationship between two individuals is valid (True/False testing).
