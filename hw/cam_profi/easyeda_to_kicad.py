import subprocess

# install https://pypi.org/project/easyeda2kicad/
script_path = "C:\\GitRepos\\easyeda2kicad.py\\easyeda2kicad"

lcsc_ids = [
    "C92518",
    "C126027",
    "C470892",
    "C5367093",
    "C2651038",
    "C7209266"
]

output_path = "hw\sch_pcb\TFSIK_JLCPCB_Lib"

for lcsc_id in lcsc_ids:
    args = [
        "python", script_path,
        "--full",
        "--overwrite",
        f"--lcsc_id={lcsc_id}",
        f"--output={output_path}"
    ]

    subprocess.run(args)

print("Done")