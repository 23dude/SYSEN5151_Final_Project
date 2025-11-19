import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(page_title="Camera Finder", layout="wide")

# ============================================================
# Top Navigation Bar
# ============================================================
st.markdown("""
<style>
/* Override Streamlit defaults */
[data-testid="stAppViewContainer"] {
    padding: 0 !important;
}

.appViewContainer {
    padding: 0 !important;
}

/* Smooth scrolling */
html {
    scroll-behavior: smooth;
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
    cursor: default;
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

/* Smooth scroll offset for fixed navbar */
.scroll-target {
    scroll-margin-top: 70px;
}

/* Add padding to main content to account for fixed navbar */
.main-content {
    margin-top: 48px;
}
</style>

<div class="navbar">
    <div class="nav-container">
        <div class="logo">📷 Camera Finder</div>
        <div class="nav-links">
            <span onclick="scrollToFeatures()">Features</span>
            <span onclick="scrollToAbout()">About</span>
            <span onclick="scrollToContact()">Contact</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# JavaScript for smooth scrolling
components.html("""
<script>
window.scrollToFeatures = function() {
    const element = parent.document.getElementById('features-section');
    if (element) {
        const yOffset = -60;
        const y = element.getBoundingClientRect().top + parent.window.pageYOffset + yOffset;
        parent.window.scrollTo({top: y, behavior: 'smooth'});
    }
}
window.scrollToAbout = function() {
    const element = parent.document.getElementById('about-section');
    if (element) {
        const yOffset = -60;
        const y = element.getBoundingClientRect().top + parent.window.pageYOffset + yOffset;
        parent.window.scrollTo({top: y, behavior: 'smooth'});
    }
}
window.scrollToContact = function() {
    const element = parent.document.getElementById('contact-section');
    if (element) {
        const yOffset = -60;
        const y = element.getBoundingClientRect().top + parent.window.pageYOffset + yOffset;
        parent.window.scrollTo({top: y, behavior: 'smooth'});
    }
}
</script>
""", height=0)

# ============================================================
# Hero Section with Button
# ============================================================
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto, sans-serif !important;
    color: #1d1d1f !important;
    background: #ffffff !important;
}

/* Add top margin to account for fixed navbar */
[data-testid="stAppViewContainer"] {
    padding-top: 48px !important;
}

.hero-section {
    text-align: center;
    padding: 10px 20px 40px;
    background: linear-gradient(135deg, #ffffff 0%, #f9f9fb 100%);
}

.hero-title {
    font-size: 72px !important;
    font-weight: 700 !important;
    letter-spacing: -2px !important;
    margin: 40px 0 20px;
    color: #1d1d1f !important;
}

.hero-subtitle {
    font-size: 24px !important;
    font-weight: 400 !important;
    color: #666666 !important;
    margin-bottom: 40px;
    line-height: 1.4;
}

.camera-icon-display {
    font-size: 140px;
    margin-bottom: 30px;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-15px); }
}

.button-wrapper {
    text-align: center;
    padding: 40px 20px 80px;
    background: linear-gradient(135deg, #ffffff 0%, #f9f9fb 100%);
}

.stButton > button {
    padding: 16px 48px !important;
    background: #0071e3 !important;
    color: white !important;
    font-size: 20px !important;
    font-weight: 600 !important;
    border: none !important;
    border-radius: 12px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 8px 20px rgba(0, 113, 227, 0.2) !important;
}

.stButton > button:hover {
    background: #0071e3 !important;
    transform: translateY(-2px);
    box-shadow: 0 12px 30px rgba(0, 113, 227, 0.3) !important;
}

.features-section {
    background: #f5f5f7;
    padding: 80px 20px;
}

.features-title {
    font-size: 40px !important;
    font-weight: 700 !important;
    text-align: center;
    margin-bottom: 60px;
    color: #1d1d1f !important;
}

.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 30px;
    max-width: 1000px;
    margin: 0 auto;
}

.feature-card {
    background: white;
    padding: 40px 30px;
    border-radius: 18px;
    border: 1px solid #e5e5e7;
    text-align: center;
    transition: all 0.3s ease;
}

.feature-card:hover {
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
    border-color: #d2d2d7;
}

.feature-icon {
    font-size: 36px;
    margin-bottom: 15px;
}

.feature-card h3 {
    font-size: 18px !important;
    font-weight: 600 !important;
    margin-bottom: 10px;
    color: #1d1d1f !important;
}

.feature-card p {
    font-size: 15px !important;
    color: #666666 !important;
    line-height: 1.5;
    margin: 0;
}

.footer-section {
    padding: 60px 20px;
    text-align: center;
    border-top: 1px solid #e5e5e7;
    background: white;
}

.footer-text {
    font-size: 14px !important;
    color: #86868b !important;
    margin: 0;
}
</style>

<div class="hero-section">
    <div class="camera-icon-display">📷</div>
    <h1 class="hero-title">Camera Finder</h1>
    <p class="hero-subtitle">
        Discover the perfect camera for your needs.<br>
        Intelligent recommendations based on your requirements.
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# Get Started Button (Centered)
# ============================================================
col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 1, 1, 1, 1])
with col4:
    if st.button("Get Started", key="start_finder", use_container_width=True):
        st.switch_page("pages/camera_finder.py")

st.markdown('<div style="padding: 20px;"></div>', unsafe_allow_html=True)

# ============================================================
# Features Section
# ============================================================
st.markdown("""
<div class="features-section scroll-target" id="features-section">
    <h2 class="features-title">Powerful Features</h2>
    <div class="features-grid">
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <h3>Smart Recommendations</h3>
            <p>AI-powered analysis to find your ideal camera instantly</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <h3>Precision Calculation</h3>
            <p>Advanced optical engineering equations at your fingertips</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3>Detailed Comparison</h3>
            <p>Compare multiple camera options side by side</p>
        </div>
    </div>
</div>

<div class="about-section scroll-target" id="about-section" style="background: #fff; padding: 80px 20px; text-align: center;">
    <h2 class="features-title">About</h2>
    <p style="font-size: 18px; color: #666; max-width: 700px; margin: 0 auto;">Camera Finder is a professional tool designed to help you select the best camera for your needs. Our intelligent system provides recommendations, comparisons, and technical insights.</p>
</div>

<div class="contact-section scroll-target" id="contact-section" style="background: #f5f5f7; padding: 80px 20px; text-align: center;">
    <h2 class="features-title">Contact</h2>
    <p style="font-size: 18px; color: #666; max-width: 700px; margin: 0 auto;">For support or inquiries, please email us at <a href="mailto:info@camerafinder.com">info@camerafinder.com</a>.</p>
</div>

<div class="footer-section">
    <p class="footer-text">Camera Finder v1.0 | Professional Camera Selection Tool</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<script>
function scrollToFeatures() {
    const element = document.getElementById('features-section');
    if (element) {
        const yOffset = -60;
        const y = element.getBoundingClientRect().top + window.pageYOffset + yOffset;
        window.scrollTo({top: y, behavior: 'smooth'});
    }
}
function scrollToAbout() {
    const element = document.getElementById('about-section');
    if (element) {
        const yOffset = -60;
        const y = element.getBoundingClientRect().top + window.pageYOffset + yOffset;
        window.scrollTo({top: y, behavior: 'smooth'});
    }
}
function scrollToContact() {
    const element = document.getElementById('contact-section');
    if (element) {
        const yOffset = -60;
        const y = element.getBoundingClientRect().top + window.pageYOffset + yOffset;
        window.scrollTo({top: y, behavior: 'smooth'});
    }
}
// Re-attach scroll functions after DOM updates (Streamlit rerender)
document.addEventListener('DOMContentLoaded', function() {
    window.scrollToFeatures = scrollToFeatures;
    window.scrollToAbout = scrollToAbout;
    window.scrollToContact = scrollToContact;
});
</script>
""", unsafe_allow_html=True)


