# VASP Codes

A collection of Python and Bash utilities for VASP DFT pre/post-processing, electronic structure visualization, equilibrium Wulff nanoparticle construction, and HPC job automation.

| Script | Path | Purpose | Key Dependencies |
|---|---|---|---|
| **DOS Plotter** | [`DOS/DOS_plotter.py`](DOS/DOS_plotter.py) | Plot PDOS/TDOS with spin filtering, customizable element schemes, bandgap reporting & *d*-band center lines | `vaspkit`, `matplotlib`, `numpy`, `pyyaml` |
| **Wulff Craft** | [`2. wulff_craft.py`](2.%20wulff_craft.py) | Interactive Wulff construction & 3D equilibrium nanoparticle builder from `POSCAR` + DFT surface energies | `wulffpack`, `ase` |
| **Wait & Run** | [`3.wait_run.sh`](3.wait_run.sh) | Monitors large file uploads (e.g., `WAVECAR`) and auto-submits VASP jobs via SLURM `sbatch` | `bash`, `slurm` (`sbatch`) |

---

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
- Install `PyQt5` for enhanced Matplotlib interactivity and more plotting options

#### Usage
- Run the script with: `python DOS_plotter.py`
- Use `help` command for detailed instructions on plotting options

Ref: [https://github.com/nishantaMishra/](https://github.com/nishantaMishra/) or [BatteryInformatics DOS-plots/PDOS](https://github.com/nishantaMishra/BatteryInformatics/tree/main/DOS-plots/PDOS)

---

## 2. wulff_craft.py

Interactive CLI for generating and visualizing equilibrium **Wulff nanoparticle shapes** from a bulk VASP `POSCAR` structure and DFT-calculated surface energies ($\gamma_{hkl}$) using [`wulffpack`](https://wulffpack.materialsmodeling.org/) and `ase`.

#### Features
- **Automatic `POSCAR` Discovery**: Searches for `POSCAR` in the current working directory by default, or loads any custom VASP structure path via `ase.io.read(..., format='vasp')`.
- **Three Nanoparticle Morphologies**: Supports equilibrium `SingleCrystal`, `Decahedron`, and `Icosahedron` constructions (defaults cleanly to `SingleCrystal`).
- **Interactive Miller Index Input**: Loops to collect facet indices and surface energies (`h k l energy`) with input-format validation until Enter is pressed.
- **Flexible Particle Sizing**: Lets you specify a target total atom count (`natoms`), or press Enter to keep `len(structure)` from `POSCAR`.
- **Instant 3D Visualization**: Builds the nanoparticle geometry and opens an interactive 3D viewer via `particle.view()`.

#### Requirements
- Python 3.8+
- `wulffpack` and `ase`:
  ```bash
  pip install wulffpack ase
  ```

#### Usage
Place your relaxed bulk `POSCAR` in the working directory and run:
```bash
python "2. wulff_craft.py"
```

#### Example Interactive Session
```text
Looking for 'POSCAR' in the current directory: /path/to/bulk_dir
Press Enter to use 'POSCAR' in current directory, or specify a different file.
Enter POSCAR filename (default: POSCAR):

Choose shape for Wulff construction:
1. SingleCrystal
2. Decahedron
3. Icosahedron
Enter choice number: 1

Enter surface facets and energies in format 'h k l energy' (or Enter to finish):
Facet (h k l energy): 1 1 1 0.85
Facet (h k l energy): 1 0 0 1.05
Facet (h k l energy): 1 1 0 1.15
Facet (h k l energy):
Number of atoms in the particle (press Enter to use POSCAR's atom count): 500
```

#### Notes
- Surface energies only need to be in consistent relative units (e.g., $\text{J/m}^2$ or $\text{eV/\AA}^2$) because equilibrium Wulff facet ratios depend on relative $\gamma_{hkl}$ values.
- See the [WulffPack documentation](https://wulffpack.materialsmodeling.org/) for methodological details on crystal, decahedral, and icosahedral reconstructions.

---

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

Run the script with: `bash 3.wait_run.sh`
