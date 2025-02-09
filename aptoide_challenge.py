import requests
import base64
import random

# Step 1: Search and display the list of apps
def search_apps():
    url = "https://ws75.aptoide.com/api/7/apps/get/store_name=apps/q=bWF4U2RrPTE5Jm1heFNjcmVlbj1ub3JtYWwmbWF4R2xlcz0yLjA/group_name=games/limit=10/offset=0/mature=false"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        apps = data.get("datalist", {}).get("list", [])
        print("List of Apps:")
        for app in apps:
            print(f"- {app.get('name')} (Package: {app.get('package')})")

        # EXTRA - Decode the 'q' parameter
        q_param = "bWF4U2RrPTE5Jm1heFNjcmVlbj1ub3JtYWwmbWF4R2xlcz0yLjA"
        # Add padding to make the length a multiple of 4
        padding = len(q_param) % 4
        if padding:
            q_param += "=" * (4 - padding)
        decoded_q = base64.b64decode(q_param).decode("utf-8")
        print(f"\nEXTRA - Decoded 'q' parameter: {decoded_q}")

        return apps  # Return the list of apps for use in Step 2
    else:
        print(f"Failed to fetch apps. Status code: {response.status_code}")
        return []

# Step 2: Display description of a random app
def display_app_description(apps):
    if not apps:
        print("No apps available to display description.")
        return

    # Select a random app
    random_app = random.choice(apps)
    package_name = random_app.get("package")
    print(f"\nSelected Random App: {random_app.get('name')} (Package: {package_name})")

    # Fetch the description of the selected app
    url = f"https://ws75.aptoide.com/api/7/app/get/store_name=apps/q=bWF4U2RrPTE5Jm1heFNjcmVlbj1ub3JtYWwmbWF4R2xlcz0yLjA/package_name={package_name}/language=pt_PT/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        description = data.get("datalist", {}).get("description", "No description available.")
        print(f"\nApp Description for '{package_name}':\n{description}")
    else:
        print(f"Failed to fetch app description. Status code: {response.status_code}")

# Step 3: Download the APK file
def download_apk():
    url = "https://aptoide-mmp.aptoide.com/api/v1/download/b2VtaWQ9VGVjaENoYWxsZW5nZVB5dGhvbiZwYWNrYWdlX25hbWU9Y29tLmZ1bi5sYXN0d2FyLmdwJnJlZGlyZWN0X3VybD1odHRwczovL3Bvb2wuYXBrLmFwdG9pZGUuY29tL2FwcHMvY29tLWZ1bi1sYXN0d2FyLWdwLTk5OTk5LTY2NjEyOTMwLWE3MThmOWZlMjE5OGM1Y2EyYzIwMmUwNDYzZTVkZDk1LmFwaw==?resolution=1080x1776"
    params = {"aptoide_uid": "testchallenge"}  # Add missing parameter
    response = requests.get(url, params=params)

    if response.status_code == 200:
        with open("com.fun.lastwar.gp.apk", "wb") as file:
            file.write(response.content)
        print("\nAPK file downloaded successfully as 'com.fun.lastwar.gp.apk'.")
    else:
        print(f"Failed to download APK. Status code: {response.status_code}")

# Main execution
if __name__ == "__main__":
    apps = search_apps()  # Fetch the list of apps
    if apps:  # Only proceed if apps were fetched successfully
        display_app_description(apps)  # Display description of a random app
        download_apk()  # Download the APK file