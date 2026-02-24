print("Welcome to spam checking")
print("--------------------")

spam_words = ["win", "free", "money", "offer", "click",
    "prize", "urgent", "lottery", "cash", "buy now"]

message = input("Enter a message: ").lower()

words = message.split()

spam_count = 0

for word in words:
    if word in spam_words:
        spam_count += 1

if spam_count > 0:
    print("This message may be spam")
else:
    print("This message looks safe")

print("Thank You for comming here")
print("Have a nice day❤️")