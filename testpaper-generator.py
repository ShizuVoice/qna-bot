# LICENSE: https://github.com/DaijobuDes/testpaper-generator/blob/main/LICENSE

import json

data = {}

def main():
    limit = int(input("Enter number of questions: "))
    school = str(input("Enter school name: "))
    subject = str(input("Enter subject: "))
    directions = str(input("Enter testpaper direction: "))

    data["school"] = school
    data["subject"] = subject
    data["directions"] = directions
    data["questions"] = {}
    for i in range(0, limit):
        question = str(input(f"Enter question number {i+1}: "))
        data["questions"][f"{str(i+1)}"] = {}
        data["questions"][f"{str(i+1)}"]["ask"] = question
        data["questions"][f"{str(i+1)}"]["choices"] = {}

        for j in range(0, 4):
            choice = str(input(f"Enter choice {j+1}: "))
            data["questions"][f"{str(i+1)}"]["choices"][f"{chr(65+j)}"] = {}
            data["questions"][f"{str(i+1)}"]["choices"][f"{chr(65+j)}"] = choice

    print(json.dumps(data, indent=4))
    subject.lower()
    with open(f'./testpaper/{subject}.json', 'w') as f:
        json.dump(data, f, indent=4)

try:
    main()
except KeyboardInterrupt:
    print("User cancelled operation.")
