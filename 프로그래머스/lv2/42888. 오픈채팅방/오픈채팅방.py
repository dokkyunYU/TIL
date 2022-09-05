def solution(record):
    answer = []
    people = {}
    for i in record:
        person_action = i.split()
        if len(person_action) == 3:
            people.update({person_action[1] : person_action[2]})
        if person_action[0] == 'Enter':
            answer.append(f"{person_action[1]}님이 들어왔습니다.")
        elif person_action[0] == 'Leave':
            answer.append(f"{person_action[1]}님이 나갔습니다.")
    for j in range(len(answer)):
        user_id = answer[j].split('님')[0]
        answer[j] = answer[j].replace(user_id, people[user_id])
        
    return answer