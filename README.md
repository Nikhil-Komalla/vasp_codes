## 1. DOS_plotter.py
To plot Partial and Total Density of States (PDOS/TDOS) from VASP outputs with spin filtering and d-band center option.

#### Features
- Optional d-band center vertical line (user input, can be skipped)
- PDOS plotting with spin filter (spin up/down)
- Clean plots without Fermi level line
- Customizable color schemes and interactive color picker
- Bandgap detection and reporting
  
#### Requirements
- `vaspkit` (required for generating PDOS/TDOS files if not present)
- Python & Python packages: `matplotlib`, `numpy`, `pyyaml`
  
#### Recommendation
- Install `PyQt5` for enhanced Matplotlib interactivity and more plotting options:

#### Usage
- Run the script with: `python DOS_plotter.py`
- use `help` command for detailed instructions on plotting options

Ref: [https://github.com/nishantaMishra/](url) OR [https://github.com/nishantaMishra/BatteryInformatics/tree/main/DOS-plots/PDOS](url)

## 3. wait_run.sh

Automated VASP job submission script with file upload verification.

#### Features

- Waits for a specified initial duration before starting file checks
- Monitors a target file (e.g., WAVECAR) and waits until it reaches the expected size
- Checks file size at regular intervals, configurable by the user
- Submits the VASP job automatically via `sbatch` when the file is ready
- Can bypass interactive submission wrappers by providing automated answers ('y', 'n') to prompts

#### Configuration

Set the variables at the top of the script:

- `FILE`: The file to monitor (default: WAVECAR)
- `EXPECTED_SIZE`: The expected size of the file in bytes
- `WAIT_INITIAL`: Initial wait time before starting checks (e.g., `1m`, `30m`, `1h`)
- `WAIT_LOOP`: Time to wait between checks in seconds (e.g., `60` for 1 minute)

#### Usage

Run the script with: `bash wait_run.sh`
