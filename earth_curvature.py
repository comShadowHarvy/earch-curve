#!/usr/bin/env python3
"""
earth_curvature.py - Earth Curvature Calculator & Comparative Analysis Tool

Compares Flat Earth claims and folk approximations (such as the 2 mi/mi² rule
and 8 in/mi² Bedford Level parabolic formula) directly against real spherical
geodetic geometry and atmospheric refraction conditions.

Author: ShadowHarvy
Version: 1.0.0
"""

import sys
import math
import argparse

# Earth Constants (WGS-84 volumetric mean radius)
EARTH_RADIUS_MILES = 3958.761
EARTH_RADIUS_KM = 6371.008

FEET_PER_MILE = 5280.0
INCHES_PER_FOOT = 12.0
METERS_PER_KM = 1000.0

# Refraction condition presets
REFRACTION_CONDITIONS = [
    {
        "name": "Severe Sub-Refraction",
        "k": 0.80,
        "kr": -0.25,
        "desc": "Extremely hot ground / desert. Ray bends UPWARD away from ground. Horizon shrinks; target drops lower (inferior mirage)."
    },
    {
        "name": "Mild Sub-Refraction",
        "k": 0.92,
        "kr": -0.09,
        "desc": "Hot sun on asphalt/sand or cold water below warm air. Target appears slightly lower than geometric."
    },
    {
        "name": "Pure Geometric (Vacuum)",
        "k": 1.00,
        "kr": 0.00,
        "desc": "Zero atmospheric refraction. Pure Euclidean ray tracing along curved sphere."
    },
    {
        "name": "Standard Atmosphere (ISA)",
        "k": 1.17, # 7/6 Earth radius
        "kr": 0.143,
        "desc": "Standard mid-latitude atmosphere (15°C, -6.5°C/km lapse). Standard geodesy & survey baseline. Extends horizon ~8%."
    },
    {
        "name": "Moderate Inversion",
        "k": 1.33, # 4/3 Earth radius
        "kr": 0.25,
        "desc": "Cool calm morning or temperature inversion aloft. Standard microwave / radar line-of-sight propagation."
    },
    {
        "name": "Strong Inversion (Looming)",
        "k": 1.65,
        "kr": 0.39,
        "desc": "Warm air advection over cold water (e.g. spring across Great Lakes). Target looms significantly above horizon."
    },
    {
        "name": "Atmospheric Ducting / Mirage",
        "k": 2.50,
        "kr": 0.60,
        "desc": "Intense thermal boundary layer. High downward ray bending (Fata Morgana, Novaya Zemlya effect). Objects visible far past horizon."
    }
]

# ANSI Color formatting
C_RESET  = "\033[0m"
C_BOLD   = "\033[1m"
C_RED    = "\033[31m"
C_GREEN  = "\033[32m"
C_YELLOW = "\033[33m"
C_BLUE   = "\033[34m"
C_MAG    = "\033[35m"
C_CYAN   = "\033[36m"
C_WHITE  = "\033[37m"
C_GRAY   = "\033[90m"


def print_banner():
    banner = f"""{C_CYAN}{C_BOLD}
╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║     ███████╗ █████╗ ██████╗ ████████╗██╗  ██╗                        ║
║     ██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║  ██║                        ║
║     █████╗  ███████║██████╔╝   ██║   ███████║                        ║
║     ██╔══╝  ██╔══██║██╔══██╗   ██║   ██╔══██║                        ║
║     ███████╗██║  ██║██║  ██║   ██║   ██║  ██║                        ║
║     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝                        ║
║                                                                       ║
║          Curvature Calculator: Flat Earth vs. Physical Reality        ║
║                                                                       ║
║       Side-by-Side Comparison • Tangent Drop • Hidden Height          ║
║               Atmospheric Refraction Spectrum Analysis                ║
║                                                                       ║
║  Author: ShadowHarvy                                                 ║
║  Version: 1.0.0                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝{C_RESET}
"""
    print(banner)


def calculate_real_earth(distance, h_obs, h_tgt, k=1.17, metric=False):
    """
    Calculate real spherical Earth geodetic curvature values.
    Inputs:
      distance: Distance to target (miles or km)
      h_obs: Observer eye height (feet or meters)
      h_tgt: Target structure height (feet or meters)
      k: Effective Earth radius refraction factor (default 1.17 = 7/6 Earth)
      metric: True if using km/m, False if using mi/ft
    """
    R_base = EARTH_RADIUS_KM if metric else EARTH_RADIUS_MILES
    height_to_dist = (1.0 / METERS_PER_KM) if metric else (1.0 / FEET_PER_MILE)
    dist_to_height = METERS_PER_KM if metric else FEET_PER_MILE

    R_eff = k * R_base

    h_obs_dist = h_obs * height_to_dist
    h_tgt_dist = h_tgt * height_to_dist

    # Observer horizon distance
    d_h = math.sqrt(2.0 * R_eff * h_obs_dist + h_obs_dist**2)

    # Tangent drop from observer level at distance d
    drop_dist = math.sqrt(R_eff**2 + distance**2) - R_eff
    drop_height = drop_dist * dist_to_height

    # Parabolic tangent drop approximation
    drop_parabolic = (distance**2 / (2.0 * R_eff)) * dist_to_height

    # Target horizon distance (distance from target to its own horizon)
    d_target_h = math.sqrt(2.0 * R_eff * h_tgt_dist + h_tgt_dist**2) if h_tgt_dist > 0 else 0.0

    # Max line of sight distance (observer top to target top)
    max_los_dist = d_h + d_target_h

    # Hidden / Obscured height behind the curve
    if distance <= d_h:
        hidden_dist = 0.0
        hidden_height = 0.0
        visible_height = h_tgt
        is_obscured = False
    else:
        d_beyond_horizon = distance - d_h
        hidden_dist = math.sqrt(R_eff**2 + d_beyond_horizon**2) - R_eff
        hidden_height = hidden_dist * dist_to_height
        visible_height = max(0.0, h_tgt - hidden_height)
        is_obscured = hidden_height > 0

    # Horizon dip angle in degrees
    if (R_eff + h_obs_dist) > 0:
        dip_rad = math.acos(min(1.0, R_eff / (R_eff + h_obs_dist)))
        dip_deg = math.degrees(dip_rad)
    else:
        dip_deg = 0.0

    return {
        "k": k,
        "R_eff": R_eff,
        "d_horizon": d_h,
        "tangent_drop": drop_height,
        "tangent_drop_parabolic": drop_parabolic,
        "hidden_height": hidden_height,
        "visible_height": visible_height,
        "max_los_dist": max_los_dist,
        "dip_angle_deg": dip_deg,
        "is_obscured": is_obscured,
        "dist_unit": "km" if metric else "miles",
        "height_unit": "meters" if metric else "feet"
    }


def calculate_flat_earth(distance, h_obs, h_tgt, metric=False):
    """
    Calculate values under Flat Earth claims and folk approximations.
    1. Bedford Level / Parabolic meme: 8 inches per mile squared = (8/12) * d² feet = (2/3) * d² feet
    2. Pure Flat Plane: Drop = 0
    """
    if metric:
        d_miles = distance * 0.621371
        h_obs_ft = h_obs * 3.28084
        h_tgt_ft = h_tgt * 3.28084
    else:
        d_miles = distance
        h_obs_ft = h_obs
        h_tgt_ft = h_tgt

    # Model 1: Folk Bedford Level meme - "8 inches per mile squared"
    fe_8in_drop_inches = 8.0 * (d_miles**2)
    fe_8in_drop_ft = (fe_8in_drop_inches / 12.0)
    fe_8in_hidden_ft = max(0.0, fe_8in_drop_ft - h_obs_ft)
    fe_8in_visible_ft = max(0.0, h_tgt_ft - fe_8in_hidden_ft)

    if metric:
        fe_8in_drop = fe_8in_drop_ft * 0.3048 # meters
        fe_8in_hidden = fe_8in_hidden_ft * 0.3048 # meters
        fe_8in_visible = fe_8in_visible_ft * 0.3048 # meters
    else:
        fe_8in_drop = fe_8in_drop_ft
        fe_8in_hidden = fe_8in_hidden_ft
        fe_8in_visible = fe_8in_visible_ft

    # Model 2: Pure Flat Plane (Disk/infinite plane)
    fe_plane_drop = 0.0
    fe_plane_hidden = 0.0
    fe_plane_visible = h_tgt

    return {
        "model_8in": {
            "name": "Bedford Level Meme: 8 in/mi²",
            "formula": "Drop = 8\" × d² = (2/3)d² ft",
            "drop": fe_8in_drop,
            "hidden": fe_8in_hidden,
            "visible": fe_8in_visible
        },
        "model_plane": {
            "name": "Pure Flat Plane (Zero Curvature)",
            "formula": "Drop = 0.0 (Infinite Plane)",
            "drop": fe_plane_drop,
            "hidden": fe_plane_hidden,
            "visible": fe_plane_visible
        }
    }


def format_val(val, unit, is_large=False):
    """Format numerical values nicely with units."""
    if is_large and val >= 10000:
        return f"{val:,.1f} {unit}"
    elif val >= 100:
        return f"{val:,.2f} {unit}"
    else:
        return f"{val:,.3f} {unit}"


def print_comparison(distance, h_obs, h_tgt, k_val=1.17, metric=False):
    """Print complete side-by-side comparison table."""
    d_unit = "km" if metric else "miles"
    h_unit = "m" if metric else "ft"

    real_geo = calculate_real_earth(distance, h_obs, h_tgt, k=1.00, metric=metric)
    real_ref = calculate_real_earth(distance, h_obs, h_tgt, k=k_val, metric=metric)
    fe = calculate_flat_earth(distance, h_obs, h_tgt, metric=metric)

    print(f"\n{C_BOLD}{C_WHITE}═══════════════════════════════════════════════════════════════════════════════════════{C_RESET}")
    print(f" {C_BOLD}{C_CYAN}INPUT PARAMETERS:{C_RESET}")
    print(f"   • Target Distance      : {C_BOLD}{C_WHITE}{distance} {d_unit}{C_RESET}")
    print(f"   • Observer Eye Height  : {C_BOLD}{C_WHITE}{h_obs} {h_unit}{C_RESET}")
    print(f"   • Target Object Height : {C_BOLD}{C_WHITE}{h_tgt} {h_unit}{C_RESET}")
    print(f"   • Refraction Factor (k): {C_BOLD}{C_YELLOW}{k_val:.2f}{C_RESET} (Effective Radius: {k_val * (EARTH_RADIUS_KM if metric else EARTH_RADIUS_MILES):,.1f} {d_unit})")
    print(f"{C_BOLD}{C_WHITE}═══════════════════════════════════════════════════════════════════════════════════════{C_RESET}")

    # Side-by-Side Comparison
    col_w = 40
    print(f"\n{C_BOLD}{'┌' + '─'*col_w + '┬' + '─'*col_w + '┐'}{C_RESET}")
    print(f"{C_BOLD}│{C_YELLOW}{' SIDE A: FLAT EARTH CLAIMS':^{col_w}}{C_RESET}{C_BOLD}│{C_CYAN}{' SIDE B: REAL EARTH GEOMETRY':^{col_w}}{C_RESET}{C_BOLD}│{C_RESET}")
    print(f"{C_BOLD}{'├' + '─'*col_w + '┼' + '─'*col_w + '┤'}{C_RESET}")

    # Row 1: Target Distance & Horizon
    r1_l = f" Target Distance: {distance} {d_unit}"
    r1_r = f" Horizon Distance: {real_ref['d_horizon']:.2f} {d_unit}"
    print(f"│{r1_l:<{col_w}}│{r1_r:<{col_w}}│")

    # Row 2: Horizon Line
    r2_l = f" Horizon Limit: None (Infinite Plane)"
    r2_r = f" Horizon Dip Angle: {real_ref['dip_angle_deg']:.4f}°"
    print(f"│{r2_l:<{col_w}}│{r2_r:<{col_w}}│")

    print(f"{C_BOLD}{'├' + '─'*col_w + '┼' + '─'*col_w + '┤'}{C_RESET}")
    print(f"│{C_BOLD}{C_MAG}{' [1] Bedford Level Meme: 8 in/mi²':<{col_w}}{C_RESET}│{C_BOLD}{C_WHITE}{' [Real] Curvature Drop & Obscurity':<{col_w}}{C_RESET}│")

    r3_l = f"   Drop: {format_val(fe['model_8in']['drop'], h_unit)}"
    r3_r = f"   Tangent Drop: {format_val(real_ref['tangent_drop'], h_unit)}"
    print(f"│{r3_l:<{col_w}}│{r3_r:<{col_w}}│")

    r4_l = f"   Hidden: {format_val(fe['model_8in']['hidden'], h_unit)}"
    r4_r = f"   Hidden (Refracted): {format_val(real_ref['hidden_height'], h_unit)}"
    print(f"│{r4_l:<{col_w}}│{r4_r:<{col_w}}│")

    print(f"{C_BOLD}{'├' + '─'*col_w + '┼' + '─'*col_w + '┤'}{C_RESET}")
    print(f"│{C_BOLD}{C_MAG}{' [2] Pure Flat Disk/Plane':<{col_w}}{C_RESET}│{C_BOLD}{C_WHITE}{' [Real] Target Portion Visible':<{col_w}}{C_RESET}│")

    r5_l = f"   Drop: 0.0 {h_unit} | Hidden: 0.0 {h_unit}"
    r5_r = f"   Geometric (k=1.0): {format_val(real_geo['visible_height'], h_unit)}"
    print(f"│{r5_l:<{col_w}}│{r5_r:<{col_w}}│")

    r6_l = f"   Visible: 100% ({h_tgt} {h_unit})"
    vis_pct = (real_ref['visible_height'] / h_tgt * 100.0) if h_tgt > 0 else 0.0
    r6_r = f"   Refracted (k={k_val:.2f}): {format_val(real_ref['visible_height'], h_unit)} ({vis_pct:.1f}%)"
    print(f"│{r6_l:<{col_w}}│{r6_r:<{col_w}}│")

    print(f"{C_BOLD}{'└' + '─'*col_w + '┴' + '─'*col_w + '┘'}{C_RESET}")

    # Physical Explanation Box
    print(f"\n{C_BOLD}{C_YELLOW}ℹ WHY DOES '8 INCHES PER MILE SQUARED' EXIST?{C_RESET}")
    print(f"{C_GRAY}   The famous formula {C_WHITE}h ≈ 8\" × d²{C_GRAY} is actually the mathematical Taylor expansion")
    print(f"   parabolic approximation of the {C_BOLD}REAL SPHERICAL EARTH{C_RESET}{C_GRAY}! For a sphere of radius R = 3,959 mi:")
    print(f"   {C_CYAN}Drop ≈ d² / (2R) = d² / 7,918 mi = (5,280 × 12 / 7,918) × d² in ≈ 7.98\" × d² ≈ 8 in/mi²{C_RESET}")
    print(f"{C_GRAY}   Flat earthers quote Rowbotham's Bedford Level experiments which ironically use the")
    print(f"   sphere's own approximation, but omit observer height (h_obs) and atmospheric refraction.{C_RESET}")

    # Atmospheric Refraction Ranges Table
    print(f"\n{C_BOLD}{C_CYAN}═══════════════════════════════════════════════════════════════════════════════════════{C_RESET}")
    print(f" {C_BOLD}{C_CYAN}ATMOSPHERIC REFRACTION RANGES & ENVIRONMENTAL CONDITIONS{C_RESET}")
    print(f"{C_GRAY} Atmospheric refraction bends light rays downward as air density drops with altitude.{C_RESET}")
    print(f"{C_GRAY} This extends the horizon and reveals objects that would otherwise be hidden behind the curve.{C_RESET}")
    print(f"{C_BOLD}{C_CYAN}═══════════════════════════════════════════════════════════════════════════════════════{C_RESET}")

    header = f" {'CONDITION':<26} │ {'FACTOR (k)':<10} │ {'HORIZON':<12} │ {'HIDDEN HEIGHT':<16} │ {'VISIBLE HEIGHT'}"
    print(f"{C_BOLD}{header}{C_RESET}")
    print(f"{C_GRAY}───────────────────────────┼────────────┼──────────────┼──────────────────┼─────────────────────────{C_RESET}")

    for cond in REFRACTION_CONDITIONS:
        k = cond["k"]
        res = calculate_real_earth(distance, h_obs, h_tgt, k=k, metric=metric)
        
        status_badge = f"{C_GREEN}VISIBLE{C_RESET}"
        if res["hidden_height"] >= h_tgt:
            status_badge = f"{C_RED}FULLY HIDDEN{C_RESET}"
        elif res["hidden_height"] > 0:
            status_badge = f"{C_YELLOW}PARTIAL{C_RESET}"

        row = (
            f" {cond['name']:<25} │ "
            f"k = {k:<6.2f} │ "
            f"{res['d_horizon']:>6.2f} {d_unit} │ "
            f"{format_val(res['hidden_height'], h_unit):>10}     │ "
            f"{format_val(res['visible_height'], h_unit):>9} ({status_badge})"
        )
        print(row)
        print(f"   {C_GRAY}↳ {cond['desc']}{C_RESET}")

    print(f"{C_BOLD}{C_CYAN}═══════════════════════════════════════════════════════════════════════════════════════{C_RESET}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Earth Curvature Calculator comparing Flat Earth claims against Real Geodetic Earth and Atmospheric Refraction Ranges.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Standard 10-mile distance, 6 ft eye level, 100 ft building
  ./earth_curvature.py -d 10 -o 6 -t 100

  # Long range 30-mile lighthouse check with Lake Michigan looming inversion (k=1.6)
  ./earth_curvature.py -d 30 -o 15 -t 150 -k 1.6

  # Metric units: 25 km distance, 2 m observer, 30 m target
  ./earth_curvature.py -d 25 -o 2 -t 30 -m
        """
    )

    parser.add_argument("-d", "--distance", type=float, default=10.0,
                        help="Target distance (miles or km) [default: 10.0]")
    parser.add_argument("-o", "--observer-height", type=float, default=6.0,
                        help="Observer eye level height (feet or meters) [default: 6.0]")
    parser.add_argument("-t", "--target-height", type=float, default=100.0,
                        help="Target object height (feet or meters) [default: 100.0]")
    parser.add_argument("-k", "--refraction", type=float, default=1.17,
                        help="Atmospheric refraction factor k (default: 1.17 for standard 7/6 Earth)")
    parser.add_argument("-m", "--metric", action="store_true",
                        help="Use metric units (km / meters) instead of imperial (miles / feet)")
    parser.add_argument("--json", action="store_true",
                        help="Output results as JSON for programmatic consumption")

    args = parser.parse_args()

    if args.distance <= 0:
        print(f"{C_RED}Error: Target distance must be greater than 0.{C_RESET}", file=sys.stderr)
        sys.exit(1)
    if args.observer_height < 0:
        print(f"{C_RED}Error: Observer height cannot be negative.{C_RESET}", file=sys.stderr)
        sys.exit(1)
    if args.target_height < 0:
        print(f"{C_RED}Error: Target height cannot be negative.{C_RESET}", file=sys.stderr)
        sys.exit(1)

    if args.json:
        import json
        real = calculate_real_earth(args.distance, args.observer_height, args.target_height, k=args.refraction, metric=args.metric)
        fe = calculate_flat_earth(args.distance, args.observer_height, args.target_height, metric=args.metric)
        payload = {
            "inputs": {
                "distance": args.distance,
                "observer_height": args.observer_height,
                "target_height": args.target_height,
                "refraction_k": args.refraction,
                "metric": args.metric
            },
            "real_earth": real,
            "flat_earth": fe,
            "refraction_spectrum": [
                {
                    "name": cond["name"],
                    "k": cond["k"],
                    "results": calculate_real_earth(args.distance, args.observer_height, args.target_height, k=cond["k"], metric=args.metric)
                } for cond in REFRACTION_CONDITIONS
            ]
        }
        print(json.dumps(payload, indent=2))
        return

    print_banner()
    print_comparison(args.distance, args.observer_height, args.target_height, k_val=args.refraction, metric=args.metric)


if __name__ == "__main__":
    main()
