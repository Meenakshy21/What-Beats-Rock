from dataclasses import dataclass
from typing import List, Dict
import random

@dataclass
class ChainState:
    nodes: List[str]
    relations: Dict[str, bool]  # Cache for word relations

class ChainBuilder:
    def __init__(self, vocabulary: List[str]):
        self.vocabulary = vocabulary
        self.reset_state()
    
    def reset_state(self):
        self.state = ChainState(
            nodes=["rock"],
            relations={"rock": True}
        )
    
    def build_chain(self, threshold: int) -> List[str]:
        """Main algorithm with fallback logic"""
        while len(self.state.nodes) < threshold:
            candidate = self._select_candidate()
            if not candidate:
                break
                
            if self._validate_move(self.state.nodes[-1], candidate):
                self.state.nodes.append(candidate)
            else:
                self._attempt_fallback()
                
        return self.state.nodes
    
    def _select_candidate(self) -> Optional[str]:
        """Random unused word selection"""
        unused = [w for w in self.vocabulary 
                 if w not in self.state.nodes]
        return random.choice(unused) if unused else None
    
    def _attempt_fallback(self):
        """Backtrack to last viable node"""
        for i in range(len(self.state.nodes)-1, -1, -1):
            if self._can_beat_rock(self.state.nodes[i]):
                self.state.nodes = self.state.nodes[:i+1]
                return
    
    def _can_beat_rock(self, word: str) -> bool:
        """Check if word → rock (with caching)"""
        if word not in self.state.relations:
            # Implement actual game query here
            self.state.relations[word] = False  # Mock response
        return self.state.relations[word]