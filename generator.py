def generate_schema(modules: list):
    schema = ""
    if "User Authentication" in modules:
        schema += "Table: Users (id, username, password_hash)\n"
    if "Session Management" in modules:
        schema += "Table: Sessions (id, user_id, token, expiry)\n"
    if "Post Management" in modules:
        schema += "Table: Posts (id, title, content, author_id)\n"
    if "Comment System" in modules:
        schema += "Table: Comments (id, post_id, user_id, content)\n"
    if "User Profiles" in modules:
        schema += "Table: Profiles (id, user_id, bio, avatar_url)\n"
    if "Product Catalog" in modules:
        schema += "Table: Products (id, name, description, price)\n"
    if "Cart System" in modules:
        schema += "Table: Carts (id, user_id, product_ids)\n"
    if "Checkout Flow" in modules:
        schema += "Table: Orders (id, user_id, total_price, status)\n"
    return schema or "No schema available"

def generate_pseudocode(modules: list):
    code = ""
    if "User Authentication" in modules:
        code += "Function login(username, password):\n"
        code += "    Check if user exists\n"
        code += "    Validate password\n"
        code += "    Create session\n\n"
    if "Post Management" in modules:
        code += "Function create_post(title, content, user_id):\n"
        code += "    Insert into Posts table\n\n"
    if "Product Catalog" in modules:
        code += "Function list_products():\n"
        code += "    Return all products from DB\n\n"
    return code or "No pseudocode available"
