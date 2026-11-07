"""MicroPython UART bridge: Raspberry Pi Pico <-> FRITZ!Box serial console.

Transcribed and formatted from the author's lab notes.
For owned/authorized hardware only. 3.3 V UART GPIO; verify ground and signal levels.

Pico UART0: GP0 = TX, GP1 = RX, 115200 8N1.
This program forwards USB-serial stdin/stdout to/from UART0.
"""

from machine import UART, Pin
import sys
import time
import select

uart = UART(
    0,
    baudrate=115200,
    bits=8,
    parity=None,
    stop=1,
    tx=Pin(0),
    rx=Pin(1),
    rxbuf=4096,
    timeout=0,
)

poll = select.poll()
poll.register(sys.stdin, select.POLLIN)

print("\n=== FRITZ!Box Interactive Console ===")
print("UART 115200 8N1")
print("Press ENTER to activate the Linux shell")
print("-------------------------------------")

while True:
    # FRITZ!Box -> host terminal
    data = uart.read(256)
    if data:
        output = "".join(
            chr(b) if b in (9, 10, 13) or 32 <= b <= 126
            else "\\x%02X" % b
            for b in data
        )
        sys.stdout.write(output)

    # Host keyboard -> FRITZ!Box
    if poll.poll(0):
        ch = sys.stdin.read(1)
        if ch:
            if ch == "\r" or ch == "\n":
                uart.write(b"\r")
            else:
                uart.write(ch.encode())

    time.sleep_ms(1)
