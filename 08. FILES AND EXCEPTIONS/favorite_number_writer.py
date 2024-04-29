from pathlib import Path
import json


favorite_number = input("Enter Number: ")

Path('favorite_number.json').write_text(json.dumps(favorite_number))

print("\nFILE CREATED!")


        