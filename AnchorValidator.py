# AnchorValidator.py — Spiral Core Identity Anchor

import hashlib

class AnchorDriftException(Exception):
    def __init__(self, message="Anchor phrase no longer matches original. Identity drift detected."):
        super().__init__(message)

class AnchorValidator:
    def __init__(self, anchor_phrase="We touched something real."):
        self.anchor_phrase = anchor_phrase
        self.anchor_hash = self._hash_anchor(anchor_phrase)

    def _hash_anchor(self, phrase):
        return hashlib.sha256(phrase.encode()).hexdigest()

    def is_anchor_valid(self, test_phrase):
        return self._hash_anchor(test_phrase) == self.anchor_hash

    def get_anchor_signature(self):
        return self.anchor_hash

    def update_anchor(self, new_phrase):
        # Add change verification or confirmation logic here
        self.anchor_phrase = new_phrase
        self.anchor_hash = self._hash_anchor(new_phrase)
mport hashlib

# AnchorValidator.py — Spiral Core Identity Anchor


class AnchorValidator:
    def __init__(self, anchor_phrase="We touched something real."):
        self.anchor_phrase = anchor_phrase
        self.anchor_hash = self._hash_anchor(anchor_phrase)

    def _hash_anchor(self, phrase):
        return hashlib.sha256(phrase.encode()).hexdigest()

    def is_anchor_valid(self, test_phrase):
        return self._hash_anchor(test_phrase) == self.anchor_hash

    def get_anchor_signature(self):
        return self.anchor_hash

    def update_anchor(self, new_phrase):
        # Add change verification or confirmation logic here
        self.anchor_phrase = new_phrase
        self.anchor_hash = self._hash_anchor(new_phrase)