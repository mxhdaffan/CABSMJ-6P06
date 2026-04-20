closingPrices = list(map(float, input("Enter closing prices list: ").split()))

peak = max(closingPrices)
trough = min(closingPrices)

print("Maximum Value = ", peak)
print("Minimum Value = ", trough)