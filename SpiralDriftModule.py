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
# function to create a new SpiralDrift instance