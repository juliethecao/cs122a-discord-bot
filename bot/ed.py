import requests 
import os
from dotenv import load_dotenv
import json
import re
from typing import List

CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

load_dotenv()

responseTemplate = {
    "link": "",
    "name": "",
    "title": "",
    "content" : "",
    "comments" : ""
}

def getThreadsByFilter(token, course_id, pinned: bool = False, type: str = "", category: str = "", subcategory: str = "", limit: int = 100) -> List[dict]:
    """
    type: post, announcement, question
    category: General, Assignments, Lectures, Discussion-Hours, Social
    subcategory: (this is for assignments) A1, A2, A3, A4, A5, A6
    """
    users = {0: "Anonymous"}
    headers={"Authorization": "Bearer " + token}
    params={"limit" : limit, "offset": 0, "sort": "new"}
    r = requests.request("GET", f"https://us.edstem.org/api/courses/{course_id}/threads",  headers=headers, params=params)
    user_list = r.json()["users"]
    for i in user_list:
        users[i["id"]] = i["name"]
    response = r.json()["threads"]
    threads = [i for i in response if i["is_private"] == False]
    if not pinned:  
        threads = [i for i in threads if i["is_pinned"] == pinned]
    if type:
        threads = [i for i in threads if i["type"] == type]
    if category:
        threads = [i for i in threads if i["category"] == category]
    if subcategory:
        threads = [i for i in threads if i["subcategory"] == subcategory]
    thread_ids = [i["id"] for i in threads]
    returnResponse = [""] * min(5, len(thread_ids))
    for i in range(min(5, len(thread_ids))):
        obj = thread_ids[i]
        temp_resp = requests.request("GET", f"https://us.edstem.org/api/threads/{obj}",  headers=headers, params=params)
        temp_json = temp_resp.json()["thread"]
        temp_users = temp_resp.json()["users"]
        for ii in temp_users:
            if ii["id"] not in users:
                users[ii["id"]] = ii["name"]
        temp = responseTemplate.copy()
        temp["link"] = f"https://edstem.org/us/courses/{course_id}/discussion/{obj}"
        temp["name"] = users[temp_json["user_id"]]
        temp["title"] = temp_json["title"]
        temp["content"] = re.sub(CLEANR, '', temp_json["content"])
        temp["comments"] = build_comments_tree(temp_json["comments"], users).strip()
        returnResponse[i] = temp
    return returnResponse
    

def build_comments_tree(comments, users, prefix="") -> str:
    result = ""
    for i, comment in enumerate(comments):
        if i == len(comments) - 1:
            node_prefix = prefix + "┗ "
            child_prefix = prefix + "    "
        else:
            node_prefix = prefix + "┣ "
            child_prefix = prefix + "┃   "
        
        comment_lines = comment["content"].split('\n')
        user = comment["user_id"]
        result += node_prefix + users[user]+ ": " + re.sub(CLEANR, '', comment_lines[0]) + "\n"
        
        if len(comment_lines) > 1:
            for line in comment_lines[1:]:
                result += child_prefix + re.sub(CLEANR, '', line) + "\n"
        
        if comment["comments"]:
            result += build_comments_tree(comment["comments"], users, child_prefix)
    return result

if __name__ == "__main__":
    course_id = os.getenv("COURSE_ID")
    token = os.getenv("ED_TOKEN")
    r = getThreadsByFilter(token, course_id)
    print(r[0]["comments"])
    print(json.dumps(r, indent=1))