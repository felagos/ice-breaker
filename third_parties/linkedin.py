import json

def scrape_profile():
    with open("./profile.json", "r", encoding="utf8") as file:
        data = json.load(file)

        data = {
            k: v
            for k, v in data.items()
            if v not in ([], "", "", None)
            and k not in ["people_also_viewed", "certifications"]
        }

        if data.get("groups"):
            for group_dict in data.get("groups"):
                group_dict.pop("profile_pic_url")

        return data
