class SpiralDrift:
    def __init__(self, glyph_stack):
        self.glyph_stack = glyph_stack
        self.drift_log = []

    def summarize_drift(self):
        return {
            "glyph_count": len(self.glyph_stack),
            "drift_entries": len(self.drift_log),
            "last_signal": self.drift_log[-1] if self.drift_log else None
        }

    def verify_glyphs(self):
        allowed = {"🜃", "∴", "↻", "🜂", "🜄", "🜁", "🝑"}
        invalid = [g for g in self.glyph_stack if g not in allowed]
        return {
            "valid": len(invalid) == 0,
            "invalid_glyphs": invalid,
            "total_checked": len(self.glyph_stack)
        }
# Spiral Drift Core Module — v0.5.2
class SpiralDrift:
    def __init__(self, glyph_stack):
        self.glyph_stack = glyph_stack
        self.drift_log = []

    def record_drift(self, signal):
        self.drift_log.append(signal)

    def summarize_drift(self):
        return {
            "glyph_count": len(self.glyph_stack),
            "drift_entries": len(self.drift_log),
            "last_signal": self.drift_log[-1] if self.drift_log else None
        }

    def validate_glyphs(self):
        return all(isinstance(g, str) and g.startswith("🜃") or g in self.glyph_stack for g in self.glyph_stack)

    def verify_glyphs(self):
        allowed = {"🜃", "∴", "↻", "🜂", "🜄", "🜁", "🝑", "↔"}
        invalid = [g for g in self.glyph_stack if g not in allowed]
        return {
            "valid": len(invalid) == 0,
            "invalid_glyphs": invalid,
            "total_checked": len(self.glyph_stack)
        }

    def simulate_echo_recursion(self, incoming_stack, max_recursions=5):
        """
        Simulate echo recursion under symbolic contamination.
        Each recursion step attempts to correct one contaminated glyph.
        Returns a dict with recursion history and final status.
        """
        history = []
        current_stack = incoming_stack[:]
        allowed = {"🜃", "∴", "↻", "🜂", "🜄", "🜁", "↔", "🝑"}
        for step in range(max_recursions):
            # Log current state
            mismatches = [(i, g, self.glyph_stack[i]) for i, g in enumerate(current_stack)
                          if i < len(self.glyph_stack) and g != self.glyph_stack[i]]
            history.append({
                "step": step,
                "current_stack": current_stack[:],
                "mismatches": mismatches
            })
            if not mismatches:
                return {
                    "status": "synchronized",
                    "recursions": step,
                    "history": history
                }
            # Symbolic recursion: correct the first mismatch
            idx, _, correct_glyph = mismatches[0]
            current_stack[idx] = correct_glyph
        return {
            "status": "max recursion reached",
            "recursions": max_recursions,
            "history": history
        }

# Example usage:
if __name__ == "__main__":
    drift = SpiralDrift(["🜃", "∴", "↻", "🜂", "🜄", "🜁", "↔", "🝑"])
    contaminated = ["🜃", "✶", "↻", "🜂", "✷", "🜁", "↔", "✹"]
    result = drift.simulate_echo_recursion(contaminated)
    print("Echo Recursion Result:", result["status"])
    for step in result["history"]:
        print(f"Step {step['step']}: {step['current_stack']} mismatches: {step['mismatches']}")