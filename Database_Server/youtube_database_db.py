import sqlite3
connection = sqlite3.connect("youtube.db")

cursor = connection.cursor()

cursor.execute(''' 
               CREATE TABLE IF NOT EXISTS  videos (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL
               )
               ''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_video():
    name = input("Enter the name of video : ")
    time = input("Enter the time of video : ")

    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    connection.commit()

    
def update_videos():
    video_id = int(input("Enter the ID of the video to update: "))
    new_name = input("Enter the new name: ")
    new_time = input("Enter the new time: ")

    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    connection.commit()
    print("✅ Video updated successfully!")

    
def delete_videos():
    video_id = int(input("Enter the ID of the video to update: "))
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    connection.commit()
    print("✅ Video deleted successfully!")




def main():
    while True:
        print("\n" + "-"*70)
        print("YOUTUBE VIDEO MANAGER".center(70))
        print("-"*70)
        print("1. View All Videos")
        print("2. Add New Video")
        print("3. Update Existing Video")
        print("4. Delete a Video")
        print("5. Exit")
        print("-"*70)
        choice = int(input("Enter your choice : "))
        
        if choice ==1:
            list_videos()
        elif choice==2 :
            add_video()
        elif choice==3 :
            update_videos()
        elif choice==4 :
            delete_videos()
        elif choice==5:
            break
        else:
            print("Invalid Choice!")

    connection.close()

if __name__ == "__main__":
    main()


