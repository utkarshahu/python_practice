import json

ytFile = "youtube.txt"

def list_all_videos(videos):
    print("\n" + "="*70)
    print("ALL YOUTUBE VIDEOS".center(70))
    print("="*70)
    
    if not videos:
        print("No videos found. Please add some videos first.\n")
        return
    
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Title: {video['name'].title()} | Duration: {video['time']}")
    
    print("="*70)

def update_video(videos):
    list_all_videos(videos)
    if not videos:
        return
    try:
        index = int(input("Enter the video number to update: "))
        if 1 <= index <= len(videos):
            print(f"Current title: {videos[index-1]['name']} | Current duration: {videos[index-1]['time']}")
            name = input("Enter new title: ").strip()
            time = input("Enter new duration (e.g., 10:30): ").strip()
            videos[index - 1] = {"name": name, "time": time}
            save_data_helper(videos)
            print("Video updated successfully.\n")
        else:
            print("Invalid video number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def add_video(videos):
    print("\nADD NEW VIDEO")
    name = input("Enter video title: ").strip()
    time = input("Enter video duration (e.g., 10:30): ").strip()
    if name and time:
        videos.append({'name': name, 'time': time})
        save_data_helper(videos)
        print("Video added successfully.\n")
    else:
        print("Title and duration cannot be empty.\n")

def delete_video(videos):
    list_all_videos(videos)
    if not videos:
        return
    try:
        index = int(input("Enter the video number to delete: "))
        if 1 <= index <= len(videos):
            deleted_video = videos.pop(index - 1)
            save_data_helper(videos)
            print(f"Deleted video: {deleted_video['name']}\n")
        else:
            print("Invalid video number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def load_data():
    try:
        with open(ytFile, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    try:
        with open(ytFile, "w") as file:
            json.dump(videos, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

def print_menu():
    print("\n" + "-"*70)
    print("YOUTUBE VIDEO MANAGER".center(70))
    print("-"*70)
    print("1. View All Videos")
    print("2. Add New Video")
    print("3. Update Existing Video")
    print("4. Delete a Video")
    print("5. Exit")
    print("-"*70)

def main():
    videos = load_data()
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("\nExiting the YouTube Manager. Have a great day!\n")
                break
            case _:
                print("Invalid choice. Please select a valid option (1-5).\n")

if __name__ == "__main__":
    main()
