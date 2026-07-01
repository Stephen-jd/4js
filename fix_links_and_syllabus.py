import os
import re

gcse_path = "c:/Users/steph/Downloads/theos/website/templates/website/gcse.html"

detailed_syllabus = """
<!-- Detailed Syllabus Sections -->
<section class="section" style="background: #fdfdfd;">
    <div class="container" style="max-width: 900px;">
        <h2 style="text-align: center; margin-bottom: 50px; font-size: 2.5rem;">Detailed Syllabus & Past Papers</h2>
        
        <div id="maths" class="syllabus-module" style="margin-bottom: 60px; padding: 30px; background: white; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
            <h3 style="font-size: 1.8rem; margin-bottom: 16px; color: var(--text-dark); border-bottom: 2px solid var(--scandi-teal-dark); padding-bottom: 10px;">Mathematics</h3>
            <p style="margin-bottom: 20px;">Our comprehensive GCSE Mathematics programme covers the full spectrum of the Edexcel and AQA specifications.</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-bottom: 30px;">
                <div style="background: var(--off-white); padding: 20px; border-radius: 8px;">
                    <h4 style="color: var(--scandi-teal-dark); margin-bottom: 10px;">Number & Algebra</h4>
                    <ul style="list-style: disc; margin-left: 20px; color: var(--text-light);">
                        <li>Fractions, Decimals, Percentages</li>
                        <li>Quadratic Equations and Graphs</li>
                        <li>Simultaneous Equations</li>
                    </ul>
                </div>
                <div style="background: var(--off-white); padding: 20px; border-radius: 8px;">
                    <h4 style="color: var(--scandi-teal-dark); margin-bottom: 10px;">Geometry & Measure</h4>
                    <ul style="list-style: disc; margin-left: 20px; color: var(--text-light);">
                        <li>Trigonometry & Circle Theorems</li>
                        <li>Area, Volume, Vectors</li>
                    </ul>
                </div>
            </div>
            <div style="background: #eef5f9; padding: 20px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div><strong>Download Past Papers:</strong> AQA/Edexcel</div>
                <div>
                    <a href="https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-83001H-QP-JUN22.PDF" target="_blank" class="btn-primary" style="padding: 8px 16px; font-size: 0.9rem;">2022 AQA Paper</a>
                </div>
            </div>
        </div>

        <div id="science" class="syllabus-module" style="margin-bottom: 60px; padding: 30px; background: white; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
            <h3 style="font-size: 1.8rem; margin-bottom: 16px; color: var(--text-dark); border-bottom: 2px solid var(--scandi-teal-dark); padding-bottom: 10px;">Science (Triple & Combined)</h3>
            <p style="margin-bottom: 20px;">In-depth coverage of Biology, Chemistry, and Physics modules.</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-bottom: 30px;">
                <div style="background: var(--off-white); padding: 20px; border-radius: 8px;">
                    <h4 style="color: var(--scandi-teal-dark); margin-bottom: 10px;">Biology</h4>
                    <ul style="list-style: disc; margin-left: 20px; color: var(--text-light);">
                        <li>Cell Biology & Organization</li>
                        <li>Infection and Response</li>
                    </ul>
                </div>
                <div style="background: var(--off-white); padding: 20px; border-radius: 8px;">
                    <h4 style="color: var(--scandi-teal-dark); margin-bottom: 10px;">Physics & Chem</h4>
                    <ul style="list-style: disc; margin-left: 20px; color: var(--text-light);">
                        <li>Atomic Structure & Bonding</li>
                        <li>Forces & Energy</li>
                    </ul>
                </div>
            </div>
            <div style="background: #eef5f9; padding: 20px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div><strong>Download Past Papers:</strong> AQA Combined Science</div>
                <div>
                    <a href="https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-8464B1H-QP-JUN22.PDF" target="_blank" class="btn-primary" style="padding: 8px 16px; font-size: 0.9rem;">2022 Biology Paper</a>
                </div>
            </div>
        </div>
        
        <div id="english" class="syllabus-module" style="margin-bottom: 60px; padding: 30px; background: white; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
            <h3 style="font-size: 1.8rem; margin-bottom: 16px; color: var(--text-dark); border-bottom: 2px solid var(--scandi-teal-dark); padding-bottom: 10px;">English Language & Literature</h3>
            <p style="margin-bottom: 20px;">Master unseen poetry, Shakespeare, modern texts, and creative writing.</p>
            <div style="background: #eef5f9; padding: 20px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div><strong>Download Past Papers:</strong> AQA English</div>
                <div>
                    <a href="https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-87001-QP-JUN22.PDF" target="_blank" class="btn-primary" style="padding: 8px 16px; font-size: 0.9rem;">2022 Language Paper 1</a>
                </div>
            </div>
        </div>

    </div>
</section>
"""

if os.path.exists(gcse_path):
    with open(gcse_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update the Book Maths Tutor links to WhatsApp
    content = content.replace('href="#contact" style="color: var(--accent); font-weight: 600;">Book Maths Tutor', 'href="https://wa.me/447534715058?text=I%20would%20like%20to%20book%20a%20GCSE%20Maths%20Tutor" style="color: var(--accent); font-weight: 600;" target="_blank">Book Maths Tutor')
    content = content.replace('href="#contact" style="color: var(--accent); font-weight: 600;">Book Science Tutor', 'href="https://wa.me/447534715058?text=I%20would%20like%20to%20book%20a%20GCSE%20Science%20Tutor" style="color: var(--accent); font-weight: 600;" target="_blank">Book Science Tutor')
    content = content.replace('href="#contact" style="color: var(--accent); font-weight: 600;">Book English Tutor', 'href="https://wa.me/447534715058?text=I%20would%20like%20to%20book%20a%20GCSE%20English%20Tutor" style="color: var(--accent); font-weight: 600;" target="_blank">Book English Tutor')

    # 2. Inject the detailed syllabus before the Mock Exam Section
    if '<!-- Mock Exam Section -->' in content:
        content = content.replace('<!-- Mock Exam Section -->', detailed_syllabus + '\n<!-- Mock Exam Section -->')

    with open(gcse_path, 'w', encoding='utf-8') as f:
        f.write(content)


# Base HTML update for Instagram link
base_path = "c:/Users/steph/Downloads/theos/website/templates/website/base.html"
if os.path.exists(base_path):
    with open(base_path, 'r', encoding='utf-8') as f:
        base_content = f.read()
    
    # Replace Instagram link
    base_content = re.sub(r'href="[^"]*" class="social-icon"><i class="fab fa-instagram">', 'href="https://www.instagram.com/4js_edu?igsh=OGdvM3Q2c295ejN3" target="_blank" class="social-icon"><i class="fab fa-instagram">', base_content)
    
    with open(base_path, 'w', encoding='utf-8') as f:
        f.write(base_content)
