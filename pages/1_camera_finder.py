import streamlit as st
import math
import numpy as np
import random
from PIL import Image, ImageDraw
import os

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(page_title="Camera Selector", layout="wide")

# Sidebar navigation styling
st.markdown("""
<style>
/* Sidebar navigation styling */
[data-testid="stSidebarNav"] {
    padding-top: 2rem;
}

[data-testid="stSidebarNav"] ul {
    padding: 0;
}

[data-testid="stSidebarNav"] li {
    list-style: none;
}

[data-testid="stSidebarNav"] a {
    font-size: 15px !important;
    font-weight: 400 !important;
    color: #1d1d1f !important;
    text-decoration: none !important;
    padding: 8px 16px !important;
    display: block !important;
    border-radius: 6px !important;
    transition: background-color 0.2s ease !important;
}

[data-testid="stSidebarNav"] a:hover {
    background-color: #f5f5f7 !important;
}

[data-testid="stSidebarNav"] a[aria-current="page"] {
    font-weight: 600 !important;
    color: #1d1d1f !important;
    background-color: #e8e8ed !important;
}

/* Top Navigation Bar - Fixed Position */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: rgba(255, 255, 255, 0.98);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid #e5e5e7;
    padding: 0 20px;
    height: 48px;
    display: flex;
    align-items: center;
    z-index: 9999;
    width: 100%;
}

.nav-container {
    max-width: 1400px;
    margin: 0 auto;
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-size: 16px !important;
    font-weight: 700 !important;
    color: #1d1d1f !important;
    text-decoration: none;
    letter-spacing: -0.5px;
    cursor: pointer;
}

.nav-links {
    display: flex;
    gap: 0;
    list-style: none;
    margin: 0;
    padding: 0;
}

.nav-links span {
    padding: 0 16px;
    height: 48px;
    display: flex;
    align-items: center;
    font-size: 14px !important;
    color: #1d1d1f !important;
    text-decoration: none;
    transition: color 0.2s ease;
    cursor: pointer;
}

.nav-links span:hover {
    color: #0071e3 !important;
}
</style>

<div class="navbar">
    <div class="nav-container">
        <span class="logo" onclick="window.location.href='/'">📷 Camera Finder</span>
        <div class="nav-links">
            <span onclick="window.location.href='/'">Home</span>
            <span onclick="window.location.href='/camera_finder'">Camera Finder</span>
            <span onclick="window.location.href='/camera_checker'">Camera Checker</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# Apple-style Typography & UI Overhaul
# ============================================================
st.markdown("""
<style>

/* GLOBAL FONT --------------------------------------------------------*/
html, body, [class*="css"] {
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display",
                 "Segoe UI", Roboto, Arial, sans-serif !important;
    color: #1d1d1f !important;
    background: #ffffff !important;
}

/* Add top padding to account for fixed navbar */
[data-testid="stAppViewContainer"] {
    padding-top: 48px !important;
}

/* Input Labels --------------------------------------------------------*/
label, .stSelectbox label, .stSlider label, .stTextInput label {
    font-size: 14px !important;
    font-weight: 400 !important;
    color: #1d1d1f !important;
}

/* Main Page Title (56px) -------------------------------------------------*/
.main-title, h1 {
    font-size: 48px !important;
    font-weight: 600 !important;
    margin-bottom: 2rem !important;
    letter-spacing: -0.5px !important;
}

/* Section Title / Card Title (32px) --------------------------------*/
.section-title, h2, .card-title {
    font-size: 28px !important;
    font-weight: 600 !important;
    margin-bottom: 1.5rem !important;
    letter-spacing: -0.3px !important;
}

/* Larger title used specifically for the Camera View Simulation card */
.simulation-title {
    font-size: 28px !important;
    font-weight: 600 !important;
    margin-bottom: 1rem !important;
    letter-spacing: -0.3px !important;
}

/* Best Recommended Camera model name (largest, Apple blue) ----------*/
.best-model-name {
    font-size: 32px !important;
    font-weight: 600 !important;
    color: #0071e3 !important;
    margin-bottom: 1rem !important;
    letter-spacing: -0.3px !important;
}

/* Body text in cards ------------------------------------------------*/
.apple-card p, .compare-card p, .stMarkdown {
    font-size: 15px !important;
}

/* Object selection buttons - styled as cards */
div[data-testid="stMain"] .stButton>button[key^="obj_"] {
    width: 100% !important;
    border: 2px solid #e5e5e7 !important;
    border-radius: 8px !important;
    background: white !important;
    color: #1d1d1f !important;
    padding: 16px !important;
    font-size: 16px !important;
    font-weight: 400 !important;
    transition: border-color 0.2s ease !important;
    box-shadow: none !important;
}

div[data-testid="stMain"] .stButton>button[key^="obj_"]:hover {
    border-color: #0071e3 !important;
    box-shadow: none !important;
    background: white !important;
    color: #1d1d1d !important;
}

div[data-testid="stMain"] .stButton>button[key^="obj_"]:focus {
    border-color: #0071e3 !important;
    border-width: 3px !important;
    box-shadow: none !important;
}

/* ALL OTHER BUTTONS - Blue background with pill shape */
div[data-testid="stMain"] .stButton > button:not([key^="obj_"]) {
    padding: 12px 32px !important;
    background: #0071e3 !important;
    color: white !important;
    font-size: 17px !important;
    font-weight: 400 !important;
    border: none !important;
    border-radius: 980px !important;
    transition: all 0.3s ease !important;
    box-shadow: none !important;
}

div[data-testid="stMain"] .stButton > button:not([key^="obj_"]):hover {
    background: #0077ed !important;
    color: white !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 12px rgba(0, 113, 227, 0.2) !important;
}

/* Up/Down arrow buttons - smaller size */
div[data-testid="stMain"] .stButton > button[key^="up_"],
div[data-testid="stMain"] .stButton > button[key^="down_"] {
    padding: 8px 12px !important;
    font-size: 14px !important;
    min-width: 36px !important;
    height: 36px !important;
}

/* Style for radio buttons as cards */
.stRadio {
    margin-bottom: 0.75rem;
}

.stRadio > label {
    font-size: 14px !important;
    font-weight: 400 !important;
    color: #1d1d1f !important;
    margin-bottom: 0.75rem !important;
    display: block !important;
}

.stRadio > div {
    display: grid !important;
    grid-template-columns: 1fr !important;
    gap: 0.75rem !important;
}

.stRadio > div > label {
    border: 2px solid #e5e5e7 !important;
    border-radius: 8px !important;
    padding: 12px 16px !important;
    background: white !important;
    color: #1d1d1f !important;
    text-align: left !important;
    cursor: pointer !important;
    font-weight: 400 !important;
    font-size: 14px !important;
    transition: border-color 0.2s ease !important;
    margin: 0 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important;
    min-height: 44px !important;
}

.stRadio > div > label:hover {
    border-color: #0071e3 !important;
}

.stRadio > div > label > input[type="radio"]:checked ~ span {
    color: #000 !important;
}

.stRadio > div > label:has(input[type="radio"]:checked) {
    border: 3px solid #0071e3 !important;
    background: white !important;
}

/* Cards --------------------------------------------------------------*/
.apple-card {
    background: white !important;
    border: 1px solid #e5e5e7 !important;
    border-radius: 12px !important;
    padding: 24px !important;
    margin-bottom: 24px !important;
    box-shadow: none !important;
}

/* Object selection cards */
.object-selector-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
    gap: 1rem;
    margin-bottom: 1.5rem;
}

.object-card {
    aspect-ratio: 1;
    border: 2px solid #d9d9d9 !important;
    border-radius: 12px !important;
    padding: 1.5rem !important;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    cursor: pointer;
    background: white !important;
    transition: all 0.3s ease;
    font-weight: 500;
    font-size: 16px !important;
    color: #000 !important;
}

.object-card:hover {
    border-color: #0071e3 !important;
    box-shadow: none !important;
}

.object-card.selected {
    border: 3px solid #0071e3 !important;
    background: white !important;
    box-shadow: none !important;
}

/* Comparison cards */
.compare-card {
    background: white !important;
    border: 1px solid #e5e5e7 !important;
    border-radius: 12px !important;
    padding: 20px !important;
    box-shadow: none !important;
}

/* Camera View Simulation - Display at 50% size with high quality */
[data-testid="stImage"] img {
    max-width: 50% !important;
    height: auto !important;
    display: block !important;
    margin: 0 auto !important;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# TOP NAV - Back to Home Button
# ============================================================
st.markdown("""
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
    <div style="font-size: 48px; font-weight: 700; color: #1d1d1f;">Camera Finder</div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# DATABASES — Object Definitions
# ============================================================
OBJECTS = {
    "Human Face": ("human_face.jpg", 18, 80),
    "Door Lock": ("door_lock.jpg", 6, 100),
    "Pet": ("dog.jpg", 25, 90),
    "License Plate": ("plate.jpg", 35, 150),
    "Food Item": ("food.jpg", 10, 80),
}

# ============================================================
# DATABASES — Sensor Formats
# ============================================================
SENSORS = {
    "Small": {
        "1/3\"": (4.8, 3.6),
        "1/2.8\"": (6.4, 4.8),
        "1/2.5\"": (6.9, 5.2),
        "1/2.3\"": (6.3, 4.7),
    },
    "Medium": {
        "1/2\"": (6.4, 4.8),
        "1/1.8\"": (7.2, 5.4),
        "2/3\"": (8.8, 6.6),
        "1\"": (13.2, 8.8),
    },
    "Large": {
        "1.1\"": (14.2, 10.4),
        "4/3\"": (17.3, 13.0),
        "APS-C": (23.5, 15.6),
    }
}

# ============================================================
# DATABASES — Resolution / Focal Length / F-numbers
# ============================================================
COMMON_RESOLUTIONS = [
    ("VGA", 640, 480),
    ("HD", 1280, 720),
    ("FHD / 2MP", 1920, 1080),
    ("3MP", 2048, 1536),
    ("5MP", 2592, 1944),
    ("8MP", 3840, 2160),
    ("12MP", 4000, 3000)
]

COMMON_FOCAL_LENGTHS = [2.8, 3.0, 3.2, 3.6, 4.0, 4.4, 5.0, 6.0, 8.0, 12.0, 16.0, 25.0, 35.0]
COMMON_F_NUMBERS = [1.8, 2.0, 2.2, 2.4, 2.8, 3.2, 4.0, 5.6, 8.0, 11.0, 16.0]

# Used to map size labels in UI to database keys
CAMERA_SIZE_OPTIONS = {
    "Small (25×25×20 – 40×40×25 mm)": "Small",
    "Medium (40×40×40 – 60×60×50 mm)": "Medium",
    "Large (70×70×60 – 100×100×80 mm)": "Large"
}

# ============================================================
# Random Model Name Generator
# ============================================================
BRANDS = ["IMX","AUR","SIG","FOX","NANO","CORE","OPT","VISTA","ZEN","GLO","NEOS","PIX","CAM","ARC","RPT"]
SUFFIXES = ["","S","X","R","Pro","Ultra","Mini"]

def generate_model_name():
    brand = random.choice(BRANDS)
    num = str(random.randint(100,9999))
    suf = random.choice(SUFFIXES)
    return f"{brand}-{num}" if suf=="" else f"{brand}-{num}-{suf}"

# ============================================================
# LAYOUT — LEFT (65%) + RIGHT(35%)
# ============================================================
left_col, right_col = st.columns([0.65, 0.35])

# ============================================================
# RIGHT — INPUT PANEL (Apple-style Card)
# ============================================================
with right_col:
    st.markdown("""
    <div class='apple-card'>
        <div class='section-title simulation-title'>Camera Requirements</div>
    """, unsafe_allow_html=True)

    # Object selection with radio buttons styled as cards
    object_keys = list(OBJECTS.keys())
    object_type = st.radio(
        "Object to recognize",
        object_keys,
        horizontal=False,
        label_visibility="visible"
    )

    # Distances & HFOV
    max_distance = st.slider("Maximum recognition distance (cm)", 20, 500, 200)
    min_distance = st.slider("Minimum useful distance (cm)", 5, max_distance, 30)
    dfov_deg = st.slider("Desired Field of View (DFOV, degrees)", 10, 150, 80)
    
    # Validate that min_distance does not exceed max_distance
    if min_distance > max_distance:
        st.error("⚠️ Minimum useful distance cannot be greater than maximum recognition distance. Please adjust.")
        min_distance = max_distance
    
    # Track which parameter is being adjusted (using session state for feedback)
    if "prev_max_distance" not in st.session_state:
        st.session_state.prev_max_distance = 200
    if "prev_dfov_deg" not in st.session_state:
        st.session_state.prev_dfov_deg = 80
    
    # Determine which parameter changed
    actively_adjusting_distance = max_distance != st.session_state.prev_max_distance
    actively_adjusting_dfov = dfov_deg != st.session_state.prev_dfov_deg
    
    # Store current values for next iteration
    st.session_state.prev_max_distance = max_distance
    st.session_state.prev_dfov_deg = dfov_deg

    # Camera size with radio buttons styled as cards
    camera_size_label = st.radio(
        "Preferred camera size",
        list(CAMERA_SIZE_OPTIONS.keys()),
        horizontal=False,
        label_visibility="visible"
    )
    camera_size = CAMERA_SIZE_OPTIONS[camera_size_label]

    # ============================================================
    # RANKING PRIORITIES - DRAGGABLE ORDER
    # ============================================================
    st.markdown("""
    <div style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid #e5e5e7;">
        <div style="font-size: 17px; font-weight: 600; margin-bottom: 0.75rem;">Ranking Priorities</div>
        <div style="font-size: 14px; color: #666; margin-bottom: 1rem;">Use ↑↓ buttons to reorder</div>
    </div>
    """, unsafe_allow_html=True)

    priority_options = [
        "Low-light performance",
        "Low distortion",
        "High resolution"
    ]
    
    priority_descriptions = [
        "f-number",
        "focal length",
        "pixel count"
    ]

    # Initialize priority order in session state
    if "priority_order" not in st.session_state:
        st.session_state.priority_order = list(range(3))  # [0, 1, 2]

    # Display priority items with up/down buttons
    for i in range(3):
        col1, col2, col3 = st.columns([0.85, 0.075, 0.075])
        
        priority_idx = st.session_state.priority_order[i]
        priority_title = priority_options[priority_idx]
        priority_desc = priority_descriptions[priority_idx]
        
        with col1:
            st.markdown(f"""
            <div style="padding: 12px 16px; background: #f5f5f7; border: 1px solid #e5e5e7; border-radius: 8px; 
                       display: flex; flex-direction: column; gap: 3px;">
                <div style="font-weight: 600; color: #1d1d1f; font-size: 14px;">
                    <span style="color: #0071e3; margin-right: 6px; font-weight: 700;">{i+1}.</span>{priority_title}
                </div>
                <div style="font-size: 12px; color: #86868b;">{priority_desc}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            if i > 0:
                if st.button("↑", key=f"up_{i}", help="Move up"):
                    # Swap with previous
                    st.session_state.priority_order[i], st.session_state.priority_order[i-1] = \
                        st.session_state.priority_order[i-1], st.session_state.priority_order[i]
                    st.rerun()
            else:
                st.write("")
        
        with col3:
            if i < 2:
                if st.button("↓", key=f"down_{i}", help="Move down"):
                    # Swap with next
                    st.session_state.priority_order[i], st.session_state.priority_order[i+1] = \
                        st.session_state.priority_order[i+1], st.session_state.priority_order[i]
                    st.rerun()
            else:
                st.write("")

    # Get the ordered priorities
    priority_1 = priority_options[st.session_state.priority_order[0]]
    priority_2 = priority_options[st.session_state.priority_order[1]]
    priority_3 = priority_options[st.session_state.priority_order[2]]

    # Start button
    start = st.button("Start Finding Your Camera")

    st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# LEFT — CAMERA VIEW SIMULATION (FULL CARD)
# ============================================================
with left_col:
    # ---- Card Begin ----
    st.markdown("""
    <div class='apple-card'>
        <div class='section-title simulation-title'>Camera View Simulation</div>
        <div id='sim_block'>
    """, unsafe_allow_html=True)

    # Load selected object
    image_path, obj_width_cm, required_px = OBJECTS[object_type]

    if os.path.exists(image_path):
        base_img = Image.open(image_path).convert("RGBA")

        # Square canvas - simulating actual camera viewfinder (1:1 ratio) - HIGH QUALITY
        canvas_size = 600
        view_w, view_h = canvas_size, canvas_size
        
        # --------------------------------------------------------
        # Calculate object display size based on physics
        # DFOV affects diagonal FOV - larger DFOV means narrower field at center
        # --------------------------------------------------------
        aspect_ratio = 16 / 9
        hfov_rad = 2 * math.atan(math.tan(math.radians(dfov_deg / 2)) / math.sqrt(1 + aspect_ratio ** 2))
        hfov_deg_calc = math.degrees(hfov_rad)
        
        # Object size based on actual distance and HFOV
        # The object's angular size = 2 * arctan(object_width / (2 * distance))
        # The canvas width represents hfov_deg_calc
        # So: obj_display_w / canvas_width = object_angular_size / hfov_deg_calc
        
        hfov_width_cm = 2 * max_distance * math.tan(math.radians(hfov_deg_calc / 2))
        obj_angular_width = 2 * math.degrees(math.atan(obj_width_cm / (2 * max_distance)))
        obj_display_w = int((obj_angular_width / hfov_deg_calc) * view_w)
        
        obj_display_w = max(obj_display_w, 30)  # minimum visible size
        obj_display_w = min(obj_display_w, int(view_w * 0.5))  # maximum

        # Aspect-ratio correct height
        obj_h = int(obj_display_w * (base_img.height / base_img.width))
        obj_resized = base_img.resize((int(obj_display_w), int(obj_h)))

        # Create square canvas with gradient background (simulating camera sensor)
        canvas = Image.new("RGBA", (view_w, view_h), (240, 240, 245, 255))
        draw = ImageDraw.Draw(canvas)

        # --------------------------------------------------------
        # DFOV VISUALIZATION - Show visible area based on diagonal FOV
        # --------------------------------------------------------
        max_fov = 150
        visible_ratio = dfov_deg / max_fov
        visible_size = int(canvas_size * visible_ratio)
        
        # Mask areas outside the DFOV (darker corners)
        if visible_ratio < 1.0:
            mask_offset = (canvas_size - visible_size) // 2
            
            # Create corner masks for diamond/octagon effect showing DFOV boundaries
            if mask_offset > 0:
                corner_mask = Image.new("RGBA", (mask_offset, mask_offset), (200, 200, 210, 100))
                canvas.alpha_composite(corner_mask, (0, 0))
                canvas.alpha_composite(corner_mask, (canvas_size - mask_offset, 0))
                canvas.alpha_composite(corner_mask, (0, canvas_size - mask_offset))
                canvas.alpha_composite(corner_mask, (canvas_size - mask_offset, canvas_size - mask_offset))

        # --------------------------------------------------------
        # Draw camera viewfinder frame - outer square border
        # --------------------------------------------------------
        frame_margin = 0
        frame_color = (180, 180, 190)
        frame_width = 2
        
        # Main outer square frame
        draw.rectangle(
            [frame_margin, frame_margin, view_w - frame_margin, view_h - frame_margin],
            outline=frame_color,
            width=frame_width
        )

        # --------------------------------------------------------
        # ACTUAL VIEWABLE AREA - Inner frame showing actual image bounds
        # Based on the DFOV, show which area is actually visible
        # --------------------------------------------------------
        inner_margin = int((canvas_size - visible_size) / 2)
        inner_frame_color = (100, 150, 220)  # Blue to distinguish from outer frame
        inner_frame_width = 2
        
        if inner_margin > 0:
            # Draw inner rectangle showing actual visible area
            draw.rectangle(
                [inner_margin, inner_margin, canvas_size - inner_margin, canvas_size - inner_margin],
                outline=inner_frame_color,
                width=inner_frame_width
            )
        
        # Add corner markers for the inner frame (blue accent corners)
        corner_size = 10
        corner_accent_width = 1
        if inner_margin > 0:
            # Top-left
            draw.line([(inner_margin, inner_margin), (inner_margin + corner_size, inner_margin)], 
                     fill=inner_frame_color, width=corner_accent_width)
            draw.line([(inner_margin, inner_margin), (inner_margin, inner_margin + corner_size)], 
                     fill=inner_frame_color, width=corner_accent_width)
            
            # Top-right
            draw.line([(canvas_size - inner_margin, inner_margin), (canvas_size - inner_margin - corner_size, inner_margin)], 
                     fill=inner_frame_color, width=corner_accent_width)
            draw.line([(canvas_size - inner_margin, inner_margin), (canvas_size - inner_margin, inner_margin + corner_size)], 
                     fill=inner_frame_color, width=corner_accent_width)
            
            # Bottom-left
            draw.line([(inner_margin, canvas_size - inner_margin), (inner_margin + corner_size, canvas_size - inner_margin)], 
                     fill=inner_frame_color, width=corner_accent_width)
            draw.line([(inner_margin, canvas_size - inner_margin), (inner_margin, canvas_size - inner_margin - corner_size)], 
                     fill=inner_frame_color, width=corner_accent_width)
            
            # Bottom-right
            draw.line([(canvas_size - inner_margin, canvas_size - inner_margin), (canvas_size - inner_margin - corner_size, canvas_size - inner_margin)], 
                     fill=inner_frame_color, width=corner_accent_width)
            draw.line([(canvas_size - inner_margin, canvas_size - inner_margin), (canvas_size - inner_margin, canvas_size - inner_margin - corner_size)], 
                     fill=inner_frame_color, width=corner_accent_width)
        
        # Add center crosshair for better focus reference
        center_x, center_y = view_w // 2, view_h // 2
        crosshair_size = 10
        crosshair_color = (200, 200, 200)
        
        # Horizontal line
        draw.line([(center_x - crosshair_size, center_y), (center_x + crosshair_size, center_y)], 
                 fill=crosshair_color, width=1)
        # Vertical line
        draw.line([(center_x, center_y - crosshair_size), (center_x, center_y + crosshair_size)], 
                 fill=crosshair_color, width=1)
        
        # Small center circle
        circle_size = 3
        draw.ellipse([center_x - circle_size, center_y - circle_size, center_x + circle_size, center_y + circle_size], 
                    outline=crosshair_color, width=1)

        # --------------------------------------------------------
        # OBJECT POSITIONING - Center in the square
        # --------------------------------------------------------
        x = (view_w - obj_display_w) // 2
        y = (view_h - obj_h) // 2
        
        # Add subtle shadow effect
        shadow_offset = 2
        shadow = Image.new("RGBA", (obj_display_w + shadow_offset * 2, obj_h + shadow_offset * 2), (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow)
        shadow_draw.ellipse(
            [(shadow_offset, shadow_offset), (obj_display_w + shadow_offset, obj_h + shadow_offset)],
            fill=(0, 0, 0, 8)
        )
        canvas.alpha_composite(shadow, (x - shadow_offset, y + shadow_offset))
        
        # Composite the object
        canvas.alpha_composite(obj_resized, (x, y))

        # --------------------------------------------------------
        # INFO PANEL BELOW - Separate from the square viewfinder
        # --------------------------------------------------------
        info_height = 85
        total_height = view_w + info_height
        final_canvas = Image.new("RGBA", (view_w, total_height), (255, 255, 255, 255))
        
        # Composite the square viewfinder at top
        final_canvas.alpha_composite(canvas, (0, 0))
        
        # Draw subtle separator line
        draw_final = ImageDraw.Draw(final_canvas)
        draw_final.line([(0, view_w), (view_w, view_w)], fill=(230, 230, 235), width=1)

        from PIL import ImageFont
        try:
            label_font = ImageFont.truetype("arial.ttf", 12)
            value_font = ImageFont.truetype("arial.ttf", 18)
        except:
            label_font = ImageFont.load_default()
            value_font = ImageFont.load_default()

        # --------------------------------------------------------
        # INFO PANEL - Three columns with color feedback
        # --------------------------------------------------------
        info_y_start = view_w + 6
        info_y_label = info_y_start + 8
        info_y_value = info_y_start + 28
        
        # Determine colors based on active adjustment
        distance_color = (0, 113, 227) if actively_adjusting_distance else (29, 29, 31)
        dfov_color = (0, 113, 227) if actively_adjusting_dfov else (29, 29, 31)
        object_color = (29, 29, 31)
        
        # Column 1: Distance
        col1_x = view_w // 6
        draw_final.text(
            (col1_x, info_y_label),
            "Distance",
            fill=(155, 155, 160),
            font=label_font,
            anchor="mm"
        )
        draw_final.text(
            (col1_x, info_y_value),
            f"{max_distance} cm",
            fill=distance_color,
            font=value_font,
            anchor="mm"
        )
        
        # Column 2: Diagonal FOV
        col2_x = view_w // 2
        draw_final.text(
            (col2_x, info_y_label),
            "Diagonal FOV",
            fill=(155, 155, 160),
            font=label_font,
            anchor="mm"
        )
        draw_final.text(
            (col2_x, info_y_value),
            f"{dfov_deg}°",
            fill=dfov_color,
            font=value_font,
            anchor="mm"
        )
        
        # Column 3: Object size
        col3_x = (view_w * 5) // 6
        draw_final.text(
            (col3_x, info_y_label),
            "Object Size",
            fill=(155, 155, 160),
            font=label_font,
            anchor="mm"
        )
        draw_final.text(
            (col3_x, info_y_value),
            f"{obj_width_cm:.1f} cm",
            fill=object_color,
            font=value_font,
            anchor="mm"
        )

        # --------------------------------------------------------
        # Display simulation
        # --------------------------------------------------------
        st.image(final_canvas, use_container_width=True)

    else:
        st.error("Image file missing: " + image_path)

    # ---- Card End ----
    st.markdown("</div></div>", unsafe_allow_html=True)

# ============================================================
# OPTICAL ENGINE (Runs only after Start)
# ============================================================
lambda_um = 0.55
candidates = []

if start:

    for sensor_name, (sw, sh) in SENSORS[camera_size].items():

        # Minimum focal length to achieve required DFOV (using diagonal)
        diag = math.sqrt(sw**2 + sh**2)
        f_min = diag / (2 * math.tan(math.radians(dfov_deg / 2)))

        # Focal lengths that satisfy DFOV constraint
        valid_focals = []
        for f in COMMON_FOCAL_LENGTHS:
            diag = math.sqrt(sw**2 + sh**2)
            real_dfov = 2 * math.degrees(math.atan(diag / (2 * f)))
            if real_dfov >= dfov_deg:
                valid_focals.append((f, real_dfov))

        if not valid_focals:
            continue

        # Choose focal length closest to minimal
        f_chosen, real_dfov = min(valid_focals, key=lambda x: abs(x[0] - f_min))

        # Required resolution along horizontal axis
        # Calculate HFOV from focal length and sensor width
        real_hfov = 2 * math.degrees(math.atan(sw / (2 * f_chosen)))
        hfov_w_at_max = 2 * max_distance * math.tan(math.radians(real_hfov / 2))
        cm_per_px = obj_width_cm / required_px
        req_res = int(math.ceil(hfov_w_at_max / cm_per_px))

        selected_res = None
        for (name, rw, rh) in COMMON_RESOLUTIONS:
            if rw >= req_res:
                selected_res = (name, rw, rh)
                break

        if not selected_res:
            continue

        res_name, rw, rh = selected_res
        pixel_pitch = (sw / rw) * 1000  # um

        # DOF calculation to find smallest valid f-number
        chosen_fnum = None
        for N in COMMON_F_NUMBERS:

            airy = 2.44 * lambda_um * N
            delta = max(airy, pixel_pitch)
            C = (2 * delta) / 1000  # mm

            fmm = f_chosen
            u_mm = max_distance * 10

            H = fmm + (fmm * fmm) / (N * C)

            near_mm = (H * u_mm) / (H + (u_mm - fmm))
            far_mm = (H * u_mm) / (H - (u_mm - fmm)) if u_mm < H else float("inf")

            near_cm = near_mm / 10
            far_cm = float("inf") if far_mm == float("inf") else far_mm / 10

            if near_cm <= min_distance and far_cm >= max_distance:
                chosen_fnum = N
                break

        if not chosen_fnum:
            continue

        # Compute both HFOV and DFOV
        real_hfov = 2 * math.degrees(math.atan(sw / (2 * f_chosen)))
        diag = math.sqrt(sw ** 2 + sh ** 2)
        real_dfov = 2 * math.degrees(math.atan(diag / (2 * f_chosen)))

        # Store candidate
        candidates.append({
            "model_name": generate_model_name(),
            "sensor_name": sensor_name,
            "sensor_w": sw,
            "sensor_h": sh,
            "focal_length": f_chosen,
            "f_number": chosen_fnum,
            "resolution": (res_name, rw, rh),
            "pixel_pitch": pixel_pitch,
            "real_hfov": real_hfov,
            "real_dfov": real_dfov,
            "near_cm": near_cm,
            "far_cm": far_cm,
            "h_res": rw,  # Store horizontal resolution for ranking
            "v_res": rh   # Store vertical resolution for ranking
        })

    # ================================================================
    # CUSTOM RANKING BASED ON USER PRIORITIES
    # ================================================================
    if candidates:
        # Define priority mapping (strip emoji for mapping)
        priority_map = {
            "Low-light performance": "light",
            "Low distortion": "distortion",
            "High resolution": "resolution"
        }
        
        priorities = [priority_map[priority_1], priority_map[priority_2], priority_map[priority_3]]
        weights = [0.5, 0.3, 0.2]  # Default weights: higher for 1st priority
        
        # Normalize scores for each candidate
        light_scores = [1.0 / c["f_number"] for c in candidates]
        distortion_scores = [c["focal_length"] for c in candidates]
        resolution_scores = [c["h_res"] * c["v_res"] for c in candidates]
        
        # Normalize to [0, 1] range
        def normalize_scores(scores):
            if not scores or max(scores) == min(scores):
                return [1.0] * len(scores)
            min_s, max_s = min(scores), max(scores)
            return [(s - min_s) / (max_s - min_s) if max_s > min_s else 1.0 for s in scores]
        
        light_scores_norm = normalize_scores(light_scores)
        distortion_scores_norm = normalize_scores(distortion_scores)
        resolution_scores_norm = normalize_scores(resolution_scores)
        
        # Assign scores based on priority order
        score_maps = {
            "light": light_scores_norm,
            "distortion": distortion_scores_norm,
            "resolution": resolution_scores_norm
        }
        
        # Calculate final scores for each candidate
        final_scores = []
        for i, candidate in enumerate(candidates):
            score = 0.0
            for priority, weight in zip(priorities, weights):
                score += weight * score_maps[priority][i]
            final_scores.append(score)
        
        # Sort by final score (descending)
        candidates_with_scores = list(zip(candidates, final_scores))
        candidates_with_scores.sort(key=lambda x: x[1], reverse=True)
        candidates = [c[0] for c in candidates_with_scores]
        
        # Keep top 3
        candidates = candidates[:3]
        
        # Store priority info in session state for display
        st.session_state.current_priorities = [priority_1, priority_2, priority_3]


# ============================================================
# BEST RECOMMENDED CAMERA (Full Card)
# ============================================================
with left_col:

    st.markdown("""
    <a name='result'></a>
    <div class='apple-card'>
        <div class='section-title'>Best Recommended Camera</div>
    """, unsafe_allow_html=True)

    if start:
        if not candidates:
            st.error("No valid camera configuration found.")
        else:
            best = candidates[0]
            res_name, rw, rh = best["resolution"]

            # ★ Model Name (Apple Blue Highlight)
            st.markdown(
                f"<div class='best-model-name'>{best['model_name']}</div>",
                unsafe_allow_html=True
            )

            # Create two columns: left for specs, right for image
            spec_col, img_col = st.columns([0.5, 0.5])
            
            with spec_col:
                # All parameters (24 px text)
                st.write(f"**Sensor Format:** {best['sensor_name']}")
                st.write(f"**Sensor Size:** {best['sensor_w']:.2f} × {best['sensor_h']:.2f} mm")
                st.write(f"**Focal Length:** {best['focal_length']:.2f} mm")
                st.write(f"**Aperture:** f/{best['f_number']:.1f}")
                st.write(f"**Resolution:** {res_name} ({rw} × {rh})")
                st.write(f"**Pixel Pitch:** {best['pixel_pitch']:.2f} µm")
                st.write(f"**Horizontal FOV:** {best['real_hfov']:.2f}°")
                st.write(f"**Diagonal FOV:** {best['real_dfov']:.2f}°")

                near_s = f"{best['near_cm']:.1f} cm"
                far_s = "∞" if best["far_cm"] == float("inf") else f"{best['far_cm']:.1f} cm"
                st.write(f"**Depth of Field:** {near_s} → {far_s}")

                # Restart button
                if st.button("Restart", key="restart_button"):
                    st.experimental_rerun()
            
            with img_col:
                # Randomly select one of the camera images
                camera_images = ["camera1.jpg", "camera2.jpg", "camera3.jpg", "camera4.jpg", "camera5.jpg"]
                selected_camera_img = random.choice(camera_images)
                
                if os.path.exists(selected_camera_img):
                    st.image(selected_camera_img, use_container_width=True)
                else:
                    st.write(f"*Camera image not found*")

    else:
        st.info("Fill inputs and click **Start Finding Your Camera** to compute results.")

    st.markdown("</div>", unsafe_allow_html=True)

# Auto-scroll to Best Recommended Camera section
if start:
    # Use st.session_state to track scroll request
    st.session_state.scroll_to_results = True

# Create an anchor point for results
with left_col:
    if "scroll_to_results" in st.session_state and st.session_state.scroll_to_results:
        st.markdown("""
        <script>
            // Try multiple methods to scroll
            setTimeout(() => {
                const mainElement = document.querySelector('[data-testid="stAppViewContainer"]') || 
                                   document.querySelector('section.main') ||
                                   window;
                const targetElement = document.querySelector('[data-testid="stVerticalBlock"]');
                if (targetElement) {
                    targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            }, 500);
        </script>
        """, unsafe_allow_html=True)


# ============================================================
# CANDIDATE COMPARISON (Full Card)
# ============================================================
with left_col:

    st.markdown("""
    <div class='apple-card'>
        <div class='section-title'>Candidate Camera Comparison</div>
    """, unsafe_allow_html=True)

    if start and candidates:
        # Display active priority order
        if "current_priorities" in st.session_state:
            priorities_text = " → ".join(st.session_state.current_priorities)
            st.markdown(f"""
            <div style="font-size: 14px; color: #555; margin-bottom: 1rem;">
            <strong>Ranking Priority:</strong> {priorities_text}
            </div>
            """, unsafe_allow_html=True)
        
        exp = st.expander("View All Candidate Cameras (Top 3)", expanded=False)

        with exp:
            cols = st.columns(len(candidates))

            for idx, cam in enumerate(candidates):
                with cols[idx]:
                    name, rw, rh = cam["resolution"]
                    near_s = f"{cam['near_cm']:.1f} cm"
                    far_s = "∞" if cam["far_cm"] == float("inf") else f"{cam['far_cm']:.1f} cm"
                    
                    st.markdown(f"""
                    <div class='compare-card'>
                        <h3>{cam["model_name"]}</h3>
                        <p><strong>Sensor:</strong> {cam['sensor_name']}</p>
                        <p><strong>Size:</strong> {cam['sensor_w']:.2f} × {cam['sensor_h']:.2f} mm</p>
                        <p><strong>Focal Length:</strong> {cam['focal_length']:.2f} mm</p>
                        <p><strong>Aperture:</strong> f/{cam['f_number']:.1f}</p>
                        <p><strong>Resolution:</strong> {name} ({rw} × {rh})</p>
                        <p><strong>Pixel Pitch:</strong> {cam['pixel_pitch']:.2f} µm</p>
                        <p><strong>HFOV:</strong> {cam['real_hfov']:.2f}°</p>
                        <p><strong>DFOV:</strong> {cam['real_dfov']:.2f}°</p>
                        <p><strong>DOF:</strong> {near_s} → {far_s}</p>
                    </div>
                    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
