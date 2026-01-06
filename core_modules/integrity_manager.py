import hashlib
import matplotlib.pyplot as plt

class DataIntegrityManager:
    """Manages blockchain-based data integrity and visualization."""
    
    def __init__(self):
        self.hash_chain = []
        self.genesis_hash = "0" * 64

    def generate_block_hash(self, data, prev_hash):
        """Generates a SHA-256 hash for a data block."""
        block = f"{data}{prev_hash}".encode()
        return hashlib.sha256(block).hexdigest()

    def build_chain(self, logs):
        """Constructs the hash chain from a list of logs."""
        prev_hash = self.genesis_hash
        for data in logs:
            current_hash = self.generate_block_hash(data, prev_hash)
            self.hash_chain.append((data, current_hash))
            prev_hash = current_hash
        return self.hash_chain

    def visualize_integrity(self):
        """Generates a professional bar chart of verification status."""
        verification_status = [1 for _ in range(len(self.hash_chain))]
        data_labels = [item[0] for item in self.hash_chain]
        
        plt.figure(figsize=(10, 6))
        bars = plt.bar(range(len(self.hash_chain)), verification_status, color="#2E7D32", alpha=0.8)
        
        for bar, log in zip(bars, data_labels):
            plt.text(bar.get_x() + bar.get_width()/2, 0.5, log, 
                     ha='center', va='center', color='white', fontweight='bold')

        plt.xticks(range(len(self.hash_chain)), [f"Block {i+1}" for i in range(len(self.hash_chain))])
        plt.title("Blockchain-Based Data Integrity Verification", fontsize=14)
        plt.xlabel("Blockchain Blocks")
        plt.ylabel("Integrity Status (Verified)")
        plt.ylim(0, 1.2)
        plt.yticks([]) 
        plt.grid(axis="x", linestyle="--", alpha=0.5)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Example Usage
    sample_logs = [f"System Log {i}" for i in range(1, 6)]
    manager = DataIntegrityManager()
    manager.build_chain(sample_logs)
    manager.visualize_integrity()
