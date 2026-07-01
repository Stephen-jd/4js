import os

gcse_path = "c:/Users/steph/Downloads/theos/website/templates/website/gcse.html"

detailed_syllabus = """
<!-- Detailed Syllabus Sections -->
<section class="section" style="background: #fdfdfd;">
    <div class="container" style="max-width: 1000px;">
        <h2 style="text-align: center; margin-bottom: 50px; font-size: 2.5rem;">Detailed Syllabus & Past Papers Library</h2>
        
        <!-- MATHEMATICS -->
        <div id="maths" class="syllabus-module" style="margin-bottom: 80px; padding: 40px; background: white; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
            <div style="display: flex; align-items: center; gap: 15px; border-bottom: 3px solid var(--scandi-teal-dark); padding-bottom: 15px; margin-bottom: 30px;">
                <i class="fas fa-square-root-alt" style="font-size: 2.5rem; color: var(--scandi-teal-dark);"></i>
                <h3 style="font-size: 2.2rem; margin: 0; color: var(--text-dark);">Mathematics</h3>
            </div>
            
            <p style="font-size: 1.1rem; color: var(--text-light); margin-bottom: 30px;">An exhaustive, module-by-module breakdown of the GCSE Mathematics curriculum. We prepare students for every tier (Foundation & Higher) across all major exam boards.</p>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-bottom: 40px;">
                <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                    <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-hashtag"></i> 1. Number</h4>
                    <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Structure and calculation</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Fractions, decimals, and percentages</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Measures and accuracy</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Surds and Standard Form</li>
                    </ul>
                </div>
                <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                    <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-function"></i> 2. Algebra</h4>
                    <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Algebraic notation and vocabulary</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Solving equations & inequalities</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Sequences and nth term</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Graphs of quadratics & cubics</li>
                    </ul>
                </div>
                <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                    <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-shapes"></i> 3. Geometry & Measure</h4>
                    <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Properties and constructions</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Mensuration (Area & Volume)</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Vectors & Transformations</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Advanced Trigonometry</li>
                    </ul>
                </div>
                <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                    <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-chart-bar"></i> 4. Statistics & Probability</h4>
                    <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Data recording & representation</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Scatter graphs and correlation</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Theoretical probability</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Tree diagrams & Venn diagrams</li>
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
                                <th style="padding: 12px; color: #495057;">Paper 1 (Non-Calc)</th>
                                <th style="padding: 12px; color: #495057;">Paper 2 (Calc)</th>
                                <th style="padding: 12px; color: #495057;">Paper 3 (Calc)</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="border-bottom: 1px solid #eee;">
                                <td style="padding: 12px; font-weight: 600;">AQA</td>
                                <td style="padding: 12px;">2022</td>
                                <td style="padding: 12px;"><a href="https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-83001H-QP-JUN22.PDF" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                                <td style="padding: 12px;"><a href="https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-83002H-QP-JUN22.PDF" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                                <td style="padding: 12px;"><a href="https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-83003H-QP-JUN22.PDF" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                            </tr>
                            <tr style="border-bottom: 1px solid #eee; background: #fcfcfc;">
                                <td style="padding: 12px; font-weight: 600;">Edexcel</td>
                                <td style="padding: 12px;">2022</td>
                                <td style="padding: 12px;"><a href="https://qualifications.pearson.com/content/dam/pdf/GCSE/mathematics/2015/exam-materials/1MA1_1H_que_20220520.pdf" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                                <td style="padding: 12px;"><a href="https://qualifications.pearson.com/content/dam/pdf/GCSE/mathematics/2015/exam-materials/1MA1_2H_que_20220607.pdf" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                                <td style="padding: 12px;"><a href="https://qualifications.pearson.com/content/dam/pdf/GCSE/mathematics/2015/exam-materials/1MA1_3H_que_20220613.pdf" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                            </tr>
                            <tr style="border-bottom: 1px solid #eee;">
                                <td style="padding: 12px; font-weight: 600;">AQA</td>
                                <td style="padding: 12px;">2021</td>
                                <td style="padding: 12px;"><a href="https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2021/november/AQA-83001H-QP-NOV21.PDF" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                                <td style="padding: 12px;"><a href="https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2021/november/AQA-83002H-QP-NOV21.PDF" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                                <td style="padding: 12px;"><a href="https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2021/november/AQA-83003H-QP-NOV21.PDF" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
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
                <h3 style="font-size: 2.2rem; margin: 0; color: var(--text-dark);">Science (Triple & Combined)</h3>
            </div>
            
            <p style="font-size: 1.1rem; color: var(--text-light); margin-bottom: 30px;">The GCSE Science syllabus is massive. We break down the core concepts across Biology, Chemistry, and Physics, ensuring students are prepared for both the 6-mark extended answers and the rigorous required practicals.</p>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-bottom: 40px;">
                <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                    <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-leaf"></i> Biology</h4>
                    <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Cell biology & Organisation</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Infection and response</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Bioenergetics</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Homeostasis & Inheritance</li>
                    </ul>
                </div>
                <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                    <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-vial"></i> Chemistry</h4>
                    <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Atomic structure & Periodic table</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Quantitative chemistry</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Chemical changes & Organic chem</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Chemistry of the atmosphere</li>
                    </ul>
                </div>
                <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                    <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-bolt"></i> Physics</h4>
                    <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Energy & Electricity</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Particle model of matter</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Forces & Waves</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Magnetism and electromagnetism</li>
                    </ul>
                </div>
            </div>

            <!-- Past Papers Table -->
            <div style="background: #f8faff; border: 1px solid #cce5ff; border-radius: 12px; overflow: hidden;">
                <div style="background: #0056b3; color: white; padding: 15px 24px; font-weight: 700; font-size: 1.2rem;">
                    <i class="fas fa-file-pdf" style="margin-right: 10px;"></i> Past Papers Library
                </div>
                <div style="padding: 24px; overflow-x: auto;">
                    <table style="width: 100%; border-collapse: collapse; text-align: left; min-width: 600px;">
                        <thead>
                            <tr style="border-bottom: 2px solid #dee2e6;">
                                <th style="padding: 12px; color: #495057;">Board</th>
                                <th style="padding: 12px; color: #495057;">Year</th>
                                <th style="padding: 12px; color: #495057;">Biology (P1)</th>
                                <th style="padding: 12px; color: #495057;">Chemistry (P1)</th>
                                <th style="padding: 12px; color: #495057;">Physics (P1)</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="border-bottom: 1px solid #eee;">
                                <td style="padding: 12px; font-weight: 600;">AQA</td>
                                <td style="padding: 12px;">2022</td>
                                <td style="padding: 12px;"><a href="https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-8464B1H-QP-JUN22.PDF" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                                <td style="padding: 12px;"><a href="https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-8464C1H-QP-JUN22.PDF" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                                <td style="padding: 12px;"><a href="https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-8464P1H-QP-JUN22.PDF" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                            </tr>
                            <tr style="border-bottom: 1px solid #eee; background: #fcfcfc;">
                                <td style="padding: 12px; font-weight: 600;">Edexcel</td>
                                <td style="padding: 12px;">2022</td>
                                <td style="padding: 12px;"><a href="https://qualifications.pearson.com/content/dam/pdf/GCSE/Science/2011/Exam-materials/1SC0_1BH_que_20220517.pdf" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                                <td style="padding: 12px;"><a href="https://qualifications.pearson.com/content/dam/pdf/GCSE/Science/2011/Exam-materials/1SC0_1CH_que_20220527.pdf" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                                <td style="padding: 12px;"><a href="https://qualifications.pearson.com/content/dam/pdf/GCSE/Science/2011/Exam-materials/1SC0_1PH_que_20220609.pdf" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- ENGLISH -->
        <div id="english" class="syllabus-module" style="margin-bottom: 60px; padding: 40px; background: white; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
            <div style="display: flex; align-items: center; gap: 15px; border-bottom: 3px solid var(--scandi-teal-dark); padding-bottom: 15px; margin-bottom: 30px;">
                <i class="fas fa-book-open" style="font-size: 2.5rem; color: var(--scandi-teal-dark);"></i>
                <h3 style="font-size: 2.2rem; margin: 0; color: var(--text-dark);">English Language & Literature</h3>
            </div>
            
            <p style="font-size: 1.1rem; color: var(--text-light); margin-bottom: 30px;">Mastering the English curriculum requires strong analytical skills and creative flair. We cover all mandatory texts, unseen poetry techniques, and advanced creative writing structures.</p>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-bottom: 40px;">
                <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                    <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-pen-nib"></i> Language Paper 1</h4>
                    <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Explorations in creative reading</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Analyzing unseen fiction texts</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Descriptive writing techniques</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Narrative writing structure</li>
                    </ul>
                </div>
                <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                    <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-newspaper"></i> Language Paper 2</h4>
                    <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Writers' viewpoints and perspectives</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Analyzing non-fiction & literary non-fiction</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Writing to present a viewpoint</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Arguing and persuading</li>
                    </ul>
                </div>
                <div style="background: var(--off-white); padding: 24px; border-radius: 12px; border: 1px solid var(--border-light);">
                    <h4 style="color: var(--scandi-teal-dark); margin-bottom: 12px; font-size: 1.2rem;"><i class="fas fa-theater-masks"></i> Literature Texts</h4>
                    <ul style="list-style: none; padding: 0; color: var(--text-light); line-height: 1.8;">
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Shakespeare (Macbeth, Romeo & Juliet)</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> The 19th-century novel</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Modern texts (An Inspector Calls)</li>
                        <li><i class="fas fa-check" style="color: #4CAF50; margin-right: 8px;"></i> Poetry anthology & Unseen poetry</li>
                    </ul>
                </div>
            </div>

            <!-- Past Papers Table -->
            <div style="background: #f8faff; border: 1px solid #cce5ff; border-radius: 12px; overflow: hidden;">
                <div style="background: #0056b3; color: white; padding: 15px 24px; font-weight: 700; font-size: 1.2rem;">
                    <i class="fas fa-file-pdf" style="margin-right: 10px;"></i> Past Papers Library
                </div>
                <div style="padding: 24px; overflow-x: auto;">
                    <table style="width: 100%; border-collapse: collapse; text-align: left; min-width: 600px;">
                        <thead>
                            <tr style="border-bottom: 2px solid #dee2e6;">
                                <th style="padding: 12px; color: #495057;">Board</th>
                                <th style="padding: 12px; color: #495057;">Year</th>
                                <th style="padding: 12px; color: #495057;">Language P1</th>
                                <th style="padding: 12px; color: #495057;">Language P2</th>
                                <th style="padding: 12px; color: #495057;">Literature P1</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="border-bottom: 1px solid #eee;">
                                <td style="padding: 12px; font-weight: 600;">AQA</td>
                                <td style="padding: 12px;">2022</td>
                                <td style="padding: 12px;"><a href="https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-87001-QP-JUN22.PDF" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                                <td style="padding: 12px;"><a href="https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-87002-QP-JUN22.PDF" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                                <td style="padding: 12px;"><a href="https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-87021-QP-JUN22.PDF" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                            </tr>
                            <tr style="border-bottom: 1px solid #eee; background: #fcfcfc;">
                                <td style="padding: 12px; font-weight: 600;">Edexcel</td>
                                <td style="padding: 12px;">2022</td>
                                <td style="padding: 12px;"><a href="https://qualifications.pearson.com/content/dam/pdf/GCSE/English%20Language/2015/Exam-materials/1EN0_01_que_20220518.pdf" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                                <td style="padding: 12px;"><a href="https://qualifications.pearson.com/content/dam/pdf/GCSE/English%20Language/2015/Exam-materials/1EN0_02_que_20220610.pdf" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                                <td style="padding: 12px;"><a href="https://qualifications.pearson.com/content/dam/pdf/GCSE/English%20Literature/2015/Exam-materials/1ET0_01_que_20220525.pdf" target="_blank" style="color: #0056b3; text-decoration: underline;">Download PDF</a></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</section>
"""

with open(gcse_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the old detailed syllabus block.
# The old one started with '<!-- Detailed Syllabus Sections -->' and ended with '<!-- Mock Exam Section -->'
if '<!-- Detailed Syllabus Sections -->' in content and '<!-- Mock Exam Section -->' in content:
    start_idx = content.find('<!-- Detailed Syllabus Sections -->')
    end_idx = content.find('<!-- Mock Exam Section -->')
    new_content = content[:start_idx] + detailed_syllabus + '\n' + content[end_idx:]
    with open(gcse_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        print("Updated GCSE syllabus successfully.")
else:
    print("Could not find syllabus markers.")
