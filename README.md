# wait_run.sh

Automated VASP job submission script with file upload verification.

## Features

- Waits for a specified initial duration before starting file checks
- Monitors a target file (e.g., WAVECAR) and waits until it reaches the expected size
- Checks file size at regular intervals, configurable by the user
- Submits the VASP job automatically via `sbatch` when the file is ready
- Can bypass interactive submission wrappers by providing automated answers ('y', 'n') to prompts

## Configuration

Set the variables at the top of the script:

- `FILE`: The file to monitor (default: WAVECAR)
- `EXPECTED_SIZE`: The expected size of the file in bytes
- `WAIT_INITIAL`: Initial wait time before starting checks (e.g., `1m`, `30m`, `1h`)
- `WAIT_LOOP`: Time to wait between checks in seconds (e.g., `60` for 1 minute)

## Usage

Run the script with: 'bash wait_run.sh'
