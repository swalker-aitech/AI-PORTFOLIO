VERSION = "1.0"

from core.logger import log_info
from modes.document_mode import run_document_mode
from modes.general_mode import run_general_mode


def titan_banner():

    print(f"""
========================================
          TITAN AI ASSISTANT
              Version {VERSION}
========================================

Local AI Document Intelligence System

Model: Mistral
Memory: Enabled
Commands: Available

========================================
""")


titan_banner()

log_info("Titan started")


mode = input(
    "\nSelect mode:\n"
    "1. Document Mode\n"
    "2. General Chat\n\n"
    "Choice: "
)


if mode == "1":
    run_document_mode()

elif mode == "2":
    run_general_mode()

else:
    print("Invalid selection.")