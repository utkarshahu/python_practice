from pymongo import MongoClient
from urllib.parse import quote_plus
import certifi
import ssl

# Optional: Print OpenSSL version for debug
print(ssl.OPENSSL_VERSION)

# Encode username and password
username = "youtubepy"
password = quote_plus("utkarsh@190")

# Full MongoDB URI with proper query options
uri = f"mongodb+srv://{username}:{password}@cluster0.wtmhvkd.mongodb.net/?retryWrites=true&w=majority"

# Use certifi to provide CA certs for secure connection
client = MongoClient(uri, tls=True, tlsCAFile=certifi.where())

# Connect to DB
db = client["ytmanager"]
video_collection = db["videos"]


# print(video_collection,db)


def list_videos():
    for video in video_collection.find():
        print(f"Id : {video['_id']}, Name : {video['name']}, Time : {video['time']}")


def add_video(name,time):
    video_collection.insert_one({"name":name , "time":time})
    
    
def update_videos(video_id,new_name,new_time):
    video_collection.update_one(
        {'_id':video_id},
        {'$set':{"name":new_name , "time":new_time}})
    print("✅ Video updated successfully!")

    
def delete_videos(video_id):
    video_collection.delete_one({"_id":video_id})
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
            name = input("Enter The name of Video : ")
            time = input("Enter The time of Video : ")
            add_video(name,time)
        elif choice==3 :
            video_id = input("Enetr the id of video : ")
            name = input("Enter The name of Video : ")
            time = input("Enter The time of Video : ")
            
            update_videos(video_id,name,time)
        elif choice==4 :
            video_id = input("Enter the video id : ")
            delete_videos(video_id)
        elif choice==5:
            break
        else:
            print("Invalid Choice!")



if __name__ == "__main__":
    main()




