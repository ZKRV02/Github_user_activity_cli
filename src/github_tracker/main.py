import urllib.request, json 

def output(push_counter, other_activities):
    for i in push_counter:
        print(f"Pushed {push_counter[i]} commit(s) to {i}")
    for i in other_activities:
        if i[0] == "CreateEvent":
            print(f"Created a new repository: {i[1]}")
        elif i[0] == "ForkEvent":
            print(f"Forked a repository: {i[1]}")
        elif i[0] == "WatchEvent":
            print(f"Started watching a repository: {i[1]}")
        elif i[0] == "PullRequestEvent":
            print(f"Created a pull request in repository: {i[1]}")
        elif i[0] == "IssuesEvent":
            print(f"Created an issue in repository: {i[1]}")
        elif i[0] == 'DeleteEvent':
            print(f"Deleted a repository: {i[1]}")

def main():
    push_counter = {}
    other_activities = []
    count = 0
    username = input("Enter github user: ")
    try:
        with urllib.request.urlopen(f"https://api.github.com/users/{username}/events") as url:
            data = json.loads(url.read().decode())
            for i in data:
                event_type = i.get("type")
                repo = i.get("repo").get("name")
                if event_type == "PushEvent":
                    count += 1
                    push_counter[repo] = count
                else:
                    activity = [event_type, repo]
                    other_activities.append(activity)
        output(push_counter=push_counter, other_activities=other_activities)                           
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == "__main__":
    main()