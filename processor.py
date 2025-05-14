def analyze_requirement(requirement: str):
    requirement = requirement.lower()
    modules = []

    if "login" in requirement:
        modules.extend(["User Authentication", "Session Management"])
    if "blog" in requirement:
        modules.extend(["Post Management", "Comment System", "User Profiles"])
    if "ecommerce" in requirement or "product" in requirement:
        modules.extend(["Product Catalog", "Cart System", "Checkout Flow"])
    if not modules:
        modules.append("Generic Module A")

    return modules
