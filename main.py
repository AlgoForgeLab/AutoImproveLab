from strategy.macd_strategy import generate_signal
from strategy.trend_strategy import generate_trend

print("AutoImproveLab started")

def run():
    print("Framework ready")
    print("MACD:", generate_signal())
    print("Trend:", generate_trend())

if __name__ == "__main__":
    run()
