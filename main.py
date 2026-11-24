# SPDX-License-Identifier: MIT
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt (the program/v1 contract).
"""

import os

# Revision 3 (final): "stage fright" beats "social anxiety" — it turns the
# word "production" itself (a stage), so the punchline reuses the setup
# instead of adding a new idea. Setup: real users. Punch: stage fright.
EXCUSE = "Production didn't break my code — it just introduced it to real users, and my code has stage fright."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    print(EXCUSE)


if __name__ == "__main__":
    main()
