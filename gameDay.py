contributors = []
projects = []
projectsFinalDetails = []

x, y = input("Contributor & projects count: ").split()
contributorCount = int(x)
projectCount = int(y)
for i in range(contributorCount):
    name, z = input("Name & skill count: ").split()
    skillCount = int(z)
    contributors.append({
        "name": name,
        "skills": []
    })
    for j in range(skillCount):
        skillName, zz = input("Skill name & skill no: ").split()
        skillRate = int(zz)
        contributors[i]["skills"].append({
            "skill": skillName,
            "skillRate": skillRate
        })

for i in range(projectCount):
    name, a2, a3, a4, a5 = input("Project name, full days, score, BB date, no of roles: ").split()
    noOfDates = int(a2)
    score = int(a3)
    bbDate = int(a4)
    roles = int(a5)
    projects.append({
        "name": name,
        "noOfDates": noOfDates,
        "score": score,
        "bbdate": bbDate,
        "noOfRoles": roles,
        "roles": []
    })
    for j in range(roles):
        roleName, z3 = input("role name, skill req").split()
        reqSkill = int(z3)
        projects[i]["roles"].append({
            "roleName": roleName,
            "reqSkill": reqSkill
        })


for i in projects:
    currentProject = i["name"]
    suitableContributors = []
    contributorsRollVIce = []
    selectedContributors = []
    for j in i["roles"]:
        contributorsRollVIce.append({
            "name": j["roleName"],
            "contributorsDetails": {
                "lowSkilled": [],
                "skilled": []
            }
        })
        for k in contributors:
            for l in k["skills"]:
                if (j["roleName"] == l["skill"]) and ((l["skillRate"] + 1) >= j["reqSkill"]):
                    if not(k in suitableContributors):
                        suitableContributors.append(k)
        for mm in suitableContributors:
            for m in mm["skills"]:
                if (m["skill"] == j["roleName"]):
                    if (m["skillRate"] + 1) == (j["reqSkill"]):
                        if len(contributorsRollVIce) != 0:
                            contributorsRollVIce[0]["contributorsDetails"]["lowSkilled"].append(mm)
                    elif (m["skillRate"] >= j["reqSkill"]):
                            contributorsRollVIce[0]["contributorsDetails"]["skilled"].append(mm)

    for j in contributorsRollVIce:
        if (len(j["contributorsDetails"]["lowSkilled"]) != 0) and (len(j["contributorsDetails"]["skilled"]) != 0):
            selectedContributors.append({
                "role": j["name"],
                "contributor": [j["contributorsDetails"]["lowSkilled"][0]]
            })
        
    print(selectedContributors)

    # for j in contributors:
    #     if j["skills"]["skill"]
    # projectsFinalDetails.append({
    #     "projectName": i[name],

    # })

    # print(suitableContributors)
    # for p in suitableContributors:
    #     print(p)

# for p in projects:
#     print(p)

# for k in contributors:
#         print(k)