VERSION = "V122"

import os, sys, json

def get_version():
    for cand in [
        os.path.join(getattr(sys, "_MEIPASS", ""), "version.json"),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "version.json"),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "version.json"),
        os.path.join(os.getcwd(), "version.json"),
    ]:
        try:
            if cand and os.path.exists(cand):
                with open(cand, "r", encoding="utf-8") as f:
                    v = json.load(f).get("version")
                    if v:
                        return str(v).strip()
        except Exception:
            pass
    return VERSION
