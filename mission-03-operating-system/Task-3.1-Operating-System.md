# Task 3.1 — Explore your operating system

| Information explored | What it tells you | Your observation (privacy-safe) |
| --- | --- | --- |
| Operating system / system details | Shows the specific operating system name, release version, kernel name, and hardware CPU architecture. | macOS (`Darwin 27.2.0 arm64`) |
| Current account identity | Identifies the active user session executing commands and determines system access permissions. | `[redacted]` (User Account Unsername) |
| Available and used storage |Displays total disk size, used space, available free space, and mount point in human-readable units (-h). | Root filesystem (`/`): Total 926 GiB, Used 13 GiB, Available 822 GiB (~2% used) |
| System activity snapshot | Takes a 1-sample snapshot (-l 1) of active CPU, memory load, and top running processes. | Active snapshot showed CPU load distributed across core services like `WindowServer`, system daemons (`launchd`), and active applications. |