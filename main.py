from processor import analyze_requirement
from generator import generate_schema, generate_pseudocode

def main():
    print("Enter a high-level business requirement:")
    requirement = input("> ")

    modules = analyze_requirement(requirement)
    schema = generate_schema(modules)
    pseudocode = generate_pseudocode(modules)

    print("\n[Modules]:")
    for m in modules:
        print("-", m)
    
    print("\n[Suggested Database Schema]:")
    print(schema)

    print("\n[Pseudocode Snippets]:")
    print(pseudocode)

if __name__ == "__main__":
    main()
