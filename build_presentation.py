import os
import json
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# -------------------------------------------------------------
# Color Palette (Modern Deep Dark Slate Theme)
# -------------------------------------------------------------
BG_COLOR = RGBColor(11, 15, 25)         # Deepest Slate
CARD_BG = RGBColor(21, 29, 46)          # Card container slate
CARD_BORDER = RGBColor(37, 50, 75)      # Card border
TEXT_WHITE = RGBColor(248, 250, 252)    # Title / prominent text
TEXT_LIGHT = RGBColor(203, 213, 225)    # Body text
TEXT_MUTED = RGBColor(148, 163, 184)    # Subtitle / labels
TEXT_DIM = RGBColor(100, 116, 139)      # Footers / minor notes

ACCENT_CYAN = RGBColor(56, 189, 248)    # Edge AI / General accent
ACCENT_GREEN = RGBColor(52, 211, 153)   # Embedded / Success
ACCENT_AMBER = RGBColor(245, 158, 11)   # Robotics / Hardware
ACCENT_PURPLE = RGBColor(168, 85, 247)  # RL / Simulation
ACCENT_BLUE = RGBColor(96, 165, 250)    # Technical details

BASE_DIR = r"c:\Users\DELL\portfolio\portofolio"
IMAGES_DIR = os.path.join(BASE_DIR, "assets", "images")
OUTPUT_PPTX = os.path.join(BASE_DIR, "Fitra_Nurmayadi_Technical_Portfolio.pptx")
GHPAGES_PPTX = r"c:\Users\DELL\portfolio\fitranurmayadi.github.io\Fitra_Nurmayadi_Technical_Portfolio.pptx"

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # Blank slide

    def set_slide_bg(slide):
        """Creates a dark slate background covering the entire slide."""
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background() # No line
        return bg

    def add_header(slide, title, category_tag=None, subtitle=None):
        """Adds standard clean header to content slides."""
        top = Inches(0.4)
        
        # Category Tag badge
        if category_tag:
            tag_box = slide.shapes.add_textbox(Inches(0.8), top, Inches(11.5), Inches(0.35))
            tf_tag = tag_box.text_frame
            tf_tag.word_wrap = True
            tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
            p_tag = tf_tag.paragraphs[0]
            p_tag.text = category_tag.upper()
            p_tag.font.name = "Segoe UI"
            p_tag.font.size = Pt(10)
            p_tag.font.bold = True
            p_tag.font.color.rgb = ACCENT_CYAN
            top += Inches(0.32)

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), top, Inches(11.5), Inches(0.55))
        tf = title_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Segoe UI"
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE

        # Subtitle
        if subtitle:
            sub_box = slide.shapes.add_textbox(Inches(0.8), top + Inches(0.48), Inches(11.5), Inches(0.35))
            tf_sub = sub_box.text_frame
            tf_sub.word_wrap = True
            tf_sub.margin_left = tf_sub.margin_top = tf_sub.margin_right = tf_sub.margin_bottom = 0
            p_sub = tf_sub.paragraphs[0]
            p_sub.text = subtitle
            p_sub.font.name = "Segoe UI"
            p_sub.font.size = Pt(11)
            p_sub.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER):
        """Creates a subtle rounded rectangular card."""
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        if border_color:
            card.line.color.rgb = border_color
            card.line.width = Pt(1)
        else:
            card.line.fill.background()
        return card

    # =========================================================================
    # SLIDE 1: Cover / Hero Slide
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide1)

    # Accent decorative bar
    bar = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.3), Inches(0.12), Inches(4.8))
    bar.fill.solid()
    bar.fill.fore_color.rgb = ACCENT_CYAN
    bar.line.fill.background()

    # Hero Text Box
    hero_box = slide1.shapes.add_textbox(Inches(1.2), Inches(1.2), Inches(11.0), Inches(5.0))
    tf1 = hero_box.text_frame
    tf1.word_wrap = True

    # Pre-title
    p0 = tf1.paragraphs[0]
    p0.text = "TECHNICAL PORTFOLIO & RESEARCH SHOWCASE"
    p0.font.name = "Segoe UI"
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = ACCENT_CYAN
    p0.space_after = Pt(10)

    # Main Name
    p1 = tf1.add_paragraph()
    p1.text = "FITRA NURMAYADI"
    p1.font.name = "Segoe UI"
    p1.font.size = Pt(40)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.space_after = Pt(6)

    # Title
    p2 = tf1.add_paragraph()
    p2.text = "Computer & Embedded Systems Engineer"
    p2.font.name = "Segoe UI"
    p2.font.size = Pt(20)
    p2.font.color.rgb = TEXT_LIGHT
    p2.space_after = Pt(24)

    # Core Domains
    p3 = tf1.add_paragraph()
    p3.text = "CORE ENGINEERING DISCIPLINES"
    p3.font.name = "Segoe UI"
    p3.font.size = Pt(11)
    p3.font.bold = True
    p3.font.color.rgb = TEXT_MUTED
    p3.space_after = Pt(8)

    domains = [
        "1. Edge AI & Hardware Benchmarking (Hailo-8L, Jetson Orin Nano, On-Chip INT8 LLMs)",
        "2. Robotics & Autonomous Control (6-DOF Kinematics, Dynamic Inverted Pendulums, BLDC)",
        "3. Reinforcement Learning & Simulation (PyBullet 6-DOF VTVL, MuJoCo, PPO/SAC/TD3)",
        "4. Embedded Systems & Custom Hardware (ESP32-S3/C3, FreeRTOS, LoRa, CAN-Bus, KiCad PCBs)"
    ]
    for d in domains:
        pd = tf1.add_paragraph()
        pd.text = "•  " + d
        pd.font.name = "Segoe UI"
        pd.font.size = Pt(12)
        pd.font.color.rgb = TEXT_LIGHT
        pd.space_after = Pt(4)

    # Bottom links box
    links_box = slide1.shapes.add_textbox(Inches(1.2), Inches(6.3), Inches(11.0), Inches(0.6))
    tf_links = links_box.text_frame
    pl = tf_links.paragraphs[0]
    pl.text = "🌐  fitranurmayadi.github.io     |     💻  github.com/fitranurmayadi"
    pl.font.name = "Segoe UI"
    pl.font.size = Pt(11)
    pl.font.color.rgb = ACCENT_CYAN

    # =========================================================================
    # SLIDE 2: Core Competencies & Architecture
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide2)
    add_header(slide2, "Engineering Overview & Technical Architecture", "CORE COMPETENCIES", "Bridging on-device intelligence, high-frequency dynamic control, and custom PCB hardware.")

    cards_data = [
        ("Edge AI & NPU Benchmarking", ACCENT_CYAN, [
            "Empirical benchmarking across SBCs & NPUs",
            "Hailo-8L (13 TOPS), Jetson Orin Nano, RK3588",
            "1.84M INT8 Generative LLM on ESP32-S3",
            "Flash-mapped RAG & Vector Embeddings",
            "Inference latency, wattage & thermal profiling"
        ]),
        ("Robotics & Autonomous Systems", ACCENT_AMBER, [
            "3-DOF Manipulator with YOLOv11 Visual Sorting",
            "Inverse Kinematics & coordinate transformation",
            "Two-Wheeled Self-Balancing Robot (BLDC)",
            "High-speed optical quadrature velocity loops",
            "FreeRTOS dual-core multitasking control loops"
        ]),
        ("RL & Physics Simulation", ACCENT_PURPLE, [
            "PyBullet 6-DOF Falcon 9 VTVL Simulator",
            "Aerodynamic crosswinds & TVC gimbal dynamics",
            "Deep RL algorithms: PPO, SAC, TD3, DDPG",
            "MuJoCo dynamic balancing environments",
            "Sim-to-Real policy transfer & ONNX deployment"
        ]),
        ("Custom Hardware & IoT", ACCENT_GREEN, [
            "KiCad 2-layer PCB layout & component assembly",
            "ideaSTEAM XB1: ESP32 development board",
            "Automotive ISO 11898 CAN-Bus telemetry",
            "Long-range solar LoRa wireless sensor networks",
            "Industrial power & environmental telemetry"
        ])
    ]

    c_w = Inches(2.76)
    c_h = Inches(5.1)
    c_y = Inches(1.8)
    for i, (title, color, bullets) in enumerate(cards_data):
        c_x = Inches(0.8 + i * 2.95)
        add_card(slide2, c_x, c_y, c_w, c_h)

        # Card Title
        tb = slide2.shapes.add_textbox(c_x + Inches(0.2), c_y + Inches(0.2), c_w - Inches(0.4), Inches(0.8))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Segoe UI"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = color

        # Divider line
        div = slide2.shapes.add_shape(MSO_SHAPE.RECTANGLE, c_x + Inches(0.2), c_y + Inches(0.95), c_w - Inches(0.4), Inches(0.02))
        div.fill.solid()
        div.fill.fore_color.rgb = color
        div.line.fill.background()

        # Bullets
        tb_b = slide2.shapes.add_textbox(c_x + Inches(0.2), c_y + Inches(1.1), c_w - Inches(0.4), Inches(3.8))
        tf_b = tb_b.text_frame
        tf_b.word_wrap = True
        for b_idx, b in enumerate(bullets):
            p_b = tf_b.paragraphs[0] if b_idx == 0 else tf_b.add_paragraph()
            p_b.text = "• " + b
            p_b.font.name = "Segoe UI"
            p_b.font.size = Pt(10.5)
            p_b.font.color.rgb = TEXT_LIGHT
            p_b.space_after = Pt(10)

    # =========================================================================
    # SLIDE 3: Flagship 1 - YOLO11-OBB Single Board Computer & Edge NPU Benchmark Suite
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide3)
    add_header(slide3, "YOLO11-OBB SBC & Edge NPU Benchmark Suite", "FLAGSHIP RESEARCH · MASTER'S THESIS", "Empirical cross-platform evaluation of oriented object detection on edge silicon.")

    # Left Column (Details)
    w_left = Inches(6.0)
    add_card(slide3, Inches(0.8), Inches(1.7), w_left, Inches(5.3))

    tb3 = slide3.shapes.add_textbox(Inches(1.0), Inches(1.9), w_left - Inches(0.4), Inches(4.9))
    tf3 = tb3.text_frame
    tf3.word_wrap = True

    p = tf3.paragraphs[0]
    p.text = "RESEARCH HIGHLIGHTS & ARCHITECTURE"
    p.font.name = "Segoe UI"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p.space_after = Pt(10)

    points3 = [
        ("Evaluated Hardware Platforms", "Raspberry Pi 5 (Cortex-A76), Raspberry Pi AI Kit with Hailo-8L NPU (13 TOPS via PCIe Gen2), NVIDIA Jetson Orin Nano (40 TOPS GPU/NVDLA), and Khadas Edge 2 (RK3588S, 6 TOPS NPU)."),
        ("Model & Workload", "YOLO11-OBB (Oriented Bounding Box) for aerial and arbitrary-oriented target detection, converted across native runtime backends: Hailo HEF, TensorRT, RKNN, ONNX."),
        ("Multi-Metric Empirical Suite", "Evaluated inference latency (ms), frame throughput (FPS), active power draw (Watts via hardware USB power meter), Joules-per-frame energy cost, and thermal throttling under continuous 15-minute load."),
        ("Key Conclusion", "Dedicated NPUs (Hailo-8L & RK3588) provide up to 5.4x higher energy efficiency (FPS/Watt) compared to standard host CPU inference while maintaining sub-20ms inference latency.")
    ]

    for label, desc in points3:
        p_l = tf3.add_paragraph()
        p_l.text = "▶  " + label + ":"
        p_l.font.name = "Segoe UI"
        p_l.font.size = Pt(11)
        p_l.font.bold = True
        p_l.font.color.rgb = TEXT_WHITE
        
        p_d = tf3.add_paragraph()
        p_d.text = desc
        p_d.font.name = "Segoe UI"
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = TEXT_LIGHT
        p_d.space_after = Pt(8)

    # Right Column (Charts)
    w_right = Inches(5.5)
    img_fps = os.path.join(IMAGES_DIR, "obb_benchmark_fps.png")
    img_lat = os.path.join(IMAGES_DIR, "obb_benchmark_latency.png")

    if os.path.exists(img_fps):
        add_card(slide3, Inches(7.0), Inches(1.7), w_right, Inches(2.55))
        slide3.shapes.add_picture(img_fps, Inches(7.1), Inches(1.75), width=Inches(5.3), height=Inches(2.45))

    if os.path.exists(img_lat):
        add_card(slide3, Inches(7.0), Inches(4.45), w_right, Inches(2.55))
        slide3.shapes.add_picture(img_lat, Inches(7.1), Inches(4.5), width=Inches(5.3), height=Inches(2.45))

    # =========================================================================
    # SLIDE 4: Flagship 2 - ESP32 Micro-LM: On-Chip 1.84M Language Model
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide4)
    add_header(slide4, "ESP32 Micro-LM: 1.84M On-Chip Generative Language Model", "EDGE AI & EMBEDDED INTELLIGENCE", "100% disconnected on-device token generation with flash-mapped RAG on ESP32-S3.")

    # 3 Cards Layout
    col_w = Inches(3.75)
    col_h = Inches(5.2)

    # Card 1: Hardware & Memory
    add_card(slide4, Inches(0.8), Inches(1.8), col_w, col_h)
    tb4_1 = slide4.shapes.add_textbox(Inches(1.0), Inches(2.0), col_w - Inches(0.4), col_h - Inches(0.4))
    tf4_1 = tb4_1.text_frame
    tf4_1.word_wrap = True
    p = tf4_1.paragraphs[0]
    p.text = "HARDWARE CONSTRAINTS"
    p.font.name = "Segoe UI"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p.space_after = Pt(12)

    c1_items = [
        "SoC Target: ESP32-S3 (Dual-Core Xtensa LX7 @ 240 MHz)",
        "Octal PSRAM: 8MB high-speed memory for KV-cache and intermediate activations",
        "SPI Flash: 16MB mapped via MMU for zero-copy weight execution",
        "Power Envelope: 3.3V, < 240mA active consumption",
        "Firmware Framework: Pure ESP-IDF (C++) with FreeRTOS dual-core task affinity"
    ]
    for it in c1_items:
        pi = tf4_1.add_paragraph()
        pi.text = "• " + it
        pi.font.name = "Segoe UI"
        pi.font.size = Pt(10.5)
        pi.font.color.rgb = TEXT_LIGHT
        pi.space_after = Pt(8)

    # Card 2: Quantization & Architecture
    add_card(slide4, Inches(4.78), Inches(1.8), col_w, col_h)
    tb4_2 = slide4.shapes.add_textbox(Inches(4.98), Inches(2.0), col_w - Inches(0.4), col_h - Inches(0.4))
    tf4_2 = tb4_2.text_frame
    tf4_2.word_wrap = True
    p = tf4_2.paragraphs[0]
    p.text = "QUANTIZATION & PIPELINE"
    p.font.name = "Segoe UI"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN
    p.space_after = Pt(12)

    c2_items = [
        "Parameter Scale: 1.84M parameters customized for domain-specific telemetry queries",
        "INT8 W8A32 Quantization: Weights stored as signed 8-bit integers, 32-bit accumulators to prevent overflow",
        "Dual-Core Pipelining: Core 0 handles token decoding & attention compute; Core 1 handles stream buffering & UART/OLED display",
        "SIMD Acceleration: Utilizing Xtensa PIE (Processor Instruction Extension) for vector dot-product acceleration"
    ]
    for it in c2_items:
        pi = tf4_2.add_paragraph()
        pi.text = "• " + it
        pi.font.name = "Segoe UI"
        pi.font.size = Pt(10.5)
        pi.font.color.rgb = TEXT_LIGHT
        pi.space_after = Pt(8)

    # Card 3: Offline Flash RAG & Impact
    add_card(slide4, Inches(8.76), Inches(1.8), col_w, col_h)
    tb4_3 = slide4.shapes.add_textbox(Inches(8.96), Inches(2.0), col_w - Inches(0.4), col_h - Inches(0.4))
    tf4_3 = tb4_3.text_frame
    tf4_3.word_wrap = True
    p = tf4_3.paragraphs[0]
    p.text = "FLASH RAG & BENEFITS"
    p.font.name = "Segoe UI"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER
    p.space_after = Pt(12)

    c3_items = [
        "Flash-Mapped Vector Index: Knowledge base encoded into compact INT8 embeddings in flash memory partition",
        "Zero Cloud Dependency: Operates completely offline in air-gapped industrial, defense, or wilderness environments",
        "Zero Subscription / API Cost: No OpenAI or cloud vendor lock-in",
        "Sub-Millisecond Retrieval: Cosine similarity search over sensor datasheets and device error codes",
        "Immediate Privacy: Raw data never leaves local chip boundary"
    ]
    for it in c3_items:
        pi = tf4_3.add_paragraph()
        pi.text = "• " + it
        pi.font.name = "Segoe UI"
        pi.font.size = Pt(10.5)
        pi.font.color.rgb = TEXT_LIGHT
        pi.space_after = Pt(8)

    # =========================================================================
    # SLIDE 5: Flagship 3 - RocketLander3D: 6-DOF Falcon 9 VTVL Simulator & RL
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide5)
    add_header(slide5, "RocketLander3D: 6-DOF Falcon 9 VTVL Flight Simulation & RL", "PHYSICS SIMULATION & REINFORCEMENT LEARNING", "Continuous 6-DOF rocketry flight simulator with thrust vectoring & aerodynamic crosswinds.")

    # Left Column
    w5_left = Inches(5.8)
    add_card(slide5, Inches(0.8), Inches(1.7), w5_left, Inches(5.3))

    tb5 = slide5.shapes.add_textbox(Inches(1.0), Inches(1.9), w5_left - Inches(0.4), Inches(4.9))
    tf5 = tb5.text_frame
    tf5.word_wrap = True

    p = tf5.paragraphs[0]
    p.text = "DYNAMICS & CONTROL POLICY"
    p.font.name = "Segoe UI"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE
    p.space_after = Pt(10)

    points5 = [
        ("High-Fidelity 6-DOF Physics", "Modeled in PyBullet & Farama Gymnasium. Accounts for variable mass depletion as propellant burns, changing center of mass (CoM), and moment of inertia tensor over time."),
        ("Actuation & Aerodynamics", "Simulates Thrust Vector Control (TVC) 2-axis engine gimbal deflection (+/- 15 deg), cold gas thruster attitude control, dynamic atmospheric crosswinds, and landing leg ground contact mechanics."),
        ("Reinforcement Learning Algorithms", "Trained continuous action-space neural policies: Proximal Policy Optimization (PPO) and Soft Actor-Critic (SAC) against reward formulations prioritizing fuel conservation, upright attitude, and touchdown velocity < 1.0 m/s."),
        ("Baseline Benchmarking", "Compared RL policy convergence against classical Cascaded PID and LQR controllers under turbulent wind shear.")
    ]

    for label, desc in points5:
        p_l = tf5.add_paragraph()
        p_l.text = "▶  " + label + ":"
        p_l.font.name = "Segoe UI"
        p_l.font.size = Pt(11)
        p_l.font.bold = True
        p_l.font.color.rgb = TEXT_WHITE
        
        p_d = tf5.add_paragraph()
        p_d.text = desc
        p_d.font.name = "Segoe UI"
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = TEXT_LIGHT
        p_d.space_after = Pt(8)

    # Right Column Images
    w5_right = Inches(5.7)
    img_rsim = os.path.join(IMAGES_DIR, "rocketlander3d_sim.png")
    img_rrep = os.path.join(IMAGES_DIR, "rocketlander3d_report.png")

    if os.path.exists(img_rsim):
        add_card(slide5, Inches(6.8), Inches(1.7), w5_right, Inches(2.55))
        slide5.shapes.add_picture(img_rsim, Inches(6.9), Inches(1.75), width=Inches(5.5), height=Inches(2.45))

    if os.path.exists(img_rrep):
        add_card(slide5, Inches(6.8), Inches(4.45), w5_right, Inches(2.55))
        slide5.shapes.add_picture(img_rrep, Inches(6.9), Inches(4.5), width=Inches(5.5), height=Inches(2.45))

    # =========================================================================
    # SLIDE 6: Flagship 4 - 3-DOF Robotic Arm with YOLOv11 Visual Sorting
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide6)
    add_header(slide6, "3-DOF Robotic Arm with YOLOv11 Visual Sorting", "ROBOTICS & COMPUTER VISION", "Integration of real-time machine vision, inverse kinematics, and multi-servo actuation.")

    # Left Column
    w6_left = Inches(5.8)
    add_card(slide6, Inches(0.8), Inches(1.7), w6_left, Inches(5.3))

    tb6 = slide6.shapes.add_textbox(Inches(1.0), Inches(1.9), w6_left - Inches(0.4), Inches(4.9))
    tf6 = tb6.text_frame
    tf6.word_wrap = True

    p = tf6.paragraphs[0]
    p.text = "HARDWARE & VISION PIPELINE"
    p.font.name = "Segoe UI"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER
    p.space_after = Pt(10)

    points6 = [
        ("Robotic Manipulator Hardware", "Heavy-duty aluminum alloy chassis with 3 degrees of freedom plus end-effector gripper. Powered by high-torque metal-gear servos (MG996R / DS3218) driven by a dedicated 16-channel PCA9685 I2C PWM driver."),
        ("Vision Pipeline (YOLOv11)", "Overhead camera stream processed via YOLOv11 inference for real-time item classification and bounding box localization."),
        ("Spatial Coordinate Mapping", "Calibrated OpenCV homography and perspective transformation mapping 2D image pixel coordinates (u, v) into physical millimeter coordinates (X, Y, Z) on the conveyor sorting plane."),
        ("Inverse Kinematics Solver", "Geometric and trigonometric IK solver executing on the embedded controller, converting target (X, Y, Z) coordinates into precise joint angles (theta_1, theta_2, theta_3) with trajectory smoothing.")
    ]

    for label, desc in points6:
        p_l = tf6.add_paragraph()
        p_l.text = "▶  " + label + ":"
        p_l.font.name = "Segoe UI"
        p_l.font.size = Pt(11)
        p_l.font.bold = True
        p_l.font.color.rgb = TEXT_WHITE
        
        p_d = tf6.add_paragraph()
        p_d.text = desc
        p_d.font.name = "Segoe UI"
        p_d.font.size = Pt(10)
        p_d.font.color.rgb = TEXT_LIGHT
        p_d.space_after = Pt(8)

    # Right Column Images
    w6_right = Inches(5.7)
    img_arm1 = os.path.join(IMAGES_DIR, "robotic_arm_1.jpeg")
    img_arm2 = os.path.join(IMAGES_DIR, "robotic_arm_2.jpeg")

    if os.path.exists(img_arm1):
        add_card(slide6, Inches(6.8), Inches(1.7), w6_right, Inches(2.55))
        slide6.shapes.add_picture(img_arm1, Inches(7.4), Inches(1.75), width=Inches(4.3), height=Inches(2.45))

    if os.path.exists(img_arm2):
        add_card(slide6, Inches(6.8), Inches(4.45), w6_right, Inches(2.55))
        slide6.shapes.add_picture(img_arm2, Inches(7.4), Inches(4.5), width=Inches(4.3), height=Inches(2.45))

    # =========================================================================
    # SLIDE 7: Robotics & Autonomous Control Highlights
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide7)
    add_header(slide7, "Robotics & Dynamic Control Highlights", "ROBOTICS & CONTROL SYSTEMS", "High-frequency embedded balance loops, competitive robotics, and kinematic platforms.")

    robotics_projects = [
        ("TWSBR Nidec 24H BLDC Hardware", ACCENT_AMBER, [
            "Dynamic inverted-pendulum balancing robot",
            "Dual Nidec 24H brushless DC motors with optical quadrature encoders",
            "MPU6050 6-axis IMU complementary sensor fusion filter",
            "High-frequency FreeRTOS dual-core balance loop",
            "Live WiFi / OSC telemetry for state debugging"
        ]),
        ("Competition Line Follower Robot", ACCENT_CYAN, [
            "7-channel front phototransistor array with LM339 comparators",
            "High-RPM coreless DC motors with magnetic hall encoders",
            "Non-volatile EEPROM calibration for on-track PID tuning",
            "Dynamic cornering braking & acceleration feedforward"
        ]),
        ("Wi-Fi Combat Sumo Robot", ACCENT_GREEN, [
            "High-torque differential drive combat platform on ESP32",
            "On-board asynchronous web server (ESPAsyncWebServer)",
            "Zero-latency responsive touch GUI with dual fader controls",
            "SoftAP local wireless network with failsafe timeout"
        ]),
        ("Quadruped Spider & Myo EMG Arm", ACCENT_PURPLE, [
            "8-DOF spider robot with parametric gait kinematics",
            "Myo EMG armband decoding muscle biopotential signals",
            "Prosthetic hand teleoperation via gesture classification",
            "Smooth servo interpolation avoiding high current spikes"
        ])
    ]

    for i, (p_title, color, bullets) in enumerate(robotics_projects):
        rx = Inches(0.8 + (i % 2) * 5.95)
        ry = Inches(1.8 + (i // 2) * 2.65)
        rw = Inches(5.75)
        rh = Inches(2.45)
        add_card(slide7, rx, ry, rw, rh)

        tb = slide7.shapes.add_textbox(rx + Inches(0.25), ry + Inches(0.2), rw - Inches(0.5), rh - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = p_title
        p.font.name = "Segoe UI"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = color
        p.space_after = Pt(8)

        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = "• " + b
            pb.font.name = "Segoe UI"
            pb.font.size = Pt(10)
            pb.font.color.rgb = TEXT_LIGHT
            pb.space_after = Pt(3)

    # =========================================================================
    # SLIDE 8: Reinforcement Learning & Simulation Showcase
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide8)
    add_header(slide8, "Reinforcement Learning & Physics Simulation", "RL ALGORITHMS & DYNAMICS", "Evaluating continuous control algorithms in rigorous physics simulation engines.")

    # 2 Big Cards
    add_card(slide8, Inches(0.8), Inches(1.8), Inches(5.75), Inches(5.1))
    tb8_1 = slide8.shapes.add_textbox(Inches(1.05), Inches(2.0), Inches(5.25), Inches(4.7))
    tf8_1 = tb8_1.text_frame
    tf8_1.word_wrap = True

    p = tf8_1.paragraphs[0]
    p.text = "twsbr-rl: Inverted Pendulum RL Benchmark"
    p.font.name = "Segoe UI"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p.space_after = Pt(12)

    twsbr_points = [
        ("Simulated Physics Engines", "Implemented across both MuJoCo and PyBullet for high-speed parallel rollouts."),
        ("Continuous Deep RL Benchmark", "Benchmarked Soft Actor-Critic (SAC), Proximal Policy Optimization (PPO), and Twin Delayed DDPG (TD3) under random impulse disturbances."),
        ("Baseline Comparison", "Evaluated against analytical Linear Quadratic Regulator (LQR) and Cascaded PID controllers."),
        ("Observation & Reward Space", "Includes tilt angle (theta), angular velocity (theta_dot), cart position (x), linear velocity (x_dot), and motor torque penalization."),
        ("Edge Deployment Pipeline", "Trained policy networks exported to ONNX format for on-device inference on embedded ARM/ESP32 microcontrollers.")
    ]
    for lbl, desc in twsbr_points:
        pl = tf8_1.add_paragraph()
        pl.text = "▶ " + lbl + ":"
        pl.font.name = "Segoe UI"
        pl.font.size = Pt(10.5)
        pl.font.bold = True
        pl.font.color.rgb = TEXT_WHITE
        pd = tf8_1.add_paragraph()
        pd.text = desc
        pd.font.name = "Segoe UI"
        pd.font.size = Pt(9.5)
        pd.font.color.rgb = TEXT_LIGHT
        pd.space_after = Pt(6)

    # Card 2: LunarLander3D & Sim-to-Real
    add_card(slide8, Inches(6.75), Inches(1.8), Inches(5.75), Inches(5.1))
    tb8_2 = slide8.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.25), Inches(4.7))
    tf8_2 = tb8_2.text_frame
    tf8_2.word_wrap = True

    p = tf8_2.paragraphs[0]
    p.text = "LunarLander3D & Sim-to-Real Methodologies"
    p.font.name = "Segoe UI"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE
    p.space_after = Pt(12)

    lunar_points = [
        ("3D Continuous Low-Gravity Control", "Gymnasium environment simulating descent, attitude orientation, thruster throttling, and leg contact in lunar gravity (1.62 m/s²)."),
        ("Domain Randomization", "Perturbing friction coefficients, ground slope, sensor noise, and engine response lag during training to prevent overfitting."),
        ("Multi-Objective Reward Engineering", "Balancing soft landing speed (< 0.5 m/s), low fuel expenditure, vertical alignment, and landing pad touchdown accuracy."),
        ("Sim-to-Real Readiness", "Quantizing observation tensors to fixed-point / INT8, ensuring real-time inference latency fits within hardware micro-loop budgets (< 5ms).")
    ]
    for lbl, desc in lunar_points:
        pl = tf8_2.add_paragraph()
        pl.text = "▶ " + lbl + ":"
        pl.font.name = "Segoe UI"
        pl.font.size = Pt(10.5)
        pl.font.bold = True
        pl.font.color.rgb = TEXT_WHITE
        pd = tf8_2.add_paragraph()
        pd.text = desc
        pd.font.name = "Segoe UI"
        pd.font.size = Pt(9.5)
        pd.font.color.rgb = TEXT_LIGHT
        pd.space_after = Pt(6)

    # =========================================================================
    # SLIDE 9: Custom Embedded Systems, IoT & PCB Hardware
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide9)
    add_header(slide9, "Custom Embedded Hardware, IoT & PCB Engineering", "EMBEDDED SYSTEMS & HARDWARE CODESIGN", "Production-grade microcontrollers, custom PCBs, CAN-bus networks, and wireless telemetry.")

    embedded_projects = [
        ("ideaSTEAM XB1: Custom ESP32 Dev Board", ACCENT_GREEN, [
            "Designed 2-layer PCB in KiCad with USB-C CP2102 auto-flasher",
            "High-efficiency LDO regulator circuit with reverse polarity protection",
            "Breadboard-friendly standardized 0.1\" breakout headers",
            "Tested and deployed for educational STEM & robotics prototyping"
        ]),
        ("Electric Vehicle (EV) CAN-Bus Telemetry", ACCENT_CYAN, [
            "Automotive ISO 11898 standard implementation via MCP2515 transceiver",
            "Real-time battery pack thermals, cell voltages, and motor RPM telemetry",
            "High-reliability differential signaling rejecting EMI/noise",
            "Local TFT dashboard visualization and alert trigger thresholds"
        ]),
        ("ESP32-C3 RISC-V AC Power Monitoring", ACCENT_AMBER, [
            "Isolated AC power meter via PZEM-004T optical UART isolation",
            "Monitors active power (W), voltage, current (A), energy (kWh), and frequency",
            "MQTT message broker telemetry published to InfluxDB and Grafana",
            "ESP32-C3 single-core RISC-V with WiFi & BLE 5.0"
        ]),
        ("Solar Long-Range LoRa Agricultural System", ACCENT_BLUE, [
            "Semtech SX1278 433 MHz LoRa transceiver with +20 dBm PA",
            "Deep sleep current < 15 uA powered by solar LiFePO4 battery management",
            "Multi-sensor array: soil moisture, air temperature, relative humidity, light",
            "Range > 5 km non-line-of-sight telemetry in remote farm fields"
        ])
    ]

    for i, (p_title, color, bullets) in enumerate(embedded_projects):
        rx = Inches(0.8 + (i % 2) * 5.95)
        ry = Inches(1.8 + (i // 2) * 2.65)
        rw = Inches(5.75)
        rh = Inches(2.45)
        add_card(slide9, rx, ry, rw, rh)

        tb = slide9.shapes.add_textbox(rx + Inches(0.25), ry + Inches(0.2), rw - Inches(0.5), rh - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = p_title
        p.font.name = "Segoe UI"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = color
        p.space_after = Pt(8)

        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = "• " + b
            pb.font.name = "Segoe UI"
            pb.font.size = Pt(10)
            pb.font.color.rgb = TEXT_LIGHT
            pb.space_after = Pt(3)

    # =========================================================================
    # SLIDE 10: Environmental & Industrial IoT Deployments
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide10)
    add_header(slide10, "Industrial & Environmental IoT Deployments", "APPLIED IOT SYSTEMS", "Real-world telemetry solutions operating in aquacultural, agricultural, and residential facilities.")

    iot_deployments = [
        ("Biofloc Fish Pond Automation", [
            "Real-time dissolved oxygen (DO), pH, temperature, and water level monitoring",
            "Automated aerator motor control relays with hysteresis thresholds",
            "GSM/GPRS and Wi-Fi dual-fallback telemetry alerting farm managers"
        ]),
        ("Vertical Hydroponic & Nutrient Control", [
            "Total Dissolved Solids (TDS) and Electrical Conductivity (EC) feedback loops",
            "Peristaltic dosing pumps for precision pH up/down and nutrient A/B injection",
            "Cyclic irrigation scheduler maintaining root oxygenation"
        ]),
        ("Low-Power Weather Parameter Station", [
            "Barometric pressure (BME280), wind speed anemometer, rainfall tipping bucket",
            "Ultra-low-power battery telemetry transmitting via LoRa / MQTT",
            "Tested under tropical outdoor climate conditions for continuous operations"
        ]),
        ("Automated Mushroom Cultivation Environment", [
            "Ultrasonic mist humidifiers and exhaust fan ventilation control",
            "High-humidity capacitive sensors preventing spore saturation",
            "Dual-relay actuation maintaining strict 85-95% RH microclimate"
        ])
    ]

    for i, (title, bullets) in enumerate(iot_deployments):
        rx = Inches(0.8 + (i % 2) * 5.95)
        ry = Inches(1.8 + (i // 2) * 2.65)
        rw = Inches(5.75)
        rh = Inches(2.45)
        add_card(slide10, rx, ry, rw, rh)

        tb = slide10.shapes.add_textbox(rx + Inches(0.25), ry + Inches(0.2), rw - Inches(0.5), rh - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Segoe UI"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GREEN
        p.space_after = Pt(8)

        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = "• " + b
            pb.font.name = "Segoe UI"
            pb.font.size = Pt(10)
            pb.font.color.rgb = TEXT_LIGHT
            pb.space_after = Pt(3)

    # =========================================================================
    # SLIDE 11: End-to-End Technology & Tooling Stack
    # =========================================================================
    slide11 = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide11)
    add_header(slide11, "End-to-End Technology & Tooling Stack", "ENGINEERING CAPABILITIES", "Full vertical integration from schematic capture and board layout to deep learning & cloud.")

    tech_pillars = [
        ("HARDWARE & FIRMWARE", ACCENT_CYAN, [
            "Microcontrollers: ESP32, ESP32-S3, ESP32-C3 RISC-V, STM32, Arduino",
            "OS & Frameworks: ESP-IDF, FreeRTOS, STM32 HAL, PlatformIO",
            "Protocols: CAN-Bus (ISO 11898), LoRa, I2C, SPI, UART, Modbus RS485",
            "EDA / CAD: KiCad (schematic & multi-layer layout), Fusion 360 (CAD/STL)"
        ]),
        ("EDGE AI & MACHINE LEARNING", ACCENT_AMBER, [
            "Frameworks: PyTorch, TensorFlow Lite for Microcontrollers (TFLM)",
            "Edge Runtimes: Hailo Dataflow Compiler (HEF), NVIDIA TensorRT, RKNN-Toolkit2",
            "Computer Vision: YOLO11-OBB, YOLOv8, OpenCV, Homography / Calibration",
            "Quantization: INT8 W8A32, PTQ (Post-Training Quantization), Flash RAG"
        ]),
        ("SIMULATION & CONTROL", ACCENT_PURPLE, [
            "Physics Engines: MuJoCo, PyBullet, Farama Gymnasium",
            "RL Algorithms: Stable-Baselines3 (SAC, PPO, TD3, DDPG, A2C)",
            "Control Theory: LQR (Linear Quadratic Regulator), Cascaded PID, State-Space",
            "Export Formats: ONNX runtime, C++ embedded inference deployment"
        ]),
        ("SYSTEMS, DEVOPS & TELEMETRY", ACCENT_GREEN, [
            "Languages: Python, C/C++, JavaScript, Bash, SQL",
            "IoT & Telemetry: MQTT, WebSockets, OSC, REST API, ESPAsyncWebServer",
            "Data & Monitoring: InfluxDB, Grafana, Node-RED, Linux / Docker",
            "Version Control & CI/CD: Git, GitHub, Automated testing & documentation"
        ])
    ]

    for i, (title, color, items) in enumerate(tech_pillars):
        rx = Inches(0.8 + (i % 2) * 5.95)
        ry = Inches(1.8 + (i // 2) * 2.65)
        rw = Inches(5.75)
        rh = Inches(2.45)
        add_card(slide11, rx, ry, rw, rh)

        tb = slide11.shapes.add_textbox(rx + Inches(0.25), ry + Inches(0.2), rw - Inches(0.5), rh - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Segoe UI"
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = color
        p.space_after = Pt(8)

        for it in items:
            pb = tf.add_paragraph()
            pb.text = "• " + it
            pb.font.name = "Segoe UI"
            pb.font.size = Pt(10)
            pb.font.color.rgb = TEXT_LIGHT
            pb.space_after = Pt(3)

    # =========================================================================
    # SLIDE 12: Project Index & Open Source Repositories
    # =========================================================================
    slide12 = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide12)
    add_header(slide12, "Open Source Project Index & GitHub Repositories", "PUBLIC CODEBASES", "Well-documented, verifiable engineering repositories available on GitHub.")

    repos = [
        ("obb-sbc-benchmark", "Master's Thesis: Cross-platform YOLO11-OBB benchmark on Hailo-8L, Jetson, Khadas", "Python, TensorRT, HEF"),
        ("esp32-microlm", "100% on-device 1.84M INT8 generative language model & flash RAG on ESP32-S3", "C++, ESP-IDF, FreeRTOS"),
        ("rocketlander3d", "6-DOF Falcon 9 VTVL flight simulator with thrust vector control and deep RL", "Python, PyBullet, Gymnasium"),
        ("twsbr-rl", "MuJoCo/PyBullet simulation environment & RL balance benchmark with ONNX export", "Python, MuJoCo, SB3"),
        ("ESP32C3-PowerMonitoring", "AC energy monitoring via PZEM-004T optical UART and MQTT telemetry", "C++, ESP32-C3, MQTT"),
        ("line-follower", "High-speed line follower with on-track EEPROM PID auto-calibration", "C++, PWM, Hardware Encoders"),
        ("S2SProject", "On-chip Genetic Algorithm PID auto-tuning on dual-core ESP32-S3", "C++, GA, Embedded Optimization"),
        ("weather-stations-lora-mqtt", "Solar-powered long-range multi-sensor meteorological station", "C++, LoRa, Deep Sleep"),
        ("waterflow-monitoring-mqtt", "Precision Hall-effect fluid dynamics telemetry with MQTT alerting", "C++, Pulse Counter, FreeRTOS"),
        ("muse-myo-arduino-js", "EMG biopotential classification and robotic hand teleoperation", "C++, JavaScript, Web Bluetooth")
    ]

    # Two-column repo listing
    for i, (name, desc, stack) in enumerate(repos):
        col = i // 5
        row = i % 5
        rx = Inches(0.8 + col * 5.95)
        ry = Inches(1.8 + row * 1.05)
        rw = Inches(5.75)
        rh = Inches(0.95)

        add_card(slide12, rx, ry, rw, rh)

        tb = slide12.shapes.add_textbox(rx + Inches(0.15), ry + Inches(0.1), rw - Inches(0.3), rh - Inches(0.2))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = "github.com/fitranurmayadi/" + name
        p.font.name = "Segoe UI"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = ACCENT_CYAN

        p2 = tf.add_paragraph()
        p2.text = desc + "  (" + stack + ")"
        p2.font.name = "Segoe UI"
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 13: Summary & Contact / Collaboration
    # =========================================================================
    slide13 = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide13)

    add_card(slide13, Inches(1.5), Inches(1.2), Inches(10.333), Inches(5.1))

    tb13 = slide13.shapes.add_textbox(Inches(2.0), Inches(1.6), Inches(9.333), Inches(4.3))
    tf13 = tb13.text_frame
    tf13.word_wrap = True

    p = tf13.paragraphs[0]
    p.text = "ENGINEERING PHILOSOPHY & SUMMARY"
    p.font.name = "Segoe UI"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p.space_after = Pt(14)

    p_body = tf13.add_paragraph()
    p_body.text = (
        "Committed to rigorous, first-principles engineering across the full hardware-software stack. "
        "Whether deploying INT8 quantized neural networks to resource-constrained microcontrollers, "
        "modeling 6-DOF dynamic physics environments, or routing impedance-controlled PCBs in KiCad, "
        "the objective remains clear: high reliability, verifiable benchmarks, and zero unnecessary fluff."
    )
    p_body.font.name = "Segoe UI"
    p_body.font.size = Pt(14)
    p_body.font.color.rgb = TEXT_LIGHT
    p_body.space_after = Pt(28)

    # Contact Box
    p_c_title = tf13.add_paragraph()
    p_c_title.text = "CONNECT & COLLABORATE"
    p_c_title.font.name = "Segoe UI"
    p_c_title.font.size = Pt(12)
    p_c_title.font.bold = True
    p_c_title.font.color.rgb = ACCENT_AMBER
    p_c_title.space_after = Pt(10)

    contacts = [
        ("Portfolio Website", "https://fitranurmayadi.github.io"),
        ("GitHub Profile", "https://github.com/fitranurmayadi"),
        ("Primary Disciplines", "Edge AI Acceleration · Embedded Systems · Robotics & Dynamics · Physics Simulation")
    ]
    for lbl, val in contacts:
        pc = tf13.add_paragraph()
        pc.text = lbl + ":  " + val
        pc.font.name = "Segoe UI"
        pc.font.size = Pt(12)
        pc.font.bold = (lbl == "Portfolio Website")
        pc.font.color.rgb = TEXT_WHITE if lbl != "Primary Disciplines" else TEXT_MUTED
        pc.space_after = Pt(4)

    # Save to portofolio
    prs.save(OUTPUT_PPTX)
    print("Saved PPTX to:", OUTPUT_PPTX)

    # Also save to github.io
    prs.save(GHPAGES_PPTX)
    print("Saved copy to:", GHPAGES_PPTX)

if __name__ == "__main__":
    create_deck()
