import matplotlib.pyplot as plt

def plot_user_sentiment(satisfied_pct, unsatisfied_pct):
    """
    Visualizes user feedback metrics during phased system rollouts.
    Useful for HCI (Human-Computer Interaction) reporting.
    """
    labels = ['Satisfied Users', 'Unsatisfied Users']
    sizes = [satisfied_pct, unsatisfied_pct]
    colors = ['#4CAF50', '#F44336']  # Material Design Green and Red
    explode = (0.1, 0) 

    plt.figure(figsize=(8, 6))
    plt.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        explode=explode,
        shadow=False,
        textprops={'fontsize': 12, 'fontweight': 'bold'}
    )

    plt.title("Post-Deployment User Satisfaction Analysis", fontsize=14, pad=20)
    plt.axis('equal') 
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Standard rollout metrics
    plot_user_sentiment(89, 11)
