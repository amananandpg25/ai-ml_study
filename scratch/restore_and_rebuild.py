import os
import shutil
import subprocess

base_dir = "/Users/amananand/Downloads/SDE/ai:ml"
print("1. Restoring files from backups...")
for w in range(1, 18):
    if w <= 15:
        backup_file = os.path.join(base_dir, "_backup", f"week{w}.html")
    else:
        backup_file = os.path.join(base_dir, "_backup_gemini", f"week{w}.html")
    dest_file = os.path.join(base_dir, f"week{w}.html")
    if os.path.exists(backup_file):
        shutil.copyfile(backup_file, dest_file)
        print(f"  Restored week{w}.html from {os.path.basename(os.path.dirname(backup_file))}")

# Define the scripts to run in order
scripts = [
    "fix_base_typos.py",
    "fix_malformed_day_sections.py",
    "fix_nested_day_sections_v3.py",
    "fix_double_divs.py",
    "generate_week18.py",
    "apply_patches.py",
    "deepen_content.py",
    "inject_new_modules.py",
    "generate_missing_features.py",
    "inject_missing_visuals.py",
    "fix_takeaways_divs.py",
    "fix_week6_headers.py",
    "add_flashcards_safe.py",
    "fix_week_summary.py",
    "fix_duplicate_ids.py",
    "add_week4_diagrams.py",
    "patch_interactive_features.py",
    "improve_run_code.py",
    "replace_youtube_resources.py",
    "fix_mermaid_quotes.py",
    "fix_check_predict_syntax_v2.py",
    "calibrate_weeks_1_4.py",
    "add_missing_resources_w12_w13.py",
    "fix_roadmap_master.py",
    "align_roadmap_ranges.py",
    "fix_roadmap_sidebar.py",
    "patch_resources.py"
]

print("\n2. Executing pipeline scripts in order...")
for script in scripts:
    script_path = os.path.join(base_dir, "scratch", script)
    if os.path.exists(script_path):
        print(f"\n---> Running {script}...")
        # Run using python3
        res = subprocess.run(["python3", script_path], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"  ERROR running {script}:")
            print(res.stderr)
        else:
            # Print last few lines of output
            output_lines = res.stdout.strip().split("\n")
            print("\n".join(output_lines[-5:]))
    else:
        print(f"  Warning: {script} does not exist at {script_path}")

print("\nRebuild pipeline complete!")
