# SPDX-FileCopyrightText: 2026 Stephen Hsu (許家誠)
# SPDX-License-Identifier: MIT
"""Standalone UI template for a neutral Offline Editor form.

This file intentionally does not import GPL core code. It is a permissively
licensed UI template that nonprofit projects may adapt before connecting it to
their own governance backend.
"""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


def build_demo_form(root: tk.Tk) -> None:
    root.title("Offline Editor Demo Form")
    root.geometry("640x360")

    frame = ttk.Frame(root, padding=16)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Stable ID").grid(row=0, column=0, sticky="w")
    ttk.Entry(frame).grid(row=0, column=1, sticky="ew", pady=4)

    ttk.Label(frame, text="Route").grid(row=1, column=0, sticky="w")
    ttk.Entry(frame).grid(row=1, column=1, sticky="ew", pady=4)

    ttk.Label(frame, text="Title").grid(row=2, column=0, sticky="w")
    ttk.Entry(frame).grid(row=2, column=1, sticky="ew", pady=4)

    ttk.Label(frame, text="Body").grid(row=3, column=0, sticky="nw")
    text = tk.Text(frame, height=8)
    text.grid(row=3, column=1, sticky="nsew", pady=4)

    ttk.Button(frame, text="Validate draft").grid(row=4, column=1, sticky="e", pady=12)

    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(3, weight=1)


if __name__ == "__main__":
    app = tk.Tk()
    build_demo_form(app)
    app.mainloop()
