# region CRUD App (uuid4) — LOGIN + ROLE Version (NO FUNCTIONS)
from uuid import uuid4
from pprint import pprint


# ------------------------------------------------------------------
# LOGIN DATA (Username -> password)
# ------------------------------------------------------------------
users = {
    "admin": "1234",
    "ipek": "0000",
    "guest": "guest"
}

# ------------------------------------------------------------------
# ROLE DATA (Username -> role)
# ------------------------------------------------------------------
roles = {
    "admin": "admin",   # full access
    "ipek": "editor",   # create + read + update
    "guest": "viewer"   # read only
}

MAX_TRY = 3


# ------------------------------------------------------------------
# SAMPLE DATA (Nested Dict)
# ------------------------------------------------------------------
categories = {
    'd912b8cf-0b59-4efb-bfcf-17356dd59c9b': {
        'name': 'Boxing Gloves',
        'description': 'Best boxing gloves'
    },
    '9ecfa748-ee8e-4ac3-a471-33e1fd9fe52c': {
        'name': 'MMA Gloves',
        'description': 'Best MMA gloves'
    }
}


# ------------------------------------------------------------------
# LOGIN FLOW
# ------------------------------------------------------------------
print("🔐 LOGIN REQUIRED")

logged_in = False
current_user = None
current_role = None

for attempt in range(1, MAX_TRY + 1):
    username = input("Username: ").strip().lower()
    password = input("Password: ").strip()

    if username in users and users[username] == password:
        logged_in = True
        current_user = username
        current_role = roles.get(username, "viewer")  # default viewer
        break
    else:
        remaining = MAX_TRY - attempt
        print(f"❌ Wrong credentials. Remaining attempt: {remaining}")

if not logged_in:
    print("🚫 Too many failed attempts. Exiting...")
    raise SystemExit

print(f"\n✅ Welcome, {current_user}!  | Role: {current_role}")


# ------------------------------------------------------------------
# ROLE PERMISSIONS (NO FUNCTIONS)
# ------------------------------------------------------------------
# admin  -> create, get all, get by id, get by name, update, delete
# editor -> create, get all, get by id, get by name, update
# viewer -> get all, get by id, get by name

allowed_processes = set()

if current_role == "admin":
    allowed_processes = {
        "create", "get all", "get by id", "get by name", "update", "delete", "exit"
    }
elif current_role == "editor":
    allowed_processes = {
        "create", "get all", "get by id", "get by name", "update", "exit"
    }
else:  # viewer
    allowed_processes = {
        "get all", "get by id", "get by name", "exit"
    }


# ------------------------------------------------------------------
# CRUD LOOP
# ------------------------------------------------------------------
while True:
    process = input(
        "\nType a process name "
        "(create | get all | get by id | get by name | update | delete | exit): "
    ).lower().strip()

    # Permission check
    if process not in allowed_processes:
        print(f"⛔ Access denied for '{process}'. Your role: {current_role}")
        print(f"✅ Allowed: {', '.join(sorted(allowed_processes))}")
        continue

    match process:
        case 'create':
            new_name = input('Please type a category name: ').strip()
            new_descp = input('Please type a description: ').strip()

            categories[str(uuid4())] = {
                'name': new_name,
                'description': new_descp
            }

            print('✅ Category created successfully!')
            pprint(categories)

        case 'get all':
            print('📦 All Categories:')
            pprint(categories)

        case 'get by id':
            category_key = input('Category Key: ').strip()

            result = categories.get(category_key)
            if result is None:
                print('❌ There is no such a category..!')
            else:
                print('✅ Found:')
                pprint(result)

        case 'get by name':
            cat_name = input('Category name: ').strip().lower()

            filtered_categories = [
                category for category in categories.values()
                if cat_name in category.get('name', '').lower()
            ]

            if filtered_categories:
                print('🔍 Matching Categories:')
                pprint(filtered_categories)
            else:
                print('❌ No category found.')

        case 'update':
            category_key = input('Category Key: ').strip()

            if category_key in categories:
                new_name = input('Please type a category name: ').strip()
                new_descp = input('Please type a description: ').strip()

                categories.update({
                    category_key: {
                        'name': new_name,
                        'description': new_descp
                    }
                })

                print(f'✅ {category_key} has been edited..!')
                pprint(categories[category_key])
            else:
                print('❌ There is no such a category..!')

        case 'delete':
            category_key = input('Category Key: ').strip()

            if category_key in categories:
                del categories[category_key]
                print(f'✅ {category_key} has been removed..!')
                pprint(categories)
            else:
                print('❌ There is no such a category..!')

        case 'exit':
            print(f'👋 Exiting application... Bye, {current_user}! (Role: {current_role})')
            break

        case _:
            print('❌ Invalid process type!')
# endregion