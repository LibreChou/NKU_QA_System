# 处理csv文件，获取教师和职称、所属部门的关系链接
import pandas as pd


if __name__ == '__main__':
    # 教师
    person = pd.read_csv("data/csv/person_all.csv")
    # 职称
    pt = pd.read_csv("data/csv/professional_title.csv")
    # 所属部门
    department = pd.read_csv("data/csv/department.csv")
    # print(person)

    person_pt_pid = []
    person_pt_tid = []

    person_d_pid = []
    person_d_did = []

    # 获取关系链接
    for i in range(len(person)):
        # 职称
        if person['pt'][i]:
            tid = 0
            for j in range(len(pt)):
                if pt['name'][j] == person['pt'][i]:
                    tid = pt['tid'][j]
            person_pt_pid.append(person['pid'][i])
            person_pt_tid.append(tid)
        # 所属部门
        if person['department'][i]:
            did = 0
            for k in range(len(department)):
                if department['name'][k] == person['department'][i]:
                    did = department['did'][k]
            person_d_pid.append(person['pid'][i])
            person_d_did.append(did)

    person_to_pt_dict = {'pid': person_pt_pid, 'tid': person_pt_tid}
    person_to_d_dict = {'pid': person_d_pid, 'did': person_d_did}

    p_to_t = pd.DataFrame(person_to_pt_dict)
    p_to_d = pd.DataFrame(person_to_d_dict)

    p_to_t.to_csv('data/csv/person_to_pt.csv', index=False)
    p_to_d.to_csv('data/csv/person_to_department.csv', index=False)