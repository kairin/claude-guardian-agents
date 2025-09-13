#!/usr/bin/env python3
"""
Generate custom SVG designs for all guardian agents.
Each SVG has a unique design that represents the agent's role and specialization.
"""

from pathlib import Path

# Project root
PROJECT_ROOT = Path("/home/kkk/Apps/claude-guardian-agents")
ASSETS_DIR = PROJECT_ROOT / "assets"


def create_cto_leadership_svg():
    """Create CTO Leadership Guardian SVG with tech leadership symbolism."""
    return """<?xml version="1.0" encoding="UTF-8"?>
<svg width="100%" height="220px" viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg" style="background-color: #0a0a0a;">
  <title>CTO Leadership Guardian</title>
  <desc>Technology vision and engineering leadership</desc>
  <defs>
    <linearGradient id="cto-tech-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#00D4FF;" />
      <stop offset="50%" style="stop-color:#0099FF;" />
      <stop offset="100%" style="stop-color:#0066CC;" />
    </linearGradient>
    <linearGradient id="cto-accent-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#FFD700;" />
      <stop offset="100%" style="stop-color:#FFA500;" />
    </linearGradient>
    <radialGradient id="cto-glow">
      <stop offset="0%" stop-color="#00D4FF" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#00D4FF" stop-opacity="0"/>
    </radialGradient>
    <pattern id="circuit-pattern" x="0" y="0" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M10,10 L30,10 M20,10 L20,30 M10,30 L30,30" stroke="#0099FF" stroke-width="0.5" fill="none" opacity="0.3"/>
      <circle cx="10" cy="10" r="2" fill="#00D4FF" opacity="0.5"/>
      <circle cx="30" cy="30" r="2" fill="#00D4FF" opacity="0.5"/>
    </pattern>
  </defs>

  <!-- Background circuit board pattern -->
  <rect x="0" y="0" width="400" height="220" fill="url(#circuit-pattern)"/>

  <!-- Central glow effect -->
  <circle cx="200" cy="110" r="80" fill="url(#cto-glow)" />

  <!-- Leadership crown/peak symbol -->
  <path d="M150,110 L170,70 L185,90 L200,60 L215,90 L230,70 L250,110 Z"
        fill="url(#cto-tech-grad)" stroke="#00D4FF" stroke-width="2" opacity="0.9"/>

  <!-- Technology core hexagon -->
  <polygon points="200,70 240,90 240,130 200,150 160,130 160,90"
           fill="none" stroke="url(#cto-tech-grad)" stroke-width="3"/>

  <!-- Inner technology symbol -->
  <g transform="translate(200,110)">
    <!-- Central processor -->
    <rect x="-20" y="-20" width="40" height="40" fill="url(#cto-tech-grad)" stroke="#000" stroke-width="2"/>
    <!-- Connection nodes -->
    <circle cx="-30" cy="0" r="5" fill="url(#cto-accent-grad)"/>
    <circle cx="30" cy="0" r="5" fill="url(#cto-accent-grad)"/>
    <circle cx="0" cy="-30" r="5" fill="url(#cto-accent-grad)"/>
    <circle cx="0" cy="30" r="5" fill="url(#cto-accent-grad)"/>
    <!-- Connection lines -->
    <line x1="-20" y1="0" x2="-25" y2="0" stroke="#FFD700" stroke-width="2"/>
    <line x1="20" y1="0" x2="25" y2="0" stroke="#FFD700" stroke-width="2"/>
    <line x1="0" y1="-20" x2="0" y2="-25" stroke="#FFD700" stroke-width="2"/>
    <line x1="0" y1="20" x2="0" y2="25" stroke="#FFD700" stroke-width="2"/>
  </g>

  <!-- Binary code decoration -->
  <text x="200" y="180" text-anchor="middle" fill="#0099FF" font-family="monospace" font-size="10" opacity="0.6">
    01100011 01110100 01101111
  </text>
</svg>"""


def create_coo_leadership_svg() -> str:
    """Create COO Leadership Guardian SVG with operations excellence symbolism."""
    return """<?xml version="1.0" encoding="UTF-8"?>
<svg width="100%" height="220px" viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg" style="background-color: #0a0a0a;">
  <title>COO Leadership Guardian</title>
  <desc>Operations strategy and organizational efficiency</desc>
  <defs>
    <linearGradient id="coo-ops-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#FF6B6B;" />
      <stop offset="50%" style="stop-color:#D0021B;" />
      <stop offset="100%" style="stop-color:#8B0000;" />
    </linearGradient>
    <linearGradient id="coo-accent-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#FFD93D;" />
      <stop offset="100%" style="stop-color:#F5A623;" />
    </linearGradient>
    <radialGradient id="coo-glow">
      <stop offset="0%" stop-color="#FFD93D" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#FFD93D" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- Central glow -->
  <circle cx="200" cy="110" r="70" fill="url(#coo-glow)" />

  <!-- Gear system representing operations -->
  <g id="gear-large">
    <circle cx="200" cy="110" r="45" fill="none" stroke="url(#coo-ops-grad)" stroke-width="3"/>
    <path d="M200,65 L205,70 L200,75 L195,70 Z" fill="url(#coo-ops-grad)"/>
    <path d="M245,110 L240,115 L235,110 L240,105 Z" fill="url(#coo-ops-grad)"/>
    <path d="M200,155 L195,150 L200,145 L205,150 Z" fill="url(#coo-ops-grad)"/>
    <path d="M155,110 L160,105 L165,110 L160,115 Z" fill="url(#coo-ops-grad)"/>
    <!-- Diagonal teeth -->
    <path d="M230,80 L235,85 L230,90 L225,85 Z" fill="url(#coo-ops-grad)" transform="rotate(45 200 110)"/>
    <path d="M230,130 L235,125 L230,120 L225,125 Z" fill="url(#coo-ops-grad)" transform="rotate(45 200 110)"/>
    <path d="M170,80 L175,85 L170,90 L165,85 Z" fill="url(#coo-ops-grad)" transform="rotate(45 200 110)"/>
    <path d="M170,130 L175,125 L170,120 L165,125 Z" fill="url(#coo-ops-grad)" transform="rotate(45 200 110)"/>
  </g>

  <!-- Small gear 1 -->
  <g transform="translate(150,85)">
    <circle r="20" fill="none" stroke="url(#coo-accent-grad)" stroke-width="2"/>
    <circle r="8" fill="url(#coo-accent-grad)"/>
  </g>

  <!-- Small gear 2 -->
  <g transform="translate(250,135)">
    <circle r="20" fill="none" stroke="url(#coo-accent-grad)" stroke-width="2"/>
    <circle r="8" fill="url(#coo-accent-grad)"/>
  </g>

  <!-- Central efficiency symbol -->
  <g transform="translate(200,110)">
    <polygon points="0,-25 15,-15 15,0 0,10 -15,0 -15,-15"
             fill="url(#coo-ops-grad)" stroke="#000" stroke-width="2"/>
    <!-- Upward arrow for growth -->
    <path d="M0,5 L0,-15 M-5,-10 L0,-15 L5,-10"
          stroke="url(#coo-accent-grad)" stroke-width="3" fill="none"/>
  </g>

  <!-- Efficiency metrics bars -->
  <g transform="translate(200,170)">
    <rect x="-30" y="0" width="8" height="15" fill="url(#coo-accent-grad)" opacity="0.7"/>
    <rect x="-15" y="-5" width="8" height="20" fill="url(#coo-accent-grad)" opacity="0.7"/>
    <rect x="0" y="-10" width="8" height="25" fill="url(#coo-accent-grad)" opacity="0.7"/>
    <rect x="15" y="-15" width="8" height="30" fill="url(#coo-accent-grad)" opacity="0.7"/>
  </g>
</svg>"""


def create_first_principles_svg():
    """Create First Principles Guardian SVG with physics/fundamental laws symbolism."""
    return """<?xml version="1.0" encoding="UTF-8"?>
<svg width="100%" height="220px" viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg" style="background-color: #0a0a0a;">
  <title>First Principles Guardian</title>
  <desc>Fundamental physics and reductionist reasoning</desc>
  <defs>
    <linearGradient id="physics-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#9013FE;" />
      <stop offset="100%" style="stop-color:#4A0088;" />
    </linearGradient>
    <linearGradient id="physics-accent" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#FFFFFF;" />
      <stop offset="100%" style="stop-color:#E0E0E0;" />
    </linearGradient>
    <radialGradient id="physics-glow">
      <stop offset="0%" stop-color="#9013FE" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#9013FE" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- Atomic structure background -->
  <circle cx="200" cy="110" r="70" fill="url(#physics-glow)" />

  <!-- Electron orbits -->
  <ellipse cx="200" cy="110" rx="60" ry="20" fill="none" stroke="url(#physics-grad)" stroke-width="1" opacity="0.6"/>
  <ellipse cx="200" cy="110" rx="60" ry="20" fill="none" stroke="url(#physics-grad)" stroke-width="1" opacity="0.6" transform="rotate(60 200 110)"/>
  <ellipse cx="200" cy="110" rx="60" ry="20" fill="none" stroke="url(#physics-grad)" stroke-width="1" opacity="0.6" transform="rotate(120 200 110)"/>

  <!-- Electrons -->
  <circle cx="260" cy="110" r="4" fill="url(#physics-accent)">
    <animateTransform attributeName="transform" type="rotate" from="0 200 110" to="360 200 110" dur="10s" repeatCount="indefinite"/>
  </circle>
  <circle cx="170" cy="95" r="4" fill="url(#physics-accent)">
    <animateTransform attributeName="transform" type="rotate" from="0 200 110" to="360 200 110" dur="8s" repeatCount="indefinite"/>
  </circle>
  <circle cx="200" cy="50" r="4" fill="url(#physics-accent)">
    <animateTransform attributeName="transform" type="rotate" from="0 200 110" to="360 200 110" dur="12s" repeatCount="indefinite"/>
  </circle>

  <!-- Central nucleus -->
  <g transform="translate(200,110)">
    <circle r="20" fill="url(#physics-grad)" stroke="#000" stroke-width="2"/>
    <!-- Protons and neutrons -->
    <circle cx="-5" cy="-5" r="6" fill="url(#physics-accent)" opacity="0.8"/>
    <circle cx="5" cy="-5" r="6" fill="#FFD700" opacity="0.8"/>
    <circle cx="0" cy="5" r="6" fill="url(#physics-accent)" opacity="0.8"/>
  </g>

  <!-- Mathematical formulas -->
  <text x="200" y="180" text-anchor="middle" fill="url(#physics-grad)" font-family="serif" font-size="14" font-style="italic">
    F = ma
  </text>
  <text x="200" y="195" text-anchor="middle" fill="url(#physics-grad)" font-family="serif" font-size="14" font-style="italic">
    E = mc²
  </text>

  <!-- Quantum wave function -->
  <path d="M100,110 Q150,90 200,110 T300,110" fill="none" stroke="url(#physics-accent)" stroke-width="1" opacity="0.4"/>
</svg>"""


def create_mathematician_svg():
    """Create Mathematician Guardian SVG with mathematical symbols and formulas."""
    return """<?xml version="1.0" encoding="UTF-8"?>
<svg width="100%" height="220px" viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg" style="background-color: #0a0a0a;">
  <title>Mathematician Logical Guardian</title>
  <desc>Mathematical precision and logical reasoning</desc>
  <defs>
    <linearGradient id="math-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2E7D32;" />
      <stop offset="100%" style="stop-color:#1B5E20;" />
    </linearGradient>
    <linearGradient id="math-accent" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#64B5F6;" />
      <stop offset="100%" style="stop-color:#1976D2;" />
    </linearGradient>
    <pattern id="grid-pattern" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M20,0 L0,0 L0,20" fill="none" stroke="#2E7D32" stroke-width="0.5" opacity="0.2"/>
    </pattern>
  </defs>

  <!-- Grid background -->
  <rect x="0" y="0" width="400" height="220" fill="url(#grid-pattern)"/>

  <!-- Golden ratio spiral -->
  <path d="M200,110 Q230,110 230,80 Q230,50 200,50 Q140,50 140,110 Q140,200 230,200"
        fill="none" stroke="url(#math-grad)" stroke-width="2" opacity="0.6"/>

  <!-- Central infinity symbol -->
  <g transform="translate(200,110)">
    <path d="M-30,0 Q-30,-20 -10,-20 Q10,-20 10,0 Q10,20 -10,20 Q-30,20 -30,0
             M30,0 Q30,20 10,20 Q-10,20 -10,0 Q-10,-20 10,-20 Q30,-20 30,0 Z"
          fill="url(#math-grad)" stroke="#000" stroke-width="2"/>
  </g>

  <!-- Mathematical symbols floating around -->
  <text x="120" y="70" fill="url(#math-accent)" font-family="serif" font-size="20" font-style="italic">∫</text>
  <text x="280" y="70" fill="url(#math-accent)" font-family="serif" font-size="20">∑</text>
  <text x="120" y="150" fill="url(#math-accent)" font-family="serif" font-size="20">π</text>
  <text x="280" y="150" fill="url(#math-accent)" font-family="serif" font-size="20">∂</text>

  <!-- Logic gates -->
  <g transform="translate(150,110)">
    <path d="M0,-10 L-15,-10 L-15,10 L0,10 Q10,0 0,-10 Z" fill="none" stroke="url(#math-accent)" stroke-width="1"/>
    <text x="-10" y="4" fill="url(#math-accent)" font-family="monospace" font-size="8">AND</text>
  </g>

  <g transform="translate(250,110)">
    <path d="M0,-10 L-15,-10 L-15,10 L0,10 Q10,0 0,-10 Z" fill="none" stroke="url(#math-accent)" stroke-width="1"/>
    <circle cx="12" cy="0" r="3" fill="none" stroke="url(#math-accent)" stroke-width="1"/>
    <text x="-10" y="4" fill="url(#math-accent)" font-family="monospace" font-size="8">NOT</text>
  </g>

  <!-- Formula -->
  <text x="200" y="185" text-anchor="middle" fill="url(#math-grad)" font-family="serif" font-size="12" font-style="italic">
    ∀x ∈ ℝ : x² ≥ 0
  </text>
</svg>"""


def create_creative_lateral_svg() -> str:
    """Create Creative Lateral Guardian SVG with artistic and unconventional elements."""
    return """<?xml version="1.0" encoding="UTF-8"?>
<svg width="100%" height="220px" viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg" style="background-color: #0a0a0a;">
  <title>Creative Lateral Guardian</title>
  <desc>Lateral thinking and artistic innovation</desc>
  <defs>
    <linearGradient id="creative-grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#FF006E;" />
      <stop offset="33%" style="stop-color:#8338EC;" />
      <stop offset="66%" style="stop-color:#3A86FF;" />
      <stop offset="100%" style="stop-color:#06FFB4;" />
    </linearGradient>
    <linearGradient id="creative-grad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#FFBE0B;" />
      <stop offset="50%" style="stop-color:#FB5607;" />
      <stop offset="100%" style="stop-color:#FF006E;" />
    </linearGradient>
    <filter id="paint-splatter">
      <feTurbulence baseFrequency="0.02" numOctaves="3" seed="5"/>
      <feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 20 -10"/>
    </filter>
  </defs>

  <!-- Paint splatter effect -->
  <ellipse cx="180" cy="100" rx="40" ry="35" fill="url(#creative-grad1)" opacity="0.6" filter="url(#paint-splatter)"/>
  <ellipse cx="220" cy="120" rx="35" ry="40" fill="url(#creative-grad2)" opacity="0.6" filter="url(#paint-splatter)"/>

  <!-- Abstract brush strokes -->
  <path d="M100,80 Q150,120 200,90 T300,110" fill="none" stroke="url(#creative-grad1)" stroke-width="8" stroke-linecap="round" opacity="0.7"/>
  <path d="M120,130 Q180,100 240,130 T320,100" fill="none" stroke="url(#creative-grad2)" stroke-width="6" stroke-linecap="round" opacity="0.7"/>

  <!-- Central creative burst -->
  <g transform="translate(200,110)">
    <!-- Irregular star burst -->
    <path d="M0,0 L-10,-30 L0,-15 L15,-35 L5,-10 L30,-15 L10,0 L35,10 L10,5 L25,30 L0,10 L-20,35 L-5,5 L-30,20 L-10,0 L-35,-10 Z"
          fill="url(#creative-grad1)" stroke="#000" stroke-width="1" opacity="0.9"/>
    <!-- Paint palette -->
    <ellipse cx="0" cy="0" rx="20" ry="15" fill="none" stroke="#000" stroke-width="2"/>
    <circle cx="-8" cy="-5" r="3" fill="#FF006E"/>
    <circle cx="0" cy="-5" r="3" fill="#8338EC"/>
    <circle cx="8" cy="-5" r="3" fill="#3A86FF"/>
    <circle cx="-4" cy="3" r="3" fill="#FFBE0B"/>
    <circle cx="4" cy="3" r="3" fill="#06FFB4"/>
  </g>

  <!-- Thought bubbles breaking convention -->
  <circle cx="150" cy="60" r="8" fill="none" stroke="url(#creative-grad2)" stroke-width="2" stroke-dasharray="3,3"/>
  <circle cx="170" cy="50" r="10" fill="none" stroke="url(#creative-grad2)" stroke-width="2" stroke-dasharray="3,3"/>
  <circle cx="250" cy="60" r="8" fill="none" stroke="url(#creative-grad1)" stroke-width="2" stroke-dasharray="3,3"/>
  <circle cx="230" cy="50" r="10" fill="none" stroke="url(#creative-grad1)" stroke-width="2" stroke-dasharray="3,3"/>
</svg>"""


def create_inventor_svg() -> str:
    """Create Inventor Guardian SVG with gears, lightbulb, and innovation symbols."""
    return """<?xml version="1.0" encoding="UTF-8"?>
<svg width="100%" height="220px" viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg" style="background-color: #0a0a0a;">
  <title>Inventor Innovative Guardian</title>
  <desc>Practical innovation and systematic invention</desc>
  <defs>
    <linearGradient id="invent-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#FFC107;" />
      <stop offset="100%" style="stop-color:#FF6F00;" />
    </linearGradient>
    <linearGradient id="invent-accent" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#00BCD4;" />
      <stop offset="100%" style="stop-color:#006064;" />
    </linearGradient>
    <radialGradient id="bulb-glow">
      <stop offset="0%" stop-color="#FFEB3B" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#FFEB3B" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- Glowing lightbulb effect -->
  <circle cx="200" cy="100" r="60" fill="url(#bulb-glow)" />

  <!-- Lightbulb -->
  <g transform="translate(200,100)">
    <path d="M-20,-30 Q-25,-15 -25,0 Q-25,15 -15,25 L15,25 Q25,15 25,0 Q25,-15 20,-30 Q15,-40 0,-40 Q-15,-40 -20,-30 Z"
          fill="url(#invent-grad)" stroke="#000" stroke-width="2"/>
    <!-- Filament -->
    <path d="M-10,0 Q-5,-10 0,-15 Q5,-10 10,0" fill="none" stroke="#FF6F00" stroke-width="2"/>
    <!-- Base -->
    <rect x="-12" y="25" width="24" height="10" fill="#666" stroke="#000" stroke-width="1"/>
    <line x1="-12" y1="28" x2="12" y2="28" stroke="#444" stroke-width="1"/>
    <line x1="-12" y1="31" x2="12" y2="31" stroke="#444" stroke-width="1"/>
  </g>

  <!-- Innovation gears -->
  <g transform="translate(150,100)" opacity="0.7">
    <circle r="15" fill="none" stroke="url(#invent-accent)" stroke-width="2"/>
    <path d="M0,-15 L3,-18 L-3,-18 Z M15,0 L18,3 L18,-3 Z M0,15 L-3,18 L3,18 Z M-15,0 L-18,-3 L-18,3 Z"
          fill="url(#invent-accent)"/>
    <circle r="5" fill="url(#invent-accent)"/>
  </g>

  <g transform="translate(250,100)" opacity="0.7">
    <circle r="15" fill="none" stroke="url(#invent-accent)" stroke-width="2"/>
    <path d="M0,-15 L3,-18 L-3,-18 Z M15,0 L18,3 L18,-3 Z M0,15 L-3,18 L3,18 Z M-15,0 L-18,-3 L-18,3 Z"
          fill="url(#invent-accent)"/>
    <circle r="5" fill="url(#invent-accent)"/>
  </g>

  <!-- Blueprint grid lines -->
  <g opacity="0.3">
    <line x1="100" y1="50" x2="300" y2="50" stroke="url(#invent-accent)" stroke-width="0.5" stroke-dasharray="5,5"/>
    <line x1="100" y1="150" x2="300" y2="150" stroke="url(#invent-accent)" stroke-width="0.5" stroke-dasharray="5,5"/>
    <line x1="100" y1="50" x2="100" y2="150" stroke="url(#invent-accent)" stroke-width="0.5" stroke-dasharray="5,5"/>
    <line x1="300" y1="50" x2="300" y2="150" stroke="url(#invent-accent)" stroke-width="0.5" stroke-dasharray="5,5"/>
  </g>

  <!-- Innovation sparks -->
  <g transform="translate(200,100)">
    <path d="M-35,-35 L-30,-30 M35,-35 L30,-30 M-35,35 L-30,30 M35,35 L30,30"
          stroke="url(#invent-grad)" stroke-width="3" stroke-linecap="round"/>
  </g>
</svg>"""


def create_human_patterns_svg() -> str:
    """Create Human Patterns Guardian SVG with anthropological and cultural symbols."""
    return """<?xml version="1.0" encoding="UTF-8"?>
<svg width="100%" height="220px" viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg" style="background-color: #0a0a0a;">
  <title>Human Patterns Guardian</title>
  <desc>Cultural anthropology and behavioral patterns</desc>
  <defs>
    <linearGradient id="human-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#8B4513;" />
      <stop offset="100%" style="stop-color:#5D2F0B;" />
    </linearGradient>
    <linearGradient id="human-accent" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#FFB74D;" />
      <stop offset="100%" style="stop-color:#E65100;" />
    </linearGradient>
  </defs>

  <!-- Cultural circle pattern -->
  <circle cx="200" cy="110" r="60" fill="none" stroke="url(#human-grad)" stroke-width="2" opacity="0.6"/>
  <circle cx="200" cy="110" r="45" fill="none" stroke="url(#human-grad)" stroke-width="1" opacity="0.5"/>
  <circle cx="200" cy="110" r="30" fill="none" stroke="url(#human-grad)" stroke-width="1" opacity="0.4"/>

  <!-- Human figures in circle formation -->
  <g id="human-figure">
    <circle cx="0" cy="-5" r="4" fill="url(#human-accent)"/>
    <path d="M0,-1 L0,10 M0,2 L-5,8 M0,2 L5,8 M0,10 L-3,18 M0,10 L3,18"
          stroke="url(#human-accent)" stroke-width="2" stroke-linecap="round"/>
  </g>

  <!-- Figures around the circle -->
  <use href="#human-figure" transform="translate(200,60)"/>
  <use href="#human-figure" transform="translate(250,110)"/>
  <use href="#human-figure" transform="translate(200,160)"/>
  <use href="#human-figure" transform="translate(150,110)"/>
  <use href="#human-figure" transform="translate(235,75)"/>
  <use href="#human-figure" transform="translate(235,145)"/>
  <use href="#human-figure" transform="translate(165,75)"/>
  <use href="#human-figure" transform="translate(165,145)"/>

  <!-- Central connection web -->
  <g transform="translate(200,110)" opacity="0.4">
    <line x1="0" y1="-50" x2="50" y2="0" stroke="url(#human-accent)" stroke-width="1"/>
    <line x1="50" y1="0" x2="0" y2="50" stroke="url(#human-accent)" stroke-width="1"/>
    <line x1="0" y1="50" x2="-50" y2="0" stroke="url(#human-accent)" stroke-width="1"/>
    <line x1="-50" y1="0" x2="0" y2="-50" stroke="url(#human-accent)" stroke-width="1"/>
    <line x1="35" y1="-35" x2="35" y2="35" stroke="url(#human-accent)" stroke-width="1"/>
    <line x1="35" y1="35" x2="-35" y2="35" stroke="url(#human-accent)" stroke-width="1"/>
    <line x1="-35" y1="35" x2="-35" y2="-35" stroke="url(#human-accent)" stroke-width="1"/>
    <line x1="-35" y1="-35" x2="35" y2="-35" stroke="url(#human-accent)" stroke-width="1"/>
  </g>

  <!-- Cultural symbols -->
  <text x="200" y="115" text-anchor="middle" fill="url(#human-grad)" font-size="24" font-weight="bold">∞</text>
</svg>"""


def create_psychologist_svg() -> str:
    """Create Psychologist Guardian SVG with brain, behavior, and psychology symbols."""
    return """<?xml version="1.0" encoding="UTF-8"?>
<svg width="100%" height="220px" viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg" style="background-color: #0a0a0a;">
  <title>Psychologist Behavioral Guardian</title>
  <desc>Psychological analysis and behavioral insights</desc>
  <defs>
    <linearGradient id="psych-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#E91E63;" />
      <stop offset="100%" style="stop-color:#880E4F;" />
    </linearGradient>
    <linearGradient id="psych-accent" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#9C27B0;" />
      <stop offset="100%" style="stop-color:#4A148C;" />
    </linearGradient>
    <radialGradient id="mind-glow">
      <stop offset="0%" stop-color="#E91E63" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#E91E63" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- Mind glow effect -->
  <ellipse cx="200" cy="110" rx="70" ry="60" fill="url(#mind-glow)" />

  <!-- Brain outline -->
  <g transform="translate(200,110)">
    <path d="M-30,-20 Q-35,-30 -25,-35 Q-15,-40 -5,-35 Q0,-40 5,-35 Q15,-40 25,-35 Q35,-30 30,-20
             Q35,-10 30,0 Q35,10 25,20 Q20,30 10,30 Q0,35 -10,30 Q-20,30 -25,20 Q-35,10 -30,0 Q-35,-10 -30,-20 Z"
          fill="url(#psych-grad)" stroke="#000" stroke-width="2"/>

    <!-- Brain folds -->
    <path d="M-20,-15 Q-10,-20 0,-15 M0,-15 Q10,-20 20,-15 M-15,0 Q-5,-5 5,0 M5,0 Q15,-5 20,5 M-10,15 Q0,10 10,15"
          fill="none" stroke="#880E4F" stroke-width="1.5"/>

    <!-- Neural connections -->
    <circle cx="-10" cy="-10" r="3" fill="url(#psych-accent)"/>
    <circle cx="10" cy="-10" r="3" fill="url(#psych-accent)"/>
    <circle cx="0" cy="5" r="3" fill="url(#psych-accent)"/>
    <circle cx="-15" cy="10" r="3" fill="url(#psych-accent)"/>
    <circle cx="15" cy="10" r="3" fill="url(#psych-accent)"/>

    <!-- Synaptic connections -->
    <line x1="-10" y1="-10" x2="10" y2="-10" stroke="url(#psych-accent)" stroke-width="1" opacity="0.6"/>
    <line x1="0" y1="5" x2="-15" y2="10" stroke="url(#psych-accent)" stroke-width="1" opacity="0.6"/>
    <line x1="0" y1="5" x2="15" y2="10" stroke="url(#psych-accent)" stroke-width="1" opacity="0.6"/>
  </g>

  <!-- Behavioral wave patterns -->
  <path d="M100,150 Q150,140 200,150 T300,150" fill="none" stroke="url(#psych-accent)" stroke-width="2" opacity="0.6"/>
  <path d="M100,160 Q150,170 200,160 T300,160" fill="none" stroke="url(#psych-accent)" stroke-width="2" opacity="0.5"/>
  <path d="M100,170 Q150,160 200,170 T300,170" fill="none" stroke="url(#psych-accent)" stroke-width="2" opacity="0.4"/>

  <!-- Psychology symbol (Psi) -->
  <text x="200" y="50" text-anchor="middle" fill="url(#psych-accent)" font-size="24" font-family="serif">Ψ</text>
</svg>"""


def create_child_naive_svg() -> str:
    """Create Child Naive Guardian SVG with playful, simple, curious elements."""
    return """<?xml version="1.0" encoding="UTF-8"?>
<svg width="100%" height="220px" viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg" style="background-color: #0a0a0a;">
  <title>Child Naive Guardian</title>
  <desc>Child-like simplicity and naive questioning</desc>
  <defs>
    <linearGradient id="child-grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#FF69B4;" />
      <stop offset="100%" style="stop-color:#FF1493;" />
    </linearGradient>
    <linearGradient id="child-grad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#87CEEB;" />
      <stop offset="100%" style="stop-color:#4169E1;" />
    </linearGradient>
    <linearGradient id="child-rainbow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#FF0000;" />
      <stop offset="16%" style="stop-color:#FF7F00;" />
      <stop offset="33%" style="stop-color:#FFFF00;" />
      <stop offset="50%" style="stop-color:#00FF00;" />
      <stop offset="66%" style="stop-color:#0000FF;" />
      <stop offset="83%" style="stop-color:#4B0082;" />
      <stop offset="100%" style="stop-color:#8B00FF;" />
    </linearGradient>
  </defs>

  <!-- Crayon-style scribbles -->
  <path d="M120,80 Q160,90 200,85 Q240,80 280,90" fill="none" stroke="url(#child-grad1)" stroke-width="6" stroke-linecap="round" opacity="0.7"/>
  <path d="M130,130 Q170,120 210,125 Q250,130 290,120" fill="none" stroke="url(#child-grad2)" stroke-width="6" stroke-linecap="round" opacity="0.7"/>

  <!-- Simple smiley face -->
  <g transform="translate(200,110)">
    <circle r="35" fill="none" stroke="url(#child-rainbow)" stroke-width="4"/>
    <!-- Eyes -->
    <circle cx="-12" cy="-8" r="4" fill="#000"/>
    <circle cx="12" cy="-8" r="4" fill="#000"/>
    <!-- Smile -->
    <path d="M-15,5 Q0,15 15,5" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round"/>
  </g>

  <!-- Question marks floating around -->
  <text x="150" y="70" fill="url(#child-grad1)" font-size="24" font-weight="bold" transform="rotate(-15 150 70)">?</text>
  <text x="250" y="70" fill="url(#child-grad2)" font-size="20" font-weight="bold" transform="rotate(15 250 70)">?</text>
  <text x="150" y="160" fill="url(#child-grad2)" font-size="22" font-weight="bold" transform="rotate(10 150 160)">?</text>
  <text x="250" y="160" fill="url(#child-grad1)" font-size="26" font-weight="bold" transform="rotate(-10 250 160)">?</text>

  <!-- Building blocks -->
  <rect x="170" y="170" width="20" height="20" fill="url(#child-grad1)" stroke="#000" stroke-width="1" transform="rotate(-5 180 180)"/>
  <rect x="195" y="175" width="20" height="20" fill="url(#child-grad2)" stroke="#000" stroke-width="1" transform="rotate(3 205 185)"/>
  <rect x="220" y="170" width="20" height="20" fill="#FFD700" stroke="#000" stroke-width="1" transform="rotate(-3 230 180)"/>

  <!-- Stars for wonder -->
  <g id="star">
    <path d="M0,-8 L2,-2 L8,-1 L3,2 L2,8 L0,3 L-2,8 L-3,2 L-8,-1 L-2,-2 Z" fill="#FFD700"/>
  </g>
  <use href="#star" transform="translate(130,50) scale(0.7)"/>
  <use href="#star" transform="translate(270,50) scale(0.9)"/>
  <use href="#star" transform="translate(320,100) scale(0.6)"/>
  <use href="#star" transform="translate(80,110) scale(0.8)"/>
</svg>"""


def create_contrarian_svg() -> str:
    """Create Contrarian Guardian SVG with opposing arrows and challenge symbols."""
    return """<?xml version="1.0" encoding="UTF-8"?>
<svg width="100%" height="220px" viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg" style="background-color: #0a0a0a;">
  <title>Contrarian Challenger Guardian</title>
  <desc>Systematic challenging and contrarian analysis</desc>
  <defs>
    <linearGradient id="contra-grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#DC143C;" />
      <stop offset="100%" style="stop-color:#8B0000;" />
    </linearGradient>
    <linearGradient id="contra-grad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1E90FF;" />
      <stop offset="100%" style="stop-color:#00008B;" />
    </linearGradient>
    <filter id="sharp-edges">
      <feGaussianBlur in="SourceGraphic" stdDeviation="0.5"/>
      <feComponentTransfer>
        <feFuncA type="discrete" tableValues="0 1"/>
      </feComponentTransfer>
    </filter>
  </defs>

  <!-- Opposing force field -->
  <ellipse cx="150" cy="110" rx="50" ry="70" fill="url(#contra-grad1)" opacity="0.3"/>
  <ellipse cx="250" cy="110" rx="50" ry="70" fill="url(#contra-grad2)" opacity="0.3"/>

  <!-- Central conflict zone -->
  <g transform="translate(200,110)">
    <!-- Lightning bolt of opposition -->
    <path d="M-10,-40 L5,-20 L-5,-20 L10,0 L-5,0 L15,20 L0,20 L5,40 L-10,15 L-5,15 L-15,-5 L-5,-5 L-20,-25 L-5,-25 Z"
          fill="#FFD700" stroke="#000" stroke-width="2" filter="url(#sharp-edges)"/>
  </g>

  <!-- Opposing arrows -->
  <g transform="translate(200,110)">
    <!-- Left arrow (red) -->
    <path d="M-60,0 L-30,0 M-30,-10 L-30,10 L-50,0 Z"
          fill="url(#contra-grad1)" stroke="url(#contra-grad1)" stroke-width="3"/>
    <!-- Right arrow (blue) -->
    <path d="M60,0 L30,0 M30,-10 L30,10 L50,0 Z"
          fill="url(#contra-grad2)" stroke="url(#contra-grad2)" stroke-width="3"/>

    <!-- Up arrow (red) -->
    <path d="M0,-60 L0,-30 M-10,-30 L10,-30 L0,-50 Z"
          fill="url(#contra-grad1)" stroke="url(#contra-grad1)" stroke-width="3"/>
    <!-- Down arrow (blue) -->
    <path d="M0,60 L0,30 M-10,30 L10,30 L0,50 Z"
          fill="url(#contra-grad2)" stroke="url(#contra-grad2)" stroke-width="3"/>
  </g>

  <!-- Exclamation and question marks -->
  <text x="120" y="60" fill="url(#contra-grad1)" font-size="28" font-weight="bold">!</text>
  <text x="280" y="60" fill="url(#contra-grad2)" font-size="28" font-weight="bold">?</text>
  <text x="120" y="170" fill="url(#contra-grad2)" font-size="28" font-weight="bold">?</text>
  <text x="280" y="170" fill="url(#contra-grad1)" font-size="28" font-weight="bold">!</text>

  <!-- Chess pieces (opposition strategy) -->
  <g transform="translate(160,180)">
    <path d="M-5,0 L-3,-5 L-3,-8 Q-3,-10 0,-10 Q3,-10 3,-8 L3,-5 L5,0 Z" fill="url(#contra-grad1)" stroke="#000" stroke-width="1"/>
  </g>
  <g transform="translate(240,180)">
    <path d="M-5,0 L-3,-5 L-3,-8 Q-3,-10 0,-10 Q3,-10 3,-8 L3,-5 L5,0 Z" fill="url(#contra-grad2)" stroke="#000" stroke-width="1"/>
  </g>

  <!-- "NO" crossing out symbol -->
  <g transform="translate(200,110)" opacity="0.4">
    <circle r="40" fill="none" stroke="#DC143C" stroke-width="3"/>
    <line x1="-28" y1="-28" x2="28" y2="28" stroke="#DC143C" stroke-width="3"/>
  </g>
</svg>"""


def main() -> None:
    """Generate all custom SVG files."""

    # Define SVG generators and their file paths
    svg_configs = [
        (
            create_cto_leadership_svg(),
            ASSETS_DIR
            / "2-engineering/1-cto-office/041-architecture-cto-leadership-guardian.svg",
        ),
        (
            create_coo_leadership_svg(),
            ASSETS_DIR
            / "3-operations/1-coo-office/091-operations-coo-leadership-guardian.svg",
        ),
        (
            create_first_principles_svg(),
            ASSETS_DIR
            / "4-thinktank/1-analytical/101-thinktank-first-principles-guardian.svg",
        ),
        (
            create_mathematician_svg(),
            ASSETS_DIR
            / "4-thinktank/1-analytical/104-thinktank-mathematician-logical-guardian.svg",
        ),
        (
            create_creative_lateral_svg(),
            ASSETS_DIR
            / "4-thinktank/2-creative/103-thinktank-creative-lateral-guardian.svg",
        ),
        (
            create_inventor_svg(),
            ASSETS_DIR
            / "4-thinktank/2-creative/105-thinktank-inventor-innovative-guardian.svg",
        ),
        (
            create_human_patterns_svg(),
            ASSETS_DIR
            / "4-thinktank/3-human-centered/102-thinktank-human-patterns-guardian.svg",
        ),
        (
            create_psychologist_svg(),
            ASSETS_DIR
            / "4-thinktank/3-human-centered/106-thinktank-psychologist-behavioral-guardian.svg",
        ),
        (
            create_child_naive_svg(),
            ASSETS_DIR
            / "4-thinktank/4-unconventional/107-thinktank-child-naive-guardian.svg",
        ),
        (
            create_contrarian_svg(),
            ASSETS_DIR
            / "4-thinktank/4-unconventional/108-thinktank-contrarian-challenger-guardian.svg",
        ),
    ]

    print("Generating custom SVG designs...")

    for svg_content, file_path in svg_configs:
        try:
            # Ensure directory exists
            file_path.parent.mkdir(parents=True, exist_ok=True)

            # Write SVG file
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(svg_content)

            print(f"  ✓ Generated: {file_path.name}")

        except Exception as e:
            print(f"  ✗ Error generating {file_path.name}: {e}")

    print("\nCustom SVG generation complete!")


if __name__ == "__main__":
    main()
