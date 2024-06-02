import random


name = input("Please enter your name\n");
question = input("Please enter your question\n");
answer = random.randint(1,9);

print(f"\n{name} asks: {question}");

match answer:
    case 1:
        print("Magic 8-Ball says: Yes - definitely\n")
    case 2:
        print("Magic 8-Ball says: It is decidedly so\n")
    case 3:
        print("Magic 8-Ball says: Without a doubt\n")
    case 4:
        print("Magic 8-Ball says: Reply hazy, try again\n")
    case 5:
        print("Magic 8-Ball says: Ask again later\n")
    case 6:
        print("Magic 8-Ball says: Better not tell you now\n")
    case 7:
        print("Magic 8-Ball says: My sources say no\n")
    case 8:
        print("Magic 8-Ball says: Outlook not so good\n")
    case 9:
        print("Magic 8-Ball says: Very doubtful\n")
