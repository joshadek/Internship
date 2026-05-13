#Greeting
def greet():
    print("=" * 40)
    print("Welcome to SupportBot trial1")
    print("=" * 40)
    print("\nHello! I am your helpful support bot")
    print("How may i assist you  today")
    print("[1] Report a problem")
    print("[2] Info about product")
    print("[3] contact support team")
    print("[4] Exit")

#Reporting
def report_problem():
    print("\n--- Report your problem ---")
    print("Please describe your issue briefly.")
    print("Common issues:")
    print(" [1] Unable to login")
    print(" [2] Payment not working")
    print(" [3] App crashing")
    print(" [4] Other")
    print()

    issue_choice = input("Select an issue (1-4): ").strip()

    issues = {
        "1": "Login issue",
        "2": "Payment issue",
        "3": "App crash",
        "4": "Other"
    }

    issue=issues.get(issue_choice, "Unknown Choice")

    if issue == "Unknown issue":
        print("\nInvalid choice. Please try again.")
        return
    
    print(f"\nGot it. You're experiencing: {issue}")
    get_solution(issue)


#Solutions
def get_solution(issue):
    solutions = {
        "Login issue": "Try resetting your password at settings > account. If that fails, clear your app cache and retry.",
        "Payment issue": "Ensure your card details are correct and your bank isn't blocking the transaction. Try a different payment method if the issue persists.",
        "App crash": "Update the app to the latest version. If it still crashes, uninstall and reinstall it.",
        "Other": "We've noted your issue. A support agent will follow up with you shortly."
    }

    solution = solutions.get(issue, "We couldn't find a solution. Please contact support.")
    print(f"\nSuggested fix: {solution}")



#Info
def product_info():
    print("\n--- Product Information ---")

    info = {
        "1": ("What is this product?", "SupportBot Helper is an all-in-one customer support tool designed to resolve common issues quickly."),
        "2": ("What platforms is it available on?", "It is available on Android, iOS, and Web."),
        "3": ("Is there a free plan?", "Yes, the free plan includes basic features. Premium unlocks priority support and advanced tools."),
        "4": ("How do I get started?", "Download the app, create an account, and follow the setup guide in the welcome email.")
    }

    print("Frequently Asked Questions:\n")
    for key, (question, _) in info.items():
        print(f"  [{key}] {question}")
    print()

    choice = input("Select a question (1-4): ").strip()

    if choice in info:
        _, answer = info[choice]
        print(f"\n{answer}")
    else:
        print("\nInvalid choice. Please try again.")
 

#Support line
def contact_support():
    print("\n--- Contact Support ---")
    print("You can reach us through any of the following:\n")

    contacts = [
        ("Email",    "support@supportbot.com"),
        ("Phone",    "+1 800 123 4567"),
        ("Hours",    "Monday - Friday, 9am to 6pm (WAT)")
    ]

    for channel, detail in contacts:
        print(f"  {channel:<20}: {detail}")

    print("\nA human agent will get back to you within 24 hours.")




def main():
    greet()

    while True:
        choice=input("Enter your choice (1-4)").strip()
        if choice == "1":
            report_problem()
        elif choice == "4":
            print("\nThank you for reaching out. Goodbye!")
            break
        elif choice == "2":
            product_info()
        elif choice == "3":
            contact_support()
        else:
            print("\nThat option isn't built yet — coming soon!")


        
        print()
        print("What else can I help you with?")
        print("  [1] Report a problem")
        print("  [2] Product information")
        print("  [3] Contact support")
        print("  [4] Exit")
        print()
    
    
    
    '''
    option_chosen=input("Enter choice here:").strip()
    print(f"\n Option {option_chosen} selected")
    '''

if __name__=="__main__":
    main()