# 🛠️ Research Roadmap — Custom Embedded Linux Network Appliance

## Original project goal

My lab notes propose **replacing FRITZ!OS on a FRITZ!Box 7582** with a custom Linux build, potentially using [Buildroot](https://buildroot.org/docs.html), to turn the hardware into a programmable network-security appliance.

This is a **long-term project objective**, not a claim that a replacement image has been built, flashed, or booted successfully.

## Current verified milestones

- [x] Inspected the device PCB and documented a four-pad candidate UART interface.
- [x] Built a physical serial setup using a Raspberry Pi Pico rather than a dedicated USB-TTL adapter.
- [x] Communicated with the embedded Linux console at 115200 baud, 8N1.
- [x] Observed a local shell returning `uid=0(root) gid=0(root)`.
- [x] Inspected the running device's MTD partition names via `/proc/mtd` (see root README).
- [x] Recorded a MicroPython Pico UART bridge in project notes; published a source transcription.

## Planned, not yet verified

- [ ] Identify the exact SoC architecture, kernel compatibility, bootloader constraints and boot medium.
- [ ] Confirm the original notes' **ARMv7 Linux kernel** proposal against actual hardware evidence; do not assume it is correct.
- [ ] Document bootloader and recovery options *before* attempting modifications.
- [ ] Research whether a Buildroot image can support required board-specific drivers and networking hardware.
- [ ] Prototype safely using backups, read-only inspection, and an independently understood recovery method.
- [ ] Decide what secure, maintainable networking functions the appliance should implement.

## Risk controls

Never erase or overwrite flash partitions based solely on a partition-name table. The `/proc/mtd` entries are not proof of a safe flashing layout, and the router may contain device-specific calibration/configuration data. Do not redistribute proprietary firmware. Store backups and sensitive device data privately, not in this repository.

## Experiment separation

Research on the **7582 hardware** and static analysis of **7583 firmware** are kept distinct: architecture and firmware observations from one model should not be silently applied to the other.
