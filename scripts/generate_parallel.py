#!/usr/bin/env python3
"""
WingWing PPL Textbook - Parallel Unit Generator

Generates multiple units simultaneously for faster completion.
"""

import subprocess
import sys
from pathlib import Path
import time
import argparse
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent

def generate_unit_parallel(chapter, unit):
    """Generate a single unit using the detailed script."""
    script_path = PROJECT_ROOT / "scripts" / "generate_detailed.py"
    venv_python = "/sessions/zealous-optimistic-edison/ppl-venv/bin/python"

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting Chapter {chapter}, Unit {unit}")

    cmd = [
        venv_python,
        str(script_path),
        "--chapter", str(chapter),
        "--unit", unit
    ]

    start_time = time.time()

    try:
        result = subprocess.run(
            cmd,
            cwd=str(PROJECT_ROOT),
            capture_output=True,
            text=True,
            timeout=1800  # 30 minute timeout per unit
        )

        elapsed = time.time() - start_time

        if result.returncode == 0:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ✓ Chapter {chapter}, Unit {unit} COMPLETE ({elapsed/60:.1f} min)")
            return True, elapsed, result.stdout
        else:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ✗ Chapter {chapter}, Unit {unit} FAILED")
            print(f"Error output:\n{result.stderr}")
            return False, elapsed, result.stderr

    except subprocess.TimeoutExpired:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] ✗ Chapter {chapter}, Unit {unit} TIMEOUT")
        return False, 1800, "Timeout after 30 minutes"
    except Exception as e:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] ✗ Chapter {chapter}, Unit {unit} ERROR: {e}")
        return False, 0, str(e)


def generate_chapter_parallel(chapter, units, max_parallel=3):
    """Generate multiple units in parallel."""
    import concurrent.futures

    print("="*60)
    print(f"PARALLEL GENERATION - Chapter {chapter}")
    print(f"Units: {', '.join(units)}")
    print(f"Max parallel processes: {max_parallel}")
    print("="*60)

    start_time = time.time()
    results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_parallel) as executor:
        # Submit units with 30-second stagger to avoid rate limit spikes
        futures = {}
        for i, unit in enumerate(units):
            if i > 0:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Waiting 30s before starting next unit...")
                time.sleep(30)  # Stagger starts
            futures[executor.submit(generate_unit_parallel, chapter, unit)] = unit

        # Wait for all to complete
        for future in concurrent.futures.as_completed(futures):
            unit = futures[future]
            try:
                success, elapsed, output = future.result()
                results.append({
                    'chapter': chapter,
                    'unit': unit,
                    'success': success,
                    'elapsed': elapsed
                })
            except Exception as e:
                print(f"Exception for Unit {unit}: {e}")
                results.append({
                    'chapter': chapter,
                    'unit': unit,
                    'success': False,
                    'elapsed': 0
                })

    total_elapsed = time.time() - start_time

    # Print summary
    print("\n" + "="*60)
    print("PARALLEL GENERATION COMPLETE")
    print("="*60)
    print(f"Total wall-clock time: {total_elapsed/60:.1f} minutes")
    print(f"\nResults:")

    successful = 0
    for result in results:
        status = "✓" if result['success'] else "✗"
        print(f"  {status} Chapter {result['chapter']}, Unit {result['unit']}: {result['elapsed']/60:.1f} min")
        if result['success']:
            successful += 1

    print(f"\nSuccess rate: {successful}/{len(results)}")

    if successful == len(results):
        print("\n🎉 All units generated successfully!")
        print(f"Time saved vs sequential: {sum(r['elapsed'] for r in results)/60 - total_elapsed/60:.1f} minutes")

    return successful == len(results)


def main():
    parser = argparse.ArgumentParser(description="Generate multiple units in parallel")
    parser.add_argument("--chapter", type=int, required=True, help="Chapter number")
    parser.add_argument("--units", type=str, required=True, help="Units to generate (e.g., 'A,B,C')")
    parser.add_argument("--parallel", type=int, default=3, help="Max parallel processes (default: 3)")

    args = parser.parse_args()

    units = [u.strip().upper() for u in args.units.split(',')]

    print(f"\nStarting parallel generation at {datetime.now().strftime('%H:%M:%S')}")

    success = generate_chapter_parallel(args.chapter, units, args.parallel)

    if success:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
