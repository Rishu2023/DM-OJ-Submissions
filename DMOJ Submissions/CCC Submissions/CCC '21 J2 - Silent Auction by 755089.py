N = int(input())

maximumBid = -1

for count in range(N):
  personName = input()
  auctionBidAmount = int(input())
  if auctionBidAmount > maximumBid:
    auctionWinner = personName
    maximumBid = auctionBidAmount

print(auctionWinner)
