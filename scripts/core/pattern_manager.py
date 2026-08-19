import os
import random
import importlib
import inspect
import config
from scripts.data.number_pattern import NumberPattern

class PatternManager:
    def __init__(self):
        self.v_patterns, self.h_patterns = self._load_patterns()
        
    def _load_patterns(self):
        v_patterns = []
        h_patterns = []
        # Construct absolute path or rely on current working directory
        # It's safer to use absolute path based on __file__
        current_dir = os.path.dirname(os.path.abspath(__file__))
        patterns_dir = os.path.join(current_dir, "..", "data", "patterns")
        
        for filename in os.listdir(patterns_dir):
            if filename.endswith(".py") and not filename.startswith("__"):
                module_name = "scripts.data.patterns.{}".format(filename[:-3])
                module = importlib.import_module(module_name)
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if issubclass(obj, NumberPattern) and obj is not NumberPattern:
                        if name == 'DoubleArithmeticPattern':
                            h_patterns.append(obj)
                        else:
                            v_patterns.append(obj)
                            h_patterns.append(obj)
        return v_patterns, h_patterns

    def generate_all_patterns(self):
        v_sequences = {}
        h_sequences = {}
        v_answers = {}
        h_answers = {}

        # Vertical (9 colors, length = NUM_COLS = 5)
        for color in config.V_COLORS:
            pattern_class = random.choice(self.v_patterns)
            pattern_instance = pattern_class.random_instance()
            seq = pattern_instance.generate(config.NUM_COLS)
            
            hole_idx = random.randint(0, config.NUM_COLS - 1)
            v_answers[color] = seq[hole_idx]
            
            seq_with_hole = list(seq)
            seq_with_hole[hole_idx] = "?"
            v_sequences[color] = seq_with_hole

        # Horizontal (8 colors, length = NUM_H_ROWS = 8)
        for color in config.H_COLORS:
            pattern_class = random.choice(self.h_patterns)
            pattern_instance = pattern_class.random_instance()
            seq = pattern_instance.generate(config.NUM_H_ROWS)
            
            hole_idx = random.randint(0, config.NUM_H_ROWS - 1)
            h_answers[color] = seq[hole_idx]
            
            seq_with_hole = list(seq)
            seq_with_hole[hole_idx] = "?"
            h_sequences[color] = seq_with_hole

        return v_sequences, h_sequences, v_answers, h_answers
