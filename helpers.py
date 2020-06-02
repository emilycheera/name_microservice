import requests

def get_gender(name):
    """Given a name, return the probable gender."""

    result = {}
    payload = {"name": name}

    gender_res = requests.get(f"https://api.genderize.io", params=payload)
    
    if gender_res.status_code != 200:
        result["error"] = "Unable to retrieve gender"
        return result
    try:
        gender_data = gender_res.json()
    except ValueError:
        result["error"] = "Unable to retrieve gender"
        return result
    
    result["gender"] = gender_data.get("gender")
    return result


def get_age(name):
    """Given a name, return the probable age."""

    result = {}
    payload = {"name": name}

    age_res = requests.get(f"https://api.agify.io", params=payload)
    
    if age_res.status_code != 200:
        result["error"] = "Unable to retrieve age"
        return result
    try:
        age_data = age_res.json()
    except ValueError:
        result["error"] = "Unable to retrieve age"
        return result
    
    result["age"] = age_data.get("age")
    return result


def get_nationality(name):
    """Given a name, return the probable nationality."""

    result = {}
    payload = {"name": name}

    nationality_res = requests.get(f"https://api.nationalize.io", params=payload)
    
    if nationality_res.status_code != 200:
        result["error"] = "Unable to retrieve nationality"
        return result
    try:
        nationality_data = nationality_res.json()
    except ValueError:
        result["error"] = "Unable to retrieve nationality"
        return result
    
    poss_nationalities = nationality_data["country"]
    country = find_country_with_max_probability(poss_nationalities)

    result["nationality"] = nationality_data.get("nationality")
    return result


def find_country_with_max_probability(poss_nationalities):
    """Given a list of dicts, return the country with highest probability."""

    max_probability = 0
    max_country = None

    for country in poss_nationalities:
        if country["probability"] > max_probability:
            max_probability = country["probability"]
            max_country = country["country_id"]

    return max_country

