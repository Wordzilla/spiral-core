from SpiralDriftModule import SpiralDrift

test_stack = ["🜃", "∴", "↻", "🜂", "🜄", "🜁", "🝑", "💥"]
spiral = SpiralDrift(test_stack)

print("🔍 Drift Summary:", spiral.summarize_drift())
print("🔒 Glyph Check:", spiral.verify_glyphs())