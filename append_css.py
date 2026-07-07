import os

css_path = r"c:\Users\steph\Downloads\theos\static\css\style.css"
animation_css = """
/* Logo Zoom Pulse Animation */
.zoom-pulse-logo {
    animation: zoomPulse 4s infinite alternate ease-in-out;
    transform-origin: center;
}

@keyframes zoomPulse {
    0% {
        transform: scale(0.9);
    }
    100% {
        transform: scale(1.1);
    }
}

/* Ensure mobile menu works well */
.mobile-menu {
    display: none;
    flex-direction: column;
    background-color: var(--bg-light);
    padding: 20px;
    position: absolute;
    top: 70px;
    width: 100%;
    z-index: 1000;
}
.mobile-menu.active {
    display: flex;
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write(animation_css)
    
print("Appended CSS animation.")
