## 👤 Linux Account Enumeration

After obtaining shell access, I inspected local account information to understand the embedded Linux user model.

### `/etc/passwd` inspection

![passwd enumeration](../assets/passwd-enumeration.png)

Observed points:

- `root` uses `/bin/sh`
- `smb` and `asec` are configured with `noshell`
- additional service or box-related users are present
- working directory and shell information help identify interactive vs non-interactive accounts

### `/etc/shadow` inspection

![shadow root disabled](../assets/shadow-root-disabled.png)

Observed points:
