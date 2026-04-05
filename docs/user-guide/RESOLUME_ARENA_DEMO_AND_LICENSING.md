# Resolume Arena: demo, licensing, and MCP testing

This MCP server talks to **Resolume Arena** (or Avenue) over **OSC**. Resolume itself is separate commercial software from [resolume.com](https://resolume.com/).

## Demo vs paid license

Resolume does **not** offer a long-term cloud-style “free tier.” What exists is an official **demo mode**: you install the same build as paying customers and run it **without a license**.

Per Resolume’s documentation ([Difference between Avenue and Arena](https://resolume.com/support/en/avenue-arena-difference), “Demo” section):

- **Avenue** and **Arena** are both available as **fully functional demos** from the [download page](https://resolume.com/download/).
- You can try them **for as long as you like**.
- **Everything works**; you can save projects and use features (subject to each edition’s feature set—Arena adds mapping, DMX, etc., vs Avenue).
- **Limitations in demo mode:**
  - A **visual watermark** on the output.
  - A **robotic voice** periodically reminds you which product you are using.

Purchasing a license removes the watermark/voice reminders for that product edition.

**Not** a fixed-day trial: demo is “run unlicensed until you buy,” not a 14-day cap (policy can change—always check Resolume’s site).

## What this means for resolume-mcp

- You can develop and test **resolume-mcp** against **Resolume running in demo mode**, as long as OSC is enabled and ports match your configuration.
- For **clean output** (no watermark) in a show, you need a **licensed** Resolume install.
- **Avenue vs Arena:** Arena is the superset (mapping, edge blending, DMX, SMPTE, etc.). See the same official article for the feature list.

## References

- [Difference between Avenue and Arena](https://resolume.com/support/en/avenue-arena-difference) — includes Demo section  
- [Download](https://resolume.com/download/) — Windows / macOS installers  
