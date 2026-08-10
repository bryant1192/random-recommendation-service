from rental_property import RentalProperty

properties = {}


#property1 = RentalProperty(
#    property_id = 1,
#    address = "123 Blueway St",
#    city = "Color City",
#    monthly_rent = 2000,
#    property_type = "House",
#    status = "Vacant"
#)

def add_property():
    print("\nAdd a New Property")
    print("You will need the address, city, monthly rent, property type, and status")
    print("This usually takes less than a minute")

    property_id = max(properties, default = 0) + 1

    address = input("\nAdd address, or type 'back' to cancel: ").strip()

    if address.lower() == "back":   
        print("Property creation canceled. No information was saved.")
        return
    
    city = input("City Name: ")

    while True:
        rent_input = input("Monthly Rent in Dollars: ").strip()

        try:
            monthly_rent = float(rent_input)

            if monthly_rent <= 0:
                print("Monthly rent must be greater than $0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number, such as 2000.")

    property_type = input("Property Type: ")

    status_options = {
        "1": "Vacant",
        "2": "Occupied",
        "3": "Maintenance"
    }

    print("\nSelect a property status:")
    print("1. Vacant")
    print("2. Occupied")
    print("3. Maintenance")

    while True:
        status_choice = input("Enter your choice: ")

        if status_choice in status_options:
            status = status_options[status_choice]
            break

        print("Invalid option. Please select 1, 2, or 3.")

    print("\nReview Property Information")
    print("===========================")
    print(f"Address: {address}")
    print(f"City: {city}")
    print(f"Monthly Rent: ${monthly_rent:,.2f}")
    print(f"Property Type: {property_type}")
    print(f"Status: {status}")

    confirm = input("Save this property? (yes/no): ").strip().lower()

    if confirm not in ["yes", "y"]:
        print("Property creation canceled. No information was saved.")
        return

    new_property = RentalProperty(
        property_id,
        address,
        city,
        monthly_rent,
        property_type,
        status
    )

    properties[property_id] = new_property

    print(f"New property {property_id} added successfully.")


def view_properties():
    if not properties:
        print("No properties found.")
        return

    print("\nChoose a display style:")
    print("1. Compact")
    print("2. Detailed")

    view_choice = input("Select an option: ").strip().lower()

    for prop in properties.values():
        if view_choice in ["1", "compact"]:
            print(
                f"ID: {prop.property_id} | "
                f"{prop.address} | "
                f"Status: {prop.status}"
            )
        else:
            display_property(prop)
            print()


def display_property(prop):
    print(f"Property ID: {prop.property_id}")
    print(f"Property Address: {prop.address}")
    print(f"City: {prop.city}")
    print(f"Monthly Rent: {prop.monthly_rent:,.2f}")
    print(f"Property Type: {prop.property_type}")
    print(f"Status: {prop.status}")


def generate_listing_description():
        try:
            property_id = int(
                input("Enter the Property ID: ")
            )
        except ValueError:
            print("Please enter a numeric Property ID.")
            return

        if property_id not in properties:
            print("Property not found. Use View Properties to check available IDs.")
            return
        
        prop = properties[property_id]

        print("\nGenerated Listing Description")
        print("=============================")
        print(f"Rental Property Available in {prop.city}")
        print()
        print(
            f"This {prop.property_type.lower()} is located at "
            f"{prop.address} in {prop.city}."
        )
        print(
            f"It is available for rent at "
            f"${prop.monthly_rent:,.2f} per month."
        )
        print(f"The property is currently {prop.status.lower()}.")
        print(
            "Contact the property owner for additional information "
            "or to schedule a viewing."
        )


def display_help():
    print("\n========== HELP ==========")
    print("Add Property:")
    print("Store a rental property's information in one place")
    print()
    print("View Properties:")
    print("Review the rental properties you have already added")
    print()
    print("Generate Property Description:")
    print("Create a description that can be used in a rental listing")
    print()
    print("Most actions take less than one minute")


while True:
    print("\n==============================")
    print("Rental Property Manager")
    print("==============================")
    print("1. Add Property")
    print("2. View Properties")
    print("3. Generate Property Description")
    print("4. Help")
    print("5. Exit")

    choice = input("Select an option by entering 1-5, or type the option name: ").strip().lower()

    if choice in ["1", "add", "add property"]:
        add_property()

    elif choice in ["2", "view", "view properties"]:
        view_properties()

    elif choice in ["3", "generate", "description"]:
        generate_listing_description()

    elif choice in ["4", "help"]:
        display_help()

    elif choice in ["5", "exit", "quit"]:
        print("Goodbye!")
        break

    else:
        print("Invalid option. Enter 1-5 or an available command name.")