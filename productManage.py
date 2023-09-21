#PRODUCT MANAGEMENT APPLICATION
#productmanage.py
class UserSystem:
    def __init__(self):
        self.users = {}  # Dictionary to store user information (username: password)

    def register(self, username, password):
        if username in self.users:
            print("Username already exists. Please choose a different one.")
        else:
            self.users[username] = password
            print("Registration successful. You can now log in.")

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            print("Login successful. Welcome, " + username + "!")
        else:
            print("Invalid username or password. Please try again.")


# Example usage:
user_system = UserSystem()

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product_id, name, price):
        product = Product(product_id, name, price)
        self.products.append(product)
        print(f"Product '{name}' added successfully.")

    def delete_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                print(f"Product '{product.name}' deleted successfully.")
                return
        print("Product not found.")

    def place_order(self, product_id, quantity):
        for product in self.products:
            if product.product_id == product_id:
                total_price = product.price * quantity
                print(f"Order placed for {quantity} units of '{product.name}' for a total of RS{total_price:.2f}.")
                return
        print("Product not found.")

    def display_products(self):
        if not self.products:
            print("No products available.")
        else:
            print("Available Products:")
            for product in self.products:
                print(f"Product ID: {product.product_id}, Name: {product.name}, Price: RS{product.price:.2f}")

def main():
    product_manager = ProductManager()

    while True:
        print("\nPRODUCT MANAGEMENT APP")
        print("1. Register")
        print("2. login")
        print("3. Add Product")
        print("4. Delete Product")
        print("5. Place Order")
        print("6. Display Products")
        print("7. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            user_system.register(username, password)

        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user_system.login(username, password)

        elif choice == "3":
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            product_manager.add_product(product_id, name, price)

        elif choice == "4":
            product_id = input("Enter Product ID to delete: ")
            product_manager.delete_product(product_id)

        elif choice == "5":
            product_id = input("Enter Product ID to order: ")
            quantity = int(input("Enter Quantity: "))
            product_manager.place_order(product_id, quantity)

        elif choice == "6":
            product_manager.display_products()

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
