import argparse
from game_client import GameClient
from chain_builder import ChainBuilder
from utils import load_vocabulary

def main(threshold: int = 200):
    vocab = load_vocabulary("assets/Extracted_Nouns.csv")
    builder = ChainBuilder(vocab)
    
    with GameClient() as client:
        chain = builder.build_chain(threshold)
        print(f"Final chain ({len(chain)}): {' → '.join(chain)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--threshold", type=int, default=200)
    args = parser.parse_args()
    main(args.threshold)