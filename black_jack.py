import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 10=Jack/Queen/King, 11=Ace
    return random.choice(cards)

def calculate_score(cards):
    """Calculates the total score from the list of cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "Draw!"
    elif dealer_score == 0:
        return "Lose! Dealer has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Dealer went over. You win 😁"
    elif user_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print("🃏 Welcome to Blackjack!")

    user_cards = []
    dealer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            draw_card = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if draw_card == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    # Dealer's turn
    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(user_score, dealer_score))

# Run the game
play_game()