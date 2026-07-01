import os
import re

# GCSE HTML Content
gcse_maths = """
<div class="syllabus-module">
    <h3 id="maths" style="font-size: 1.8rem; margin-bottom: 16px; color: var(--text-dark); border-bottom: 2px solid var(--scandi-teal-dark); padding-bottom: 10px;">Mathematics</h3>
    <p style="margin-bottom: 20px;">Our comprehensive GCSE Mathematics programme covers the full spectrum of the Edexcel and AQA specifications, ensuring students build confidence in both foundational arithmetic and advanced problem-solving.</p>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 30px;">
        <div style="background: var(--off-white); padding: 20px; border-radius: 8px;">
            <h4 style="color: var(--scandi-teal-dark); margin-bottom: 10px;">Module 1: Number & Algebra</h4>
            <ul style="list-style: disc; margin-left: 20px; color: var(--text-light);">
                <li>Fractions, Decimals, and Percentages</li>
                <li>Indices, Surds, and Standard Form</li>
                <li>Quadratic Equations and Graphs</li>
                <li>Simultaneous Equations</li>
            </ul>
        </div>
        <div style="background: var(--off-white); padding: 20px; border-radius: 8px;">
            <h4 style="color: var(--scandi-teal-dark); margin-bottom: 10px;">Module 2: Geometry & Measure</h4>
            <ul style="list-style: disc; margin-left: 20px; color: var(--text-light);">
                <li>Trigonometry (SOHCAHTOA, Sine/Cosine Rules)</li>
                <li>Circle Theorems and Proofs</li>
                <li>Area, Volume, and Surface Area</li>
                <li>Vectors and Transformations</li>
            </ul>
        </div>
        <div style="background: var(--off-white); padding: 20px; border-radius: 8px;">
            <h4 style="color: var(--scandi-teal-dark); margin-bottom: 10px;">Module 3: Statistics & Probability</h4>
            <ul style="list-style: disc; margin-left: 20px; color: var(--text-light);">
                <li>Histograms and Cumulative Frequency</li>
                <li>Conditional Probability and Tree Diagrams</li>
                <li>Scatter Graphs and Correlation</li>
            </ul>
        </div>
    </div>
    
    <div style="background: #eef5f9; padding: 24px; border-radius: 12px; border: 1px solid #b8daff; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 20px;">
        <div>
            <h4 style="margin-bottom: 5px; color: #004085;">Download Previous Year Papers</h4>
            <p style="font-size: 0.9rem; color: #004085; margin: 0;">Official AQA/Edexcel Past Papers & Mark Schemes</p>
        </div>
        <div style="display: flex; gap: 10px;">
            <a href="https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-83001H-QP-JUN22.PDF" target="_blank" class="btn-primary" style="padding: 10px 20px; font-size: 0.9rem;"><i class="fas fa-file-pdf"></i> 2022 AQA Higher Paper 1</a>
            <a href="https://qualifications.pearson.com/content/dam/pdf/GCSE/mathematics/2015/exam-materials/1MA1_1H_que_20220520.pdf" target="_blank" class="btn-secondary" style="padding: 10px 20px; font-size: 0.9rem;"><i class="fas fa-file-pdf"></i> 2022 Edexcel Higher Paper 1</a>
        </div>
    </div>
</div>
"""

gcse_english = """
<div class="syllabus-module" style="margin-top: 60px;">
    <h3 id="english" style="font-size: 1.8rem; margin-bottom: 16px; color: var(--text-dark); border-bottom: 2px solid var(--scandi-teal-dark); padding-bottom: 10px;">English Language & Literature</h3>
    <p style="margin-bottom: 20px;">Our English syllabus develops critical reading, analytical thinking, and sophisticated writing skills required for top grades in AQA and Edexcel exams.</p>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 30px;">
        <div style="background: var(--off-white); padding: 20px; border-radius: 8px;">
            <h4 style="color: var(--scandi-teal-dark); margin-bottom: 10px;">English Language</h4>
            <ul style="list-style: disc; margin-left: 20px; color: var(--text-light);">
                <li>Explorations in Creative Reading & Writing</li>
                <li>Writers' Viewpoints and Perspectives</li>
                <li>Descriptive and Narrative Writing</li>
                <li>Writing to Argue, Persuade, and Advise</li>
            </ul>
        </div>
        <div style="background: var(--off-white); padding: 20px; border-radius: 8px;">
            <h4 style="color: var(--scandi-teal-dark); margin-bottom: 10px;">English Literature</h4>
            <ul style="list-style: disc; margin-left: 20px; color: var(--text-light);">
                <li>Shakespeare (e.g., Macbeth, Romeo & Juliet)</li>
                <li>19th-Century Novel (e.g., A Christmas Carol)</li>
                <li>Modern Prose or Drama (e.g., An Inspector Calls)</li>
                <li>Poetry Anthology (Power and Conflict)</li>
            </ul>
        </div>
    </div>
    
    <div style="background: #eef5f9; padding: 24px; border-radius: 12px; border: 1px solid #b8daff; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 20px;">
        <div>
            <h4 style="margin-bottom: 5px; color: #004085;">Download Previous Year Papers</h4>
            <p style="font-size: 0.9rem; color: #004085; margin: 0;">Official AQA Past Papers & Mark Schemes</p>
        </div>
        <div style="display: flex; gap: 10px;">
            <a href="https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-87001-QP-JUN22.PDF" target="_blank" class="btn-primary" style="padding: 10px 20px; font-size: 0.9rem;"><i class="fas fa-file-pdf"></i> 2022 Language Paper 1</a>
            <a href="https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-87021-QP-JUN22.PDF" target="_blank" class="btn-secondary" style="padding: 10px 20px; font-size: 0.9rem;"><i class="fas fa-file-pdf"></i> 2022 Literature Paper 1</a>
        </div>
    </div>
</div>
"""


alevel_maths = """
<div class="syllabus-module">
    <h3 id="maths" style="font-size: 1.8rem; margin-bottom: 16px; color: var(--text-dark); border-bottom: 2px solid var(--scandi-teal-dark); padding-bottom: 10px;">Mathematics & Further Mathematics</h3>
    <p style="margin-bottom: 20px;">Our A-Level Mathematics curriculum is rigorous and expansive, preparing students for university-level STEM degrees through deep exploration of Pure Maths, Mechanics, and Statistics.</p>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 30px;">
        <div style="background: var(--off-white); padding: 20px; border-radius: 8px;">
            <h4 style="color: var(--scandi-teal-dark); margin-bottom: 10px;">Pure Mathematics</h4>
            <ul style="list-style: disc; margin-left: 20px; color: var(--text-light);">
                <li>Algebraic Methods and Functions</li>
                <li>Coordinate Geometry and Parametric Equations</li>
                <li>Advanced Calculus (Differentiation & Integration)</li>
                <li>Numerical Methods and Vectors</li>
            </ul>
        </div>
        <div style="background: var(--off-white); padding: 20px; border-radius: 8px;">
            <h4 style="color: var(--scandi-teal-dark); margin-bottom: 10px;">Applied Mathematics</h4>
            <ul style="list-style: disc; margin-left: 20px; color: var(--text-light);">
                <li>Mechanics: Kinematics, Forces, Moments, and Projectiles</li>
                <li>Statistics: Hypothesis Testing, Probability Distributions (Binomial & Normal)</li>
                <li>Data Presentation and Interpretation</li>
            </ul>
        </div>
        <div style="background: var(--off-white); padding: 20px; border-radius: 8px;">
            <h4 style="color: var(--scandi-teal-dark); margin-bottom: 10px;">Further Mathematics</h4>
            <ul style="list-style: disc; margin-left: 20px; color: var(--text-light);">
                <li>Complex Numbers and Argand Diagrams</li>
                <li>Matrices and Transformations</li>
                <li>Proof by Induction and Maclaurin Series</li>
                <li>Differential Equations</li>
            </ul>
        </div>
    </div>
    
    <div style="background: #eef5f9; padding: 24px; border-radius: 12px; border: 1px solid #b8daff; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 20px;">
        <div>
            <h4 style="margin-bottom: 5px; color: #004085;">Download Previous Year Papers</h4>
            <p style="font-size: 0.9rem; color: #004085; margin: 0;">Official Edexcel A-Level Past Papers</p>
        </div>
        <div style="display: flex; gap: 10px;">
            <a href="https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/exam-materials/9MA0_01_que_20220607.pdf" target="_blank" class="btn-primary" style="padding: 10px 20px; font-size: 0.9rem;"><i class="fas fa-file-pdf"></i> 2022 Edexcel Pure Maths 1</a>
            <a href="https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/exam-materials/9MA0_03_que_20220621.pdf" target="_blank" class="btn-secondary" style="padding: 10px 20px; font-size: 0.9rem;"><i class="fas fa-file-pdf"></i> 2022 Edexcel Applied Maths</a>
        </div>
    </div>
</div>
"""

# Let's read gcse.html and alevel.html and replace their simple list content with these detailed modules.

def process_html():
    gcse_path = "c:/Users/steph/Downloads/theos/website/templates/website/gcse.html"
    if os.path.exists(gcse_path):
        with open(gcse_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the entire <div class="stagger"> block in GCSE that contains Maths and English
        # with our new rich modules.
        # We will just find the <section> that has these and replace its inner contents.
        
        start_str = '<div class="stagger" style="display: grid;'
        end_str = '</section>'
        
        if start_str in content:
            before = content.split(start_str)[0]
            # Replace the simple boxes with our rich modules
            new_content = before + '<div style="max-width: 1000px; margin: 0 auto; text-align: left;">\n' + gcse_maths + '\n' + gcse_english + '\n</div>\n</section>'
            
            with open(gcse_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
                print("Updated GCSE HTML")

    alevel_path = "c:/Users/steph/Downloads/theos/website/templates/website/alevel.html"
    if os.path.exists(alevel_path):
        with open(alevel_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        start_str = '<div class="stagger" style="display: grid;'
        end_str = '</section>'
        
        if start_str in content:
            before = content.split(start_str)[0]
            new_content = before + '<div style="max-width: 1000px; margin: 0 auto; text-align: left;">\n' + alevel_maths + '\n</div>\n</section>'
            
            with open(alevel_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
                print("Updated A-Level HTML")

if __name__ == "__main__":
    process_html()
