#!/bin/bash
FILE="WAVECAR"
EXPECTED_SIZE=2942268768      # Actual expected file size in bytes
WAIT_INITIAL=30m               # You can give 1h for 1 hour wait time
WAIT_LOOP=60                 # 5 minutes in seconds

# Initial wait for expected upload time
sleep $WAIT_INITIAL

# Check every 5 minutes if the file size matches expected
while true; do
    size=$(stat -c %s "$FILE")
    size_mb=$((size / 1000000))
    expected_mb=$((EXPECTED_SIZE / 1000000))

    if [ "$size" -eq "$EXPECTED_SIZE" ]; then
        echo "$FILE is fully uploaded: $size bytes ($size_mb MB)"
        
        # Automatically respond to two prompts with 'y' then 'n'
        printf "y\nn\n" | sbatch bc_run.sh
        
        break
    else
        echo "Current size: $size bytes ($size_mb MB); expected: $EXPECTED_SIZE bytes ($expected_mb MB). Waiting..."
        sleep $WAIT_LOOP
    fi
done
