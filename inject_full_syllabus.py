import os
import re

def update_alevel():
    path = "c:/Users/steph/Downloads/theos/website/templates/website/alevel.html"
    if not os.path.exists(path): return

    detailed_syllabus = """
    <!-- Detailed Syllabus Sections -->
    <section class="section" style="background: #fdfdfd;">
        <div class="container" style="max-width: 1000px;">
            <h2 style="text-align: center; margin-bottom: 50px; font-size: 2.5rem;">Detailed Syllabus & Past Papers Library</h2>
            
            <!-- MATHEMATICS -->
            <div id="maths" class="syllabus-module" style="margin-bottom: 80px; padding: 40px; background: white; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                <div style="display: flex; align-items: center; gap: 15px; border-bottom: 3px solid var(--scandi-teal-dark); padding-bottom: 15px; margin-bottom: 30px;">
                    <i class="fas fa-infinity" style="font-size: 2.5rem; color: var(--scandi-teal-dark);"></i>
                    <h3 style="font-size: 2.2rem; margin: 0; color: var(--text-dark);">A-Level Mathematics & Further Maths</h3>
                </div>
                
                <p style="font-size: 1.1rem; color: var(--text-light); margin-bottom: 30px;">Our A-Level Mathematics curriculum is rigorous and expansive, preparing students for university-level STEM degrees through deep exploration of Pure Maths, Mechanics, and Statistics.</p>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-bottom: 40px;">
                    <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                        <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-square-root-alt"></i> Pure Mathematics</h4>
                        <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Algebraic Methods and Functions</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Coordinate Geometry & Parametric Equations</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Advanced Calculus (Differentiation & Integration)</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Numerical Methods and Vectors</li>
                        </ul>
                    </div>
                    <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                        <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-balance-scale"></i> Applied Mathematics</h4>
                        <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Kinematics, Forces, Moments</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Hypothesis Testing, Probability Distributions</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Data Presentation and Interpretation</li>
                        </ul>
                    </div>
                    <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                        <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-calculator"></i> Further Mathematics</h4>
                        <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Complex Numbers and Argand Diagrams</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Matrices and Transformations</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Differential Equations</li>
                        </ul>
                    </div>
                </div>

                <!-- Past Papers Table -->
                <div style="background: #f8faff; border: 1px solid #cce5ff; border-radius: 12px; overflow: hidden;">
                    <div style="background: #0056b3; color: white; padding: 15px 24px; font-weight: 700; font-size: 1.2rem;">
                        <i class="fas fa-file-pdf" style="margin-right: 10px;"></i> Past Papers Library
                    </div>
                    <div style="padding: 24px;">
                        <table style="width: 100%; border-collapse: collapse; text-align: left;">
                            <thead>
                                <tr style="border-bottom: 2px solid #dee2e6;">
                                    <th style="padding: 12px; color: #495057;">Board</th>
                                    <th style="padding: 12px; color: #495057;">Year</th>
                                    <th style="padding: 12px; color: #495057;">Pure Maths 1</th>
                                    <th style="padding: 12px; color: #495057;">Applied Maths 1</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr style="border-bottom: 1px solid #eee;">
                                    <td style="padding: 12px; font-weight: 600;">Edexcel</td>
                                    <td style="padding: 12px;">2022</td>
                                    <td style="padding: 12px;"><a href="https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/exam-materials/9MA0_01_que_20220607.pdf" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                                    <td style="padding: 12px;"><a href="https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/exam-materials/9MA0_03_que_20220621.pdf" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                                </tr>
                                <tr style="border-bottom: 1px solid #eee; background: #fcfcfc;">
                                    <td style="padding: 12px; font-weight: 600;">AQA</td>
                                    <td style="padding: 12px;">2022</td>
                                    <td style="padding: 12px;"><a href="https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-73571-QP-JUN22.PDF" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                                    <td style="padding: 12px;"><a href="https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-73573-QP-JUN22.PDF" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            
            <!-- SCIENCE -->
            <div id="science" class="syllabus-module" style="margin-bottom: 80px; padding: 40px; background: white; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                <div style="display: flex; align-items: center; gap: 15px; border-bottom: 3px solid var(--scandi-teal-dark); padding-bottom: 15px; margin-bottom: 30px;">
                    <i class="fas fa-flask" style="font-size: 2.5rem; color: var(--scandi-teal-dark);"></i>
                    <h3 style="font-size: 2.2rem; margin: 0; color: var(--text-dark);">A-Level Sciences</h3>
                </div>
                
                <p style="font-size: 1.1rem; color: var(--text-light); margin-bottom: 30px;">Advanced scientific study requiring profound analytical skills. We cover Biology, Chemistry, and Physics modules tailored to specific exam boards like OCR A and AQA.</p>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-bottom: 40px;">
                    <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                        <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-dna"></i> Biology</h4>
                        <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Biological Molecules and Cells</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Genetics, Populations, and Evolution</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Energy transfers in and between organisms</li>
                        </ul>
                    </div>
                    <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                        <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-vial"></i> Chemistry</h4>
                        <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Physical Chemistry (Thermodynamics)</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Inorganic Chemistry (Periodicity)</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Organic Chemistry Synthesis</li>
                        </ul>
                    </div>
                    <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                        <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-atom"></i> Physics</h4>
                        <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Particles and Radiation</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Mechanics and Materials</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Fields and their Consequences</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <!-- CS & Economics -->
            <div id="cs" class="syllabus-module" style="margin-bottom: 80px; padding: 40px; background: white; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                <div style="display: flex; align-items: center; gap: 15px; border-bottom: 3px solid var(--scandi-teal-dark); padding-bottom: 15px; margin-bottom: 30px;">
                    <i class="fas fa-laptop-code" style="font-size: 2.5rem; color: var(--scandi-teal-dark);"></i>
                    <h3 style="font-size: 2.2rem; margin: 0; color: var(--text-dark);">Computer Science & Economics</h3>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-bottom: 40px;">
                    <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                        <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-code"></i> Computer Science</h4>
                        <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Fundamentals of programming & Algorithms</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Data representation & Computer systems</li>
                        </ul>
                    </div>
                    <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                        <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-chart-line"></i> Economics</h4>
                        <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Microeconomics (Markets, Failure)</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Macroeconomics (National Economy)</li>
                        </ul>
                    </div>
                </div>
            </div>

        </div>
    </section>
    """

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find where to inject in alevel.html
    # We will replace <div class="stagger" ... with our new section, up to the Mock Exam section.
    if '<div class="stagger"' in content and '<!-- Mock Exam Section -->' in content:
        start_idx = content.find('<div class="stagger"')
        end_idx = content.find('<!-- Mock Exam Section -->')
        new_content = content[:start_idx] + detailed_syllabus + '\n' + content[end_idx:]
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)


def update_primary():
    path = "c:/Users/steph/Downloads/theos/website/templates/website/primary.html"
    if not os.path.exists(path): return

    detailed_syllabus = """
    <!-- Detailed Syllabus Sections -->
    <section class="section" style="background: #fdfdfd;">
        <div class="container" style="max-width: 1000px;">
            <h2 style="text-align: center; margin-bottom: 50px; font-size: 2.5rem;">Detailed Primary Curriculum & Past Papers</h2>
            
            <div id="ks1" class="syllabus-module" style="margin-bottom: 80px; padding: 40px; background: white; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                <div style="display: flex; align-items: center; gap: 15px; border-bottom: 3px solid var(--scandi-teal-dark); padding-bottom: 15px; margin-bottom: 30px;">
                    <i class="fas fa-child" style="font-size: 2.5rem; color: var(--scandi-teal-dark);"></i>
                    <h3 style="font-size: 2.2rem; margin: 0; color: var(--text-dark);">Key Stage 1 (Years 1 & 2)</h3>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-bottom: 40px;">
                    <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                        <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-book"></i> English & Phonics</h4>
                        <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Letters and Sounds (Phonics Screening)</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Early Reading Comprehension</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Basic Grammar and Punctuation</li>
                        </ul>
                    </div>
                    <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                        <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-calculator"></i> Mathematics</h4>
                        <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Number bonds to 10 and 20</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Addition, Subtraction, Multiplication basics</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Shape, Space, and Measures</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div id="ks2" class="syllabus-module" style="margin-bottom: 80px; padding: 40px; background: white; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                <div style="display: flex; align-items: center; gap: 15px; border-bottom: 3px solid var(--scandi-teal-dark); padding-bottom: 15px; margin-bottom: 30px;">
                    <i class="fas fa-users" style="font-size: 2.5rem; color: var(--scandi-teal-dark);"></i>
                    <h3 style="font-size: 2.2rem; margin: 0; color: var(--text-dark);">Key Stage 2 (Years 3 - 5)</h3>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-bottom: 40px;">
                    <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                        <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-pen-fancy"></i> English & SPaG</h4>
                        <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Spelling, Punctuation and Grammar</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Advanced Reading Comprehension</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Creative and Recount Writing</li>
                        </ul>
                    </div>
                    <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                        <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-square-root-alt"></i> Mathematics</h4>
                        <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Times Tables Mastery (up to 12x)</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Fractions, Decimals, Percentages</li>
                            <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Multi-step word problems</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div id="sats" class="syllabus-module" style="margin-bottom: 80px; padding: 40px; background: white; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                <div style="display: flex; align-items: center; gap: 15px; border-bottom: 3px solid var(--scandi-teal-dark); padding-bottom: 15px; margin-bottom: 30px;">
                    <i class="fas fa-star" style="font-size: 2.5rem; color: var(--scandi-teal-dark);"></i>
                    <h3 style="font-size: 2.2rem; margin: 0; color: var(--text-dark);">Year 6 SATs Preparation</h3>
                </div>
                
                <!-- Past Papers Table -->
                <div style="background: #f8faff; border: 1px solid #cce5ff; border-radius: 12px; overflow: hidden;">
                    <div style="background: #0056b3; color: white; padding: 15px 24px; font-weight: 700; font-size: 1.2rem;">
                        <i class="fas fa-file-pdf" style="margin-right: 10px;"></i> SATs Past Papers Library
                    </div>
                    <div style="padding: 24px;">
                        <table style="width: 100%; border-collapse: collapse; text-align: left;">
                            <thead>
                                <tr style="border-bottom: 2px solid #dee2e6;">
                                    <th style="padding: 12px; color: #495057;">Subject</th>
                                    <th style="padding: 12px; color: #495057;">Year</th>
                                    <th style="padding: 12px; color: #495057;">Paper 1</th>
                                    <th style="padding: 12px; color: #495057;">Paper 2</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr style="border-bottom: 1px solid #eee;">
                                    <td style="padding: 12px; font-weight: 600;">Maths</td>
                                    <td style="padding: 12px;">2022</td>
                                    <td style="padding: 12px;"><a href="#" style="color: #0056b3; text-decoration: underline;">Arithmetic PDF</a></td>
                                    <td style="padding: 12px;"><a href="#" style="color: #0056b3; text-decoration: underline;">Reasoning PDF</a></td>
                                </tr>
                                <tr style="border-bottom: 1px solid #eee; background: #fcfcfc;">
                                    <td style="padding: 12px; font-weight: 600;">English</td>
                                    <td style="padding: 12px;">2022</td>
                                    <td style="padding: 12px;"><a href="#" style="color: #0056b3; text-decoration: underline;">Reading PDF</a></td>
                                    <td style="padding: 12px;"><a href="#" style="color: #0056b3; text-decoration: underline;">SPaG PDF</a></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

        </div>
    </section>
    """

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<div class="stagger"' in content and '<!-- Support Section -->' in content:
        start_idx = content.find('<div class="stagger"')
        end_idx = content.find('<!-- Support Section -->')
        new_content = content[:start_idx] + detailed_syllabus + '\n' + content[end_idx:]
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)

if __name__ == "__main__":
    update_alevel()
    update_primary()
