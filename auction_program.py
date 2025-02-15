import art

print(art.logo_auction)

auction_list={}
end = False

def higest_bid(list):
    
    higest=0
    
    for bid in auction_list:
        bid_amout = auction_list[bid]
        if bid_amout>higest:
            higest=bid_amout
    print(f"The highest bid was made by {bid} with an amount of {higest}")
           
while not end:
    print("Welcome to the secret auction program.")
    name = input("What is your name? ")  
    bid = int(input("What is your bid? "))
    end = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
        
    auction_list[name] = bid
        
    if end=="no":
        higest_bid(list=auction_list)
        end=True
        
    elif end=="yes":
        print(f"{auction_list}")
        end = False
    else:
        print("Incorrect input")
            
        