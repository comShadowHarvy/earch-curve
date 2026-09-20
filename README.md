# Earth Curvature Calculator: Flat Earth vs. Physical Reality & Refraction

<div align="center">

```
   ███████╗ █████╗ ██████╗ ████████╗██╗  ██╗
   ██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║  ██║
   █████╗  ███████║██████╔╝   ██║   ███████║
   ██╔══╝  ██╔══██║██╔══██╗   ██║   ██╔══██║
   ███████╗██║  ██║██║  ██║   ██║   ██║  ██║
   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
```

**Side-by-Side Analysis • Tangent Drop • Hidden Height • Atmospheric Refraction Spectrum**

**Author:** ShadowHarvy  
**Version:** 1.0.0  
**License:** MIT

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Side-by-Side Comparison Architecture](#-side-by-side-comparison-architecture)
  - [Side A: Flat Earth Formulas & Claims](#side-a-flat-earth-formulas--claims)
  - [Side B: Real Earth Geodetic Reality](#side-b-real-earth-geodetic-reality)
- [Atmospheric Refraction Spectrum](#-atmospheric-refraction-spectrum)
- [The Mathematics: Why 8 Inches Per Mile Squared Exists](#-the-mathematics-why-8-inches-per-mile-squared-exists)
- [Usage: Interactive Web UI & Command-Line Utility](#-usage-interactive-web-ui--command-line-utility)
  - [1. Interactive Web Application](#1-interactive-web-application)
  - [2. Terminal Command-Line Tool](#2-terminal-command-line-tool)
- [Example Calculations](#-example-calculations)

---

## 🌟 Overview

The **Earth Curvature Calculator** is a dual-interface scientific analysis tool (Interactive Web App + Terminal CLI) designed to calculate and visually demonstrate Earth's physical curvature, observer horizon geometry, and terrestrial atmospheric refraction.

It provides an explicit **side-by-side comparison** contrasting Flat Earth claims and folk approximations against real spherical geodetic physics and empirical atmospheric optics.

---

## ⚖️ Side-by-Side Comparison Architecture

### Side A: Flat Earth Formulas & Claims

The calculator models the two primary Flat Earth assertions:

1. **Bedford Level Meme: 8 Inches per Mile Squared**
   $$\text{Drop} = 8\text{ in} \times d^2 = \frac{2}{3} d^2\text{ (feet)}$$
   - Derived from Samuel Rowbotham’s 19th-century *Zetetic Astronomy* experiments along the Old Bedford River.
   - Ironically, this formula is the Taylor-series parabolic approximation of the **real spherical Earth** ($\frac{d^2}{2R}$), but flat earth arguments misapply it by ignoring observer eye height ($h_0$) and atmospheric refraction.
2. **Pure Planar Earth (Zero Curvature)**
   $$\text{Drop} = 0\text{ ft} \quad | \quad \text{Hidden Height} = 0\text{ ft}$$
   - Assumes an infinite flat plane where all objects remain 100% geometrically visible regardless of distance, disproven by ships and skylines sinking bottom-first below the horizon.

---

### Side B: Real Earth Geodetic Reality

Based on the WGS-84 volumetric mean Earth radius $R = 3,958.761\text{ miles}$ ($6,371.008\text{ km}$):

1. **Observer Horizon Distance ($d_h$)**:
   $$d_h = \sqrt{2 R h_0 + h_0^2} \approx \sqrt{2 R h_0}$$
   *(For a standard eye height of $6\text{ ft}$, the geometric horizon is exactly $3.00\text{ miles}$ away).*
2. **Total Tangent Drop from Eye Level**:
   $$h_{\text{drop}} = \sqrt{R^2 + d^2} - R \approx \frac{d^2}{2 R}$$
3. **Hidden / Obscured Target Height ($h_{\text{hidden}}$)**:
   - If distance $d \le d_h$: Target is in direct line of sight ($h_{\text{hidden}} = 0$).
   - If distance $d > d_h$: Distance beyond horizon is $d_{\text{tgt}} = d - d_h$, and:
     $$h_{\text{hidden}} = \sqrt{R^2 + d_{\text{tgt}}^2} - R \approx \frac{d_{\text{tgt}}^2}{2 R}$$
4. **Visible Target Height**:
   $$h_{\text{visible}} = \max(0, h_1 - h_{\text{hidden}})$$
5. **Horizon Dip Angle**:
   $$\alpha = \arccos\left(\frac{R}{R + h_0}\right) \approx \sqrt{\frac{2 h_0}{R}}$$

---

## 🌫️ Atmospheric Refraction Spectrum

Light traveling through Earth's atmosphere does not travel in a Euclidean straight line. Because air density decreases with altitude ($\frac{dn}{dh} < 0$), light rays bend downward toward the ground. 

In surveying and geodesy, this is modeled by an **Effective Earth Radius Factor** ($k$):
$$R_{\text{effective}} = k \cdot R \quad \text{where } k = \frac{1}{1 - k_r}$$

| Environmental Condition | Factor ($k$) | Surveying Coeff ($k_r$) | Physical Effect on Visibility |
| :--- | :--- | :--- | :--- |
| **Severe Sub-Refraction** | $k = 0.80$ | $k_r = -0.25$ | Sun-baked desert or hot asphalt. Rays curve **upward** away from ground. Horizon shrinks closer; targets drop lower (inferior mirage). |
| **Mild Sub-Refraction** | $k = 0.92$ | $k_r = -0.09$ | Hot sun on sand or cold water under warm air. Target appears slightly lower than geometric. |
| **Pure Geometric (Vacuum)** | $k = 1.00$ | $k_r = 0.00$ | Zero refraction (space/vacuum). Pure Euclidean ray along curved sphere. |
| **Standard Atmosphere (ISA)** | $k = 1.17$ | $k_r = 0.143$ | Normal mid-latitude atmosphere ($15^\circ\text{C}$, $-6.5^\circ\text{C/km}$ lapse). Standard geodesy baseline ($7/6$ Earth radius). Extends horizon $\approx 8\%$. |
| **Moderate Inversion** | $k = 1.33$ | $k_r = 0.25$ | Cool calm morning or temperature inversion aloft. Standard radar/microwave propagation ($4/3$ Earth radius). |
| **Strong Inversion (Looming)** | $k = 1.65$ | $k_r = 0.39$ | Warm air over cold water (e.g. spring across Lake Michigan). Target looms high above horizon. |
| **Atmospheric Ducting / Mirage** | $k = 2.50$ | $k_r = 0.60$ | Intense thermal boundary layer. Light curves along Earth's curvature (Fata Morgana, Novaya Zemlya effect). |

---

## 📐 The Mathematics: Why "8 Inches Per Mile Squared" Exists

Flat Earthers frequently cite:
$$\text{Drop} \approx 8\text{ in/mi}^2 \times d^2$$

Where did this number come from? **It is the Taylor expansion of a sphere!**

For any sphere of radius $R$:
$$\text{Drop} = R - \sqrt{R^2 - d^2} = R\left(1 - \sqrt{1 - \frac{d^2}{R^2}}\right)$$
Using the binomial series $\sqrt{1 - x} \approx 1 - \frac{1}{2}x$:
$$\text{Drop} \approx R \left(1 - \left(1 - \frac{d^2}{2 R^2}\right)\right) = \frac{d^2}{2 R}$$

For Earth's mean radius $R = 3,959\text{ miles}$:
$$\frac{1}{2 R} = \frac{1}{7,918}\text{ mi/mi}^2$$
Converting miles to inches:
$$\frac{5,280 \times 12}{7,918} = \frac{63,360}{7,918} \approx 7.98\text{ in/mi}^2 \approx \mathbf{8\text{ inches per mile squared}}$$

### The Flaw in the Flat Earth Usage:
The formula $\frac{d^2}{2 R} \approx 8\text{ in/mi}^2$ calculates the drop **from a tangent line starting at ground level ($h_0 = 0$)**.
When a human stands with eyes at $h_0 = 6\text{ ft}$, their horizon is pushed out to $3\text{ miles}$. The curve does not start hiding the target until **past** that $3\text{ mile}$ horizon! 

At $10\text{ miles}$, the 8 in/mi² naive formula claims $66.7\text{ ft}$ is hidden, whereas the real hidden height is only **$26.0\text{ ft}$** under standard refraction.

---

## 💻 Usage: Live Web App, Local UI & Command-Line Tool

### 🌐 1. Live Web Application (GitHub Pages)
Visit the live deployed site in any modern browser:
👉 **[https://comshadowharvy.github.io/earch-curve/](https://comshadowharvy.github.io/earch-curve/)**

---

### 🖥️ 2. Local Desktop Web App
Run the launcher script to open the calculator in your default browser:

```bash
# Launch via helper script
./earth_curvature_gui.sh

# Or open directly
xdg-open index.html
```

**Web App Features**:
- Two-way bound sliders and numeric input controls.
- Instant Imperial (mi/ft) $\leftrightarrow$ Metric (km/m) toggle.
- Side-by-side cards comparing Flat Earth models vs. Real Earth geodesy.
- Dynamic SVG cross-section ray-tracing diagram with animated beams and color-coded visible/hidden target splits.
- 7-condition Atmospheric Refraction Spectrum table.

---

### ⚡ 3. Terminal Command-Line Tool
Run `./earth_curvature.py` directly from the repository root:

```bash
# Standard 10-mile scan (6 ft observer eye level, 100 ft target)
./earth_curvature.py -d 10 -o 6 -t 100

# Long distance observation (45 miles, 20 ft eye level, 1450 ft skyscraper)
./earth_curvature.py -d 45 -o 20 -t 1450 -k 1.65

# Metric units (25 km distance, 2 m observer, 30 m target)
./earth_curvature.py -d 25 -o 2 -t 30 -m

# JSON output for scripting or automation
./earth_curvature.py -d 15 -o 6 -t 80 --json
```

---

## 🔬 Example Calculations

### Observation: Target at 10 Miles, Observer at 6 Feet, Target 100 Feet High

```text
┌────────────────────────────────────────┬────────────────────────────────────────┐
│        SIDE A: FLAT EARTH CLAIMS       │       SIDE B: REAL EARTH GEOMETRY      │
├────────────────────────────────────────┼────────────────────────────────────────┤
│ Target Distance: 10.0 miles            │ Horizon Distance: 3.24 miles           │
│ Horizon Limit: None (Infinite Plane)   │ Horizon Dip Angle: 0.0401°             │
├────────────────────────────────────────┼────────────────────────────────────────┤
│ [1] Bedford Level Meme: 8 in/mi²       │ [Real] Curvature Drop & Obscurity      │
│   Drop: 66.667 ft                      │   Tangent Drop: 56.998 ft              │
│   Hidden: 60.667 ft                    │   Hidden (Refracted): 26.012 ft        │
├────────────────────────────────────────┼────────────────────────────────────────┤
│ [2] Pure Flat Disk/Plane               │ [Real] Target Portion Visible          │
│   Drop: 0.0 ft | Hidden: 0.0 ft        │   Geometric (k=1.0): 67.319 ft         │
│   Visible: 100% (100.0 ft)             │   Refracted (k=1.17): 73.988 ft (74.0%)│
└────────────────────────────────────────┴────────────────────────────────────────┘
```
