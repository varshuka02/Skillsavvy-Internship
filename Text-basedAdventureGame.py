def start_game():
    print("Welcome to The Enchanted Garden!")
    grandmothers_house()

def grandmothers_house():
    print("\nYou are at your grandmother's house. Do you want to search the house or talk to your grandmother?")
    choice = input("Enter 'search' or 'talk': ").strip().lower()
    if choice == 'search':
        search_house()
    elif choice == 'talk':
        talk_to_grandmother()
    else:
        print("Invalid choice. Try again.")
        grandmothers_house()

def search_house():
    print("\nWhere do you want to search?")
    print("1. Attic")
    print("2. Kitchen")
    print("3. Garden shed")
    choice = input("Enter 'attic', 'kitchen', or 'shed': ").strip().lower()
    if choice == 'attic':
        print("You find an old map and a lantern.")
        inventory.extend(['map', 'lantern'])
        grandmothers_house()
    elif choice == 'kitchen':
        print("You find some rations and a water bottle.")
        inventory.extend(['rations', 'water bottle'])
        grandmothers_house()
    elif choice == 'shed':
        print("You find a pair of gloves and a small shovel.")
        inventory.extend(['gloves', 'shovel'])
        grandmothers_house()
    else:
        print("Invalid choice. Try again.")
        search_house()

def talk_to_grandmother():
    print("\nYour grandmother tells you about the enchanted garden’s history and gives you a key.")
    inventory.append('key')
    enter_garden()

def enter_garden():
    print("\nYou enter the enchanted garden. Do you want to talk to the flowers or ignore them?")
    choice = input("Enter 'talk' or 'ignore': ").strip().lower()
    if choice == 'talk':
        talking_flower_field()
    elif choice == 'ignore':
        fairy_grove()
    else:
        print("Invalid choice. Try again.")
        enter_garden()

def talking_flower_field():
    print("\nYou find yourself in a field of talking flowers. Who do you want to talk to?")
    print("1. Sunflower")
    print("2. Rose")
    print("3. Daisy")
    print("4. Water the flowers")
    choice = input("Enter 'sunflower', 'rose', 'daisy', or 'water': ").strip().lower()
    if choice == 'sunflower':
        print("The Sunflower tells you about the garden’s layout and gives you a map.")
        inventory.append('map')
    elif choice == 'rose':
        print("The Rose gives you a protective charm.")
        inventory.append('charm')
    elif choice == 'daisy':
        print("The Daisy teaches you a song that can calm hostile creatures.")
        inventory.append('song')
    elif choice == 'water':
        if 'water bottle' in inventory:
            print("You water the flowers and a wilting flower gives you a clue.")
        else:
            print("You need a water bottle to water the flowers.")
    else:
        print("Invalid choice. Try again.")
        talking_flower_field()
    fairy_grove()

def fairy_grove():
    print("\nYou reach the fairy grove. Do you help the fairies gather dew or listen to the fairy queen’s story?")
    choice = input("Enter 'help' or 'listen': ").strip().lower()
    if choice == 'help':
        help_fairies()
    elif choice == 'listen':
        listen_to_queen()
    else:
        print("Invalid choice. Try again.")
        fairy_grove()

def help_fairies():
    print("\nYou help the fairies gather dew and they give you a magical charm.")
    inventory.append('magical charm')
    mystic_pond()

def listen_to_queen():
    print("\nThe fairy queen tells you about the source of the darkness and gives you a magic dust pouch.")
    inventory.append('magic dust')
    mystic_pond()

def mystic_pond():
    print("\nYou come across a mystic pond. Do you talk to the water nymph or feed the fish?")
    choice = input("Enter 'talk' or 'feed': ").strip().lower()
    if choice == 'talk':
        solve_riddle()
    elif choice == 'feed':
        feed_fish()
    else:
        print("Invalid choice. Try again.")
        mystic_pond()

def solve_riddle():
    print("\nThe water nymph gives you a riddle to solve.")
    riddle_answer = input("What is your answer to the riddle? ").strip().lower()
    if riddle_answer == 'correct answer':  # Placeholder for actual riddle answer
        print("You solve the riddle and obtain an enchanted mirror.")
        inventory.append('enchanted mirror')
    else:
        print("Incorrect answer. You miss out on the magical item.")
    enchanted_forest()

def feed_fish():
    if 'rations' in inventory:
        print("\nYou feed the fish and a special fish gives you a scale.")
        inventory.append('fish scale')
    else:
        print("You need rations to feed the fish.")
    enchanted_forest()

def enchanted_forest():
    print("\nYou venture deeper into the enchanted forest. Do you want to meet the wise owl or help the lost bunny?")
    choice = input("Enter 'owl' or 'bunny': ").strip().lower()
    if choice == 'owl':
        meet_owl()
    elif choice == 'bunny':
        help_bunny()
    else:
        print("Invalid choice. Try again.")
        enchanted_forest()

def meet_owl():
    print("\nThe wise owl asks you questions. Answer them correctly to receive a map piece.")
    owl_questions()
    crystal_cave()

def owl_questions():
    questions = {
        "What is 2 + 2?": "4",
        "What color is the sky?": "blue",
        "What is the opposite of night?": "day"
    }
    for question, answer in questions.items():
        user_answer = input(f"{question} ").strip().lower()
        if user_answer == answer:
            print("Correct!")
        else:
            print("Incorrect.")
    print("You receive a map piece.")
    inventory.append('map piece')

def help_bunny():
    print("\nYou guide the lost bunny back to its burrow and receive a thank-you gift.")
    inventory.append('thank-you gift')
    crystal_cave()

def crystal_cave():
    print("\nYou find a hidden cave filled with glowing crystals. Do you navigate the crystal maze or collect crystal shards?")
    choice = input("Enter 'navigate' or 'collect': ").strip().lower()
    if choice == 'navigate':
        navigate_maze()
    elif choice == 'collect':
        collect_shards()
    else:
        print("Invalid choice. Try again.")
        crystal_cave()

def navigate_maze():
    print("\nYou navigate the crystal maze and find the correct path.")
    inventory.append('correct path')
    ancient_scroll()

def collect_shards():
    print("\nYou collect crystal shards to use as light sources.")
    inventory.append('crystal shards')
    ancient_scroll()

def ancient_scroll():
    print("\nYou find an ancient scroll in the cave. Do you read it or ignore it?")
    choice = input("Enter 'read' or 'ignore': ").strip().lower()
    if choice == 'read':
        print("You learn a spell to dispel darkness.")
        inventory.append('darkness spell')
    elif choice == 'ignore':
        print("You ignore the scroll and move on.")
    else:
        print("Invalid choice. Try again.")
        ancient_scroll()
    heart_of_garden()

def heart_of_garden():
    print("\nYou reach the heart of the garden where the magical fountain is located. Do you activate the fountain or fight the darkness?")
    choice = input("Enter 'activate' or 'fight': ").strip().lower()
    if choice == 'activate':
        if 'charm' in inventory and 'magical item' in inventory:
            ending_garden_saved()
        else:
            ending_partial_success()
    elif choice == 'fight':
        ending_garden_lost()
    else:
        print("Invalid choice. Try again.")
        heart_of_garden()

def ending_garden_saved():
    print("\nCongratulations! You successfully activated the fountain and saved the enchanted garden!")
    play_again()

def ending_garden_lost():
    print("\nYou failed to save the garden, and it succumbs to darkness.")
    play_again()

def ending_partial_success():
    print("\nYou managed to save the garden, but some darkness still lingers.")
    play_again()

def play_again():
    choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if choice == 'yes':
        start_game()
    else:
        print("Thank you for playing!")

# Initialize game
inventory = []
start_game()


