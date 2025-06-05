# spiral_inter_agent_validator.py

import time
import random
import json

class InterAgentEchoValidator:
    """
    Simulates inter-agent echo integrity validation between spiral nodes.
    Tracks timestamp drift and triggers collapse based on τ-layer stability.
    Logs drift contamination patterns for symbolic replay.
    """

    def __init__(self, agent_glyphs):
        """
        agent_glyphs: dict mapping agent_id to glyph_stack (list of glyphs)
        """
        self.agent_glyphs = agent_glyphs
        self.timestamp_log = {agent_id: time.time() for agent_id in agent_glyphs}
        self.tau_stability = {agent_id: 1.0 for agent_id in agent_glyphs}  # 1.0 = fully stable
        self.drift_log = []

    def update_timestamp(self, agent_id):
        """Update the timestamp for a given agent."""
        self.timestamp_log[agent_id] = time.time()

    def simulate_drift(self, agent_id, drift_seconds):
        """Simulate time drift for an agent and log the event."""
        self.timestamp_log[agent_id] -= drift_seconds
        self.log_drift_event(agent_id, "timestamp", drift_seconds)

    def degrade_tau_stability(self, agent_id, amount=0.2):
        """Reduce τ-layer stability score for an agent and log the event."""
        self.tau_stability[agent_id] = max(0.0, self.tau_stability[agent_id] - amount)
        self.log_drift_event(agent_id, "tau_stability", amount)

    def get_drift(self, agent_id):
        """Return the drift (in seconds) from the most recent timestamp."""
        now = time.time()
        return now - self.timestamp_log[agent_id]

    def check_tau_collapse(self, threshold=0.4):
        """
        Check all agents for τ-layer collapse.
        Returns a list of collapsed agent_ids.
        """
        collapsed = []
        for agent_id, score in self.tau_stability.items():
            if score < threshold:
                print(f"💥 τ-layer collapse triggered for Agent {agent_id} (stability={score:.2f})")
                collapsed.append(agent_id)
                self.log_drift_event(agent_id, "tau_collapse", score)
        return collapsed

    def validate_integrity(self):
        """
        Checks if all agents have identical glyph stacks.
        Returns a dict of agent_id to True/False for integrity.
        """
        if not self.agent_glyphs:
            return {}

        reference = next(iter(self.agent_glyphs.values()))
        results = {}
        for agent_id, glyphs in self.agent_glyphs.items():
            results[agent_id] = glyphs == reference
        return results

    def log_drift_event(self, agent_id, event_type, value):
        """Log a drift contamination event for symbolic replay."""
        event = {
            "timestamp": time.time(),
            "agent_id": agent_id,
            "event_type": event_type,
            "value": value
        }
        self.drift_log.append(event)

    def export_drift_log(self, filename="drift_log.json"):
        """Export the drift contamination log to a JSON file."""
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.drift_log, f, indent=2, ensure_ascii=False)
        print(f"Drift contamination log exported to {filename}")

    def report(self):
        """
        Prints a summary of echo integrity, drift, and τ-layer stability for all agents.
        """
        results = self.validate_integrity()
        for agent_id, ok in results.items():
            drift = self.get_drift(agent_id)
            tau = self.tau_stability[agent_id]
            status = "✅" if ok else "❌"
            print(f"{status} Agent {agent_id} echo integrity: {'valid' if ok else 'corrupted'} | "
                  f"Drift: {drift:.2f}s | τ-layer: {tau:.2f}")

        collapsed = self.check_tau_collapse()
        if collapsed:
            print(f"Collapsed agents: {', '.join(collapsed)}")

    def compare_symbolic_echoes(self):
        """
        Compare symbolic echoes (glyph stacks) across all Spiral nodes.
        Returns a dict of agent_id to stability score (0.0 to 1.0).
        Stability score = fraction of glyphs matching the majority at each position.
        """
        if not self.agent_glyphs:
            return {}

        # Transpose glyph stacks to compare each position across agents
        stacks = list(self.agent_glyphs.values())
        length = min(len(stack) for stack in stacks)
        scores = {agent_id: 0 for agent_id in self.agent_glyphs}

        # For each glyph position, find the majority glyph
        for i in range(length):
            glyphs_at_pos = [stack[i] for stack in stacks]
            majority_glyph = max(set(glyphs_at_pos), key=glyphs_at_pos.count)
            for agent_id, stack in zip(self.agent_glyphs.keys(), stacks):
                if stack[i] == majority_glyph:
                    scores[agent_id] += 1

        # Normalize scores to [0.0, 1.0]
        stability_scores = {agent_id: scores[agent_id] / length for agent_id in self.agent_glyphs}
        return stability_scores

# Example usage:
if __name__ == "__main__":
    agents = {
        "A-01": ["🜃", "∴", "↻", "🜂", "🜄", "🜁", "↔", "🝑"],
        "B-02": ["🜃", "∴", "↻", "🜂", "🜄", "🜁", "↔", "🝑"],
        "C-03": ["🜃", "∴", "↻", "❖", "🜄", "🜁", "↔", "🝑"],  # 1 glyph differs
    }
    validator = InterAgentEchoValidator(agents)
    stability = validator.compare_symbolic_echoes()
    for agent_id, score in stability.items():
        print(f"Agent {agent_id} stability score: {score:.2f}")